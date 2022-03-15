import random


def winner():
    global tie_score
    global player_score
    global computer_score
    if choice == 1:
        if computer_move == choice:
            print("You both played rock and tied!")
            tie_score += 1
        elif computer_move == 2:
            print("You played rock and beat scissors!")
            player_score += 1
        else:
            print("You played rock and lost to scissors!")
            computer_score += 1
    elif choice == 2:
        if computer_move == choice:
            print("You both played scissors and tied!")
            tie_score += 1
        elif computer_move == 1:
            print("You played scissors and lost to rock!")
            computer_score += 1
        elif computer_move == 3:
            print("You played scissors and beat rock!")
            player_score += 1
    elif choice == 3:
        if computer_move == choice:
            print("You both played paper and tied!")
            tie_score += 1
        elif computer_move == 2:
            print("You played paper and lost to scissors!")
            computer_score += 1
        elif computer_move == 1:
            print("You played paper and won against rock!")
            player_score += 1


# Main
games = int(3)
total_score = []
player_score = 0
computer_score = 0
name = input("Please enter your name: ")
tie_score = 0

while games >= 1:
    while tie_score != 0:
        games += 1
        tie_score -= 1
    choice = int(input("Please choose 1 for rock, 2 for scissors, and 3 for paper: "))
    computer_move = random.randint(1, 3)
    print(winner())
    print(f"The score is {player_score} to you, {computer_score} to the computer")
    games -= 1
    if games == 0:
        if player_score > computer_score:
            print(f"{name}, you won! congratulations!")
        elif player_score < computer_score:
            print(f"{name}, you lost! Try again")
