def reverse_number(x):
    temp=0
    while x>0:
        rem=x%10
        temp=temp*10+rem
        x=x//10
    print (temp)

n=int(input())
reverse_number(n)