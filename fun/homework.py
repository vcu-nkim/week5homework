"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    list1 = [1, 22, 3, 11, 10]
    list1.sort()
    print("Largest element is: ", max(list1))


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    list1 = [1, 22, 3, 11, 10]
    list1.sort()
    print("Smallest element is: ", min(list1))


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    my_list = [1,2,3,4,5]
    print "The sum of my_list is", sum(my_list)

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    list1 = ["N","A","M"]
    print("The length of the list is: ", len(list1))
     
