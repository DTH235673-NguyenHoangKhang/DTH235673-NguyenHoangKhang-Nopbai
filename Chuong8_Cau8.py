from tkinter import *
from tkinter import messagebox

def fahrenheit_to_celsius():
    """Hàm chuyển đổi độ F sang độ C."""
    try:
        # Lấy giá trị độ F từ ô nhập liệu
        f_temp_str = entry_f.get()
        
        # Kiểm tra nếu ô nhập rỗng
        if not f_temp_str:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập giá trị độ F.")
            return

        # Chuyển đổi sang số thực (để xử lý các giá trị thập phân)
        f_temp = float(f_temp_str)

        # Áp dụng công thức chuyển đổi
        c_temp = (f_temp - 32) * (5/9)

        # Làm tròn kết quả đến 2 chữ số thập phân (tùy chọn)
        c_temp_rounded = round(c_temp, 2)

        # Cập nhật Label kết quả
        result_var.set(f"{c_temp_rounded} °C")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Giá trị nhập vào phải là một số hợp lệ.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# --- Thiết lập Giao diện Tkinter ---
root = Tk()
root.title("Chuyển đổi Độ F sang Độ C")

# Khung chính với màu nền vàng (giống đề bài)
main_frame = Frame(root, bg='yellow', padx=20, pady=20, bd=2, relief=SOLID)
main_frame.pack(padx=10, pady=10)

# --- Hàng 1: Nhập độ F ---
label_input = Label(main_frame, text="Nhập độ F", bg='yellow')
label_input.grid(row=0, column=0, padx=5, pady=10, sticky="w")

entry_f = Entry(main_frame, width=10, justify='center')
entry_f.insert(0, "350") # Giá trị mặc định theo đề bài
entry_f.grid(row=0, column=1, padx=5, pady=10)
# Gán sự kiện Enter cho ô nhập liệu
entry_f.bind("<Return>", lambda event: fahrenheit_to_celsius())

# --- Hàng 2: Nút Chuyển đổi ---
btn_convert = Button(main_frame, text="Chuyển", command=fahrenheit_to_celsius)
btn_convert.grid(row=1, column=1, padx=5, pady=10, sticky="e") 

# --- Hàng 3: Kết quả Độ C ---
label_output = Label(main_frame, text="Độ C", bg='yellow')
label_output.grid(row=2, column=0, padx=5, pady=10, sticky="w")

# Biến để lưu và cập nhật kết quả
result_var = StringVar()
# Giá trị mặc định
result_var.set("Độ C ở đây") 

result_label = Label(main_frame, textvariable=result_var, bg='yellow', font=('Arial', 10, 'bold'), fg='black')
result_label.grid(row=2, column=1, padx=5, pady=10, sticky="w")

root.mainloop()