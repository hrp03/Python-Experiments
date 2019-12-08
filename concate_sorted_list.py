# Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].
# You can do this quicker than concatenating them followed by a sort.

def concateAndSortInbuilt(list1, list2):
    
    list1.extend(list2)
    list1.sort()
    return list1

def concateAndSort(list1, list2):
    newList = [None] * (len(list1) + len(list2))
    
    for i in range(len(list1)):
        newList[i] =list1[i]

    m = len(list1)

    for i in range(len(list2)):
        newList[i + m] = list2[i]

    newList.sort()

    return newList

list1 = [1,4,6]
list2 = [2,3,5]

print(f"Sorted Merged List (Inbuilt function) : {concateAndSortInbuilt(list1, list2)}")
print(f"Sorted Merged List (Without Inbuilt function) : {concateAndSort(list1, list2)}")