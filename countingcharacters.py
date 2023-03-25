def counting_characters(string,target):
    total = 0
    index = 0
    while index < len(string):
        if string[index] == target:
           total += 1
        index += 1
    return total 

print(counting_characters("maria","a"))
    

           