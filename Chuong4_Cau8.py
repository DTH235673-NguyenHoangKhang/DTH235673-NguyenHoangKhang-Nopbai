#Cau8
import math
print("Chương trình tính Logarit")
a=int(input("Nhập cơ số a(a>0 và a!=1): "))
x=int(input("Nhập biến số x(x>0): "))
if a<=0 or a==1 or x<=0:
    print("Dữ liệu không hợp lệ")
else:
    log=math.log(x,a)
    print(f"Logarit cơ số {a} của {x} là: {log}")