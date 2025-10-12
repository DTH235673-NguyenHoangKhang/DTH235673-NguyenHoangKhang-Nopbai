#Cau10
def NhapMaTran():
    A=[]
    a=int(input("Nhập số dòng:"))
    b=int(input("Nhập số cột:"))
    for i in range(a):
        row=[]
        for j in range(b):
            x=int(input(f"Nhập phần tử A[{i}][{j}]:"))
            row.append(x)
        A.append(row)
    return A
def XuatMaTran(M):
    for row in M:
        for element in row:
            print(element,end='\t')
        print()
def MatrixHoanVi(A):
    for i in range(len(A)):
        for j in range(len(A[0])//2):
            A[i][j],A[i][len(A[0])-j-1]=A[i][len(A[0])-j-1],A[i][j]
    return A
A=NhapMaTran()
B=NhapMaTran()
print("Ma trận A:")
XuatMaTran(A)
print("Ma trận B:")
XuatMaTran(B)
def CongMaTran(A,B):
    if len(A)!=len(B) or len(A[0])!=len(B[0]):
        return None
    C=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(A[0])):
            row.append(A[i][j]+B[i][j])
        C.append(row)
    return C
C=CongMaTran(A,B)
print("Ma trận C=A+B:")
if C is not None:
    XuatMaTran(C)
else:
    print("Không thể cộng hai ma trận do kích thước không khớp.")
print("Ma trận A sau khi hoán vị:")
A_hoanvi=MatrixHoanVi(A)
XuatMaTran(A_hoanvi)
print("Ma trận B sau khi hoán vị:")
B_hoanvi=MatrixHoanVi(B)
XuatMaTran(B_hoanvi)

