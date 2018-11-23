def swap(newElem, Elem):
    result = []
    listElem = list(Elem)
    listElem.insert(0, newElem)
    #result.append(''.join(listElem))
    result += ''.join(listElem)
    for i in range(1, len(listElem)):
        preList = listElem[:]  # 注意这个地方
        listElem[0], listElem[i] = listElem[i], listElem[0]
        if listElem != preList:  # 处理重复情况
            #result.append(''.join(listElem))
            result += ''.join(listElem)
        listElem[0], listElem[i] = listElem[i], listElem[0]
    return result
print(swap('1', '234'))