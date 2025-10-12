#Cau18
n=int(input("Moi nhap so nguyen duong n: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
    
n=int(input("Moi nhap so nguyen duong n: "))
for i in range(1,n+1):
    print("* "*i)
    
n=int(input("Moi nhap so nguyen duong n: "))
for i in range(1,n+1):
    print(" " * (n-1) + "* " * i)