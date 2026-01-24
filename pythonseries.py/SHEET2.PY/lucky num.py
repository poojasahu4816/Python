A, B = map(int, input().split())

lucky_numbers = []
for num in range(A, B + 1):
    s = str(num)
    if all(ch in '47' for ch in s):
        lucky_numbers.append(str(num))

if lucky_numbers:
    print(" ".join(lucky_numbers))
else:
    print(-1)