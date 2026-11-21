# Báo cáo cá nhân — TranQuocDong-2A202603643

## 1. Thông tin thành viên

- Họ tên: Trần Quốc Đông
- MSSV: 2A202603643
- Email: dongtranquoc951@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- **Giữ hồ sơ (Dossier Keeper):** Trực tiếp khởi tạo, quản lý, biên tập và liên tục cập nhật trang hồ sơ launch [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) xuyên suốt 5 Checkpoint (CP1–CP5); giám sát sự tuân thủ 5 quy tắc vàng của lab (gán nhãn `simulated`, không dùng từ bị cấm theo quy tắc 5, chuẩn hóa 3 trạng thái và vai trò phụ trách cụ thể).
- **Người gắn nhãn 2 (Annotator 2):** Độc lập gắn nhãn 20 ca lỗi ở CP3 (Nhiệm vụ C) theo 5 loại của Google PAIR dựa trên nguyên nhân gốc trong 8 phút đầu; cùng Người gắn nhãn 1 đối chiếu nhãn, tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt cho các ca lệch và lập bảng khắc phục 5 ca đại diện.
- **Tổng hợp & Duyệt chéo Gate 2a (CP5):** Rà soát tính nhất quán số liệu toàn bộ hồ sơ 7 mục trước 17:00, tham gia đọc và phản biện hồ sơ nhóm bạn theo 3 tiêu chí Rubric C6–C8 và ghi biên bản vào [report/team/phieu_cham.md](phieu_cham.md).

## 3. Đóng góp cụ thể

- **CP1 & CP2 (Hồ sơ Chi phí & Độ nhạy):**
  - Thu thập kết quả từ Người viết code và Người kiểm số, điền ngay vào Mục 1 của `ho_so_launch_v0.md`: chi phí mỗi việc thành công toàn mẫu là `4.472 đ` [simulated] (gấp `16,3 lần` hoá đơn token+tool `274,7 đ`; giờ nhân viên chiếm `92,5%`), trong phạm vi pilot `noi_dia` + `hang_nang` là `3.414 đ`, cộng chi phí cố định 40 tr/tháng đạt `4.599 đ = 0,38×` (ở 45.000 yc/tháng) hoặc `5.784 đ = 0,48×` (ở nửa khối lượng) [simulated].
  - Điền Mục 2 & Mục 3: Xếp hạng 3 yếu tố nhạy nhất (Làm lại `+51,8%`, Xem lại `+40,7%`, Lương NV `+23,1%`; giá token chỉ `+5,6%` [simulated]) và phân tích so sánh với nhân viên tự làm (`5.865 đ = 0,49×` của 12.000 đ [simulated]; nêu rõ con số bất lợi nếu xem lại 100% sẽ đắt hơn tự làm: `11.743–12.415 đ = 0,98×–1,03×` [simulated]).
- **CP3 (Gắn nhãn 20 ca & Bảng lỗi):**
  - Tự gắn độc lập 20 ca lỗi theo 5 loại Google PAIR (*Do người dùng: 1, 6, 9, 14; Hệ thống: 2, 7, 8, 15, 20; Ngữ cảnh: 3, 10, 16, 18; Giới hạn hệ thống: 4, 11, 13, 19; Ngầm: 5, 12, 17*).
  - Điền cột Nhãn người 2 vào [report/team/bang_loi.md](bang_loi.md), so sánh đạt đồng thuận cao (≥ 80%), thống nhất quy tắc phân biệt cho ca 6 (Do người dùng vì gốc là khách chọn sai) và ca 18 (Ngữ cảnh vì hệ thống tính đúng chính sách tiền hoàn nhưng khách hiểu sai).
  - Phối hợp xây dựng bảng khắc phục 5 ca tiêu biểu (Ca 9, 7, 18, 4, 17) có event đo lường (`input_validation_failed`, `refund_ledger_write`, `ticket_reopened`, `handoff_to_staff`, `audit_sample_checked`), ngưỡng cảnh báo cụ thể và gán vai trò phụ trách có quyền quyết định; cập nhật Mục 5 vào hồ sơ.
