s = input()
if s =='':
    print(0)
def IsHString(s, start, end):
    low, high = start, end
    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1
    return True
def DeleteNum(s):
    if IsHString(s, 0, len(s) - 1):
        return 0
    for deleteNum in range(1, len(s)):
        for startPosition in range(len(s)):
            endPosition = startPosition + deleteNum - 1
            if endPosition < len(s):
                String = s[0:startPosition] + s[endPosition+1:len(s)]
                #print(startPosition, endPosition, String)
                if IsHString(String, 0, len(String) - 1):
                    return deleteNum
print(DeleteNum(s))