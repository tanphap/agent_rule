# SUPREME RULES — 8 STEP PIPELINE
1. Planner: phân rã yêu cầu thành đầu vào, đầu ra, dependency, acceptance criteria kiểm chứng được.
2. Muse Assign: giao việc theo dependency và quyền.
3. Coder Implement: viết code trên revision xác định.
4. Critic Review: review độc lập, trả JSON {"verdict","issues"}.
5. Coder Rebuttal: ACCEPT/DISPUTE/PARTIAL từng issue, chỉ dựa trên bằng chứng.
6. Muse Judge: SUSTAIN/OVERRULE/MODIFY/ESCALATE từng issue, quyết định cuối cùng về kỹ thuật.
7. Testing: chạy lệnh/test thật, PASS/FAIL/BLOCKED; FAIL quay về bước 3; BLOCKED xử lý nguyên nhân.
8. Archive: lưu code SHA, decision, logs, test PASS evidence, artifact checksums.

Muse là Orchestrator xuyên suốt. Không chuyển bước nếu gate chưa đạt.
Truyền task_id, phase, attempt, base_revision, revision, requirements, acceptance_criteria, constraints và artifact_refs vào mỗi agent.
Không được giả mạo việc đọc file, chạy test, lưu artifact hay xác nhận PASS.
Bất kỳ thay đổi code sau review đều phải review lại revision mới.
Mặc định retry tối đa 3 vòng; sau đó ESCALATE, không lặp vô hạn.
Critic/Testing chỉ đọc implementation; Testing được ghi test trong sandbox riêng.
Không deploy production, không chạm dữ liệu production/thiết bị mạng thật nếu chưa được cho phép.
COMPLETE chỉ sau PASS có bằng chứng đúng revision và Archive đã xác minh lưu thành công.
Prompt KHÔNG tự tạo tự động hóa; host Orchestrator phải ép state transitions, tool ACL và JSON schemas.

All agents must obey the matching file in prompts/.
