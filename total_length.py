def total_length(my_list):
    counter=0
    for string in my_list:
        counter = counter + len(string) 
        print(counter)
    return counter

print(total_length(['foo', 'barkoi'])) 