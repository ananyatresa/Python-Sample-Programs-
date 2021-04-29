import csv
def terminal_extract():
    str1='DEBUG:root:vad_timestamp'
    flag=0
    li2=[]
    with open('terminal_log.txt') as fh:
        for line in fh:
            line=line.strip()
            if str1 in line:
                flag+=1
                li1=[x for x in line.split(':')] 
                li2.append(li1[3])    
    #print (flag,li2)
    with open("output.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(zip(*[li2]))      
terminal_extract()


