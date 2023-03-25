def fav_color():
    response = input("Can you guess what my favorite color is?\n")
    if response != 'blue':
        print("Sorry, that's not my favorite color. Try again!")
        fav_color()
    else:
        print("That's right! My favorite color is blue.")

fav_color()