from tkinter import *
from tkinter import messagebox

# --- Công thức và Dữ liệu Can Chi ---
CAN = ["Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ", "Canh", "Tân", "Nhâm", "Quý"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]

def convert_to_lunaryear():
    """Hàm chuyển đổi năm Dương lịch sang Can Chi."""
    try:
        # Lấy năm từ ô nhập liệu
        year_str = entry_year.get()
        
        # Kiểm tra nếu ô nhập rỗng
        if not year_str:
            messagebox.showwarning("Lỗi", "Vui lòng nhập năm Dương lịch.")
            return

        # Chuyển đổi sang số nguyên
        year = int(year_str)

        # 1. Tính Can (10 Can)
        # Lấy index của Can: (Năm - 3) chia lấy dư cho 10
        can_index = (year - 3) % 10
        ten_can = CAN[can_index-1]

        # 2. Tính Chi (12 Chi)
        # Lấy index của Chi: (Năm - 3) chia lấy dư cho 12
        chi_index = (year - 3) % 12
        ten_chi = CHI[chi_index-1]

        # Ghép Can và Chi
        lunar_year = f"{ten_can} {ten_chi}"

        # Hiển thị kết quả (cập nhật Label)
        result_var.set(lunar_year)
        
    except ValueError:
        messagebox.showerror("Lỗi", "Năm nhập vào phải là một số nguyên.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# --- Thiết lập Giao diện Tkinter ---
root = Tk()
root.title("Chuyển đổi Dương - Âm lịch")

main_frame = Frame(root, bg='yellow', padx=20, pady=20, bd=2, relief=SOLID)
main_frame.pack(padx=10, pady=10)

# --- Hàng 1: Nhập năm Dương lịch ---
label_input = Label(main_frame, text="Nhập năm dương:", bg='yellow')
label_input.grid(row=0, column=0, padx=5, pady=10, sticky="w")

entry_year = Entry(main_frame, width=10, justify='center')
entry_year.insert(0, "1982") # Giá trị mặc định theo đề bài
entry_year.grid(row=0, column=1, padx=5, pady=10)

# --- Hàng 2: Nút Chuyển đổi ---
btn_convert = Button(main_frame, text="Chuyển", command=convert_to_lunaryear)
btn_convert.grid(row=1, column=1, padx=5, pady=10, sticky="e") 
entry_year.bind("<Return>", lambda event: convert_to_lunaryear()) # Cho phép bấm Enter

# --- Hàng 3: Kết quả Năm Âm lịch ---
label_output = Label(main_frame, text="Năm âm:", bg='yellow')
label_output.grid(row=2, column=0, padx=5, pady=10, sticky="w")

# Biến để lưu và cập nhật kết quả
result_var = StringVar()
result_label = Label(main_frame, textvariable=result_var, bg='yellow', font=('Arial', 10, 'bold'), fg='black')
result_label.grid(row=2, column=1, padx=5, pady=10, sticky="w")

convert_to_lunaryear() 

root.mainloop()