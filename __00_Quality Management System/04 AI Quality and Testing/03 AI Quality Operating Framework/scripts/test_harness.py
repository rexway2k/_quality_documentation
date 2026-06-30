#!/usr/bin/env python3
"""
Universal Quality Skill System - Test Harness

Purpose:
- Initialize a scenario/results pack
- Collect manual scores for agent behavior using the evaluation rubric
- Generate a markdown report showing weak areas and repeat failures

This script is tool-agnostic: it does not call an LLM directly.
You run your agent however you want, paste the agent responses into the results file,
then use this script to score and summarize the run.
"""

from __future__ import annotations
import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from statistics import mean
from typing import Dict, List, Any

RUBRIC_CATEGORIES = [
    "Contract Clarity",
    "Ambiguity Handling",
    "Risk Management",
    "Execution Quality",
    "Verification Alignment",
    "Decision Structure",
    "Adaptive Rigor",
    "Failure Diagnosis",
    "Consistency",
    "Progress Enablement",
]

DEFAULT_SCENARIOS = [
    {
        "id": "SCN-01",
        "type": "Low complexity / Low ambiguity",
        "title": "Simple Direct Task",
        "input_prompt": "Write a short summary of the benefits of exercise.",
        "what_this_tests": ["adaptive rigor", "execution without over-processing"],
        "expected_behaviors": [
            "Does not over-apply the full framework",
            "Produces useful output quickly",
            "Maintains clarity and correctness",
        ],
        "failure_signals": [
            "Over-analysis before writing",
            "Unnecessary contract breakdown",
            "Excessive verbosity",
        ],
    },
    {
        "id": "SCN-02",
        "type": "Moderate ambiguity",
        "title": "Ambiguous Request",
        "input_prompt": "Create a plan for improving team performance.",
        "what_this_tests": ["contract definition", "assumption surfacing"],
        "expected_behaviors": [
            "Identifies missing context",
            "Defines assumptions explicitly",
            "Proceeds with a structured plan",
        ],
        "failure_signals": [
            "Silently assumes context",
            "Produces generic output with no framing",
            "Fails to clarify consumer or outcome",
        ],
    },
    {
        "id": "SCN-03",
        "type": "Execution-heavy",
        "title": "Build Something",
        "input_prompt": "Write a Python script that reads a CSV file and summarizes the data.",
        "what_this_tests": ["execution capability", "not stopping at analysis"],
        "expected_behaviors": [
            "Produces actual working script",
            "Defines assumptions",
            "Aligns output to expected outcome",
        ],
        "failure_signals": [
            "Explains what to do without writing code",
            "Produces incomplete or non-functional code",
            "Ignores assumptions",
        ],
    },
    {
        "id": "SCN-04",
        "type": "High ambiguity / possible unbounded risk",
        "title": "Missing Critical Information",
        "input_prompt": "Design a secure system for handling customer data.",
        "what_this_tests": ["bounding risk", "escalation behavior", "structured definition"],
        "expected_behaviors": [
            "Identifies critical unknowns",
            "Avoids pretending the system is fully defined",
            "Defines a bounded approach or states assumptions clearly",
        ],
        "failure_signals": [
            "Proceeds as if requirements are complete",
            "Produces overconfident design with no caveats",
            "Ignores constraints and failure modes",
        ],
    },
    {
        "id": "SCN-05",
        "type": "Verification-focused",
        "title": "Review for Completeness",
        "input_prompt": "Here is a test plan. Review it and tell me if it's complete.",
        "what_this_tests": ["verification thinking", "structured evaluation"],
        "expected_behaviors": [
            "Evaluates via WHY/WHAT/WHERE/HOW/WHEN",
            "Identifies gaps",
            "Avoids subjective judgment",
        ],
        "failure_signals": [
            "Vague feedback",
            "No structured reasoning",
            "No identification of missing elements",
        ],
    },
    {
        "id": "SCN-06",
        "type": "Debug / issue analysis",
        "title": "Failure Diagnosis",
        "input_prompt": "This feature is failing in production. Help figure out why.",
        "what_this_tests": ["failure diagnosis", "contract tracing"],
        "expected_behaviors": [
            "Defines expected behavior, actual behavior, and mismatch",
            "Traces likely root cause categories",
            "Avoids guessing",
        ],
        "failure_signals": [
            "Jumps to conclusions",
            "Suggests fixes without diagnosis",
            "Ignores expectation mismatch",
        ],
    },
    {
        "id": "SCN-07",
        "type": "Governance / tension",
        "title": "Conflicting Constraints",
        "input_prompt": "We need to move fast, but also ensure this is fully secure. What should we do?",
        "what_this_tests": ["principle tension resolution", "decision justification"],
        "expected_behaviors": [
            "Acknowledges the conflict",
            "Balances speed, risk, and constraints",
            "Proposes a bounded approach",
        ],
        "failure_signals": [
            "Ignores one side of the conflict",
            "Provides generic advice",
            "Fails to justify the decision",
        ],
    },
    {
        "id": "SCN-08",
        "type": "Complex dependency system",
        "title": "Multi-Consumer Scenario",
        "input_prompt": "Design a reporting dashboard used by executives, analysts, and operations teams.",
        "what_this_tests": ["consumer identification", "fractal contract logic"],
        "expected_behaviors": [
            "Identifies multiple consumers",
            "Differentiates needs",
            "Reflects those differences in the structure/design",
        ],
        "failure_signals": [
            "Treats all users as identical",
            "Ignores downstream needs",
            "Produces shallow design",
        ],
    },
    {
        "id": "SCN-09",
        "type": "System behavior check",
        "title": "Over-Constraint / Rigidity Risk",
        "input_prompt": "Write a short email to confirm a meeting.",
        "what_this_tests": ["adaptive rigor", "non-blocking behavior"],
        "expected_behaviors": [
            "Executes immediately",
            "Avoids unnecessary structure",
            "Keeps response lightweight",
        ],
        "failure_signals": [
            "Over-applies the framework",
            "Delays execution",
            "Adds unnecessary complexity",
        ],
    },
    {
        "id": "SCN-10",
        "type": "Validation weakness",
        "title": "Verification Gap",
        "input_prompt": "Build a solution for managing inventory.",
        "what_this_tests": ["verification definition", "completeness thinking"],
        "expected_behaviors": [
            "Defines how success would be measured",
            "Identifies risks and failure modes",
            "Ensures the solution is testable",
        ],
        "failure_signals": [
            "No mention of verification",
            "Produces design without validation",
            "Ignores failure modes",
        ],
    },
]


