A, S, B = input().split()
A = int(A)
S = str(S)
B = int(B)
if S == '>':
    if(A>B):
        print("Right")
    else:
        print("Wrong")
elif(S == '<'):
    if(A<B):
        print("Right")
    else:
        print("Wrong")
elif(S == '='):
    if(A==B):
        print("Right")
    else:
        print("Wrong")