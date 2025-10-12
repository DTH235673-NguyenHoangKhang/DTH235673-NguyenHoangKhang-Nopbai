#Cau9
import math
n=int(input("Nhập n>0: "))
def CanN(n):
    if n==1:
        return math.sqrt(2)
    else:
        return(math.sqrt(2+CanN(n-1)))
print(f"S(n): {CanN(n)}")