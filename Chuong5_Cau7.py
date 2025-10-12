#Cau7
def ToiUuHoa(s):
    s2=s.lower()
    
    s2=s2.strip() 
    arr=s2.split(' ') 
    s2="" 
    for x in arr: 
        word=x 
        if len(word.strip())!=0: 
            s2=s2+word+" " 
    
    result=""
    for i in range(0,len(s2)-1):
        if i==0:
            result=result+s2[i].upper()
        elif s2[i-1]==' ':
            result=result+s2[i].upper() 
        else:
            result=result+s2[i]
    return result.strip()
s="    trần     dUy     Thanh   "
print(ToiUuHoa(s))