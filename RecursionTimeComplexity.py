#function to merge two sorted lists into one sorted list
def merge_sorted_list(list1, list2):
    i = 0      #pointer for list 1
    j = 0      #pointer for list 2
    merge_list = []   #new list

    #cpmpare elements from both lists and insert the smaller one
    while i<len(list1) and j<len(list2):
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1

    #if there are remaining elements in list1, and then
    while i<len(list1):
        merge_list.append(list1[i])
        i += 1

    #if there are remaining elements in list2, then
    while j<len(list2):
        merge_list.append(list2[j])
        j += 1
    
    return merge_list

#example usage
list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 10]

#Printing the lists
print("List A: ",list_a)
print("List B: ",list_b)

#sorting the two lists
merge = merge_sorted_list(list_a, list_b)

#printing the new merged sorted list
print("Merged Sorted List: ",merge)