num1= int(input("enter the 1st number "))
num2= int(input("enter the 2st number "))
num3= int(input("enter the 3st number "))
num4= int(input("enter the 4st number "))
if num1>=num2 and num1>=num3 and num1>=num4:
    largest =num1
    print(largest)
elif num2>=num3 and num2>=num4:
    largest=num2
elif num3>=num4:
    largest=num3
else:
    largest=num4
print("largest number of given number is ",largest)
