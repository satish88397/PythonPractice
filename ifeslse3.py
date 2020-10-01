quantity= int(input("enter the quantity "))
if quantity*100>1000:

    print(" discounted cost is ",((quantity*100)-(.1*quantity*100)))
else:
    print("cost is :=",quantity*100,"thts why you cant get discount ")