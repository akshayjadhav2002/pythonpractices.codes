#Nth_number = int (input("Enter the nth even number:"))
Nth_number = 3
start =0
cnt  =0
while(cnt<=Nth_number):
    start = start + 1
    if(start % 2 != 0):
        odd = start
        cnt+=1
        #print(odd)
    if(cnt==Nth_number):
        print(odd)


