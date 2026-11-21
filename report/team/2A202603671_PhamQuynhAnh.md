# Báo cáo cá nhân — PhamQuynhAnh-2A202603671

## 1. Thông tin thành viên

- Họ tên: Phạm Quỳnh Anh
- MSSV: 2A202603671
- Email: quynhanh112125@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc kỹ đề bài, theo dõi điều kiện "Xong khi" và 5 quy tắc bắt buộc của lab xuyên suốt CP1–CP5.
- Gắn nhãn độc lập 20 ca lỗi ở CP3 theo 5 loại Google PAIR (nguyên nhân gốc), so nhãn với Người gắn nhãn 2 để tính tỉ lệ đồng thuận, thống nhất quy tắc phân biệt và điền bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- Kiểm tra tính nhất quán và đầy đủ điều kiện nộp bài của hồ sơ trước phiên duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- Kiểm tra code và số liệu CP1–CP2 mới pull (`src/lab13.py`, `report/team/bang_chi_phi.md`), đối chiếu đạt đủ 3 phép thử A1 (`1,20 · 1,25 · 1,25`) và khớp số A2, A3, A4, B1–B4.
- Kiểm tra điều kiện "Xong khi" cho CP4–CP5: xác nhận `report/team/pilot_plan.yaml` hợp lệ với `yaml.safe_load`, không còn dấu `?` ngoài dòng chú thích, đủ 3 luật dừng 4 vế; xác nhận `report/team/chi_so.md` khớp 3 chỉ số (`82,83%`, `27,12%`, `4,25%`) và có 10 event gắn `trace_id`.
- Soạn bảng khắc phục 5 ca đại diện đủ 5 loại Google PAIR (Ca 9, 7, 18, 4, 17) trong `report/team/bang_loi.md` (giữ trống 2 cột nhãn độc lập để điền kết quả gắn thật).
- Tổng hợp hồ sơ 7 mục `report/team/ho_so_launch_v0.md` (đề xuất `Go có điều kiện`), soạn `report/team/group_report.md` và cập nhật `TEAM.md`.

## 4. Bằng chứng

- Các file đã cập nhật/kiểm tra: `report/team/bang_loi.md`, `report/team/ho_so_launch_v0.md`, `report/team/group_report.md`, `TEAM.md`, `report/team/2A202603671_PhamQuynhAnh.md`.
- Kiểm tra xác nhận đã chạy: 3 phép thử A1 ĐẠT, đối chiếu số liệu A2–E1 từ `logix_runs.csv` và `logix_requests.csv`, kiểm tra cú pháp YAML và quét `?` trên `report/team/pilot_plan.yaml`, quét không có từ cấm trên toàn bộ `report/team/`.
- Commit: `[cập nhật mã commit sau khi push]`.

## 5. Công cụ AI đã dùng

- Công cụ: Trợ lý AI trong IDE (Antigravity).
- Mục đích sử dụng: Tóm tắt đề bài và luồng nghiệp vụ LogiX-VN, rà soát code đồng đội pull về (`src/lab13.py`), kiểm tra điều kiện "Xong khi" các checkpoint và soạn khung bảng khắc phục/hồ sơ nhóm.
- Cách tự kiểm tra: Chạy lệnh kiểm tra trực tiếp trên `logix_runs.csv` và `logix_requests.csv` để đối chiếu toàn bộ số liệu A1–E1 theo công thức chuẩn; kiểm tra hợp lệ `yaml.safe_load` và quét từ cấm; tự gắn nhãn độc lập 20 ca lỗi cùng Người gắn nhãn 2 (không dùng AI bịa bộ nhãn hay kết quả duyệt chéo).

## 6. Tự đánh giá

- Mức độ hoàn thành: Nắm vững mô hình chi phí thật (bao gồm giờ nhân viên xem lại/làm lại và chi phí cố định), phân biệt nguyên nhân gốc khi gắn nhãn lỗi, và cách kiểm tra điều kiện tách tác động + cỡ mẫu cụm cho pilot.
- Việc cần chốt tiếp: Hoàn tất ghép 2 bộ nhãn độc lập 20 ca trong `bang_loi.md` và cập nhật trạng thái Mục 5 ở `ho_so_launch_v0.md`, cài `statsmodels` vào `.venv` để chạy kiểm tra trọn vẹn `src/lab13.py` trên máy cá nhân, bổ sung thông tin cá nhân/thành viên còn thiếu, và tham gia duyệt chéo Gate 2a lúc 17:00.
