import os

# --- CẤU HÌNH TỆP DỮ LIỆU ---
DATA_FILE_DM = 'danh_muc.txt' # Tệp lưu danh mục
DATA_FILE_SP = 'san_pham.txt' # Tệp lưu sản phẩm
DELIMITER = '|' 

# --- CẤU TRÚC DỮ LIỆU ĐƠN GIẢN (GLOBAL) ---
# Danh sách chứa các dictionary: [{'ma': 'TH', 'ten': 'Thời trang'}, ...]
DANH_MUC = [] 
# Danh sách chứa các dictionary: [{'ma': 'IP12', 'ten': 'iPhone 12', 'gia': 18000000.0, 'ma_dm': 'DT'}, ...]
SAN_PHAM = [] 

# ====================================================================
# --- CÁC HÀM XỬ LÝ TỆP VÀ DỮ LIỆU ---
# ====================================================================

def doc_du_lieu():
    """Đọc dữ liệu từ hai tệp TEXT: danh_muc.txt và san_pham.txt."""
    global DANH_MUC, SAN_PHAM
    
    # 1. Đọc Danh Mục
    if os.path.exists(DATA_FILE_DM):
        try:
            with open(DATA_FILE_DM, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            temp_dm = []
            for line in lines:
                line = line.strip()
                if not line: continue
                parts = line.split(DELIMITER)
                if len(parts) == 2:
                    temp_dm.append({'ma': parts[0], 'ten': parts[1]})
            DANH_MUC = temp_dm
            print(f"✅ Đã đọc {len(DANH_MUC)} Danh mục.")
        except Exception as e:
            print(f"❌ Lỗi khi đọc tệp Danh mục: {e}")
    else:
        print(f"📣 Tệp {DATA_FILE_DM} không tồn tại. DM trống.")

    # 2. Đọc Sản Phẩm
    if os.path.exists(DATA_FILE_SP):
        try:
            with open(DATA_FILE_SP, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            temp_sp = []
            for line in lines:
                line = line.strip()
                if not line: continue
                parts = line.split(DELIMITER)
                if len(parts) == 4:
                    try:
                        temp_sp.append({
                            'ma': parts[0], 
                            'ten': parts[1], 
                            'gia': float(parts[2]), 
                            'ma_dm': parts[3]
                        })
                    except ValueError:
                        print(f"Lỗi: Giá không hợp lệ cho sản phẩm có mã {parts[0]}")
            SAN_PHAM = temp_sp
            print(f"✅ Đã đọc {len(SAN_PHAM)} Sản phẩm.")
        except Exception as e:
            print(f"❌ Lỗi khi đọc tệp Sản phẩm: {e}")
    else:
        print(f"📣 Tệp {DATA_FILE_SP} không tồn tại. SP trống.")

def luu_du_lieu():
    """Ghi dữ liệu từ DANH_MUC và SAN_PHAM vào hai tệp TEXT."""
    global DANH_MUC, SAN_PHAM
    
    # 1. Ghi Danh Mục
    try:
        with open(DATA_FILE_DM, 'w', encoding='utf-8') as f:
            for dm in DANH_MUC:
                f.write(f"{dm['ma']}{DELIMITER}{dm['ten']}\n")
        print(f"✅ Đã lưu {len(DANH_MUC)} Danh mục vào {DATA_FILE_DM}.")
    except Exception as e:
        print(f"❌ Lỗi khi lưu tệp Danh mục: {e}")

    # 2. Ghi Sản Phẩm
    try:
        with open(DATA_FILE_SP, 'w', encoding='utf-8') as f:
            for sp in SAN_PHAM:
                f.write(f"{sp['ma']}{DELIMITER}{sp['ten']}{DELIMITER}{sp['gia']}{DELIMITER}{sp['ma_dm']}\n")
        print(f"✅ Đã lưu {len(SAN_PHAM)} Sản phẩm vào {DATA_FILE_SP}.")
    except Exception as e:
        print(f"❌ Lỗi khi lưu tệp Sản phẩm: {e}")

# --- CÁC HÀM HỖ TRỢ CRUD ---

def tim_dm_theo_ma(ma):
    """Tìm danh mục trong DANH_MUC theo mã."""
    for dm in DANH_MUC:
        if dm['ma'] == ma:
            return dm
    return None

def tim_sp_theo_ma(ma):
    """Tìm sản phẩm trong SAN_PHAM theo mã."""
    for sp in SAN_PHAM:
        if sp['ma'] == ma:
            return sp
    return None

def dem_sp_thuoc_dm(ma_dm):
    """Đếm số lượng sản phẩm thuộc một danh mục."""
    count = 0
    for sp in SAN_PHAM:
        if sp['ma_dm'] == ma_dm:
            count += 1
    return count

# --- CÁC HÀM CHÍNH (CRUD VÀ TÌM KIẾM/SẮP XẾP) ---

def them_dm():
    """Thêm Danh mục mới."""
    ma = input("Nhập Mã DM: ").upper()
    if tim_dm_theo_ma(ma):
        print(f"❌ Lỗi: Mã danh mục '{ma}' đã tồn tại.")
        return
    
    ten = input("Nhập Tên DM: ")
    DANH_MUC.append({'ma': ma, 'ten': ten})
    print(f"✅ Đã thêm danh mục mới: Mã={ma}, Tên={ten}")

def them_sp():
    """Thêm Sản phẩm mới."""
    ma = input("Nhập Mã SP: ").upper()
    if tim_sp_theo_ma(ma):
        print(f"❌ Lỗi: Mã sản phẩm '{ma}' đã tồn tại.")
        return
    
    ten = input("Nhập Tên SP: ")
    
    try:
        gia = float(input("Nhập Đơn giá: "))
    except ValueError:
        print("❌ Lỗi: Đơn giá phải là một số.")
        return

    ma_dm = input("Nhập Mã DM thuộc về: ").upper()
    if not tim_dm_theo_ma(ma_dm):
        print(f"❌ Lỗi: Mã danh mục '{ma_dm}' không tồn tại. Vui lòng thêm DM trước.")
        return
            
    SAN_PHAM.append({'ma': ma, 'ten': ten, 'gia': gia, 'ma_dm': ma_dm})
    print(f"✅ Đã thêm sản phẩm mới: Mã={ma}, Tên={ten}, Giá={gia:,.0f} VNĐ")

def sua_du_lieu():
    """Sửa thông tin Danh mục hoặc Sản phẩm."""
    item_type = input("Sửa (D)anh mục hay (S)ản phẩm? (D/S): ").upper()
    ma = input(f"Nhập Mã {item_type} cần sửa: ").upper()
    
    if item_type == 'D':
        dm = tim_dm_theo_ma(ma)
        if not dm:
            print(f"❌ Lỗi: Mã danh mục '{ma}' không tồn tại.")
            return
        new_ten = input(f"Nhập Tên Danh mục mới (hiện tại: {dm['ten']}): ")
        dm['ten'] = new_ten
        print(f"✅ Đã cập nhật Tên danh mục '{ma}' thành '{new_ten}'.")
        
    elif item_type == 'S':
        sp = tim_sp_theo_ma(ma)
        if not sp:
            print(f"❌ Lỗi: Mã sản phẩm '{ma}' không tồn tại.")
            return
        
        print(f"--- Thông tin SP hiện tại: {sp['ten']} | {sp['gia']:,.0f} VNĐ | DM: {sp['ma_dm']}")
        
        new_ten = input("Nhập Tên SP mới (Bỏ qua nếu không đổi): ")
        if new_ten:
            sp['ten'] = new_ten
            
        new_gia_str = input("Nhập Giá mới (Bỏ qua nếu không đổi): ")
        if new_gia_str:
            try:
                sp['gia'] = float(new_gia_str)
            except ValueError:
                print("❌ Lỗi: Giá mới không hợp lệ. Thao tác sửa giá bị hủy.")
                return

        new_ma_dm = input("Nhập Mã DM mới (Bỏ qua nếu không đổi): ").upper()
        if new_ma_dm and new_ma_dm != sp['ma_dm']:
            if not tim_dm_theo_ma(new_ma_dm):
                print(f"❌ Lỗi: Mã danh mục mới '{new_ma_dm}' không tồn tại.")
                return
            sp['ma_dm'] = new_ma_dm
            print(f"🔄 Đã chuyển SP '{ma}' sang DM '{new_ma_dm}'.")

        print(f"✅ Đã cập nhật SP '{ma}'.")
    else:
        print("Lựa chọn không hợp lệ.")

def xoa_du_lieu():
    """Xóa Danh mục hoặc Sản phẩm."""
    global DANH_MUC, SAN_PHAM
    item_type = input("Xóa (D)anh mục hay (S)ản phẩm? (D/S): ").upper()
    ma = input(f"Nhập Mã {item_type} cần xóa: ").upper()
    
    if item_type == 'D':
        dm = tim_dm_theo_ma(ma)
        if not dm:
            print(f"❌ Lỗi: Mã danh mục '{ma}' không tồn tại.")
            return

        # Lọc lại danh sách sản phẩm, giữ lại những SP không thuộc DM này
        sp_truoc = len(SAN_PHAM)
        SAN_PHAM = [sp for sp in SAN_PHAM if sp['ma_dm'] != ma]
        sp_da_xoa = sp_truoc - len(SAN_PHAM)
        
        # Lọc lại danh sách danh mục, xóa DM này
        DANH_MUC = [dm for dm in DANH_MUC if dm['ma'] != ma]
        
        print(f"✅ Đã xóa Danh mục '{ma}' và {sp_da_xoa} sản phẩm liên quan.")

    elif item_type == 'S':
        sp = tim_sp_theo_ma(ma)
        if not sp:
            print(f"❌ Lỗi: Mã sản phẩm '{ma}' không tồn tại.")
            return
        
        # Lọc lại danh sách sản phẩm, giữ lại những SP có mã khác
        SAN_PHAM = [sp_item for sp_item in SAN_PHAM if sp_item['ma'] != ma]
        print(f"✅ Đã xóa Sản phẩm '{ma}' - {sp['ten']}.")
        
    else:
        print("Lựa chọn không hợp lệ.")

def tim_kiem_sp():
    """Tìm kiếm sản phẩm theo Tên hoặc Mã."""
    keyword = input("Nhập từ khóa (Mã hoặc Tên SP): ").lower().strip()
    results = []
    
    for sp in SAN_PHAM:
        if keyword in sp['ten'].lower() or keyword in sp['ma'].lower():
            results.append(sp)
            
    print(f"\n🔎 Tìm thấy {len(results)} kết quả:")
    for sp in results:
        print(f"  [SP] Mã: {sp['ma']} | Tên: {sp['ten']:<15} | Giá: {sp['gia']:,.0f} VNĐ | DM: {sp['ma_dm']}")
    
def hien_thi_all():
    """Hiển thị tất cả danh mục và sản phẩm (sắp xếp theo mã danh mục)."""
    
    # 1. Sắp xếp Danh mục theo mã (sử dụng sorted() với lambda)
    dm_sorted = sorted(DANH_MUC, key=lambda dm: dm['ma'])
    
    print("-" * 60)
    print(f"TỔNG QUAN DỮ LIỆU ({len(DANH_MUC)} DM, {len(SAN_PHAM)} SP)")
    print("-" * 60)
    
    for dm in dm_sorted:
        ma_dm = dm['ma']
        ten_dm = dm['ten']
        
        # Đếm và in Danh mục
        so_luong_sp = dem_sp_thuoc_dm(ma_dm)
        print(f"[DM] Mã: {ma_dm} | Tên: {ten_dm:<20} | Số lượng SP: {so_luong_sp}")
        
        # Lọc và Sắp xếp Sản phẩm thuộc Danh mục này (sắp xếp theo Tên SP)
        sp_trong_dm = [sp for sp in SAN_PHAM if sp['ma_dm'] == ma_dm]
        sp_sorted = sorted(sp_trong_dm, key=lambda sp: sp['ten'].lower())
        
        if not sp_sorted:
            print("  (Danh mục này chưa có sản phẩm nào)")
        else:
            for sp in sp_sorted:
                print(f"  [SP] Mã: {sp['ma']} | Tên: {sp['ten']:<15} | Giá: {sp['gia']:,.0f} VNĐ")
        print("-" * 60)

# ====================================================================
# --- CHƯƠNG TRÌNH CHÍNH (MAIN FUNCTION) ---
# ====================================================================

def main():
    doc_du_lieu() # Tự động đọc dữ liệu khi khởi động
    
    while True:
        print("\n" * 2)
        print("=" * 40)
        print("QUẢN LÝ SẢN PHẨM (CODE ĐƠN GIẢN)")
        print("=" * 40)
        print("1. Thêm mới Danh mục")
        print("2. Thêm mới Sản phẩm (Yêu cầu DM đã tồn tại)")
        print("3. Sửa/Xóa dữ liệu")
        print("4. Hiển thị tất cả SP theo DM (Có sắp xếp theo Tên SP)")
        print("5. Tìm kiếm Sản phẩm (theo Mã hoặc Tên)")
        print("6. Lưu dữ liệu và Thoát")
        print("7. Chỉ Thoát (Không Lưu)")
        print("-" * 40)
        
        choice = input("Nhập lựa chọn của bạn (1-7): ")

        if choice == '1':
            them_dm()
        elif choice == '2':
            them_sp()
        elif choice == '3':
            sua_xoa_choice = input("Bạn muốn (1) Sửa hay (2) Xóa? (1/2): ")
            if sua_xoa_choice == '1':
                sua_du_lieu()
            elif sua_xoa_choice == '2':
                xoa_du_lieu()
            else:
                print("Lựa chọn không hợp lệ.")
        elif choice == '4':
            hien_thi_all()
        elif choice == '5':
            tim_kiem_sp()
        elif choice == '6':
            luu_du_lieu()
            print("Thoát chương trình. Tạm biệt!")
            break
        elif choice == '7':
            print("Thoát chương trình mà không lưu. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 7.")

if __name__ == "__main__":
    main()
