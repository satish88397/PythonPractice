#list=[1,2,3,4]
#for i in list:print(i) 1 2 3 4
#Take inputs from user to make a list. Again take one input from user and
# search it in the list and delete that element, if found. Iterate over list using for loop
num_list=[]
inp= int(input("enter the range \n "))
for i in range(0,inp):
  print("enter item in list")
  item=int(input())
num_list.append(item)
for element in num_list:
  print("your final list is ",element )


