def selection_sort(my_list):
    # return the list if there's nothing to sort
    if len(my_list) <= 1:
        return my_list

    for i in range(len(my_list)):
        # set the 1st element to the smallest by now
        minim = i
        for j in range(i + 1, len(my_list)):
            # if an element is smaller than the set minim, set minim to this element
            if my_list[j] < my_list[minim]:
                minim = j

        # swap the order of the two elements
        my_list[i], my_list[minim] = my_list[minim], my_list[i]

    return my_list


# input
my_list = [4, 1, 3, 7, 0, -9, 3, 14, 4, 5]

print(selection_sort(my_list))