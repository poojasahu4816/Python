A, B, C = map(int, input().split())

if A <= B and A <= C:
    smallest = A
    if B <= C:
     middle = B
     largest = C
    else:
       middle = C
       largest = B
elif B <= A and B <= C:
    smallest = B
    if A <= C:
     middle = A
     largest = C
    else:
       middle = C
       largest = A
else:
    smallest = C
    if A <= B:
      middle = A
      largest = B
    else:
       middle = B
       largest = A

print(smallest)
print(middle)
print(largest)

print()

print(A)
print(B)
print(C)