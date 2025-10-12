#Cau7
print("Chuong trinh tim ngay")
ngay=int(input("Moi nhap vao ngay: "))
thang=int(input("Moi nhap vao thang: "))
nam=int(input("Moi nhap vao nam: "))
if thang in [1,3,5,7,8,10,12]:
    if ngay==31:
        thang+=1
        if thang>12:
            thang=1
            nam+=1
        print(f"1/{thang}/{nam}")
    else: 
        ngay+=1
        print(f"{ngay}/{thang}/{nam}")
elif thang in [4,6,9,11]:
    if ngay==30:
        thang+=1
        if thang>12:
            thang=1
            nam+=1
        print(f"1/{thang}/{nam}")
    else: 
        ngay+=1
        print(f"{ngay}/{thang}/{nam}")

elif thang==2:
    if (nam%4==0 and nam%100!=0) or (nam%400==0):
        if ngay==29:
            thang+=1
            if thang>12:
                thang=1
                nam+=1
            print(f"1/{thang}/{nam}")
    else:
        if ngay==28:
            thang+=1
            if thang>12:
                thang=1
                nam+=1
            print(f"1/{thang}/{nam}")
else:
    ngay+=1
    print(f"{ngay}/{thang}/{nam}")