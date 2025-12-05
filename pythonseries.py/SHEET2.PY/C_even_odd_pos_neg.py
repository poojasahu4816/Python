N = int(input())
arr = list(map(int, input().split()))

even = 0
odd = 0
positive = 0
negative = 0

for X in arr:
    if X % 2 == 0:
        even += 1
    else:
        odd += 1

    if X > 0:
        positive += 1
    elif X < 0:
        negative += 1

print("Even:", even)
print("Odd:", odd)
print("Positive:", positive)
print("Negative:", negative)
