"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
    print(max_num_in_list([11, 3, 5, 0]))


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    min = list [ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
    print(smallest_num_in_list([11, 3, 5, 0]))


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    my_list = [1,2,3,4,5]
    result = sum(my_list)
    return result

    
def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    list1 = ["N","A","M"]
    print("The length of the list is: ", len(list1))
