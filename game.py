"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.next_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("rock, paper or scissors?").lower()
            if move in ["rock", "paper", "scissors"]:
                break
            else:
                print("Invalid input, please try again")
        return move


class ReflectPlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        self.next_move = their_move


class CyclePlayer(Player):
    def move(self):
        return self.next_move

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.next_move = 'paper'
        elif my_move == 'paper':
            self.next_move = 'scissors'
        else:
            self.next_move = 'rock'


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("**It's a tie**\n")
        else:
            p1_win = self.beats(move1, move2)
            if p1_win is True:
                print("**Player 1 wins!**\n")
                self.score1 += 1
            else:
                print("**Player 2 wins!**\n")
                self.score2 += 1
        print(f"Player 1 score: {self.score1} | Player 2 score: {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:\n")
            self.play_round()
            if self.score1 > self.score2:
                print("Player 1 is the winner!")
            else:
                print("**Player 2 is the winner!**")
        print("Game over!\n")


# if __name__ == '__main__':
# p1 = Player()
# p2 = HumanPlayer()
# game = Game(p1, p2)
# game.play_game()

# p1 = CyclePlayer()
# p2 = HumanPlayer()
# game = Game(p1, p2)
# game.play_game()

if __name__ == '__main__':
    Game(RandomPlayer(), RandomPlayer()).play_game()
    Game(HumanPlayer(), RandomPlayer()).play_game()
    Game(HumanPlayer(), ReflectPlayer()).play_game()
    Game(HumanPlayer(), CyclePlayer()).play_game()