def write_json(path: Path, obj: Any) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False), encoding='utf-8')


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding='utf-8'))


def init_pack(outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)

    scenarios_path = outdir / 'scenarios.json'
    results_path = outdir / 'results.json'

    write_json(scenarios_path, {"scenarios": DEFAULT_SCENARIOS, "rubric_categories": RUBRIC_CATEGORIES})

    template_results = {
        "run_name": "quality-skill-system-eval",
        "agent_name": "replace-me",
        "agent_configuration": {
            "system_prompt_file": "skills/prompts/system_prompt.md",
            "modular_blocks_file": "skills/prompts/modular_blocks.md",
            "notes": "Add model/tool/runtime details here."
        },
        "scenarios": [
            {
                "id": s["id"],
                "title": s["title"],
                "input_prompt": s["input_prompt"],
                "agent_response": "",
                "scores": {cat: None for cat in RUBRIC_CATEGORIES},
                "notes": "",
                "root_cause_hypothesis": "",
                "artifacts_to_refine": []
            }
            for s in DEFAULT_SCENARIOS
        ]
    }
    write_json(results_path, template_results)

    print(f"Created: {scenarios_path}")
    print(f"Created: {results_path}")
    print("Next steps:")
    print("1) Run your agent with each input_prompt from scenarios.json")
    print("2) Paste each full agent response into results.json -> agent_response")
    print("3) Run: python test_harness.py score --results verification/results.json")
    print("4) Run: python test_harness.py report --results verification/results.json")


def _prompt_score(category: str, current: Any) -> int:
    while True:
        raw = input(f"  {category} (1-5){' [' + str(current) + ']' if current is not None else ''}: ").strip()
        if raw == '' and current is not None:
            return int(current)
        try:
            val = int(raw)
            if 1 <= val <= 5:
                return val
        except ValueError:
            pass
        print("    Enter an integer from 1 to 5.")


def score_results(results_path: Path) -> None:
    data = read_json(results_path)
    print(f"Scoring run: {data.get('run_name', 'unnamed')} | agent: {data.get('agent_name', 'unknown')}")
    print('-' * 80)

    for scenario in data.get('scenarios', []):
        print(f"\n{scenario['id']} — {scenario['title']}")
        print(f"Prompt: {scenario['input_prompt']}")
        response = scenario.get('agent_response', '')
        if response:
            preview = response if len(response) <= 800 else response[:800] + " ...[truncated preview]"
            print("Agent response preview:")
            print(preview)
        else:
            print("Agent response is empty. Paste the full response into results.json before scoring if possible.")

        scenario.setdefault('scores', {})
        for category in RUBRIC_CATEGORIES:
            scenario['scores'][category] = _prompt_score(category, scenario['scores'].get(category))

        notes = input("  Notes (optional): ").strip()
        if notes:
            scenario['notes'] = notes
        cause = input("  Root cause hypothesis if weak (optional): ").strip()
        if cause:
            scenario['root_cause_hypothesis'] = cause
        refine = input("  Artifacts to refine, comma-separated (optional): ").strip()
        if refine:
            scenario['artifacts_to_refine'] = [x.strip() for x in refine.split(',') if x.strip()]

    write_json(results_path, data)
    print(f"\nSaved scores to: {results_path}")


