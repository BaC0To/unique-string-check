
def unique(input_string:str):
    """Function that checks if all characters in a string are unique
    params: input_string : str
    return: isUnique: bool"""

    try:
        
        isUnique = False
        
        input_string_length = len(input_string)
        input_string_to_set = set(input_string)
        length_input_string_to_set = len(input_string_to_set)

        input_string_to_list = list(input_string)
        length_input_string_to_list = len (input_string_to_list)

        if length_input_string_to_set == length_input_string_to_list:
            isUnique = True

        return isUnique
    
    except (TypeError) as exc:
        print(exc)


result = unique("Tuesday")
print(result)
