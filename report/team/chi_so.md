# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại            | Chỉ số                                                                                          | Công thức                                                                                                      | Tính thử trên 1.200 yêu cầu                                                                                        |
| --------------- | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày                                        | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu                                  | Chỉ số trong đợt chạy thử là **82,83%** (994/1.200); trong phạm vi `noi_dia` + `hang_nang` là **92,26%** (906/982) |
| Dùng            | Tỉ lệ bỏ qua gợi ý                                                                              | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại                                          | Chỉ số trong đợt chạy thử là **27,12%** (48/177 yêu cầu được xem lại)                                              |
| An toàn         | Tỉ lệ lỗi lọt đến khách                                                                         | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu                                                             | Chỉ số trong đợt chạy thử là **4,25%** (51/1.200); trong phạm vi `noi_dia` + `hang_nang` là **3,97%** (39/982)     |
| Dùng            | Nhóm tự đề xuất: Tỉ lệ nhân viên mở trợ lý ở nhóm can thiệp                                     | Số yêu cầu thuộc nhóm can thiệp có event `agent_suggestion_shown` chia tổng số yêu cầu phân cho nhóm can thiệp | Không cần tính                                                                                                     |
| An toàn         | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn kiểm tra mẫu có `so_tien_da_hoan` khác `so_tien_dung` chia tổng số đơn kiểm tra mẫu (100 đơn/tuần)      | Không cần tính                                                                                                     |

Lưu ý: Chỉ viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số từ 0,70", vì đợt chạy thử 2 tuần không có nhóm đối chứng.

## Danh sách event

Mười event dưới đây đều gắn `trace_id` để nối trực tiếp với trace của agent và đo thời gian xem lại/làm lại thật (thay thế số `simulated` sau tuần 1 của pilot):

