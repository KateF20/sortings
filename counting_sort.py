def counting_sort(my_list):
    # return the list if there's nothing to sort
    if len(my_list) <= 1:
        return my_list

    # a list to store sorted elements in
    new_li = [0] * len(my_list)
    # a list to keep the track of the count of each element in my_list
    count_li = [0] * (len(my_list) + 1)
    # count the frequency
    for elem in my_list:
        count_li[elem] += 1

    # adds the count of the previous element to the count of the current element
    for i in range(1, (len(my_list) + 1)):
        count_li[i] += count_li[i - 1]
    # count_li[i] now contains the number of elements less than or equal to i in my_list

    # iterate over the list starting from the last element
    x = len(my_list) - 1
    while x >= 0:
        element = my_list[x]
        # keep track of the remaining instances of the same element
        count_li[element] -= 1
        # calculate the current position of the current element
        current = count_li[my_list[x]]
        # place the current element in new_li
        new_li[current] = my_list[x]
        x -= 1

    return new_li


# input
li = [5, 3, 6, 2, 2, 6, 4, 1, 0, 5, 5, 2, 6]

print(counting_sort(li))