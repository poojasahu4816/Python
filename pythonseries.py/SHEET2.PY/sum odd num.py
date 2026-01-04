T = int(input())
for _ in range(T):
    X,Y = map(int, input().split())
    str, end = min(X, Y), max(X, Y)
    total = 0

    for i in range(str + 1, end):

        if i % 2 == 1:
            total += i

    print(total)