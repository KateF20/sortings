def quick_sort(my_list):
    # return the list if there's nothing to sort
    if len(my_list) <= 1:
        return my_list

    # set the first element as a pivot of the list
    pivot = my_list[0]
    # compare each element to it and store them in the list for those greater, less, or equal to the pivot
    lower = [i for i in my_list if i < pivot]
    higher = [i for i in my_list if i > pivot]
    equal = [i for i in my_list if i == pivot]

    # recursively do this for two lists of greater and smaller and return them in the correct order
    return quick_sort(lower) + equal + quick_sort(higher)


# input
my_list = [4, 1, 3, 7, 0, -9, 3, 14, 4, 5]

print(quick_sort(my_list))