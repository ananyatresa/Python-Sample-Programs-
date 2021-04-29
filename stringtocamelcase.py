def camel_case(str1):   
    str2=[]
    print (str1)
    for i in str1:
        a=i.capitalize()
        str2.append(a)
    print (*str2, sep="")

x=list(input().split())
camel_case(x)

#alternate

def camel_case(str1):   
    str2=str1.title()
    print (str2)

x=input()
camel_case(x)