n, m = map(float, input().split())
result = int(1 / 2 * m / (1 - (1 / 2) ** n))
print(result)