year = int(input("Enter a random year: ").strip())
if(year % 400 == 0):
    print("it's leap year...")
elif(year % 4 == 0):
    print("it's leap year...")
else:
    print("not a leap year")