| Event                    | Ai tạo                       | Thuộc tính chính                                                                          | Thời điểm                                            |
| ------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| `refund_request_created` | App khách / cổng tiếp nhận   | `request_id`, `loai`, `depot`, `so_tien_vnd`, `arm`, `staff_id`, `created_at`, `trace_id` | Khi khách gửi yêu cầu hoàn phí                       |
| `agent_run_completed`    | Dịch vụ Agent                | `run_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id`        | Sau mỗi lần chạy của agent (kể cả lần lỗi)           |
| `agent_suggestion_shown` | Giao diện CSKH               | `request_id`, `staff_id`, `so_tien_de_xuat`, `shown_at`, `trace_id`                       | Khi gợi ý của trợ lý hiển thị cho nhân viên          |
| `staff_review_decision`  | Nhân viên CSKH               | `request_id`, `staff_id`, `quyet_dinh` (`giu`/`sua`/`bo`), `phut_xem_lai`, `trace_id`     | Khi nhân viên bấm gửi, sửa hoặc bỏ gợi ý             |
| `staff_rework_completed` | Nhân viên CSKH               | `request_id`, `staff_id`, `phut_lam_lai`, `ly_do`, `trace_id`                             | Khi nhân viên hoàn tất xử lý làm lại một ca sai      |
| `refund_ledger_write`    | Dịch vụ sổ cái               | `idempotency_key`, `request_id`, `so_tien_da_hoan`, `ket_qua`, `trace_id`                 | Khi ghi nhận giao dịch hoàn tiền vào sổ cái          |
| `handoff_to_staff`       | Dịch vụ Agent                | `request_id`, `reason`, `tom_tat`, `trace_id`                                             | Khi agent dừng chạy và chuyển yêu cầu sang nhân viên |
| `ticket_closed`          | Hệ thống ticket              | `request_id`, `closed_at`, `trace_id`                                                     | Khi yêu cầu hoàn phí được đóng                       |
| `ticket_reopened`        | Khách hàng / hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id`                                         | Khi khách mở lại yêu cầu sau khi đã đóng             |
| `audit_sample_checked`   | Bộ phận Kế toán              | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `bang_gia_version`, `trace_id`           | Khi kiểm tra mẫu 100 đơn/tuần                        |

**Kiểm tra chéo:** đối chiếu từng chỉ số ở bảng E1 với danh sách event (mọi chỉ số đều đo được, không có chỉ số nào bị thiếu event):

- **Chỉ số chính (% đóng trong 24h và không mở lại trong 7 ngày):** tính từ `refund_request_created` (`created_at`), `ticket_closed` (`closed_at - created_at <= 24h`) và không có `ticket_reopened` trong 7 ngày sau `closed_at`, ghép bằng `trace_id`.
- **Chỉ số dùng — Tỉ lệ bỏ qua gợi ý:** tính từ `staff_review_decision` (đếm `quyet_dinh` thuộc `sua` hoặc `bo` chia tổng số event `staff_review_decision`).
- **Chỉ số an toàn — Tỉ lệ lỗi lọt đến khách:** tính từ `ticket_reopened` (trong 7 ngày sau `ticket_closed`) chia tổng số `refund_request_created`.
- **Chỉ số dùng tự đề xuất — Tỉ lệ mở trợ lý ở nhóm can thiệp:** tính từ số `request_id` có `agent_suggestion_shown` chia tổng số `refund_request_created` có `arm = treatment`.
- **Chỉ số an toàn tự đề xuất — Tỉ lệ đơn hoàn sai tiền (lỗi ngầm):** tính từ `audit_sample_checked` (`so_tien_da_hoan != so_tien_dung` chia tổng số bản ghi kiểm tra mẫu) và đối chiếu thêm `refund_ledger_write` bằng `trace_id` để phát hiện hoàn trùng.
- **Chi phí mỗi việc thành công đo thật (thay số `simulated`):** tính từ `agent_run_completed` (token, tool), `staff_review_decision` (`phut_xem_lai`), `staff_rework_completed` (`phut_lam_lai`) và `ticket_closed` / `ticket_reopened`.

## E2 · Rủi ro kinh tế

Số liệu tác động lấy trực tiếp từ bảng độ nhạy và chi phí cố định trong `report/team/bang_chi_phi.md`:

| Rủi ro                                                   | Tác động đã tính                                                                                                                                                                                               | Dấu hiệu theo dõi                                                                                                 | Hành động                                                                                                                              | Người phụ trách    |
| -------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, hạng 1 B2) | Chi phí mỗi việc thành công tăng **+51,8%**, từ 4.472 đ lên **6.787 đ** [simulated]                                                                                                                            | Tỉ lệ ca `lam_lai` theo tuần vượt 7% trong phạm vi pilot (mức chạy thử là 4,9%: 48/982 yêu cầu)                   | Thu hẹp phạm vi về chỉ `noi_dia`, rà 20 trace `lam_lai` gần nhất để sửa lỗi gốc trước khi mở lại `hang_nang`                           | PM trợ lý hoàn phí |
| Phải duy trì xem lại 100% kéo dài (B4)                   | Chi phí mỗi việc thành công tăng lên **11.743 đ = 0,98×** (làm lại 9 phút/ca) hoặc **12.415 đ = 1,03×** (làm lại 15,3 phút/ca như dữ liệu), đắt hơn nhân viên tự làm 12.000 đ [simulated]                      | Tỉ lệ yêu cầu bị xem lại còn > 50% cuối bước rollout `0.25`, hoặc thời gian xem lại trung bình > 4,8 phút/yêu cầu | Thực hiện lộ trình giảm tỉ lệ xem lại theo bậc với `noi_dia` khi tỉ lệ `sua + bo` < 15% và tối ưu giao diện rút ngắn thời gian xem lại | Trưởng nhóm CSKH   |
| Khối lượng xử lý thực tế thấp hơn dự kiến (A4)           | Chi phí cố định 40 triệu đ/tháng tăng gấp đôi từ **1.185 đ** lên **2.370 đ/việc** khi khối lượng giảm một nửa, đẩy tổng chi phí mỗi việc thành công từ **4.599 đ (0,38×)** lên **5.784 đ (0,48×)** [simulated] | Số việc thành công hằng tuần < 50% kế hoạch dự kiến (< 4.200 việc/tuần ở quy mô đầy đủ)                           | Tạm dừng kế hoạch mở rộng pilot và đàm phán lại cấu trúc chi phí cố định 40 triệu đ/tháng theo mức sử dụng                             | PM trợ lý hoàn phí |
