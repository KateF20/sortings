def insertion_sort(my_list):
    # return the list if there's nothing to sort
    if len(my_list) <= 1:
        return my_list

    # traverse over the list starting from the second element
    for i in range(1, len(my_list)):
        # compare an element to the element on its left
        for j in range(len(my_list) - 1):
            if my_list[i] < my_list[j]:
                # swap them if the element on the left is greater than the initial element
                my_list[i], my_list[j] = my_list[j], my_list[i]

    return my_list


# input
my_list = [4, 1, 3, 7, 0, -9, 3, 14, 4, 5]

print(insertion_sort(my_list))