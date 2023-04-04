# make sure your files are in the same directory
from insertion_sort import insertion_sort
import math


def bucket_sort(my_list, k):
    # define the size of each bucket
    size = math.ceil((max(my_list) - min(my_list) + 1) / k)
    # create an empty list of buckets
    empty_li = [[] for _ in range(k)]

    # sort elements from my_list into buckets according to their sizes
    for i in range(len(my_list)):
        index = (my_list[i] - min(my_list)) // size
        empty_li[index].append(my_list[i])

    # sort each bucket
    [insertion_sort(empty_li[i]) for i in range(len(empty_li))]

    # from each bucket in the list of buckets get a value and make a new list
    new_li = [val for sublist in empty_li for val in sublist]

    return new_li


# input
my_list = [4, 1, 3, 7, 0, -9, 3, 14, 4, 5]

print(bucket_sort(my_list, 3))