# Runbook — vận hành và xử lý sự cố

1. Nhận task → ghi nguồn yêu cầu, AC và giới hạn. Khởi tạo task_id.
2. Kiểm Planner READY, dependency và expected artifacts trước khi ASSIGN.
3. Với mỗi bản Coder, ghi commit SHA. Critic đọc cùng SHA. REBUTTAL bao phủ issue_id.
4. Muse phân xử theo issue, yêu cầu sửa nếu tồn tại vấn đề bắt buộc. Khi rework, tăng attempt, reset review/test evidence của SHA cũ.
5. Trước Testing kiểm SHA đã phê duyệt và toàn bộ AC. Chạy sandbox riêng có log command/exit status.
6. FAIL: lập defect với reproduction và evidence; quay Coder. BLOCKED: sửa quyền/env, không thay đổi kết quả thành PASS.
7. PASS: khóa revision, manifest evidence. Archivist lưu thành công mới đóng task.
8. Khi vượt max_attempts=3: ESCALATE người phụ trách, giữ toàn bộ logs.

## Recovery
- Agent unavailable: giữ phase BLOCKED; retry có backoff nhưng không tạo decision thay agent.
- Git SHA mismatch: BLOCKED, checkout lại approved commit.
- Critic JSON invalid: yêu cầu sửa JSON, không skip review.
- Rebuttal thiếu issue: trả Coder bổ sung.
- Muse ACCEPT_CODE khi còn SUSTAIN/MODIFY chưa sửa: từ chối transition.
- Test log thiếu hoặc không xác thực: BLOCKED.
- Archive write thất bại: giữ TEST PASS + ARCHIVE_PENDING; không COMPLETE.
- Concurrency: khóa theo task_id, idempotency key cho từng chuyển phase.
