from tkinter import *
from tkinter import messagebox

# Hàm xử lý khi nhấn OK
def handle_ok():
    # Lấy dữ liệu từ các ô nhập
    old_pass = entry_old.get()
    new_pass = entry_new.get()
    confirm_pass = entry_confirm.get()
    
    if new_pass == confirm_pass:
        if old_pass and new_pass: # Kiểm tra không để trống
            messagebox.showinfo("Thành công", "Mật khẩu đã được thay đổi thành công!")
            # Sau khi thành công, có thể đóng cửa sổ hoặc xóa các ô nhập
            root.destroy()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng điền đầy đủ thông tin.")
    else:
        messagebox.showerror("Lỗi", "Mật khẩu mới và xác nhận mật khẩu không khớp!")

# Hàm xử lý khi nhấn Cancel (đóng cửa sổ)
def handle_cancel():
    root.destroy()

# --- Cấu hình Cửa sổ Chính ---
root = Tk()
root.title("Enter New Password") # Đặt tiêu đề cửa sổ

# Thiết lập padding cho cửa sổ chính
root.config(padx=10, pady=10)


# --- Khởi tạo các Nhãn (Labels) ---
label_old = Label(root, text="Old Password:")
label_new = Label(root, text="New Password:")
label_confirm = Label(root, text="Enter New Password Again:")

# --- Khởi tạo các Ô Nhập (Entry Fields) ---
# Dùng 'show="*" ' để ẩn ký tự, tạo hiệu ứng mật khẩu
entry_old = Entry(root, width=30, show="*")
entry_new = Entry(root, width=30, show="*")
entry_confirm = Entry(root, width=30, show="*")

# --- Đặt vị trí các thành phần bằng Grid ---

# Các Nhãn nằm ở cột 0
label_old.grid(row=1, column=0, sticky="w", pady=5)
label_new.grid(row=2, column=0, sticky="w", pady=5)
label_confirm.grid(row=3, column=0, sticky="w", pady=5)

# Các Ô Nhập nằm ở cột 1
entry_old.grid(row=1, column=1, padx=10)
entry_new.grid(row=2, column=1, padx=10)
entry_confirm.grid(row=3, column=1, padx=10)

entry_old.focus_set()

# --- Khung chứa các Nút lệnh (Buttons) ---
frame_buttons = Frame(root)
frame_buttons.grid(row=4, column=0, columnspan=2, pady=20) # Đặt khung nút dưới cùng, chiếm 2 cột

btn_ok = Button(frame_buttons, text="OK", command=handle_ok, width=10)
btn_cancel = Button(frame_buttons, text="Cancel", command=handle_cancel, width=10)

# Đặt các nút trong khung
btn_ok.pack(side=LEFT, padx=10)
btn_cancel.pack(side=LEFT, padx=10)

root.mainloop()