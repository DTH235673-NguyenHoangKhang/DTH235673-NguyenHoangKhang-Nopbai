#Cau9
lst=[]
n=int(input("Nhập số phần tử:"))
for i in range(n):
    x=int(input("Nhập phần tử:"))
    lst.append(x)
demle=0
LstLe=[]
for x in lst:
    if x%2!=0:
        demle+=1
        LstLe.append(x)
print("Có",demle,"số lẻ trong list: ",LstLe)
demchan=0
LstChan=[]
for x in lst:
    if x%2==0:
        demchan+=1
        LstChan.append(x)
print("Có",demchan,"số chẵn trong list: ",LstChan)
LstSNT=[]
LstKSNT=[]
def CheckSNT(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for x in lst:
    if CheckSNT(x):
        LstSNT.append(x)
    else:
        LstKSNT.append(x)
print("Các số nguyên tố trong list:",LstSNT)
print("Các số không phải số nguyên tố trong list:",LstKSNT)