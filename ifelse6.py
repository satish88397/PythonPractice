print("inter the year ")
year=int (input())
if year%4==0 and year%100!=0 or year% 400==0: print("given year ias leap year")
else:
    print("not leap year")