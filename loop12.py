num1=0
num2=1
num=int(input("enter the number to find factorial "))
print(num1,end=" ")
print(num2,end=" ")
for i in range(num+1):
    fact=num1+num2
    num1=num2
    num2=fact
    print(fact,end=" ")
print("\n factorial is ",fact,end=" ")
