#Cau1
print("Chuong trinh kiem tra nam nhuan")
year=int(input("Moi nhap vao 1 nam: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(f"Nam {year} la nam nhuan")
else:
    print(f"Nam {year} khong nhuan")