import random
import csv

TEN_FILE_CSV = 'DuLieuNgauNhien.csv'
SO_DONG = 10
SO_PHAN_TU_TREN_DONG = 10
GIOI_HAN_SO = 100 # Giả sử các số ngẫu nhiên từ 1 đến 100

def tao_va_luu_csv():
    """Tạo tệp CSV với 10 dòng, mỗi dòng 10 số ngẫu nhiên, phân cách bằng ';'."""
    
    du_lieu = []
    for _ in range(SO_DONG):
        # Tạo 10 số ngẫu nhiên
        dong_du_lieu = [random.randint(1, GIOI_HAN_SO) for _ in range(SO_PHAN_TU_TREN_DONG)]
        du_lieu.append(dong_du_lieu)

    try:
        # Mở tệp tin để ghi (sử dụng encoding='utf-8' và newline='')
        with open(TEN_FILE_CSV, 'w', newline='', encoding='utf-8') as file:
            # Khởi tạo CSV writer, sử dụng delimiter=';'
            writer = csv.writer(file, delimiter=';')
            
            # Ghi tất cả các dòng dữ liệu vào tệp
            writer.writerows(du_lieu)
            
        print(f"✅ Đã tạo và lưu thành công tệp tin '{TEN_FILE_CSV}' với {SO_DONG} dòng.")
    except Exception as e:
        print(f"❌ Lỗi khi ghi tệp: {e}")

# Gọi hàm để tạo tệp
tao_va_luu_csv()