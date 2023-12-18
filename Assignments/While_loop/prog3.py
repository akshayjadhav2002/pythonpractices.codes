start =0
cnt  =0
while(cnt<7):
    start = start + 1
    if(start % 2 != 0):
        odd = start
        cnt+=1
        #print(odd)
    if(cnt==7):
        print(odd)


