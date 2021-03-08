"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    greatest = max(incoming_list)
    return greatest
    pass


def find_least_number(incoming_list):
    least = min(incoming_list)
    return least
    pass


def add_list_numbers(incoming_list):
    try:
        total = sum(incoming_list)
    except:
        total = 0
    return total
    pass

    
def longest_value_key(incoming_dict):
    try:
        result = None
        max = 0
        for key in incoming_dict.keys():
            if len(incoming_dict[key]) > max:
                max = len(incoming_dict[key])
                result = key
    except:
        result = None
    return result

    pass
