def partitionOfK(numbers, start, end, k):
    if k < 0 or numbers == [] or start < 0 or end >= len(numbers) or k > end:
        return None
    low = start
    high = end
    key = numbers[start]
    while low < high:
        while low < high and numbers[high] >= key:
            high -= 1
        numbers[low] = numbers[high]
        while low < high and numbers[low] <= key:
            low += 1
        numbers[high] = numbers[low]
    numbers[low] = key
    if low < k:
        return partitionOfK(numbers, start + 1, end, k)
    elif low > k:
        return partitionOfK(numbers, start, end - 1, k)
    else:
        return numbers[low]
numbers = [3,5,6,7,2,-1,9,3]
print(sorted(numbers))
print(partitionOfK(numbers, 0, len(numbers) - 1, 5))
