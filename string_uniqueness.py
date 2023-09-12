def is_unique(input_string) -> bool:
    """Function that checks if all characters in a string are unique
    params: input_string: string
    return: bool"""

    return len(input_string) == len(set(input_string))
    

#print(is_unique("abc"))