def is_substring(substring,string):
    for position in range(len(string)):
        if string[position:position+len(substring)] == substring:
           return True
    return False 


print(is_substring('bad', 'abracadabra')) 
print(is_substring('dab', 'abracadabra'))
print(is_substring('ne', 'maria'))

def is_substring2(substring,string):
    index = 0 
    while index < len(string):
          if string[index:index+len(substring)] == substring:
            return True
          index += 1
    return False

print(is_substring2('bad', 'abracadabra'))
print(is_substring2('dab', 'abracadabra'))
        