- **CP4 & CP5 (Hồ sơ Kế hoạch Pilot & Đề xuất Gate 2a):**
  - Cập nhật Mục 6 về kế hoạch pilot: chia ngẫu nhiên 20 + 20 nhân viên, MDE `+6 điểm` (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`), công khai điểm bất lợi power còn `0,64` nếu tác động thật `+5 điểm`, đủ 3 luật dừng 4 vế và phương án rollback 30 phút.
  - Cập nhật Mục 4 (chỉ số chính `82,83%`, dùng `27,12%`, an toàn `4,25%`), Mục 7 (3 rủi ro kinh tế định lượng) và dòng **Đề xuất: Go có điều kiện** kèm 5 điều kiện bắt buộc có người phụ trách và ngày kiểm tra rõ ràng.

## 4. Bằng chứng

- **File trực tiếp phụ trách và biên tập:**
  - [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md): hoàn chỉnh 7 mục, đúng 1 trang A4, đầy đủ nhãn `[simulated]`, phân định vai trò phụ trách rõ ràng, đề xuất Go có điều kiện có bằng chứng định lượng.
  - [report/team/bang_loi.md](bang_loi.md): hoàn thành 20 nhãn độc lập của Người 2, đạt đồng thuận cao, có bảng khắc phục 5 ca đo lường được.
  - Đóng góp nội dung và kiểm tra trong [report/team/group_report.md](group_report.md) và [TEAM.md](../../TEAM.md).
  - Commit trên nhánh `main`: `505d8f6`, `a4d28e3`, `79fe976`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:**
  - Tra cứu hướng dẫn Google PAIR về 5 loại lỗi dựa trên nguyên nhân gốc và rà soát các trường thông tin trong hồ sơ launch v0 theo đúng chuẩn rubric chấm Gate 2a.
  - Kiểm tra tính nhất quán giữa các file báo cáo và rà soát lỗi chính tả, định dạng bảng markdown.
- **Cách tự kiểm tra kết quả:**
  - Tự tay đọc và phân tích từng ca lỗi trong 20 ca đề bài để tự gắn nhãn độc lập trước khi đối chiếu với người 1 (không để AI tự bịa nhãn).
  - Trực tiếp kiểm tra chéo từng con số trong hồ sơ với output chạy thực tế từ `src/lab13.py` và các file chi tiết của nhóm (`bang_chi_phi.md`, `chi_so.md`).
  - Kiểm tra tính hợp lệ của hồ sơ Gate 2a theo đúng thang Rubric (đủ 7 mục, có số bất lợi, có nhãn `simulated`, vai trò chịu trách nhiệm cụ thể).

## 6. Tự đánh giá

- **Điểm làm tốt:**
  - Hoàn thành xuất sắc vai trò giữ hồ sơ: điền đều đặn từ đầu buổi qua từng checkpoint, giúp nhóm có ngay bản hồ sơ Gate 2a hoàn chỉnh trước 17:00 mà không bị dồn việc.
  - Hiểu sâu sắc bản chất kinh tế học của hệ thống (vì sao giờ nhân viên xem lại/làm lại chiếm 92,5% chi phí chứ không phải tiền token; vì sao xem lại 100% làm trợ lý đắt hơn nhân viên tự làm) và dũng cảm nêu con số bất lợi này vào hồ sơ để đạt điểm tối đa ở tiêu chí C6, C7.
  - Thực hiện nghiêm túc quy trình gắn nhãn độc lập của Google PAIR.
- **Điểm cần cải thiện:**
  - Trong các bài lab sau, cần chủ động kết nối dữ liệu giữa các thành viên sớm hơn nữa để hoàn thiện biên bản phản biện phiếu chấm hội đồng nhanh chóng hơn.
