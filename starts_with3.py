def starts_with(long,short):
    if long[0:len(short)]==short:
       return True
    return False 

print(starts_with("apple", "app"))
print(starts_with("manatee", "mango"))

def starts_with(long,short):
    return long[0:len(short)]==short

print(starts_with("apple", "app"))
print(starts_with("manatee", "mango"))
    