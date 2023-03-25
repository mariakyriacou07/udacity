str = 'it appears that the the appears the most in the sentence'

dictionary = {}
list = str.split(" ")

for word in list:
    if word in dictionary:
        dictionary[word] = dictionary[word] + 1
    else:
        dictionary[word] = 1

for key, value in dictionary.items():
    print(f"The '{key}' appears {value} time(s) in the string")