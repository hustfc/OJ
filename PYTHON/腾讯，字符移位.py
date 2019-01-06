import sys
def MoveChar(s):
    string = list(s)
    lastUp = len(string) - 1
    for i in range(len(string) - 1, -1, -1):
        if string[i] >= 'A' and string[i] <='Z':
            up = string[i]
            for j in range(i, lastUp):
                string[j] = string[j + 1]
            string[lastUp] = up
            lastUp -= 1
    return ''.join(string)

try:
    while True:
        s = sys.stdin.readline().strip()
        if s == '':
            break
        print(MoveChar(s))
except:
    pass
