#Find coordinate
x, y = map(int, input("Enter the coordinate.").split())
if(x>0 and y>0):
     print("First Quadrant")
elif(x<0 and y>0):
     print("Second Quadrant")
elif(x<0 and y<0):
     print("Third Quadrant")
elif(x>0 and y<0):
     print("Fourth Quadrant")
elif(x==0):
     print("On Y-axis")
elif(y==0):
     print("On X-axis")
else:
     print("Origin")