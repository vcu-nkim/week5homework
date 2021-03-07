"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    list1 = [456, 700, 200]
    print("Max value element : ", max(list1))
    

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    list1 = [456, 700, 200]
    print("Min value element : ", min(list1))
    
    
def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    numbers = [1,2,3,4,5,1,4,5] 
    Sum = sum(numbers) 
    print(Sum) 

    
def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    list1 = ["N","A","M"]
    print("The length of the list is: ", len(list1))
