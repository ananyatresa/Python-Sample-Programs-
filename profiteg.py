def profit_eg(li1):
    tot=1
    for i in li1:
        if i==1:
            a=li1[1]
            continue
        else:
            if i%a==0:
                tot+=i
    print (tot)
li2=list(map(int,input().split()))
profit_eg(li2)

