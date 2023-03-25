def word_triangle(word):
    length=len(word)
    for n in range(length): 
        print(word[:length-n])

print(word_triangle('abracadabra'))


