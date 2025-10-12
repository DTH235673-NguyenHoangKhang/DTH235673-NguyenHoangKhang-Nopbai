#Cau6
def NegativeNumberInString(s):
    result=""
    for i in range(0,len(s)):
        if s[i]=='-' and s[i+1].isdigit():
            result=result+"-"
            for j in range(i+1,len(s)):
                if s[j].isdigit():
                    result=result+s[j]
                else:
                    break
            result=result+";"
    return result.strip(';')
s="abc-5xyz-12k9l--p"
print(NegativeNumberInString(s))