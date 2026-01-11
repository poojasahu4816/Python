a, b, c = map(int, input().split())
if(a<=c<=b or a>=c>=b):
    print(f"{c} is within the range between first and second number.")
else:
    print(f"{c} is NOT within the range between first and second number i")