# Contracts & JSON

## Task envelope
Metadata cấp bởi Orchestrator (không lấy từ output tự tuyên bố của agent):

```json
{
  "protocol_version": "1.0",
  "project_id": "noc-rca",
  "task_id": "NOC-001",
  "phase": "IMPLEMENT",
  "attempt": 1,
  "base_revision": "SHA_FROM_GIT",
  "revision": "SHA_FROM_GIT",
  "requirements": ["Create a read-only alarm API"],
  "acceptance_criteria": [{"id":"AC-001","required":true,"description":"GET /alarms HTTP 200","verification_method":"pytest"}],
  "constraints": ["Staging only", "No production NMS writes"],
  "assigned_scope": ["backend/"],
  "input_artifacts": [],
  "context_refs": []
}
```

## Strict outputs
- Planner: `{task_id,status:READY|BLOCKED,goal,scope,assumptions,constraints,architecture,tasks,execution_order,parallel_groups,integration_plan,global_acceptance_criteria,verification_plan,risks,open_questions}`; task có inputs, outputs, deps, AC và verification.
- Muse ASSIGN: `{task_id,phase:"ASSIGN",status:"ASSIGNED",assignments:[{task_id,assigned_agent,scope,dependency_ids}],revision}`.
- Coder IMPLEMENT: `{task_id,phase:"IMPLEMENT",attempt,base_revision,result_revision,status:"READY_FOR_REVIEW"|"BLOCKED",files_changed,implementation_summary,requirements_mapping,self_tests,known_limitations,risks,artifact_refs}`.
- Critic: **chỉ đúng hai top-level keys** `{verdict:"APPROVE"|"CHANGES_REQUIRED"|"BLOCKED",issues:[]}`. Issue: id, severity, category, title, description, location, evidence, impact, reproduction_steps, expected_behavior, actual_behavior, suggested_fix, verification_method, confidence.
- Coder REBUTTAL: `{task_id,phase:"REBUTTAL",reviewed_revision,critic_verdict,responses:[{issue_id,position:"ACCEPT"|"DISPUTE"|"PARTIAL",technical_argument,evidence,proposed_fix,regression_risk,verification_method}],overall_position,proposed_actions,evidence_refs,unresolved_questions}`. Mọi issue_id phải được trả lời.
- Muse ADJUDICATE: `{task_id,phase:"ADJUDICATE",attempt,revision,decision:"ACCEPT_CODE"|"REQUEST_CHANGES"|"ESCALATE"|"BLOCKED",issue_decisions:[{issue_id,decision:"SUSTAIN"|"OVERRULE"|"MODIFY"|"ESCALATE",rationale,evidence_refs}],rationale,evidence_refs,required_actions,next_phase,gate_passed,timestamp}`.
- Testing: `{task_id,phase:"TESTING",model:"cx/gpt-5.6-sol",tested_revision,status:"PASS"|"FAIL"|"BLOCKED",acceptance_results,executions,defects,regression_results,evidence_refs,environment_details,summary,next_action,timestamp}`.
- Archive: `{task_id,phase:"ARCHIVE",status:"ARCHIVED"|"BLOCKED",final_revision,testing_verdict:"PASS",archive_location,manifest_ref,stored_artifacts,evidence_refs,checksums,errors,timestamp}`.

## Evidence rules
Execution fields: test_id, command, working_directory, environment, revision, start_time, end_time, exit_code, status, stdout_log_ref, stderr_log_ref, related_acceptance_criteria.
Every required AC must have PASS with test evidence; `NOT_VERIFIED` blocks aggregate PASS.
References must stay under designated artifact root; reject symlink/path traversal, missing/empty logs, SHA mismatch. A file existing is not proof of a genuine test run: production-grade runner must attest job ID, SHA, commands and statuses.
