import pandas as pd
import os # Dùng để kiểm tra file tồn tại

TEN_FILE = 'NhanVien.xlsx'

# --- 1. Tạo hoặc Đọc File ---
def doc_du_lieu(ten_file):
    """Đọc dữ liệu từ file Excel, nếu file chưa có thì trả về DataFrame rỗng."""
    if os.path.exists(ten_file):
        # Đảm bảo cột Tuổi là số nguyên khi đọc
        df = pd.read_excel(ten_file, dtype={'Tuổi': int})
        return df
    else:
        # Tạo DataFrame rỗng với cấu trúc mong muốn
        return pd.DataFrame(columns=['STT', 'Mã', 'Tên', 'Tuổi'])

# --- 2. Lưu Nhân Viên (Thêm mới) ---
def luu_nhan_vien(ma, ten, tuoi):
    df = doc_du_lieu(TEN_FILE)
    
    # Tạo dữ liệu mới
    du_lieu_moi = {'Mã': ma, 'Tên': ten, 'Tuổi': int(tuoi)}
    
    # Thêm dữ liệu mới vào DataFrame
    # ignore_index=True để tự động thêm index mới
    df = pd.concat([df, pd.DataFrame([du_lieu_moi])], ignore_index=True)
    
    # Cập nhật cột STT (STT = index + 1)
    df['STT'] = df.index + 1
    
    # Lưu lại vào file Excel
    df.to_excel(TEN_FILE, index=False) # index=False để không ghi cột index của pandas vào file
    print(f"✅ Đã thêm nhân viên {ten} ({ma}) vào file.")

# --- 3. Đọc và Hiển Thị Danh Sách ---
def doc_danh_sach():
    df = doc_du_lieu(TEN_FILE)
    if df.empty:
        print("❌ Danh sách nhân viên trống.")
    else:
        print("\n=== 📋 DANH SÁCH NHÂN VIÊN HIỆN TẠI ===")
        print(df.to_string(index=False)) # Hiển thị không kèm index của pandas
        print("========================================\n")

# --- 4. Sắp xếp Nhân viên theo Tuổi tăng dần ---
def sap_xep_theo_tuoi():
    df = doc_du_lieu(TEN_FILE)
    if df.empty:
        print("❌ Không có dữ liệu để sắp xếp.")
        return

    # Sắp xếp theo cột 'Tuổi' tăng dần (ascending=True)
    df_sorted = df.sort_values(by='Tuổi', ascending=True)
    
    # Cập nhật lại cột STT theo thứ tự mới sau khi sắp xếp
    df_sorted['STT'] = range(1, len(df_sorted) + 1)
    
    print("\n=== 📈 DANH SÁCH NHÂN VIÊN SẮP XẾP THEO TUỔI TĂNG DẦN ===")
    print(df_sorted.to_string(index=False))
    print("==============================================================\n")
    
    # Tùy chọn: Ghi kết quả sắp xếp lại vào file (nếu cần)
    # df_sorted.to_excel(TEN_FILE, index=False)
    # print("✅ Đã cập nhật file Excel theo thứ tự tuổi tăng dần.")


# --- VÍ DỤ SỬ DỤNG CÁC HÀM ---
# 1. Thêm một vài nhân viên
luu_nhan_vien('NV7', 'Khánh', 28)
luu_nhan_vien('NV8', 'Minh', 21)

# 2. Đọc danh sách
doc_danh_sach()

# 3. Sắp xếp và in ra
sap_xep_theo_tuoi()