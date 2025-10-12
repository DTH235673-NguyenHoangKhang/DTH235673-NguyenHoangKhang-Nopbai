#Cau11
while True:
    n=int(input("Nhap mot so nguyen duong: "))
    demo=0
    for i in range(1,n+1):
        if n%i==0:
            demo+=1
    if demo==2:
        print(f"{n} la so nguyen to")
    else:
        print(f"{n} khong phai la so nguyen to")
    tieptuc=input("Ban co muon tiep tuc khong (y/n): ")
    if tieptuc.lower()=="n":
        break   
print("Cam on ban da su dung chuong trinh")