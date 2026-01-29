S = input().strip()        # symbol
N = int(input().strip())   # number of elements
numbers = list(map(int, input().split()))

for x in numbers:
    print(S * x)
    