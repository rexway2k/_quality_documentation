# Archive Migration Review

## Purpose

This document captures archived content that appears to be missing or only partially represented in the active quality management system. The goal is to review each item and decide whether it should be included, moved, or left archived.

## Review Approach

For each item, consider:
- whether the content adds unique value
- whether the topic is already represented in a newer or better form
- whether the content should be moved into a more suitable part of the quality management system
- whether it should remain archived for historical context

## Candidates to Review

### 1. Legacy quality 101 decision artifacts

#### [Archive_Save/_quality_101/_00_shared_definition_of_quality.md](../../Archive_Save/_quality_101/_00_shared_definition_of_quality.md)
- Suggested review area: quality foundations
- Possible destination: [__00_Quality Management System/00 Quality Foundations](../00 Quality Foundations)
- Status: intentionally not migrated; the current quality foundations already cover this concept.

#### [Archive_Save/_quality_101/00_core_quality_and_testing_principles.md](../../Archive_Save/_quality_101/00_core_quality_and_testing_principles.md)
- Suggested review area: quality foundations and standards
- Status: intentionally not migrated; the current quality model already accounts for these principles.

#### [Archive_Save/_quality_101/01_quality_decision_field_guide.md](../../Archive_Save/_quality_101/01_quality_decision_field_guide.md)
#### [Archive_Save/_quality_101/02_quality_decision_card.md](../../Archive_Save/_quality_101/02_quality_decision_card.md)
#### [Archive_Save/_quality_101/03_quality_decision_visual_grid.md](../../Archive_Save/_quality_101/03_quality_decision_visual_grid.md)
- Suggested review area: playbooks and templates
- Possible destination: [__00_Quality Management System/06 Playbooks and Starter Guides/04 Templates and Checklists](../04 Templates and Checklists)
- Notes: These appear to be early versions of decision aids and may be useful if the format is still valuable.

### 2. Universal quality operating layer for AI work

#### [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work)
- Suggested review area: AI quality and testing
- Possible destination: [__00_Quality Management System/04 AI Quality and Testing](../04 AI Quality and Testing)
- Notes: This is the most substantial archive cluster and may contain useful operational and implementation guidance that is not currently represented in the main system.

##### Suggested sub-items to review
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/00_system_specification.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/00_system_specification.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/01_operating_guide.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/01_operating_guide.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/02_agent_build_and_test_guide.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/02_agent_build_and_test_guide.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/README.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/README.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/scripts/test_harness.py](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/scripts/test_harness.py)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/scripts/test_harness_usage.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/scripts/test_harness_usage.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/library/apply_quality_questions.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/library/apply_quality_questions.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/prompts/system_prompt.md](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/prompts/system_prompt.md)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/schemas/skills.json](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/schemas/skills.json)
- [Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/schemas/skills.yaml](../../Archive_Save/Quality AI Resources/_universal_quality_operating_layer_for_AI_work/skills/schemas/skills.yaml)

### 3. AI testing and quality model materials

These are already represented in the current AI testing model folders and should be skipped for migration review for now:
- [Archive_Save/Quality AI Resources/AI Testing and Quality Model/AI Testing & Quality Model.md](../../Archive_Save/Quality AI Resources/AI Testing and Quality Model/AI Testing & Quality Model.md)
- [Archive_Save/Quality AI Resources/AI Testing and Quality Model/Evalutation and Observability - AI Testing Model](../../Archive_Save/Quality AI Resources/AI Testing and Quality Model/Evalutation and Observability - AI Testing Model)

## Recommendation Matrix

| Candidate | Suggested Action | Notes |
| --- | --- | --- |
| Legacy quality 101 decision artifacts | Review for inclusion or archival | The decision aids were migrated as companions; the shared definition and core principles are intentionally not being migrated because the current foundations already cover them |
| AI operating layer framework | Review for migration | Highest-value candidate for inclusion |
| AI test harness and prompt/schema assets | Review for migration or archival | Useful if the team wants operational AI quality guidance |
| Existing AI testing model materials | Skip for migration review | Already represented in the current AI quality and testing structure |

## Next Step

Review each candidate and decide:
- include in the QMS
- move to a more appropriate folder
- or keep archived for reference
