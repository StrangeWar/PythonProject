rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

signs = [rock, paper, scissors]
import random
def game(choice):
    while choice=='y':
        user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        pc_choice = random.randint(0, 2)  # computer's random choice.

        # display of player,s choice.

        if user_choice == 0:
            print(rock)
        elif user_choice == 1:
            print(paper)
        else:
            print(scissors)

        # display of computer player's choice.pc_choice.

        print("Computer choose:\n")

        if pc_choice == 0:
            print(rock)
        elif pc_choice == 1:
            print(paper)
        else:
            print(scissors)

        # working of the choice comparison of both players.
        # rock = 0, paper = 1, scissors = 2
        # (rock < paper) and (paper < scissors) and (scissors < rock)

        if user_choice == 0 and pc_choice == 2:
            print("You Win!")
        elif user_choice == 2 and pc_choice == 0:
            print("You lose!")
        else:
            if user_choice < pc_choice:
                print("You lose!")
            elif user_choice == pc_choice:
                print("Draw!")
            else:
                print("You Win!")
        choice = input("If you want to play again type 'Y' or if not type 'N'\n").lower()
game('y')


