import time
items = []

def print_pause(message):
    print(message)
    time.sleep(2)

def valid_input(msg, option1, option2):
    while True:
        response = input(msg).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I Don't understand!")

def play_game():
    items = []
    intro()
    ride_elevator()

def intro():
    print_pause("You have just arrived at your new job!")
    print_pause("You are in the elevator")

def first_floor():
    print_pause("You push the button for the first floor")
    print_pause("After a few moments, you find yourself in the lobby.")
    if "ID card" in items:
        print_pause("The clerk greets you, but she has already"
                    "given you your ID card, so there is nothing"
                    "more to do here now")
    else:
        print_pause("The clerk greets you and gives you your ID "
                        "card")
        items.append("ID card")
    print_pause("You head back to the elevator")
    ride_elevator()

def second_floor():
    print_pause("You push the button for the second floor.")
    print_pause("After a few moments, you find yourself in the human resources department")
    if "handbook" in items:
        print_pause("Nothing more here")
    else:
        print_pause("HR approaches")
        if "ID card" in items:
            print_pause("He looks at your ID card and then gives you a copy of the employee handbook.")
            items.append("handbook")
        else:
            print_pause("He has something for you, but says he can't"
                        "give it to you until you go get your ID card")
    print_pause("You head back to the elevator")
    ride_elevator()

def third_floor():
    print_pause("You push the button for the third floor.")
    print_pause("After a few moments, you find yourself in the engineering department")
    if "ID card" in items:
        print_pause("You use your ID card to open the door."
                        "Your program manager greets you and tells you that you need to have a copy of the"
                        "employee handbook in order to start work.")
        if "handbook" in items:
                print_pause("Fortunately, you got that from HR!"
                            "Congratulatons! You are ready to start your new job as vice president of engineering!")  
        else:
                print_pause("They scowl when they see that you don't have it, and send you back to the elevator.")                          
    else:
        print_pause("Unfortunately, the door is locked and you can't get in."
                        "It looks like you need some kind of key card to open the door."
                        "You head back to the elevator.")
    print_pause("You head back to the elevator")
    ride_elevator()
    

def ride_elevator():
    print_pause("Please enter the number for the floor you would like to visit:")
    floor_number = input("1.Lobby\n" 
                         "2.Human Resources\n"
                         "3.Engineering department\n") 
    if floor_number == "1":
        first_floor()
    elif floor_number == "2":
        second_floor()
    elif floor_number == "3":
        third_floor()
    print_pause("Where to next?")

play_game()