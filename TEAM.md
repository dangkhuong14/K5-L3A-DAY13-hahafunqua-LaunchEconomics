# Team

## Thông tin nhóm

- Tên nhóm: hahafunqua
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-hahafunqua-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/dangkhuong14/K5-L3A-DAY13-hahafunqua-LaunchEconomics`, nhánh `main`, commit chốt: `[cập nhật sau commit cuối]`

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Phạm Quỳnh Anh | 2A202603671 | quynhanh112125@gmail.com | phamquynhanh-17 | Người gắn nhãn 1 |
|   2 | [điền họ tên] | [điền MSSV] | khuongmaidev@gmail.com | dangkhuong14 | Người viết code (CP1–CP2) |
|   3 | Lê Xuân Phúc | 2A202603655 | 26ai.phuclx@vinuni.edu.vn | [điền GitHub] | Người kiểm số (CP1–CP2) / Đổi vai Người viết code (CP4–CP5) |
|   4 | Trần Quốc Đông | 2A202603643 | 26ai.dongtq@vinuni.edu.vn | dongtranquoc951 | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## PhamQuynhAnh-2A202603671

### Phần việc phụ trách

- Người gắn nhãn 1: đọc đề, theo dõi điều kiện "Xong khi" và 5 quy tắc của lab qua CP1–CP5; gắn nhãn độc lập 20 ca lỗi ở CP3, so nhãn tính đồng thuận và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`; kiểm tra nhất quán hồ sơ trước Gate 2a.

### Đóng góp cụ thể

- Kiểm tra logic và số liệu CP1–CP2 (`src/lab13.py`, `report/team/bang_chi_phi.md`) và rà soát điều kiện "Xong khi" của CP4–CP5 (`report/team/pilot_plan.yaml`, `report/team/chi_so.md`).
- Soạn bảng khắc phục 5 ca đại diện đủ 5 loại Google PAIR có event/ngưỡng đo được trong `report/team/bang_loi.md` (chờ ghép 2 bộ nhãn độc lập thật).
- Tổng hợp hồ sơ 7 mục `report/team/ho_so_launch_v0.md`, `report/team/group_report.md` và cập nhật `TEAM.md`.

### Bằng chứng

- File đóng góp/kiểm tra: `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`, `report/team/2A202603671_PhamQuynhAnh.md`.
- Kiểm tra đối chiếu: 3 phép thử A1 ĐẠT, kiểm tra `yaml.safe_load` và quét `?` trên `report/team/pilot_plan.yaml`, quét từ cấm toàn `report/team/`.
- Commit: `ebadedc` (chỉnh sửa tiếp theo cập nhật `TEAM.md`, `group_report.md`, email cá nhân).

## LeXuanPhuc-2A202603655

### Phần việc phụ trách

- Người kiểm số (CP1–CP2) và đổi vai Người viết code sau giải lao (CP4–CP5); hoàn thiện `report/team/pilot_plan.yaml` và `report/team/chi_so.md`.

### Đóng góp cụ thể

- Đối chiếu toàn bộ số liệu A1–A4, B1–B4 trong `report/team/bang_chi_phi.md`.
- Cài đặt `co_mau(...)`, `tinh_chi_so_e1(...)` và khối tính D1, E1 trong `src/lab13.py`; hoàn thiện `report/team/pilot_plan.yaml` (3 luật dừng 4 vế, rollback 30 phút, MDE +6 điểm) và `report/team/chi_so.md` (3 chỉ số thử, 2 chỉ số tự đề xuất, 10 event có `trace_id`, 3 rủi ro kinh tế).

### Bằng chứng

- Commit `a3e5ff7` (`src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`) và `9212897` (`report/team/2A202603655_LeXuanPhuc.md`).

## TranQuocDong-MSSV

### Phần việc phụ trách

- Người gắn nhãn 2, kiêm giữ hồ sơ: quản lý và liên tục hoàn thiện trang hồ sơ launch `report/team/ho_so_launch_v0.md` từ CP1–CP5; gắn nhãn độc lập 20 ca lỗi ở CP3, đối chiếu đồng thuận và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`; tham gia duyệt chéo Gate 2a.

### Đóng góp cụ thể

- Điền dần 7 mục của `report/team/ho_so_launch_v0.md` qua từng checkpoint, đảm bảo đúng 1 trang, đủ nhãn `[simulated]`, không có từ cấm `production`, và nêu rõ các con số bất lợi (xem lại 100%, power 0,64).
- Độc lập gắn nhãn 20 ca lỗi CP3 theo 5 loại Google PAIR, đạt đồng thuận cao (≥ 80%), ghi rõ quy tắc phân biệt cho ca 6 và 18, phối hợp lập bảng khắc phục 5 ca có event đo lường và vai trò phụ trách.
- Cùng nhóm rà soát tính nhất quán số liệu toàn bộ hồ sơ nhóm và đóng góp ý kiến trong `report/team/group_report.md`.

### Bằng chứng

- File trực tiếp phụ trách: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md` (Nhãn người 2 và bảng khắc phục), báo cáo cá nhân `report/team/MSSV_TranQuocDong.md`.
