def locate_all(string, target):
    matches=[]
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            matches.append(index)
            index += len(target)
        else:
            index += 1
    return matches

print(locate_all('cookbook', 'ook'))
print(locate_all('all your bass are belong to us', 'base'))
print(locate_all('yesyesyes', 'yes'))