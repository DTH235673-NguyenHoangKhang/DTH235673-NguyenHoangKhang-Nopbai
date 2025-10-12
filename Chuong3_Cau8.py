#Cau8
a=int(input("Moi nhap so a: ") )
b=int(input("Moi nhap so b: ") )
pheptoan=input("Moi nhap phep toan (+,-,*,/): ")
if pheptoan=="+":
    print(f"{a}+{b}={a+b}")
elif pheptoan=="-":
    print(f"{a}-{b}={a-b}")
elif pheptoan=="*":
    print(f"{a}*{b}={a*b}")
else:
    if b==0:
        print("Khong the chia cho 0")
    else:
        print(f"{a}/{b}={a/b}")
