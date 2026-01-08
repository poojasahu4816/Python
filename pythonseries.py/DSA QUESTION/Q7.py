# First Method

a, b, c = map(int, input("Enter three number: ").split())
if(a>b and a>c):
    print(a)
elif(b>c and b>a):
    print(b)
elif(c>a and c>b):
    print(c)
else:
    print("number are equal")
 
   
# Second Method

a, b, c = map(int, input("Enter three number: ").split())
print("Largest number is: ", max(a, b, c))