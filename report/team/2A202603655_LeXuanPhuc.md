# Báo cáo cá nhân — LeXuanPhuc-2A202603655

## 1. Thông tin thành viên

- Họ tên: Lê Xuân Phúc
- MSSV: 2A202603655
- Email: 26ai.phuclx@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): người kiểm số

## 2. Phần việc phụ trách

- **Người kiểm số (CP1–CP2):** chạy kiểm chứng code `src/lab13.py` và đối chiếu số liệu A1–A4, B1–B4 trong `report/team/bang_chi_phi.md` (kiểm tra quy tắc tuyến tính, chi phí cả hệ thống, kịch bản xem lại 100%, và nhãn `simulated`).
- **Đổi vai Người viết code sau giải lao (CP4–CP5):** cài đặt phần tính cỡ mẫu pilot (Nhiệm vụ D1) và 3 chỉ số chạy thử (Nhiệm vụ E1) trong `src/lab13.py`.
- **Hoàn thiện hồ sơ kỹ thuật CP4 & CP5:** viết hoàn chỉnh `report/team/pilot_plan.yaml` (Nhiệm vụ D) và `report/team/chi_so.md` (Nhiệm vụ E1, E2).
- **Soát số & duyệt chéo cuối buổi:** rà soát tính nhất quán của số liệu trong `report/team/ho_so_launch_v0.md` và tham gia chấm chéo Gate 2a cùng nhóm.

## 3. Đóng góp cụ thể

- **CP1 & CP2 (Kiểm số):** chạy lại `src/lab13.py` sau các commit của thành viên viết code, đối chiếu đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`), bảng A2 (`4.472 đ` [simulated], gấp `16,3 lần` hoá đơn token+tool `274,7 đ`), bảng A3 (`noi_dia` `0,22×`, `hang_nang` `0,69×`, `quoc_te` `1,88×`, `doi_tac` `0,85×`), bảng A4 (`4.599 đ = 0,38×` và `5.784 đ = 0,48×`), bảng độ nhạy B1–B2 (xác nhận tính đối xứng −½ và cộng tuyến tính `+5,6% + 40,7% = +46,3%`), B3 (giới hạn 2 lần chạy rẻ nhất cho cả hệ thống `6.901.220 đ`), và B4 (`11.743 đ` với 9 phút làm lại / `12.415 đ` với 15,3 phút làm lại).
- **CP4 (Code D1 & `pilot_plan.yaml`):** viết hàm `co_mau(...)` và khối tính 5 câu D1 trong `src/lab13.py`, chỉ ra trần cỡ mẫu hiệu dụng `20 / 0,02 = 1.000 < 1.251` nên chọn chia theo nhân viên (20 + 20) chấp nhận MDE `+6` điểm (`n = 859/nhóm`, `m ≥ 299`, `DE = 6,96`, power ở mức `+5` điểm còn `0,64`). Hoàn thiện toàn bộ `report/team/pilot_plan.yaml` gồm D1, D2, 3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, phương án rollback 30 phút và danh sách `simulated_inputs`.
- **CP5 (Code E1 & `chi_so.md`):** viết hàm `tinh_chi_so_e1(...)` tính 3 chỉ số đợt chạy thử (`82,83%`, `27,12%`, `4,25%`), đề xuất thêm 2 chỉ số dùng và an toàn, đặc tả 10 event đều có `trace_id` kèm kiểm tra chéo, và lập bảng 3 rủi ro kinh tế (E2) nối trực tiếp số từ `bang_chi_phi.md`.

## 4. Bằng chứng

- **Commit trên nhánh `main`:** `a3e5ff7` (_"Hoan thanh CP4 (D1, pilot_plan.yaml) va CP5 (E1, chi_so.md)"_).
- **Code đã bổ sung:** hàm `co_mau`, `tinh_chi_so_e1` và khối in kết quả D1, E1 trong `src/lab13.py`.
- **File hồ sơ hoàn thiện:** `report/team/pilot_plan.yaml` (đọc hợp lệ bằng `yaml.safe_load`, không còn dấu `?`) và `report/team/chi_so.md`.
- **Con số đã tự kiểm chứng trên dữ liệu:** D1 (`1.251`, `3.103`, trần `1.000`, trần `300`, `m ≥ 299` với `DE = 6,96`, power `0,64` ở mức `+5` điểm); E1 (`994/1.200 = 82,83%`, `48/177 = 27,12%`, `51/1.200 = 4,25%`, và trong phạm vi `noi_dia + hang_nang`: `906/982 = 92,26%`, mở lại `39/982 = 3,97%`).

## 5. Công cụ AI đã dùng

- **Công cụ:** Antigravity (trợ lý AI trong IDE).
- **Mục đích sử dụng:** đọc và tóm tắt cấu trúc yêu cầu lab, giải thích công thức cỡ mẫu theo cụm (`DE`, trần `c / ICC`), gợi ý cấu trúc hàm D1/E1 và rà soát tiêu chí rubric cho `pilot_plan.yaml`, `chi_so.md`.
- **Cách tự kiểm tra:**
  - Chạy thực tế `python lab13.py` trong môi trường `.venv` để toàn bộ con số A1–E1 được tính từ 2 file CSV gốc và tự phát hiện/sửa lỗi thiếu hàm `co_mau` trước khi commit.
  - Chạy kiểm tra tự động: `yaml.safe_load(open('../report/team/pilot_plan.yaml'))` ra `YAML OK`, `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không còn dấu `?`, và `grep` không có kết quả vi phạm quy tắc 5.
  - Tự đối chiếu các con số với [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) và file `bang_chi_phi.md` của nhóm để đảm bảo khớp 100% và đủ nhãn `simulated`.

## 6. Tự đánh giá

- **Điểm làm tốt:** Hoàn thành đầy đủ vai trò Người kiểm số và chủ động đổi vai viết code nửa sau đúng tiến độ; hiểu rõ bản chất thống kê của việc chia cụm theo nhân viên (`20 + 20`) và lý do không đặt ngưỡng an toàn 3% khi tỉ lệ mở lại hiện tại đã là `4,25%`.
- **Điểm cần cải thiện:** Cần phối hợp sớm hơn giữa các thành viên trên Git để cập nhật `TEAM.md` và gom các phần của hồ sơ sớm hơn trước mốc duyệt chéo 17:00.
