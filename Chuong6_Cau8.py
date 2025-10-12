#Cau8
lst=[]
n=int(input("Nhập số phần tử:"))
for i in range(n):
    x=int(input("Nhập phần tử:"))
    lst.append(x)
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]>lst[j]:
            lst[i],lst[j]=lst[j],lst[i]
print("List sau khi sắp xếp là:")
print(lst)