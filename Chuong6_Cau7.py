#Cau7
lst = []
n = int(input("Nhập số phần tử: "))

for i in range(n):
    x = int(input("Nhập phần tử: "))
    if i > 0 and x <= lst[-1]:
        print("Phần tử phải lớn hơn phần tử trước đó. Dừng nhập.")
        break
    lst.append(x)

print("List sau khi nhập là:")
print(lst)
