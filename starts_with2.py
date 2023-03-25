def starts_with(long,short):
    for position in range(len(short)): 
       if long[position] != short[position]:
            return False
    return True

print(starts_with("banana","ban"))
print(starts_with("manatee", "manager"))
print(starts_with("maria", "mar"))
print(starts_with("skata", "pissia"))