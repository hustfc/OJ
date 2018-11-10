class Solution:
    def top(self, stack):
        return stack[len(stack) - 1]
    def IsPopOrder(self, pushV, popV):
        # write code here
        if pushV == [] or popV == []:
            return False
        pushListIndex, popListIndex = 0, 0
        stack = []
        stack.append(pushV[0])
        while popListIndex != len(popV):
            while self.top(stack) != popV[popListIndex]:
                if pushListIndex == len(pushV) - 1:
                    return False  #如果压栈完了之后都发现不匹配
                pushListIndex += 1
                stack.append(pushV[pushListIndex])
            stack.pop()
            popListIndex += 1
            if stack == [] and popListIndex == len(popV):
                return True
            while self.top(stack) == popV[popListIndex]: #一直出栈，直到不匹配
                stack.pop()
                popListIndex += 1
                if stack == [] and popListIndex == len(popV):
                    return True
            #当出栈过程中不匹配，则while循环结束，继续压栈
        return False
pushV = [1]
popV = [1]
print(Solution().IsPopOrder(pushV, popV))




