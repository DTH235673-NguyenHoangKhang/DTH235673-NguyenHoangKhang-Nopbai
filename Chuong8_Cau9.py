from tkinter import *
from tkinter import messagebox

def calculate_bmi():
    """Hàm tính toán BMI và phân loại tình trạng cơ thể."""
    try:
        # Lấy dữ liệu từ ô nhập liệu
        height_m_str = entry_height.get()
        weight_kg_str = entry_weight.get()

        # Kiểm tra nếu ô nhập rỗng
        if not height_m_str or not weight_kg_str:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đủ Chiều cao và Cân nặng.")
            return

        # Chuyển đổi sang số thực (float)
        height = float(height_m_str)
        weight = float(weight_kg_str)

        # Kiểm tra dữ liệu hợp lệ
        if height <= 0 or weight <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và Cân nặng phải là số dương.")
            return

        # 1. Tính toán BMI
        # BMI = weight / (height * height)
        bmi_value = weight / (height ** 2)
        
        # 2. Phân loại tình trạng
        if bmi_value < 18.5:
            status = "Gầy"
            risk = "Thấp"
            risk_color = "green"
        elif 18.5 <= bmi_value < 25:
            status = "Bình thường"
            risk = "Trung bình"
            risk_color = "blue"
        elif 25 <= bmi_value < 30:
            status = "Mập"
            risk = "Hơi cao"
            risk_color = "orange"
        else: # bmi_value >= 30
            status = "Béo phì"
            risk = "Cao"
            risk_color = "red"

        # 3. Hiển thị kết quả
        # Làm tròn BMI đến 1 chữ số thập phân
        bmi_var.set(f"{bmi_value:.1f}") 
        status_var.set(status)
        risk_var.set(risk)
        
        # Thiết lập màu nền cho ô nguy cơ phát triển bệnh
        entry_risk.config(bg=risk_color, fg='white' if risk_color in ['blue', 'red'] else 'black')

    except ValueError:
        messagebox.showerror("Lỗi", "Giá trị nhập vào phải là số hợp lệ.")
    except Exception as e:
        messagebox.showerror("Lỗi", f"Đã xảy ra lỗi: {e}")

# --- Thiết lập Giao diện Tkinter ---
root = Tk()
root.title("Phần mềm tính BMI")

main_frame = Frame(root, bg='yellow', padx=20, pady=20, bd=2, relief=SOLID)
main_frame.pack(padx=10, pady=10)

bmi_var = StringVar(value="X")
status_var = StringVar(value="")
risk_var = StringVar(value="")

# --- Hàng 1: Nhập chiều cao ---
Label(main_frame, text="Nhập chiều cao:", bg='yellow').grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_height = Entry(main_frame, width=10, justify='center')
entry_height.insert(0, "1.8") # Giá trị mặc định: 1.8m
entry_height.grid(row=0, column=1, padx=5, pady=5)

# --- Hàng 2: Nhập cân nặng ---
Label(main_frame, text="Nhập cân nặng:", bg='yellow').grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_weight = Entry(main_frame, width=10, justify='center')
entry_weight.insert(0, "72") # Giá trị mặc định: 72kg
entry_weight.grid(row=1, column=1, padx=5, pady=5)

# --- Hàng 3: Nút Tính BMI ---
btn_bmi = Button(main_frame, text="Tính BMI", command=calculate_bmi)
btn_bmi.grid(row=2, column=1, padx=5, pady=10, sticky="ew") 
entry_weight.bind("<Return>", lambda event: calculate_bmi()) # Cho phép bấm Enter

# --- Hàng 4: BMI của bạn ---
Label(main_frame, text="BMI của bạn:", bg='yellow').grid(row=3, column=0, padx=5, pady=5, sticky="w")
entry_bmi = Entry(main_frame, width=10, state='readonly', textvariable=bmi_var, justify='center')
entry_bmi.grid(row=3, column=1, padx=5, pady=5)

# --- Hàng 5: Tình trạng của bạn ---
Label(main_frame, text="Tình trạng của bạn:", bg='yellow').grid(row=4, column=0, padx=5, pady=5, sticky="w")
entry_status = Entry(main_frame, width=10, state='readonly', textvariable=status_var, justify='center')
entry_status.grid(row=4, column=1, padx=5, pady=5)

# --- Hàng 6: Nguy cơ phát triển bệnh ---
Label(main_frame, text="Nguy cơ phát triển bệnh", bg='yellow').grid(row=5, column=0, padx=5, pady=5, sticky="w")
entry_risk = Entry(main_frame, width=10, state='readonly', textvariable=risk_var, justify='center')
entry_risk.grid(row=5, column=1, padx=5, pady=5)

# --- Hàng 7: Nút Thoát ---
btn_quit = Button(main_frame, text="Thoát", command=root.destroy)
btn_quit.grid(row=6, column=1, padx=5, pady=10, sticky="ew") 

root.mainloop()