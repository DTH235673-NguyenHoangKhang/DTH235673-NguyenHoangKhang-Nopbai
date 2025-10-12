bai5 = "Câu 5: Thao tác với danh sách (List) trong Python\n"
bai5 += "\n"

bai5 += "(a) lst = [20, 1, -34, 40, -8, 60, 1, 3]\n"
bai5 += "→ Khởi tạo danh sách gồm 8 phần tử.\n\n"

bai5 += "(b) lst[0:3] = [20, 1, -34]\n"
bai5 += "→ Cắt từ phần tử chỉ số 0 đến 2.\n\n"

bai5 += "(c) lst[4:8] = [20, 1, -34]\n"
bai5 += "→ Sai cú pháp minh hoạ, đúng ra nên là lst[4:8] = [-8, 60, 1, 3].\n\n"

bai5 += "(d) lst[4:33] = [-8, 60, 1, 3]\n"
bai5 += "→ Dù chỉ số kết thúc vượt quá độ dài danh sách, Python vẫn cắt đến phần tử cuối.\n\n"

bai5 += "(e) lst[-5:-3] = [40, -8]\n"
bai5 += "→ Cắt từ phần tử thứ 5 từ cuối đến phần tử thứ 3 từ cuối.\n\n"

bai5 += "(f) lst[-22:3] = [20, 1, -34]\n"
bai5 += "→ Vì chỉ số bắt đầu nhỏ hơn giới hạn âm của danh sách, nên sẽ tính từ đầu danh sách.\n\n"

bai5 += "(g) lst[4:] = [-8, 60, 1, 3]\n"
bai5 += "→ Cắt từ phần tử chỉ số 4 đến hết danh sách.\n\n"

bai5 += "(h) lst[:] = [20, 1, -34, 40, -8, 60, 1, 3]\n"
bai5 += "→ Sao chép toàn bộ danh sách.\n\n"

bai5 += "(i) lst[:4] = [20, 1, -34, 40]\n"
bai5 += "→ Cắt từ đầu đến phần tử chỉ số 3.\n\n"

bai5 += "(j) lst[1:5] = [1, -34, 40, -8]\n"
bai5 += "→ Cắt từ phần tử chỉ số 1 đến 4.\n\n"

bai5 += "(k) -34 in lst = True\n"
bai5 += "→ Kiểm tra phần tử -34 có trong danh sách, kết quả True.\n\n"

bai5 += "(l) -34 not in lst = False\n"
bai5 += "→ Kiểm tra phần tử -34 không có trong danh sách, kết quả False.\n\n"

bai5 += "(m) len(lst) = 8\n"
bai5 += "→ Trả về độ dài của danh sách (8 phần tử).\n"

print(bai5)
