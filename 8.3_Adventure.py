'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

import time
import random

def hermdog_rand_and_check():
    hermdog_room1 = random.randint(1, 6)
    hermdog_room2 = random.randint(1, 6)
    hermdog_room3 = random.randint(1, 6)
    if current_room == hermdog_room1:
        print("Y  O  U    L  O  S  E  !", end="\r")
        print("    Y O U  L O S E !", end="\r")
        print("       YOU LOSE!", end="\n")
    elif current_room == hermdog_room2:
        print("Y  O  U    L  O  S  E  !", end="\r")
        print("    Y O U  L O S E !", end="\r")
        print("       YOU LOSE!", end="\n")
    elif current_room == hermdog_room3:
        print("Y  O  U    L  O  S  E  !", end="\r")
        print("    Y O U  L O S E !", end="\r")
        print("       YOU LOSE!", end="\n")
    
#E N W S

room_list=[]
room = ["You are in the Hermdog's room (CSP).", 1, None, None, None]
room_list.append(room)
room = ["You are in the Business Pod.", 2, None, 0, None]
room_list.append(room)
room = ["You are in the Rooms 230-234 Pod.", 3, None, 1, None]
room_list.append(room)
room = ["You are in the Freshman Pod.", None, 4, 2, None]
room_list.append(room)
room = ["You are in the Foreign Language Pod.", 3, None, 5, None]
room_list.append(room)
room = ["You are in the English Pod.", 4, None, 0, None]
room_list.append(room)

current_room = 0
print("____________________________________________________________")
print("|        |       |     1    |     2     |        3         |")
print("|  CSP 0  \     /  Business | 230 - 234 |   Freshman Pod   |")
print("|________|       |___    ___|____   ____|_______    _______|")
print("|                                                          |")
print("|                                                          |")
print("______LOCKED____________________________________    _______|")
print("|        5       |______________________|        4         |")
print("|     English    |_Ductwork through 4&5_|   Foreign Lang   |")
print("|________________|______________________|__________________|")

print("You are a student in Urbandale High School, you have all A's except for in Hermdog's Computer Science Principles in which you have a B due to not turning in your Adventure Game...")
print("You lost your adventure game, and forgot where you put it, all you know that the game is in the english pod, but the English pod is locked off for some reason...")
print("You, the student, must find your adventure game to keep Hermdog from banning you from coming to his class ever again... Hermdog is somewhere in the school building, be cautious about what steps you take, and think about what else could happen...")

done = False
adventure = 0

while not done:
    print()
    if current_room == 5 and adventure == 0:
        print("You found your adventure game in the ENGLISH POD!");
        adventure += 1
    if adventure > 0 and current_room == 0:
        print("You slam your adventure game on Hermdog's desk, and quickly escape out of the window.  Hermdog ran into his room chasing after you, and finds your adventure game.  He gave you an A, and you can to class the next week... ");
        print("Y   O   U      W   I   N   !", end="\r")
        time.sleep(1)
        print("    Y  O  U    W  I  N  !       ", end="\r")
        time.sleep(1)
        print("       Y O U  W I N !          ", end="\r")
        time.sleep(1)
        print("         YOU WIN!             ", end="\n")
        done = True
    print(room_list[current_room][0])
    user_choice1 = input("Type N, E, S, or W for directions of traversing or Q to quit: ")
    if user_choice1 == "CHEAT":
        adventure += 1
        current_room = 0
        print("You slam your adventure game on Hermdog's desk, and quickly escape out of the window.  Hermdog ran into his room chasing after you, and finds your adventure game.  He gave you an A, and you can to class the next week... ");
        print("Y   O   U      W   I   N   !", end="\r")
        time.sleep(1)
        print("    Y  O  U    W  I  N  !       ", end="\r")
        time.sleep(1)
        print("       Y O U  W I N !          ", end="\r")
        time.sleep(1)
        print("         YOU WIN!             ", end="\n")
        done = True
    if user_choice1.lower() == "n" or user_choice1.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You may not travel in that direction!")
        else:
            current_room = next_room
            hermdog_rand_and_check
    elif user_choice1.lower() == "e" or user_choice1.lower() == "east":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You may not travel in that direction!")
        else:
            current_room = next_room
            hermdog_rand_and_check
    elif user_choice1.lower() == "s" or user_choice1.lower() == "south":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You may not travel in that direction!")
        else:
            current_room = next_room
            hermdog_rand_and_check
    elif user_choice1.lower() == "w" or user_choice1.lower() == "west":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You may not travel in that direction!")
        else:
            current_room = next_room
            hermdog_rand_and_check
    elif user_choice1.lower() == "q" or user_choice1.lower() == "quit":
        done = True
