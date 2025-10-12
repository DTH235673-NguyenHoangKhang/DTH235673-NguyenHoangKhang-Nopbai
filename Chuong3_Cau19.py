#cau19
import math
x=float(input("Moi nhap so x: "))
n=int(input("Moi nhap so n: "))
s=0
for i in range(n+1):
    s+=x**(2*i+1)/math.factorial(2*i+1)
print("S({0},{1})={2}".format(x,n,s))