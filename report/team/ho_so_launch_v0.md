# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: hahafunqua · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu: `4.472 đ` [simulated] (gấp `16,3×` hoá đơn token+tool `274,7 đ`; giờ NV chiếm `92,5%`). Phạm vi pilot `noi_dia` + `hang_nang`: `3.414 đ`; cộng cố định 40 tr/tháng: `4.599 đ` (45.000 yc/tháng) hoặc `5.784 đ` (nửa khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (`+51,8%` khi ×2 → `6.787 đ`) · 2. Tỉ lệ xem lại (`+40,7%` khi ×2 → `6.292 đ`) · 3. Lương NV (`+23,1%` khi +25% → `5.506 đ`); giá token ×2 chỉ `+5,6%` [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống toàn mẫu: `5.865 đ/yc = 0,49×` của `12.000 đ` [simulated]. Theo loại: `noi_dia` `0,22×`, `hang_nang` `0,69×`, `doi_tac` `0,85×`, `quoc_te` `1,88×` (loại `quoc_te`, `doi_tac`). Giới hạn 2 lần chạy rẻ nhất hệ thống (`6.901.220 đ`). Bất lợi: xem lại 100% lên `11.743 đ (0,98×)` hoặc `12.415 đ (1,03×)` nếu làm lại 15,3 phút [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (không đối chứng): chính `82,83%` (994/1.200; phạm vi pilot `92,26%`), dùng — bỏ qua gợi ý `27,12%` (48/177), an toàn — mở lại 7 ngày `4,25%` (51/1.200; phạm vi pilot `3,97%`); thêm 2 chỉ số tự đề xuất và 10 event gắn `trace_id` trong `chi_so.md` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Đã hoàn thiện bảng khắc phục 5 ca đại diện đủ 5 loại Google PAIR (Ca 9, 7, 18, 4, 17) có event/ngưỡng đo được và 20 nhãn độc lập của Người gắn nhãn 2 trong `bang_loi.md`; chờ Người gắn nhãn 1 bổ sung 20 nhãn độc lập để so nhãn và chốt đồng thuận ≥ 80% trước 17:00 | Chưa | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên 20 + 20 nhân viên (phân tầng 12 depot), phạm vi `noi_dia` + `hang_nang`, rollout `[0.10, 0.25, 0.50]`, MDE `+6 điểm` (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`), bất lợi: power còn `0,64` nếu hiệu ứng thật `+5 điểm`; 3 luật dừng 4 vế, rollback 30 phút, quyết định `2027-01-05` (`pilot_plan.yaml`) | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | 3 rủi ro định lượng trong `chi_so.md`: làm lại ×2 (`+51,8%`, lên `6.787 đ`), xem lại 100% kéo dài (`11.743–12.415 đ = 0,98×–1,03×`, hoà vốn ≤ `4,8–5,1` phút xem lại), khối lượng giảm 50% (cố định tăng gấp đôi lên `2.370 đ/việc`, tổng `5.784 đ`) [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** Go có điều kiện (pilot phạm vi `noi_dia` + `hang_nang`, giới hạn tối đa 2 lần chạy)

1. Hoàn tất gắn nhãn độc lập 20 ca lỗi (đồng thuận ≥ 80%, khớp ≥ 16/20) trong `report/team/bang_loi.md` — Phụ trách: PM trợ lý hoàn phí — Ngày kiểm tra: `2026-11-21` (trước 17:00 duyệt chéo; chốt lại trước mở pilot `2026-11-28`).
2. Sửa lỗi hệ thống nghiêm trọng: thêm khoá chống hoàn trùng `idempotency_key` (ca 20), đối soát sổ cái `refund_ledger_write` mỗi giờ (ca 7) và xoá bộ nhớ đệm khi đổi bảng giá (ca 17) — Phụ trách: Kỹ sư trưởng agent — Ngày kiểm tra: `2026-12-01` (trước rollout `0.10`).
3. Ký chấp nhận đánh đổi thiết kế pilot MDE `+6 điểm` (`m ≥ 299`, `DE = 6,96`; power còn `0,64` ở mức `+5 điểm`) và xác nhận quy trình tắt cờ rollback trong 30 phút — Phụ trách: Giám đốc vận hành LogiX-VN — Ngày kiểm tra: `2026-12-01`.
4. Bật đủ 10 event có `trace_id` và thay toàn bộ số phút `simulated` bằng số đo thật (`phut_xem_lai`, `phut_lam_lai`) sau tuần 1 bước `0.10` — Phụ trách: Kỹ sư trưởng agent — Ngày kiểm tra: `2026-12-08`.
5. Triển khai lộ trình giảm tỉ lệ xem lại theo bậc (giảm xem lại `noi_dia` khi `sua + bo < 15%`) và giữ thời gian xem lại trung bình ≤ 4,8 phút/yêu cầu để tránh kịch bản xem lại 100% (`0,98×–1,03×` [simulated]) — Phụ trách: Trưởng nhóm CSKH — Ngày kiểm tra: `2026-12-15` (cuối bước `0.25`).
