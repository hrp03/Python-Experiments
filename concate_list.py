# Write a function that concatenates two lists. [a,b,c], [1,2,3] → [a,b,c,1,2,3]

def concateListMethod1(list1, list2):
    return list1 + list2

def concateListMethod2(list1, list2):
    concated_list = []

    for i in range(len(list1)):
        concated_list.append(list1[i])

    for i in range(len(list2)):
        concated_list.append(list2[i])
    
    return concated_list

list1 = [1,3,4,2,5]
list2 = [10,32,45,12]

print(f"Concated List 1 : {concateListMethod1(list1, list2)}")
print(f"Concated List 2 : {concateListMethod2(list1, list2)}")