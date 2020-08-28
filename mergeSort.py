
def splitAndSort(array, start, end):
    if end <= start:
        return
    # size of left might be bigger that right array.
    mid = int((end - start) /2) + start
    splitAndSort(array, start, mid)
    splitAndSort(array, mid + 1, end)
    
    j = mid + 1
    while start <= end and j <= end:
        if array[start] > array[j]:
            index = j
            while j <= end and array[start] > array[j]:
                j += 1

            biggers = array[start: index]
            ascend = array[index: j]
            ascend.extend(biggers)

            array[start: start + len(ascend)] = ascend

            start += (j - index)
        else:
            start += 1

def mergeSortAscend(array):
    splitAndSort(array, 0, len(array) - 1)
    return array

print(mergeSortAscend([0,2,100,7,3,6,5,10]))
print(mergeSortAscend([0]))
print(mergeSortAscend([10,10,10,10,10,10,1,1,1,1,1]))
print(mergeSortAscend([6,7,10,1,2]))
