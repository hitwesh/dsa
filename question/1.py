n = int(input())
exp = int(input())
p = [int(input()) for i in range(n)]
b = [int(input()) for i in range(n)]

a = sorted(zip(p,b), key=lambda x: x[0])
ans = 0

for power, bonus in a:
    if power > exp:
        break
    exp += bonus
    ans += 1
print(ans)