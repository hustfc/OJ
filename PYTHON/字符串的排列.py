class Solution:
    def swap(self, newElem, Elem):
        result = []
        listElem = list(Elem)
        listElem.insert(0, newElem)
        result.append(''.join(listElem))
        for i in range(1, len(listElem)):
            preList = listElem[:]   #注意这个地方
            listElem[0], listElem[i] = listElem[i], listElem[0]
            if listElem != preList:   #处理重复情况
                result.append(''.join(listElem))
            listElem[0], listElem[i] = listElem[i], listElem[0]
        return result
    def recurtionPermutation(self, ss, index):
        result = []
        if index == 0:
            result.append(ss[0])
        else:
            previousList = self.recurtionPermutation(ss, index - 1)
            newElem = ss[index]
            #print(previousList)
            for Elem in previousList:
                result += self.swap(newElem, Elem)  #这里返回的是一个数组，数组加数组使用+，数组加元素使用append符号
        return result
    # def BubbleSortByDic(self, result):
    #     for i in range(len(result)):
    #         for j in range(len(result) - 1, i, -1):
    #             if result[j] < result[i]:
    #                 result[i], result[j] = result[j], result[i]
    #     return result
    def Permutation(self, ss):
        # write code here
        if ss == '':
            return []
        #return self.BubbleSortByDic(self.recurtionPermutation(ss, len(ss) - 1))
        return sorted(self.recurtionPermutation(ss, len(ss) - 1))
print(Solution().Permutation('acdfb'))