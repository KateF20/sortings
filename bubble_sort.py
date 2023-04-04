def bubble_sort(my_list):
    for i in range(len(my_list)): # traverse over the list
        for j in range(len(my_list) - i - 1): # take the next element of the list
            if my_list[j] > my_list[j + 1]: # check the two elements
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j] # swap them if the 1st is less than the 2nd

    return my_list

# input
my_list = [4, 1, 3, 7, 0, -9, 3, 14, 4, 5]
print(bubble_sort(my_list))