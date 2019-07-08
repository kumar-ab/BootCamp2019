import sys
import random
import box
import time

# Function to start the game
def start_game(player, t, start_time):
    # Initiate remaining & dice
    remaining = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    dice = [1, 2, 3, 4, 5, 6]
    # set end_time
    end_time = start_time + t
    # Start an while loop only stopping if the time is over or if the player wins
    while True:
        time_left = round((end_time - time.time()), 0)
        # If time is up skip the while loop
        if time_left <= 0:
            print("Time Up!")
            break
        # if no numbers remain, the player wins
        if len(remaining) == 0:
            # print("Time remaining: " + str(time_left) + " secs")
            print("All numbers eliminated. " + player +" wins!")
            break
        # Roll the dice
        roll_1 = random.choice(dice)
        # If the sum of remaning numbers is less than equal to 6 use only one dice
        if sum(remaining) <=6:
            roll_2 = 0
        else:
            roll_2 = random.choice(dice)
        # Sum of the dice roll(s)
        roll = roll_1 + roll_2
        print("Time remaining: " + str(time_left))
        print("Numbers still remaining: ")
        print (remaining)
        print("Sum of the dice roll: " + str(roll))
        # If the roll is valid, ask the player for intput
        if box.isvalid(roll, remaining):
            i = True
            # In case of valid roll of dice ask the user for numbers to eliminate
            # Keep the loop going till the user doesn't enter the correct number(s)
            while i:
                elim_list = input("Please enter numbers to eliminate seperated by space ")
                elim = box.parse_input(elim_list, remaining)
                if len(elim) == 0:
                    print("You did not select any number to eliminate")
                    continue
                else:
                    if sum(elim) != roll:
                        print("You selected invalid number(s)")
                        continue
                    # To check if all the element of "elim" are there in "remaining"
                    temp = 0
                    for n in elim:
                        if n in remaining:
                            temp += 1
                    # if the user enters the correct number(s) exit the loop
                    if temp == len(elim):
                        for n in elim:
                            remaining.remove(n)
                        i = False
                    else:
                        print("You selected invalid number(s)")
            print("Numbers to remove: ")
            print(elim_list)
        # If the roll is not valid, move to the next round
        else:
            print("No numbers to eliminate. Moving to next round")
    if len(remaining) != 0:
        print(player + " loses!")

# Check if the command line arguments are correctly passed
if len(sys.argv) == 3:
    n = sys.argv[1]
    t = int(sys.argv[2])
    print("The game starts now")
    start_time = time.time()
    start_game(n, t, start_time)
else:
    print("Enter player's name and time limit in seconds as arguments")
