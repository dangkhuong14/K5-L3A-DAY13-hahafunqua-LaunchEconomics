# Báo cáo cá nhân — MaiDangKhuong-2A202603627

## 1. Thông tin thành viên

- Họ tên: Mai Đăng Khương
- MSSV: 2A202603627
- Email: 26ai.khuongmd@vinuni.edu.vn
- Vai trong nhóm: Người viết code (CP1–CP2, trước giải lao)

## 2. Phần việc phụ trách

- **Người viết code CP1–CP2:** viết và chạy `src/lab13.py` cho Nhiệm vụ A (mô hình chi phí mỗi việc thành công) và Nhiệm vụ B (bảng độ nhạy); in số cho `report/team/bang_chi_phi.md` để người kiểm số đối chiếu.
- **CP3:** hỗ trợ trong lúc hai người gắn nhãn làm độc lập (không trao đổi với họ trong 8 phút gắn nhãn); hoàn thiện số B còn thiếu.
- **Bàn giao sau giải lao:** bàn giao vai viết code cho người kiểm số (Lê Xuân Phúc) để làm CP4–CP5: giải thích hàm `mo_hinh`, tham số `max_lan_chay` và chỗ `TODO CP4`.

## 3. Đóng góp cụ thể

- **A1 · Ba hàm công thức:** `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` theo E[số lần chạy] = (1 − (1 − p)^k) / p. Ba phép thử đáp án biết trước ĐẠT: 1,20 · 1,25 · 1,25.
- **A2 · `mo_hinh(runs, reqs, ...)`:** tính chi phí từ trace, tử số cộng mọi lần chạy (kể cả lần lỗi), mẫu số chỉ đếm việc `thanh_cong`. Kết quả: chi phí mỗi việc thành công **4.472 đ** [simulated] = 16,3× hoá đơn token + tool 274,7 đ; giờ nhân viên (xem lại 40,7% + làm lại 51,8%) chiếm 92,5% tổng chi phí; chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× baseline 12.000 đ [simulated].
- **A3 · Theo loại:** `noi_dia` 0,22× · `hang_nang` 0,69× · `quoc_te` 1,88× · `doi_tac` 0,85× baseline; thêm bảng tỉ lệ ok theo lần thử cho thấy chạy lại không cứu được `quoc_te` (30,0% → 11,4% → 2,2%).
- **A4 · Chi phí cố định 40 tr/tháng** cho phạm vi `noi_dia` + `hang_nang`: 4.599 đ = 0,38× (đủ khối lượng) · 5.784 đ = 0,48× (một nửa khối lượng) [simulated].
- **B1 · 9 kịch bản đổi từng yếu tố**, có tự kiểm tra tính tuyến tính trong code (kịch bản "giảm một nửa" = −½ kịch bản "gấp đôi").
- **B2 · Đổi một cặp** (giá token ×2 + xem lại ×2): 6.543 đ (+46,3%) = tổng hai tác động riêng; xếp hạng 3 yếu tố nhạy nhất: làm lại (+51,8%) > xem lại (+40,7%) > lương nhân viên (+23,1%); giá token chỉ +5,6%.
- **B3 · Giới hạn 1, 2, 3 lần chạy:** cài `max_lan_chay` trong `mo_hinh` (yêu cầu vượt giới hạn chuyển sang nhân viên); chi phí cả hệ thống thấp nhất ở giới hạn 2 lần (6.901.220 đ) [simulated]; giới hạn 1 lần cho cps thấp nhất nhưng đẩy thêm 85 việc sang nhân viên.
- **B4 · Xem lại 100%** cho `noi_dia` + `hang_nang`: 11.743 đ = 0,98× (1,03× nếu làm lại mất 15,3 phút); điểm hoà vốn 5,1 phút xem lại mỗi yêu cầu [simulated] — xem lại toàn bộ gần như xoá hết phần tiết kiệm.

## 4. Bằng chứng

- Commit trên nhánh `main`:
  - `178e37b` Tạo 3 hàm cho CP1 (`src/lab13.py`)
  - `d4b20fc` Ghi vào bảng chi phí sau khi chạy (`report/team/bang_chi_phi.md`)
  - `81cd484` Làm CP2 và bảng chi phí (`src/lab13.py`, `report/team/bang_chi_phi.md`)
- File: [src/lab13.py](../../src/lab13.py) (các mục A1–A4, B1–B4 trong `main`), [report/team/bang_chi_phi.md](bang_chi_phi.md).
- Chạy lại được: `cd src` → `python lab13.py` in ba phép thử ĐẠT và toàn bộ bảng A1–B4.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (trợ lý AI lập trình).
- **Dùng vào việc:** gợi ý cách viết hàm `mo_hinh` bằng pandas, cách cài giới hạn số lần chạy cho B3, lập checklist theo checkpoint để không bỏ sót yêu cầu.
- **Tự kiểm tra:**
  - Chạy `python lab13.py` từ đầu đến cuối, ba phép thử A1 phải in ĐẠT.
  - Tính tay đối chiếu một số con số: cps = 4.373.585 / 978 ≈ 4.472 đ; A1 với p = 0,8, k = 2: (1 − 0,2²) / 0,8 = 1,20.
  - Kiểm tra tính tuyến tính của mô hình bằng `assert` trong code (B1) và kiểm tra B2 bằng tổng hai tác động riêng.
  - So số A2, A3, B1 với đáp án tham chiếu, lệch không quá 2%.
  - Đọc CSV yêu cầu với `keep_default_na=False`, không sửa file dữ liệu; các số giả lập đều gắn nhãn `simulated`.

## 6. Tự đánh giá

- **Làm tốt:** code CP1–CP2 chạy được, có chú thích theo từng mục, số khớp đáp án; hàm `mo_hinh` viết đủ tham số nên CP2 chỉ cần gọi lại với tham số khác, và người viết code sau giải lao tiếp quản được ngay.
- **Cần cải thiện:** tôi tự điền luôn `bang_chi_phi.md` trong khi theo `TEAM.md` việc điền bảng là của người kiểm số; lần sau cần bám đúng phân vai để người kiểm số tự tính tay và điền, giữ vai trò đối chiếu độc lập với code.
