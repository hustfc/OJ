n = int(input())
a = list(map(int, input().split()))
a = sorted(a,reverse=1)
result = 0
flag = 1
for i in a:
    if flag:
        result += i
        flag = 0
    else:
        result -= i
        flag = 1
print(result)