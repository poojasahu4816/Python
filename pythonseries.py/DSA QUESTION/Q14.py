a, b, c  = map(int, input("Enter triangle adges: ").split())
if(a>0 and b>0 and c>0 and (a+b+c) == 180):
    print("The angles form a triangle.")
else:
    print("the angles do not form a triangle.")