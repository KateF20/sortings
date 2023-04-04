def radix_sort(my_list):
    # return the list if there's nothing to sort
    if len(my_list) <= 1:
        return my_list

    # set a factor to 1 and then increment it by Radix
    factor = 1
    RADIX = 10
    maximal = max(my_list)

    # loop over on the level of units, then tens, then hundreds and so on
    while factor < maximal:
        # a list with empty lists to store elements based on factor
        empty_li = [[] for _ in range(RADIX)]
        for i in my_list:
            # sort based on factor
            index = (i // factor) % RADIX
            empty_li[index].append(i)

        ind = 0
        # index i corresponds to a particular bucket of elements in empty_li
        for i in range(RADIX):
            # go through each bucket in empty_li and insert the elements in the correct order into my_list
            for j in empty_li[i]:
                my_list[ind] = j
                ind += 1

        factor *= RADIX

    return my_list


# input
radix_li = [130, 22, 57, 495, 209, 3, 58, 0, 36]

print(radix_sort(radix_li))