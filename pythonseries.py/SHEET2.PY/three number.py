K, S = map(int, input().split())

ans = 0
for X in range(K + 1):
    low = max(0, S - K - X)
    high = min(K, S - X)
    if low <= high:
        ans = ans + (high - low + 1)

print(ans)        