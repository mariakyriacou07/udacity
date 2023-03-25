import time
import random

villain = ["dragon", "gorgon", "pirate", "monster", "evil fairy"]
enemy = random.choice(villain)
weapon = []


def one_or_two():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")


def print_pause(message):
    print(message)
    time.sleep(2)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        print_pause(f"Sorry, the option {response} is invalid. Try again!")


def intro():
    global enemy
    enemy = random.choice(villain)
    print_pause("You find yourself standing in an open field,"
                "filled with grassand yellow wildflowers.\n")
    print_pause(f"Rumor has it that a {enemy} is somewhere"
                "around here, and has been terrifying the nearby village.\n")
    print_pause("In front of you is a house.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold a trusty"
                "(but not very effective) dagger.\n")
    one_or_two()


def field():
    print_pause("You walk back out to the field.")
    one_or_two()


def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens"
                f"and out steps a {enemy}.")
    print_pause(f"Eep! This is the {enemy}'s house!")
    print_pause(f"The {enemy} attacks you!")
    if "sword" not in weapon:
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a tiny dagger.")


def fight():
    player_choice = valid_input("Would you like to (1) fight or"
                                "(2) run away?\n", ['1', '2'])
    if player_choice == '1':
        if "sword" in weapon:
            print_pause(f"As the {enemy} moves to attack, you unsheath"
                        "your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in your"
                        "hand as you brace yourself for the attack")
            print_pause(f"But the {enemy} takes one look at your shiny"
                        "new toy and runs away!")
            print_pause(f"You have rid the town of the {enemy}."
                        "You are victorious! You WON!")
            play_again()
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {enemy}.")
            print_pause("You have been defeated! You lost! GAME OVER")
            play_again()
    else:
        print_pause("Luckily, you don't seem to have been followed.")
        print_pause("You run back to the field")
        one_or_two()
        play()


def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical sword of Orgoth!")
    print_pause("You discard your silly old dagger and take"
                "the sword with you.")
    weapon.append("sword")


def play_again():
    playagain = valid_input("Would you like to play again?"
                            "(yes/no)", ['yes', 'no'])
    if playagain == 'no':
        print_pause("Thanks for playing!")
        exit
    else:
        print_pause("Excellent! Restarting the game..")
        intro()
        play()


def cave_again():
    print_pause("You took the sword, not much to do here!")
    field()
    player_choose = valid_input("What would you like to do?"
                                "(Please enter 1 or 2.)", ['1', '2'])
    if player_choose == '1':
        house()
        fight()
        play_again()
    else:
        cave_again()


def play():
    player_ch = valid_input("What would you like to do?\n"
                            "(Please enter 1 or 2.)", ['1', '2'])
    if player_ch == '1':
        house()
        fight()
    else:
        if "sword" in weapon:
            cave_again()
        else:
            cave()
            field()
            play()


intro()
play()