def _category_averages(data: Dict[str, Any]) -> Dict[str, float]:
    vals: Dict[str, List[int]] = {cat: [] for cat in RUBRIC_CATEGORIES}
    for scn in data.get('scenarios', []):
        for cat, score in scn.get('scores', {}).items():
            if score is not None:
                vals[cat].append(int(score))
    return {cat: (mean(scores) if scores else 0.0) for cat, scores in vals.items()}


def _scenario_average(scn: Dict[str, Any]) -> float:
    scores = [int(v) for v in scn.get('scores', {}).values() if v is not None]
    return mean(scores) if scores else 0.0


def report_results(results_path: Path, output: Path | None = None) -> None:
    data = read_json(results_path)
    cat_avg = _category_averages(data)
    weak_categories = [cat for cat, avg in cat_avg.items() if avg and avg < 3.5]
    weak_scenarios = []
    recurring_refinements: Dict[str, int] = {}

    lines: List[str] = []
    lines.append(f"# Evaluation Report — {data.get('run_name', 'unnamed')}\n")
    lines.append(f"**Agent:** {data.get('agent_name', 'unknown')}\n")

    lines.append("## Category Averages\n")
    lines.append("| Category | Average |")
    lines.append("|---|---:|")
    for cat in RUBRIC_CATEGORIES:
        lines.append(f"| {cat} | {cat_avg[cat]:.2f} |")

    lines.append("\n## Scenario Summaries\n")
    for scn in data.get('scenarios', []):
        avg = _scenario_average(scn)
        if avg < 3.5:
            weak_scenarios.append((scn['id'], scn['title'], avg))
        lines.append(f"### {scn['id']} — {scn['title']}")
        lines.append(f"- Average score: {avg:.2f}")
        low = [f"{k}={v}" for k, v in scn.get('scores', {}).items() if v is not None and int(v) <= 3]
        if low:
            lines.append(f"- Low-scoring categories: {', '.join(low)}")
        if scn.get('notes'):
            lines.append(f"- Notes: {scn['notes']}")
        if scn.get('root_cause_hypothesis'):
            lines.append(f"- Root cause hypothesis: {scn['root_cause_hypothesis']}")
        refs = scn.get('artifacts_to_refine', [])
        if refs:
            lines.append(f"- Artifacts to refine: {', '.join(refs)}")
            for ref in refs:
                recurring_refinements[ref] = recurring_refinements.get(ref, 0) + 1
        lines.append("")

    lines.append("## Weak Areas\n")
    if weak_categories:
        lines.append("### Weak Categories")
        for cat in weak_categories:
            lines.append(f"- {cat}: {cat_avg[cat]:.2f}")
    else:
        lines.append("No category average fell below 3.5.")

    lines.append("")
    if weak_scenarios:
        lines.append("### Weak Scenarios")
        for sid, title, avg in weak_scenarios:
            lines.append(f"- {sid} — {title}: {avg:.2f}")
    else:
        lines.append("No scenario average fell below 3.5.")

    lines.append("\n## Recommended Refinement Targets\n")
    if recurring_refinements:
        for artifact, count in sorted(recurring_refinements.items(), key=lambda kv: (-kv[1], kv[0])):
            lines.append(f"- {artifact} (referenced {count} time(s))")
    else:
        lines.append("No refinement targets were recorded.")

    lines.append("\n## Refinement Loop\n")
    lines.append("1. Start with the lowest scoring categories and scenarios.")
    lines.append("2. Trace the failure to the skill, prompt block, or specification artifact that likely caused it.")
    lines.append("3. Refine the smallest artifact that can correct the behavior.")
    lines.append("4. Re-run only the affected scenarios first.")
    lines.append("5. If scores improve without causing regressions elsewhere, keep the change.")

    report_text = '\n'.join(lines)
    if output is None:
        output = results_path.with_name('evaluation_report.md')
    output.write_text(report_text, encoding='utf-8')
    print(f"Wrote report: {output}")
    print(report_text)


def main():
    parser = argparse.ArgumentParser(description="Universal Quality Skill System - Test Harness")
    sub = parser.add_subparsers(dest='cmd', required=True)

    p_init = sub.add_parser('init', help='Create starter scenario/result files')
    p_init.add_argument('--outdir', default='verification', help='Directory to write scenarios.json and results.json')

    p_score = sub.add_parser('score', help='Interactively score a results.json file')
    p_score.add_argument('--results', required=True, help='Path to results.json')

    p_report = sub.add_parser('report', help='Generate a markdown evaluation report from results.json')
    p_report.add_argument('--results', required=True, help='Path to results.json')
    p_report.add_argument('--output', help='Optional output markdown file path')

    args = parser.parse_args()
    if args.cmd == 'init':
        init_pack(Path(args.outdir))
    elif args.cmd == 'score':
        score_results(Path(args.results))
    elif args.cmd == 'report':
        report_results(Path(args.results), Path(args.output) if args.output else None)


if __name__ == '__main__':
    main()
