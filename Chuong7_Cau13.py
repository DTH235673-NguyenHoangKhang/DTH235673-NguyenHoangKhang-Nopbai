NHOM_THIET_BI = {
    'n1': 'Nhóm 1',
    'n2': 'Nhóm 2',
    'n3': 'Nhóm 3',
    # ...
}
DANH_SACH_THIET_BI = [
    {'ma': 'tb1', 'ten': 'Thiết bị 1', 'manhom': 'n1'},
    {'ma': 'tb2', 'ten': 'Thiết bị 2', 'manhom': 'n1'},
    {'ma': 'tb3', 'ten': 'Thiết bị 3', 'manhom': 'n2'},
    # ...
]
import xml.etree.ElementTree as ET
from collections import defaultdict

# --- Dữ liệu giả lập (thay cho việc đọc file) ---

# Giả lập dữ liệu từ nhomthietbi.xml
NHOM_THIET_BI_DICT = {
    'n1': 'Nhóm Máy tính',
    'n2': 'Nhóm Thiết bị mạng',
    'n3': 'Nhóm Thiết bị ngoại vi',
    'n4': 'Nhóm Phần mềm',
}

# Giả lập dữ liệu từ ThietBi.xml
DANH_SACH_THIET_BI = [
    {'ma': 'tb1', 'ten': 'Laptop Dell', 'manhom': 'n1'},
    {'ma': 'tb2', 'ten': 'Máy chủ HP', 'manhom': 'n1'},
    {'ma': 'tb3', 'ten': 'Switch Cisco', 'manhom': 'n2'},
    {'ma': 'tb4', 'ten': 'Router TP-Link', 'manhom': 'n2'},
    {'ma': 'tb5', 'ten': 'Chuột Quang', 'manhom': 'n3'},
    {'ma': 'tb6', 'ten': 'Phần mềm Kế toán', 'manhom': 'n4'},
    {'ma': 'tb7', 'ten': 'Màn hình AOC', 'manhom': 'n3'},
    {'ma': 'tb8', 'ten': 'Máy tính để bàn', 'manhom': 'n1'},
    {'ma': 'tb9', 'ten': 'Chuột không dây', 'manhom': 'n3'},
]

# --- HÀM HỖ TRỢ (Nếu bạn cần đọc XML thật) ---
def doc_xml_thiet_bi(file_path):
    """
    Hàm mẫu để đọc dữ liệu từ ThietBi.xml nếu bạn có file thật.
    Cần đảm bảo file XML của bạn tuân thủ cấu trúc.
    """
    tree = ET.parse(file_path)
    root = tree.getroot()
    
    ds_thiet_bi = []
    # Lặp qua tất cả các thẻ <thietbi>
    for thietbi_element in root.findall('thietbi'):
        # Lấy manhom từ thuộc tính (ví dụ trong hình, manhom nằm trong thẻ <thietbi manhom="n1">)
        # Nếu manhom là thẻ con: manhom_val = thietbi_element.find('manhom').text
        
        # Dựa trên cấu trúc mẫu trong hình: <thietbi manhom="n1">
        manhom_val = thietbi_element.attrib.get('manhom')
        
        ds_thiet_bi.append({
            'manhom': manhom_val,
            'ma': thietbi_element.find('ma').text,
            'ten': thietbi_element.find('ten').text
        })
    return ds_thiet_bi

# --- 1. HIỂN THỊ DANH SÁCH NHÓM THIẾT BỊ ---
def hien_thi_nhom_thiet_bi():
    """Hiển thị Mã và Tên của tất cả các nhóm thiết bị."""
    print("\n=== 1️⃣ DANH SÁCH NHÓM THIẾT BỊ ===")
    print(f"{'Mã Nhóm':<10} | {'Tên Nhóm'}")
    print("-" * 30)
    for ma, ten in NHOM_THIET_BI_DICT.items():
        print(f"{ma:<10} | {ten}")
    print("====================================")

