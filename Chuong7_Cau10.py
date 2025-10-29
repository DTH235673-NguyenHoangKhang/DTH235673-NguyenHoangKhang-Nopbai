import json
import os

# --- CẤU HÌNH TỆP DỮ LIỆU ---
DATA_FILE = 'students_data.json'

# --- CẤU TRÚC DỮ LIỆU CHÍNH (GLOBAL) ---
# Đây là danh sách các lớp học, mỗi lớp là một dictionary
CLASSES = [] 

# ====================================================================
# --- CÁC HÀM XỬ LÝ TỆP JSON ---
# ====================================================================

def doc_du_lieu_json():
    """Đọc dữ liệu từ tệp JSON."""
    global CLASSES
    
    if not os.path.exists(DATA_FILE):
        print("📣 Tệp dữ liệu không tồn tại. Bắt đầu với dữ liệu trống.")
        return

    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            CLASSES = json.load(f)
        print(f"✅ Đã đọc dữ liệu thành công từ {DATA_FILE}. Tổng {len(CLASSES)} lớp học.")
    except json.JSONDecodeError:
        print("❌ Lỗi: Tệp JSON không hợp lệ. Khởi tạo dữ liệu trống.")
        CLASSES = []
    except Exception as e:
        print(f"❌ Lỗi khi đọc tệp dữ liệu: {e}")

def luu_du_lieu_json():
    """Ghi dữ liệu vào tệp JSON."""
    global CLASSES
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            # Ghi dữ liệu với indent=4 để dễ đọc hơn
            json.dump(CLASSES, f, ensure_ascii=False, indent=4) 
        print(f"✅ Đã lưu tất cả dữ liệu thành công vào {DATA_FILE}.")
    except Exception as e:
        print(f"❌ Lỗi khi lưu tệp dữ liệu: {e}")

# ====================================================================
# --- CÁC HÀM HỖ TRỢ TÌM KIẾM ---
# ====================================================================

def tim_lop_theo_ma(ma_lop):
    """Tìm dictionary Lớp học theo mã."""
    for lop in CLASSES:
        if lop['ma_lop'].upper() == ma_lop.upper():
            return lop
    return None

def tim_sv_theo_ma(ma_sv):
    """Tìm dictionary Sinh viên theo mã trong tất cả các lớp."""
    for lop in CLASSES:
        for sv in lop['sinh_vien']:
            if sv['ma_sv'].upper() == ma_sv.upper():
                # Trả về cả sinh viên và lớp chứa sinh viên đó
                return sv, lop
    return None, None

# ====================================================================
# --- CÁC HÀM CHÍNH (CRUD) ---
# ====================================================================

# --- 1. THÊM MỚI ---
def them_lop():
    """Thêm Lớp học mới."""
    ma = input("Nhập Mã Lớp: ").upper()
    if tim_lop_theo_ma(ma):
        print(f"❌ Lỗi: Mã lớp '{ma}' đã tồn tại.")
        return
    
    ten = input("Nhập Tên Lớp: ")
    CLASSES.append({'ma_lop': ma, 'ten_lop': ten, 'sinh_vien': []})
    print(f"✅ Đã thêm lớp mới: Mã={ma}, Tên={ten}")

def them_sv():
    """Thêm Sinh viên mới."""
    ma_sv = input("Nhập Mã SV: ").upper()
    if tim_sv_theo_ma(ma_sv)[0]:
        print(f"❌ Lỗi: Mã sinh viên '{ma_sv}' đã tồn tại.")
        return
    
    ten_sv = input("Nhập Tên SV: ")
    
    try:
        nam_sinh = int(input("Nhập Năm sinh (VD: 2003): "))
    except ValueError:
        print("❌ Lỗi: Năm sinh phải là số nguyên.")
        return

    ma_lop = input("Nhập Mã Lớp thuộc về: ").upper()
    lop = tim_lop_theo_ma(ma_lop)
    
    if not lop:
        print(f"❌ Lỗi: Mã Lớp '{ma_lop}' không tồn tại. Vui lòng thêm Lớp trước.")
        return
            
    sv_moi = {'ma_sv': ma_sv, 'ten_sv': ten_sv, 'nam_sinh': nam_sinh}
    lop['sinh_vien'].append(sv_moi)
    print(f"✅ Đã thêm sinh viên mới: {ten_sv} ({ma_sv}) vào lớp {lop['ten_lop']}.")

# --- 2. SỬA ---
def sua_du_lieu():
    """Sửa thông tin Lớp hoặc Sinh viên."""
    item_type = input("Sửa (L)ớp hay (S)inh viên? (L/S): ").upper()
    ma = input(f"Nhập Mã {item_type} cần sửa: ").upper()
    
    if item_type == 'L':
        lop = tim_lop_theo_ma(ma)
        if not lop:
            print(f"❌ Lỗi: Mã lớp '{ma}' không tồn tại.")
            return
        new_ten = input(f"Nhập Tên Lớp mới (hiện tại: {lop['ten_lop']}): ")
        lop['ten_lop'] = new_ten
        print(f"✅ Đã cập nhật Tên lớp '{ma}' thành '{new_ten}'.")
        
    elif item_type == 'S':
        sv, lop = tim_sv_theo_ma(ma)
        if not sv:
            print(f"❌ Lỗi: Mã sinh viên '{ma}' không tồn tại.")
            return
        
        print(f"--- Thông tin SV hiện tại: {sv['ten_sv']} | Năm sinh: {sv['nam_sinh']} | Lớp: {lop['ten_lop']}")
        
        new_ten = input("Nhập Tên SV mới (Bỏ qua nếu không đổi): ")
        if new_ten:
            sv['ten_sv'] = new_ten
            
        new_nam_sinh_str = input("Nhập Năm sinh mới (Bỏ qua nếu không đổi): ")
        if new_nam_sinh_str:
            try:
                sv['nam_sinh'] = int(new_nam_sinh_str)
            except ValueError:
                print("❌ Lỗi: Năm sinh mới không hợp lệ. Thao tác sửa năm sinh bị hủy.")
                return

        print(f"✅ Đã cập nhật SV '{ma}'.")
    else:
        print("Lựa chọn không hợp lệ.")

