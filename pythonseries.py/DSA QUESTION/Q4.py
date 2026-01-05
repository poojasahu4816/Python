N = int(input("Enter a number: "))
if(N % 3 == 0 and N % 5 == 0):
    print("number is divisible by both 3 and 5")
elif(N % 3 == 0):
    print("number is divisible by 3")
elif(N % 5 == 0):
    print("number is divisible by 5")
else:
    print("number is not divisible ny 3 and 5")