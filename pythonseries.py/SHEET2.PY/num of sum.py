while True:
    N, M = map(int, input().split())
    if N <= 0 or M <= 0:
        break
    start, end = min(N, M), max(N, M)
    nums = range(start, end + 1)
    print(" ".join(map(str, nums)), "sum =" + str(sum(nums)))