# --- 3. XÓA ---
def xoa_du_lieu():
    """Xóa Lớp hoặc Sinh viên."""
    global CLASSES
    item_type = input("Xóa (L)ớp hay (S)inh viên? (L/S): ").upper()
    ma = input(f"Nhập Mã {item_type} cần xóa: ").upper()
    
    if item_type == 'L':
        lop = tim_lop_theo_ma(ma)
        if not lop:
            print(f"❌ Lỗi: Mã lớp '{ma}' không tồn tại.")
            return
        
        sv_count = len(lop['sinh_vien'])
        
        # Lọc lại danh sách lớp, giữ lại những lớp có mã khác
        CLASSES[:] = [l for l in CLASSES if l['ma_lop'] != ma]
        
        print(f"✅ Đã xóa Lớp '{ma}' và {sv_count} sinh viên thuộc lớp đó.")

    elif item_type == 'S':
        sv, lop = tim_sv_theo_ma(ma)
        if not sv:
            print(f"❌ Lỗi: Mã sinh viên '{ma}' không tồn tại.")
            return
        
        # Lọc lại danh sách sinh viên trong lớp đó, xóa SV có mã cần xóa
        lop['sinh_vien'][:] = [s for s in lop['sinh_vien'] if s['ma_sv'] != ma]
        print(f"✅ Đã xóa Sinh viên '{ma}' - {sv['ten_sv']} khỏi lớp {lop['ten_lop']}.")
        
    else:
        print("Lựa chọn không hợp lệ.")

# --- 4. TÌM KIẾM VÀ SẮP XẾP ---
def tim_kiem_sv():
    """Tìm kiếm sinh viên theo Tên hoặc Mã trong tất cả các lớp."""
    keyword = input("Nhập từ khóa (Mã, Tên SV hoặc Năm sinh): ").lower().strip()
    results = []
    
    for lop in CLASSES:
        for sv in lop['sinh_vien']:
            search_str = f"{sv['ma_sv']} {sv['ten_sv']} {sv['nam_sinh']}".lower()
            if keyword in search_str:
                results.append((sv, lop)) # Lưu cả SV và Lớp
            
    print(f"\n🔎 Tìm thấy {len(results)} kết quả:")
    for sv, lop in results:
        print(f"  [SV] Mã: {sv['ma_sv']} | Tên: {sv['ten_sv']:<20} | NS: {sv['nam_sinh']} | Lớp: {lop['ten_lop']} ({lop['ma_lop']})")

def hien_thi_all():
    """Hiển thị tất cả lớp và sinh viên, có sắp xếp."""
    
    # 1. Sắp xếp Danh sách Lớp theo Mã
    classes_sorted = sorted(CLASSES, key=lambda l: l['ma_lop'])
    
    print("-" * 70)
    print(f"TỔNG QUAN DỮ LIỆU ({len(CLASSES)} LỚP)")
    print("-" * 70)
    
    for lop in classes_sorted:
        ma_lop = lop['ma_lop']
        ten_lop = lop['ten_lop']
        
        # 2. Sắp xếp Sinh viên trong Lớp theo Tên
        # Tên SV là thuộc tính được ưu tiên sắp xếp
        sv_sorted = sorted(lop['sinh_vien'], key=lambda sv: sv['ten_sv'].lower())
        
        print(f"[LỚP] Mã: {ma_lop} | Tên: {ten_lop:<30} | Số lượng SV: {len(sv_sorted)}")
        
        if not sv_sorted:
            print("  (Lớp này chưa có sinh viên nào)")
        else:
            for sv in sv_sorted:
                print(f"  [SV] Mã: {sv['ma_sv']} | Tên: {sv['ten_sv']:<20} | Năm sinh: {sv['nam_sinh']}")
        print("-" * 70)

# ====================================================================
# --- CHƯƠNG TRÌNH CHÍNH (MAIN FUNCTION) ---
# ====================================================================

def main():
    doc_du_lieu_json() # Tự động đọc dữ liệu JSON khi khởi động
    
    while True:
        print("\n" * 2)
        print("=" * 60)
        print("PHẦN MỀM QUẢN LÝ SINH VIÊN (SỬ DỤNG JSON)")
        print("=" * 60)
        print("1. Thêm mới Lớp học")
        print("2. Thêm mới Sinh viên")
        print("3. Sửa thông tin (Lớp hoặc Sinh viên)")
        print("4. Xóa thông tin (Lớp hoặc Sinh viên)")
        print("5. Hiển thị tất cả (Lớp theo Mã, SV theo Tên)")
        print("6. Tìm kiếm Sinh viên")
        print("7. Lưu dữ liệu và Thoát")
        print("8. Chỉ Thoát (Không Lưu)")
        print("-" * 60)
        
        choice = input("Nhập lựa chọn của bạn (1-8): ")

        if choice == '1':
            them_lop()
        elif choice == '2':
            them_sv()
        elif choice == '3':
            sua_du_lieu()
        elif choice == '4':
            xoa_du_lieu()
        elif choice == '5':
            hien_thi_all()
        elif choice == '6':
            tim_kiem_sv()
        elif choice == '7':
            luu_du_lieu_json()
            print("Thoát chương trình. Tạm biệt!")
            break
        elif choice == '8':
            print("Thoát chương trình mà không lưu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 8.")

if __name__ == "__main__":
    main()
