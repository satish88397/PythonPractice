sum=0
for i in range(0,20):
    if i%2==0 or i%3==0 or i%5==0:
        print("")
    else:
        sum=sum+i
print("sum is",sum)
