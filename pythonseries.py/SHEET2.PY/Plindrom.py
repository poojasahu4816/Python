N = input().strip()
j = " "
for i in N:
    j = i + j
print(j.lstrip("0"))
print("YES"if (N == N[::-1]) else "NO")
