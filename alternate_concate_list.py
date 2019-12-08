# Write a function that combines two lists by alternatingly taking elements, 
# e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].

def concateList(list1, list2):
    concated_list = [None]*(len(list1)+len(list2))
    
    for i in range(0, len(list1) * 2, 2):
        concated_list[i] = list1[int(i/2)]
        
    for j in range(1, len(list2) * 2, 2):
        concated_list[j] = list2[int(j/2)]

    return concated_list

list1 = [1,3,4,2,5]
list2 = [10,32,45,12]

print(f"Alternated Concated List : {concateList(list1, list2)}")