# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: hahafunqua
- Lớp: L3A
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

- Xây dựng bộ hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN (12 depot, ~40 nhân viên CSKH, ~45.000 yêu cầu/tháng) từ dữ liệu giả lập chạy thử 2 tuần (1.200 yêu cầu, 1.624 lần chạy) để bảo vệ trước hội đồng Gate 2a.
- Trả lời bốn câu hỏi trọng tâm dựa trên bằng chứng định lượng: (1) có đáng chạy không, (2) nhân viên có dùng không, (3) khi hỏng xử lý thế nào, và (4) thiết kế pilot thế nào để tách được tác động, đủ cỡ mẫu và có luật dừng rõ ràng.

## 3. Giải pháp

- **Nhiệm vụ A & B (CP1–CP2 — Kinh tế học & độ nhạy):** Cài đặt mô hình chi phí từ trace (tử số tính mọi lần chạy kể cả lỗi + giờ nhân viên; mẫu số chỉ đếm ca `thanh_cong`), tách 4 loại yêu cầu, cộng chi phí cố định 40 triệu đ/tháng, chạy 9 kịch bản độ nhạy, tối ưu giới hạn chạy lại theo chi phí cả hệ thống và mô phỏng kịch bản xem lại 100% trong [src/lab13.py](../../src/lab13.py) và [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (CP3 — Quản trị lỗi):** Phân loại 20 ca lỗi theo 5 nhóm Google PAIR dựa trên nguyên nhân gốc (gắn độc lập rồi đối chiếu đồng thuận), kèm bảng phát hiện đo được (gắn event + ngưỡng) và vai trò khắc phục cho 5 ca đại diện trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (CP4 — Kế hoạch pilot):** Tính cỡ mẫu theo cụm (`ICC = 0,02`), kiểm tra 5 tiêu chí tách tác động, chọn chia theo nhân viên (20 + 20) kèm đánh đổi MDE `+6 điểm` và 3 luật dừng 4 vế trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (CP5 — Chỉ số, rủi ro & hồ sơ):** Đặc tả bộ chỉ số (chính, dùng, an toàn), 10 event có `trace_id`, 3 rủi ro kinh tế trong [chi_so.md](chi_so.md) và tổng hợp thành hồ sơ 1 trang 7 mục tại [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí thật & phạm vi:** Chi phí mỗi việc thành công toàn mẫu là `4.472 đ` [simulated] (gấp `16,3×` hoá đơn token+tool `274,7 đ`; giờ nhân viên chiếm `92,5%`). Chi phí cả hệ thống toàn mẫu là `5.865 đ/yêu cầu = 0,49×` của `12.000 đ` [simulated]. Thu hẹp phạm vi pilot về `noi_dia` (`0,22×`) và `hang_nang` (`0,69×`), loại `quoc_te` (`1,88×`, thành công `27,3%`) và `doi_tac` (`0,85×`). Cộng cố định 40 triệu đ/tháng, phạm vi pilot đạt `4.599 đ (0,38×)` ở 45.000 yêu cầu/tháng hoặc `5.784 đ (0,48×)` ở nửa khối lượng [simulated].
- **Độ nhạy & điểm bất lợi:** Ba yếu tố nhạy nhất là số ca làm lại (`+51,8%` khi ×2), tỉ lệ xem lại (`+40,7%` khi ×2) và lương nhân viên (`+23,1%` khi +25%) [simulated]. Giới hạn 2 lần chạy rẻ nhất cho hệ thống (`6.901.220 đ` [simulated]). Tuy nhiên nếu phải xem lại 100%, chi phí lên `11.743 đ (0,98×)` hoặc `12.415 đ (1,03×)` nếu làm lại mất 15,3 phút/ca (mức hoà vốn xem lại ≤ `4,8–5,1` phút) [simulated].
- **Chỉ số đợt chạy thử (không đối chứng) & thiết kế pilot:** Đóng 24h và không mở lại 7 ngày đạt `82,83%` (`92,26%` trong phạm vi pilot), tỉ lệ bỏ qua gợi ý `27,12%`, mở lại 7 ngày `4,25%` (`3,97%` trong phạm vi pilot). Pilot chia 20 + 20 nhân viên đạt `n = 859/nhóm` (`m ≥ 299`, `DE = 6,96`) cho MDE `+6 điểm` (power còn `0,64` nếu hiệu ứng thật `+5 điểm`).
- **Đề xuất của [ho_so_launch_v0.md](ho_so_launch_v0.md):** **Go có điều kiện** (pilot `noi_dia` + `hang_nang`, giới hạn tối đa 2 lần chạy), kèm 5 điều kiện về chốt bảng lỗi, sửa khoá chống trùng/đối soát sổ cái/xoá cache bảng giá, ký chấp nhận MDE `+6 điểm`, bật đủ 10 event có `trace_id` và lộ trình giảm xem lại theo bậc.
- **Kết quả duyệt chéo Gate 2a:** `[Cập nhật sau phiên duyệt chéo 17:00–17:45 và phiếu chấm tại report/team/phieu_cham.md]`.

## 5. Khó khăn và cách xử lý

- **Không đủ cụm cho MDE +5 điểm:** Với 40 nhân viên, cỡ mẫu hiệu dụng tối đa là `1.000 < 1.251` nên không đạt mức chênh +5 điểm. Nhóm xử lý bằng cách nâng MDE lên `+6 điểm` (`m ≥ 299`), giữ 20 cụm/nhóm để tách tác động và công khai mức power `0,64` nếu tác động thật chỉ `+5 điểm`.
- **Rủi ro kinh tế khi xem lại 100%:** Ở mức xem lại 100%, trợ lý gần như không tiết kiệm (`0,98×–1,03×` [simulated]). Nhóm đưa lộ trình giảm tỉ lệ xem lại theo bậc và giới hạn ≤ 4,8 phút xem lại thành điều kiện bắt buộc trước khi mở rộng rollout.
- **Môi trường kiểm thử thiếu `statsmodels`:** Sau khi ghép phần CP4 (`NormalIndPower`) vào `src/lab13.py`, một máy kiểm thử bị thiếu thư viện `statsmodels`; xử lý bằng cài đầy đủ qua môi trường ảo `.venv` theo `src/requirements.txt`.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md) (4 vai: Người viết code CP1–CP2, Người kiểm số / Người viết code sau giải lao CP4–CP5, Người gắn nhãn 1, Người gắn nhãn 2 kiêm giữ hồ sơ).

## 7. Hạn chế và hướng cải thiện

- **Hạn chế:** Toàn bộ thời gian xem lại/làm lại hiện là dữ liệu `simulated`; đợt chạy thử 2 tuần chưa có nhóm đối chứng nên chưa kết luận được tác động nhân quả; bộ nhãn độc lập 20 ca cần chốt hoàn tất trước phiên duyệt chéo.
- **Hướng cải thiện:** Bật đủ 10 event có `trace_id` để thay số `simulated` bằng thời gian đo thật ngay sau tuần 1 pilot; bổ sung `idempotency_key` chống hoàn trùng, đối soát sổ cái `refund_ledger_write` mỗi giờ và cơ chế tự xoá cache khi đổi bảng giá.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, [arxiv.org/abs/2504.13359](https://arxiv.org/abs/2504.13359)
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", [pair.withgoogle.com](https://pair.withgoogle.com)
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`)
