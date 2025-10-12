#Cau6
from random import randrange
n=int(input("Nhập số phần tử:"))
lst=[]
for i in range(n):
    x=randrange(0,100)
    lst.append(x)
for i in range(len(lst)-1):
    if lst[i]==lst[i+1]:
        for j in range(i+1,n):
            lst[j]=lst[j+1]
        n-=1
print("List có N số nguyên không trùng nhau:")
print(lst)
    