s1 = ["steal", "least", "stale", "tales" ]
cc = set(s1[0])
for i in s1[1:]:
        cc &= set(i)
        print(cc)
        break