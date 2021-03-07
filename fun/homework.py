"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    lis = [1, 5, 2, 6]
    print("Largest number of the list is:", max(lis))
    

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    lis = [1, 5, 2, 6]
    print("Smallest number of the list is:", min(lis))
    
    
def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    numbers = [1, 2, 3]
    numsum = sum(numbers)
    return numsum

    
def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    list1 = ["N","A","M"]
    print("The length of the list is: ", len(list1))
