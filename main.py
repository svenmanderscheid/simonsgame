import random
import time
import os


def main():
    playing = True
    game_round = 0
    simons_list = []

    while playing:
        user_list = []
        number = random.randrange(0, 3)
        simons_list.append(number)
        print(simons_list)
        time.sleep(1)
        os.system('cls')

        for i in range(len(simons_list)):
            user_guess = int(input("Enter your next Guess"))
            user_list.append(user_guess)

        if simons_list == user_list:

            game_round += 1
        else:
            playing = False
            print(f'Simons_list{simons_list}')
            print(f'User_list{user_list}')
    else:
        print(f'Game Over in Round {game_round}')


if __name__ == '__main__':
    main()
