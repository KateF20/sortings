def merge_sort(my_list):
    # return the list if there's nothing to sort
    if len(my_list) <= 1:
        return my_list

    # find the middle of the list
    mid = len(my_list) // 2
    # cut the list in two sub-lists and recursively call the function on them
    left_list = my_list[: mid]
    merge_sort(left_list)
    right_list = my_list[mid: ]
    merge_sort(right_list)

    # create a list of sorted elements
    # set three indexes to iterate over two sub-lists and the main list
    i = j = k = 0
    while i < len(left_list) and j < len(right_list):
        # check which element is smaller from two lists and add it to the main list
        if left_list[i] < right_list[j]:
            my_list[k] = left_list[i]
            i += 1
        else:
            my_list[k] = right_list[j]
            j += 1
        k += 1

    # check if there's anything left in the lists and add elements to the end of the main list
    while i < len(left_list):
        my_list[k] = left_list[i]
        k += 1
        i += 1

    while j < len(right_list):
        my_list[k] = right_list[j]
        k += 1
        j += 1

    return my_list


# input
my_list = [4, 1, 3, 7, 0, -9, 3, 14, 4, 5]

print(merge_sort(my_list))