"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.

Trạng thái: CP1 (A1–A4) và CP2 (B1–B4) xong. CP4 (D), CP5 (E1) viết tiếp ở các dòng TODO trong main.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)

# Dùng cho A4 (chi phí cố định)
CHI_PHI_CO_DINH_THANG = 40_000_000   # đồng / tháng
YEU_CAU_MOI_THANG = 45_000           # 1.500 yêu cầu/ngày × 30 ngày
PHAM_VI_PILOT = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Mỗi lần chạy đúng với xác suất p, độc lập; chạy tối đa k lần, dừng ngay khi đúng.
#   Lần thứ i được chạy khi i−1 lần trước đều sai: P = (1−p)^(i−1)
#   E[số lần chạy] = Σ_{i=1..k} (1−p)^(i−1) = (1 − (1−p)^k) / p      (k → ∞: 1/p)
#   P(thành công)  = 1 − (1−p)^k                                      (k → ∞: 1)
#   Hệ số chi phí  = E[số lần chạy] / P(thành công) = 1/p  (k triệt tiêu)
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# CP2 gọi lại hàm này với tham số giá và hệ số đã đổi (mỗi kịch bản = 1 lần gọi).
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    Thêm: chay_lai (token + tool của lần chạy thứ 2, 3), hoa_don_moi_yc ((token + tool) / số yêu cầu),
          so_yeu_cau, khong_thanh_cong.
    """
    reqs = reqs.copy()   # không sửa DataFrame gốc của người gọi
    # Chỉ giữ các lần chạy thuộc tập yêu cầu đang xét → gọi với reqs đã lọc (A3, A4) là đủ.
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    if max_lan_chay is not None:   # B1, B3: giới hạn số lần chạy
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        # Yêu cầu cần nhiều lần hơn giới hạn → không thành công, chuyển nhân viên, không còn phút xem lại/làm lại
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # Tử số: MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn tốn token và tool). Giá tính cho 1.000 token.
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    # Giờ nhân viên — SIMULATED
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai

    token, tool = tien_token.sum(), tien_tool.sum()
    tong = token + tool + xem_lai + lam_lai
    # Mẫu số: chỉ đếm yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(
        token=token,
        tool=tool,
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        so_yeu_cau=len(reqs),
        thanh_cong=thanh_cong,
        khong_thanh_cong=len(reqs) - thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(token + tool) / len(reqs),
    )


# ---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------
def bang_theo_loai(runs, reqs):
    """Mỗi giá trị cột loai: số yêu cầu, tỉ lệ thành công, lần chạy/yêu cầu, cps [simulated], so với BASELINE."""
    dong = []
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        con = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, con)
        dong.append(dict(
            loai=loai,
            so_yeu_cau=len(con),
            ti_le_thanh_cong=kq['thanh_cong'] / len(con),
            lan_chay_moi_yc=con['so_lan_chay'].mean(),
            cps=kq['cps'],
            so_voi_baseline=kq['cps'] / BASELINE,
        ))
    return pd.DataFrame(dong)


def ti_le_ok_theo_lan_thu(runs, reqs):
    """Tỉ lệ status == 'ok' theo loai × attempt: chạy lại có giúp không?"""
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m['status'] == 'ok').astype(float)
    return m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')


# ---------- Nhiệm vụ A4 · Chi phí cố định ----------
def chi_phi_co_dinh(runs, reqs, he_so_khoi_luong=1.0):
    """Cộng chi phí cố định 40 tr/tháng vào cps của phạm vi pilot (noi_dia + hang_nang).
    he_so_khoi_luong = 1.0 cho 45.000 yêu cầu/tháng; 0.5 cho một nửa khối lượng."""
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    kq = mo_hinh(runs, pv)
    # Tỉ lệ thành công đo trên TOÀN mẫu 1.200 (giả định: trợ lý chỉ nhận phần việc trong phạm vi)
    viec_tc_thang = YEU_CAU_MOI_THANG * he_so_khoi_luong * kq['thanh_cong'] / len(reqs)
    co_dinh_moi_viec = CHI_PHI_CO_DINH_THANG / viec_tc_thang
    tong_moi_viec = kq['cps'] + co_dinh_moi_viec
    return dict(he_so_khoi_luong=he_so_khoi_luong, viec_tc_thang=viec_tc_thang,
                cps_pham_vi=kq['cps'], co_dinh_moi_viec=co_dinh_moi_viec,
                tong_moi_viec=tong_moi_viec, so_voi_baseline=tong_moi_viec / BASELINE,
                tong_pham_vi=kq['tong'], thanh_cong_pham_vi=kq['thanh_cong'])


# ---------- Nhiệm vụ B · Bảng độ nhạy ----------
# Mỗi kịch bản = một lần gọi mo_hinh với MỘT tham số đổi (B1) hoặc một cặp (B2).
KICH_BAN_B1 = {
    'Giá token gấp đôi':          dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa':     dict(gia_vao=13, gia_ra=65),
    'Tỉ lệ xem lại gấp đôi':      dict(he_so_xem_lai=2),
    'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Số ca làm lại gấp đôi':      dict(he_so_lam_lai=2),
    'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương nhân viên tăng 25%':   dict(luong_phut=2500),
    'Chỉ cho chạy tối đa 2 lần':  dict(max_lan_chay=2),
    'Chỉ cho chạy 1 lần':         dict(max_lan_chay=1),
}


def bang_do_nhay(runs, reqs, kich_ban=KICH_BAN_B1):
    """B1/B2: cps [simulated] và % thay đổi so với gốc A2 cho từng kịch bản."""
    goc = mo_hinh(runs, reqs)['cps']
    dong = [dict(kich_ban='Gốc (A2)', cps=goc, thay_doi=0.0)]
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        dong.append(dict(kich_ban=ten, cps=cps, thay_doi=(cps / goc - 1) * 100))
    return pd.DataFrame(dong)


def bang_gioi_han_chay(runs, reqs, cac_gioi_han=(1, 2, 3)):
    """B3: chi phí cả hệ thống = tổng chi phí trợ lý + BASELINE × số yêu cầu không thành công
    (nhân viên phải làm thay các yêu cầu đó)."""
    dong = []
    for k in cac_gioi_han:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        dong.append(dict(gioi_han=k, tong_tro_ly=kq['tong'], khong_thanh_cong=kq['khong_thanh_cong'],
                         ca_he_thong=kq['tong'] + kq['khong_thanh_cong'] * BASELINE, cps=kq['cps']))
    return pd.DataFrame(dong)


def xem_lai_toan_bo(runs, reqs, phut_xem_moi_yc=5, phut_lam_moi_ca=9, luong_phut=LUONG_PHUT):
    """B4: phạm vi noi_dia + hang_nang, nhân viên xem lại MỌI yêu cầu có ít nhất một lần chạy ok.
    Chi phí = token + tool (mọi lần chạy) + xem lại (phut_xem_moi_yc/yc) + làm lại (phut_lam_moi_ca/ca lam_lai).
    Trả thêm mức hoà vốn: số phút xem lại tối đa để chi phí mỗi việc thành công ≤ BASELINE."""
    pv = reqs[reqs['loai'].isin(PHAM_VI_PILOT)]
    r = runs[runs['request_id'].isin(pv['request_id'])]
    token_tool = (r['tokens_in'] / 1000 * GIA_VAO + r['tokens_out'] / 1000 * GIA_RA).sum() \
        + (r['tool_calls'] * GIA_TOOL).sum()
    yc_co_ok = r.loc[r['status'] == 'ok', 'request_id'].nunique()
    ca_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    thanh_cong = int((pv['ket_qua'] == 'thanh_cong').sum())
    tien_xem = yc_co_ok * phut_xem_moi_yc * luong_phut
    tien_lam = ca_lam_lai * phut_lam_moi_ca * luong_phut
    tong = token_tool + tien_xem + tien_lam
    cps = tong / thanh_cong
    hoa_von_phut_xem = (BASELINE * thanh_cong - token_tool - tien_lam) / (yc_co_ok * luong_phut)
    return dict(so_yeu_cau=len(pv), yc_co_ok=yc_co_ok, ca_lam_lai=ca_lam_lai, thanh_cong=thanh_cong,
                phut_lam_moi_ca=phut_lam_moi_ca, token_tool=token_tool, tien_xem=tien_xem, tien_lam=tien_lam,
                tong=tong, cps=cps, so_voi_baseline=cps / BASELINE, hoa_von_phut_xem=hoa_von_phut_xem)


def in_tieu_de(chu):
    print(f'\n===== {chu} =====')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)   # bắt buộc keep_default_na=False

    # ----- A1 -----
    in_tieu_de('A1 · Ba phép thử')
    kiem_tra_dap_an_biet_truoc()
    print(f"  p=0,8 tối đa 2 lần  : {so_lan_chay_ky_vong(0.8, 2):.2f} lần chạy")
    print(f"  p=0,8 đến khi đúng  : {so_lan_chay_ky_vong(0.8):.2f} lần chạy")
    print(f"  hệ số cps tối đa 3  : {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f} × giá một lần chạy")

    # ----- A2 -----
    in_tieu_de('A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated)')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    phut_xem = reqs['phut_xem_lai_simulated'].sum()
    phut_lam = reqs['phut_lam_lai_simulated'].sum()
    gio_nv = ket_qua['xem_lai'] + ket_qua['lam_lai']
    print(f"  Số lần gọi tool         : {runs['tool_calls'].sum():,}")
    print(f"  Phút xem lại / làm lại  : {phut_xem:,} / {phut_lam:,} phút [simulated]")
    print(f"  cps / hoá đơn mỗi yc    : {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần")
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"  Tỉ trọng {k:8s}       : {ket_qua[k] / ket_qua['tong'] * 100:5.1f}%")
    print(f"  Giờ nhân viên           : {gio_nv / ket_qua['tong'] * 100:5.1f}% tổng chi phí [simulated]")
    # So với nhân viên tự làm: cộng phần nhân viên làm thay các ca không thành công
    he_thong = (ket_qua['tong'] + ket_qua['khong_thanh_cong'] * BASELINE) / ket_qua['so_yeu_cau']
    print(f"  Chi phí cả hệ thống/yc  : ({ket_qua['tong']:,.0f} + {ket_qua['khong_thanh_cong']} × {BASELINE:,}) "
          f"/ {ket_qua['so_yeu_cau']:,} = {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× [simulated]")

    # ----- A3 -----
    in_tieu_de('A3 · Theo loại yêu cầu (cps: simulated)')
    a3 = bang_theo_loai(runs, reqs)
    print(a3.to_string(index=False, formatters={
        'ti_le_thanh_cong': '{:.1%}'.format, 'lan_chay_moi_yc': '{:.2f}'.format,
        'cps': '{:,.0f}'.format, 'so_voi_baseline': '{:.2f}x'.format}))
    print('\n  Tỉ lệ ok theo lần thử (attempt):')
    print(ti_le_ok_theo_lan_thu(runs, reqs).map(lambda v: f'{v:.1%}' if pd.notna(v) else '-').to_string())

    # ----- A4 -----
    in_tieu_de('A4 · Chi phí cố định 40 tr/tháng, phạm vi noi_dia + hang_nang (simulated)')
    for hs in [1.0, 0.5]:
        a4 = chi_phi_co_dinh(runs, reqs, hs)
        print(f"  Khối lượng ×{hs:<3}: {a4['viec_tc_thang']:,.0f} việc TC/tháng · cố định {a4['co_dinh_moi_viec']:,.0f} đ/việc · "
              f"cps phạm vi {a4['cps_pham_vi']:,.0f} ({a4['tong_pham_vi']:,.0f} / {a4['thanh_cong_pham_vi']}) "
              f"→ {a4['tong_moi_viec']:,.0f} đ = {a4['so_voi_baseline']:.2f}×")

    # ----- B1 -----
    in_tieu_de('B1 · Đổi từng yếu tố (cps: simulated)')
    b1 = bang_do_nhay(runs, reqs)
    print(b1.to_string(index=False, formatters={'cps': '{:,.0f}'.format, 'thay_doi': '{:+.1f}%'.format}))
    # Tự kiểm tra tuyến tính: "giảm một nửa" = −½ × "gấp đôi"
    td = b1.set_index('kich_ban')['thay_doi']
    for x2, x05 in [('Giá token gấp đôi', 'Giá token giảm một nửa'),
                    ('Tỉ lệ xem lại gấp đôi', 'Tỉ lệ xem lại giảm một nửa'),
                    ('Số ca làm lại gấp đôi', 'Số ca làm lại giảm một nửa')]:
        assert abs(td[x05] + td[x2] / 2) < 1e-6, f'Không tuyến tính: {x2} / {x05}'
    print('  Tự kiểm tra: mỗi kịch bản "giảm một nửa" = −½ kịch bản "gấp đôi": ĐẠT')

    # ----- B2 -----
    in_tieu_de('B2 · Đổi một cặp và xếp hạng (simulated)')
    goc = ket_qua['cps']
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = td['Giá token gấp đôi'] + td['Tỉ lệ xem lại gấp đôi']
    print(f"  Giá token ×2 + xem lại ×2 : {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) "
          f"= tổng hai tác động riêng {tong_rieng:+.1f}%")
    # Xếp hạng theo mức tăng của kịch bản "gấp đôi"/"tăng" (cùng là thay đổi tương đối lớn của mỗi yếu tố)
    xep_hang = td[['Số ca làm lại gấp đôi', 'Tỉ lệ xem lại gấp đôi', 'Lương nhân viên tăng 25%',
                   'Giá token gấp đôi']].sort_values(ascending=False)
    for i, (ten, v) in enumerate(xep_hang.items(), 1):
        print(f'  {i}. {ten:28s} {v:+.1f}%')

    # ----- B3 -----
    in_tieu_de('B3 · Giới hạn chạy lại và chi phí cả hệ thống (simulated)')
    b3 = bang_gioi_han_chay(runs, reqs)
    print(b3.to_string(index=False, formatters={'tong_tro_ly': '{:,.0f}'.format, 'ca_he_thong': '{:,.0f}'.format,
                                                'cps': '{:,.0f}'.format}))
    re_nhat = b3.loc[b3['ca_he_thong'].idxmin()]
    cps_thap = b3.loc[b3['cps'].idxmin()]
    them_nv = int(cps_thap['khong_thanh_cong'] - re_nhat['khong_thanh_cong'])
    print(f"  Rẻ nhất cho công ty: {int(re_nhat['gioi_han'])} lần ({re_nhat['ca_he_thong']:,.0f} đ); "
          f"cps thấp nhất: {int(cps_thap['gioi_han'])} lần → đẩy thêm {them_nv} việc sang nhân viên")

    # ----- B4 -----
    in_tieu_de('B4 · Xem lại 100%, phạm vi noi_dia + hang_nang (simulated)')
    lam_lai_ca = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f"  Phút làm lại thực tế mỗi ca lam_lai (toàn mẫu): TB {lam_lai_ca.mean():.1f} · trung vị {lam_lai_ca.median():.1f}")
    for phut_lam in [9, round(lam_lai_ca.mean(), 1)]:
        b4 = xem_lai_toan_bo(runs, reqs, phut_lam_moi_ca=phut_lam)
        print(f"  Làm lại {phut_lam} phút/ca: {b4['yc_co_ok']} yc có run ok × 5 phút = {b4['tien_xem']:,.0f} · "
              f"{b4['ca_lam_lai']} ca làm lại = {b4['tien_lam']:,.0f} · token+tool {b4['token_tool']:,.0f}")
        print(f"      → tổng {b4['tong']:,.0f} / {b4['thanh_cong']} = {b4['cps']:,.0f} đ = {b4['so_voi_baseline']:.2f}× · "
              f"hoà vốn khi xem lại ≤ {b4['hoa_von_phut_xem']:.1f} phút/yc")
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
    # TODO CP5 · Nhiệm vụ E1: ba chỉ số (chính, dùng, an toàn).
