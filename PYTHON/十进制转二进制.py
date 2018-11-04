def change10_x(n, x):
    string = ''
    while n != 0:
        m = n % x
        string += str(m)
        n = int(n / x)
    return string[::-1]
n, x = 16, 8
print(change10_x(n, x))
