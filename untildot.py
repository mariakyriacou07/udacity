def until_dot(string):
    index = 0
    while index < len(string) and string[index] != ".":
          index += 1
    return string[:index]) 

print(until_dot("Udacity.com"))
print(until_dot("This is a sentence. This is another."))
print(until_dot("192.168.200.2"))

def untildot(string):
    for position in range(len(string)):
        if string[position] == ".":
           return string[:position]
    return string
    
print(untildot("www.maria.com"))
print(untildot("This is a sentence. This is another."))
print(untildot("No dots here"))