# --- 2. HIỂN THỊ TOÀN BỘ THIẾT BỊ ---
def hien_thi_toan_bo_thiet_bi():
    """Hiển thị tất cả thiết bị cùng với Tên Nhóm tương ứng."""
    print("\n=== 2️⃣ TOÀN BỘ DANH SÁCH THIẾT BỊ ===")
    print(f"{'Mã TB':<8} | {'Tên Thiết Bị':<20} | {'Mã Nhóm':<8} | {'Tên Nhóm'}")
    print("-" * 60)
    for tb in DANH_SACH_THIET_BI:
        # Lấy Tên Nhóm từ Dictionary
        ten_nhom = NHOM_THIET_BI_DICT.get(tb['manhom'], "Không xác định")
        print(f"{tb['ma']:<8} | {tb['ten']:<20} | {tb['manhom']:<8} | {ten_nhom}")
    print("===============================================================")

# --- 3. LỌC DANH SÁCH THIẾT BỊ THEO NHÓM THIẾT BỊ ---
def loc_thiet_bi_theo_nhom(ma_nhom_can_loc):
    """Lọc và hiển thị các thiết bị thuộc một mã nhóm cụ thể."""
    ma_nhom_can_loc = ma_nhom_can_loc.lower()
    ten_nhom = NHOM_THIET_BI_DICT.get(ma_nhom_can_loc, "Không xác định")
    
    print(f"\n=== 3️⃣ DANH SÁCH THIẾT BỊ CỦA NHÓM '{ten_nhom}' ({ma_nhom_can_loc}) ===")
    
    # Lọc danh sách
    ds_loc = [tb for tb in DANH_SACH_THIET_BI if tb['manhom'] == ma_nhom_can_loc]
    
    if not ds_loc:
        print(f"❌ Không tìm thấy thiết bị nào thuộc nhóm '{ten_nhom}'.")
        return
        
    print(f"{'Mã TB':<8} | {'Tên Thiết Bị'}")
    print("-" * 30)
    for tb in ds_loc:
        print(f"{tb['ma']:<8} | {tb['ten']}")
    print("====================================")


# --- 4. XUẤT NHÓM THIẾT BỊ CÓ SỐ LƯỢNG THIẾT BỊ NHIỀU NHẤT ---
def xuat_nhom_co_so_luong_nhieu_nhat():
    """Đếm số lượng thiết bị trong mỗi nhóm và tìm nhóm có số lượng lớn nhất."""
    
    # 1. Đếm số lượng thiết bị cho mỗi nhóm
    dem_so_luong = defaultdict(int)
    for tb in DANH_SACH_THIET_BI:
        dem_so_luong[tb['manhom']] += 1
        
    if not dem_so_luong:
        print("\n❌ Danh sách thiết bị rỗng, không thể xác định nhóm có số lượng nhiều nhất.")
        return
        
    # 2. Tìm mã nhóm có số lượng lớn nhất
    # max() với key=dem_so_luong.get sẽ tìm key (mã nhóm) có giá trị (số lượng) lớn nhất
    ma_nhom_max = max(dem_so_luong, key=dem_so_luong.get)
    so_luong_max = dem_so_luong[ma_nhom_max]
    ten_nhom_max = NHOM_THIET_BI_DICT.get(ma_nhom_max, "Không xác định")
    
    # 3. Tìm các nhóm có cùng số lượng tối đa (nếu có)
    nhom_max = [
        (ma, NHOM_THIET_BI_DICT.get(ma, "Không xác định"), so_luong_max)
        for ma, so_luong in dem_so_luong.items() if so_luong == so_luong_max
    ]

    print("\n=== 4️⃣ NHÓM CÓ SỐ LƯỢNG THIẾT BỊ NHIỀU NHẤT ===")
    for ma, ten, sl in nhom_max:
         print(f"🥇 Nhóm: **{ten}** (Mã: {ma}) với **{sl}** thiết bị.")
    print("=========================================================")

# --- CHẠY CHƯƠNG TRÌNH ---
# 1. Hiển thị danh sách nhóm
hien_thi_nhom_thiet_bi()

# 2. Hiển thị toàn bộ thiết bị
hien_thi_toan_bo_thiet_bi()

# 3. Lọc danh sách thiết bị theo một nhóm cụ thể (Ví dụ: n1)
loc_thiet_bi_theo_nhom('n1')

# 4. Xuất nhóm có số lượng thiết bị nhiều nhất
xuat_nhom_co_so_luong_nhieu_nhat()