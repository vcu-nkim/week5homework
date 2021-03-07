"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    greatest = max(incoming_list)
    return greatest
    

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    least = min(incoming_list)
    return least
    
    
def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    try:
        total = sum(incoming_list)
    except:
        total = 0
    return total

    
def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    test_list = [{'Gfg' :  "abcd", 'best' : 2},  
             {'Gfg' :  "qwertyui", 'best' : 2}, 
             {'Gfg' :  "xcvz", 'good' : 3}, 
             {'Gfg' : None, 'good' : 4}] 
    print("The original list is : " + str(test_list))
    filt_key = 'Gfg'
    temp = (sub[filt_key] for sub in test_list) 
    res = max(len(ele) for ele in temp if ele is not None)
    print("The maximum length key value : " + str(res))
