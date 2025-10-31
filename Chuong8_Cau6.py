from tkinter import *

# Khởi tạo cửa sổ chính
root = Tk()
root.title("frame 2") # Đặt tiêu đề cửa sổ theo hình mẫu

# Thiết lập padding chung cho cửa sổ
root.config(padx=10, pady=10)

# Danh sách các kiểu relief cần hiển thị
relief_styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

borderwidth_values = [0, 1, 2, 3, 4]

# --- Vòng lặp để tạo các hàng nút ---

for r, bw in enumerate(borderwidth_values):
    # Tạo một Label ở cột 0 để hiển thị giá trị borderwidth
    label_bw = Label(root, text=f"borderwidth = {bw}", anchor="w", width=15)
    label_bw.grid(row=r, column=0, padx=5, pady=5, sticky="w")
    
    # Vòng lặp để tạo 6 nút trên mỗi hàng
    for c, relief_style in enumerate(relief_styles):
        
        # Tạo Button
        btn = Button(
            root, 
            text=relief_style,
            relief=relief_style,   # Gán kiểu relief
            borderwidth=bw,        # Gán độ dày borderwidth
            width=10,
            height=1,
            bg='white' if relief_style != 'solid' else 'lightgray', 
            fg='black' if relief_style != 'solid' else 'black'
        )
        
        btn.grid(row=r, column=c + 1, padx=5, pady=5)


root.mainloop()