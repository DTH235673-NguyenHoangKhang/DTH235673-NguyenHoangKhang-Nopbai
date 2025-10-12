#Cau3
from math import sqrt
print("Chuong trinh giai phuong trinh bac 2")
a=float(input("Moi nhap he so a: "))
b=float(input("Moi nhap he so b: "))    
c=float(input("Moi nhap he so c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phuong trinh vo so nghiem")
        else:
            print("Phuong trinh vo nghiem")
    else:
        x=-c/b
        print(f"Phuong trinh co 1 nghiem x={x}")
else:
    delta = b*b-4*a*c
    if delta<0:
        print("Phuong trinh vo nghiem")
    elif delta==0:
        x=-b/(2*a)
        print(f"Phuong trinh co nghiem kep x1=x2={x}")
    else:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print(f"Phuong trinh co 2 nghiem phan biet x1={x1} va x2={x2}")