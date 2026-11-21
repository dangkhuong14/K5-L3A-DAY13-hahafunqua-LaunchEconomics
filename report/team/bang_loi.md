# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Quỳnh Anh · Người gắn nhãn 2: Trần Quốc Đông (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (hoặc `agent_run_completed` lỗi mã đơn không hợp lệ); cảnh báo khi vượt 2% tổng `refund_request_created`/ngày, rà soát hằng ngày | Nhận diện định dạng mã đơn sàn TMĐT để tự động tra sang mã vận đơn LogiX; nếu không tra được thì hiển thị hướng dẫn kèm ảnh minh hoạ thay vì dừng | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa tin nhắn báo "đã hoàn" và event `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng cảnh báo: > 0 ca lệch/giờ | Chỉ trả lời "đã hoàn tiền thành công" sau khi `refund_ledger_write` trả `ok`; nếu lỗi 503 sau 3 lần thử thì báo "đang xử lý" và phát `handoff_to_staff` | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` có `reason = nghi_sai_so_tien` nhưng kiểm tra chính sách / `audit_sample_checked` thấy số tiền đúng; theo dõi hằng tuần, cảnh báo khi > 1% số `ticket_closed`/tuần | Cập nhật mẫu tin nhắn luôn hiển thị rõ công thức tính (ví dụ: `30.000 đ × 50% = 15.000 đ`) kèm điều khoản hoàn phí áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` có `reason = thieu_du_lieu` tách theo `loai`, tổng hợp hằng tuần; cảnh báo khi tỉ lệ chuyển nhân viên > 10% trong phạm vi pilot | Duy trì cơ chế chuyển nhân viên kèm tóm tắt ngữ cảnh; loại `quoc_te` (1,88× nhân viên tự làm [simulated], thành công 27,3%) khỏi phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` kiểm tra mẫu 100 đơn/tuần so `so_tien_da_hoan` với `so_tien_dung` theo `bang_gia_version`; ngưỡng cảnh báo: > 1% số đơn kiểm tra bị lệch | Tự động xoá bộ nhớ đệm khi cập nhật bảng giá mới và ghi `bang_gia_version` vào trace mỗi lần chạy | Kế toán trưởng |
