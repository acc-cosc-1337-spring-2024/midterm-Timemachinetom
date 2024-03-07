#write functions here, don't add input('') statements here!

def reverse_string(string1):
    rev_string=""
    index = len(string1)-1
    while index >= 0:
        rev_string += string1[index]
        index= index - 1
    return rev_string