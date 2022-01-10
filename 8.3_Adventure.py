'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import time

print("Welcome to sneaking into your kitchen simulator!")
print("You are thirsty at 3 AM and everybody in your house is sleeping")
print("You must find a way to get into the kitchen and drink the sacred ice juice")
print("Waking anybody up will fail you, god help you if you wake up h̷͚͝ì̴̝m̷̼͝")
print("You have a limited amount of time, don't waste it and you will be good to go. idk why there is time but I just needed something to add.")
time.sleep(5)


room_list = []
item_list = []
key = 'This key smells faintly of AXE deoderant.'
room = ["\033[1;31;48m" "You are in your bedroom. There is the door with you in that room. Directions: N E W S, P for backpack, Q to quit, X to search, H to interact", 1, 2, 3, 4]
room_list.append(room)
room = ["\033[1;31;48m" "Bedroom 2, this room is silent and very dark, weirdly dark. Directions: N E W S, P for backpack, Q to quit, X to search, H to interact", 1, 2, 3, 4]
room_list.append(room)
room = ["\033[1;31;48m" "Bedroom 3, this room sounds sounds of a train, also known as your dad's snoring. Directions: N E W S, P for backpack, Q to quit, X to search, H to interact", 1, 2, 3, 4]
room_list.append(room)
room = ["\033[1;31;48m" "Bedroom 4, this room has a fan which is on and there is someone sleeping in the bedroom. Directions: N E W S, P for backpack, Q to quit, X to search, H to interact", 1, 2, 3, 4]
room_list.append(room)
room = ["\033[1;31;48m" "Bathroom 1, this room is what it says it is. don't bother going there because there is nothing of interest for you there. Directions: N E W S, P for backpack, Q to quit, X to search, H to interact", 1, 2, 3, 4]
room_list.append(room)

current_room = int(0)
item = [key]
done = False
while not done:
    bing = input(room_list[current_room][0])
    #NORTH
    if bing.lower()=="n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go there.")
        else:
            current_room = next_room
    #WAKES DAD UP SEQUECNCE
    #elif current_room == 1:
        #next_room = room_list[current_room][1]
    #EAST
    elif bing.lower() == "e" or bing.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go there.")
        else:
            current_room = next_room
    #SOUTH
    elif bing.lower() == "s" or bing.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go there.")
        else:
            current_room = next_room
    #WEST
    elif bing.lower() == "w" or bing.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("\033[1;31;48m""You can't go there.")
        else:
            current_room = next_room
    #QUIT
    elif bing.lower() == "q" or bing.lower() == "quit":
        done = True
    #POCKET
    elif bing.lower() == "p" or bing.lower() == "pocket":
        if len(item_list) == 0:
            print("You have nothing in your pocket")
        else:
            print(item_list)
    #SEARCH
    elif bing.lower() == "x" or bing.lower() == "search":
        if room_list[1]:
            print("\033[1;34;48m" "You have found a key in this room.")
            item_list.append(item)
        elif current_room == 1:
            print("Your father has been woken, he throws you back into your bed.")
            done = True
        else:
            print("You have found nothing in the room.")
    #UNLOCKING DOOR
    elif bing.lower() == "h" or bing.lower() == "interact":
        if len(item_list) == 1:
            print("\033[1;34;48m" "You have made it downstairs with the key that smells funny, enjoy your ice juice!")
            done = True
        else:
            print("That did nothing")


    #STUID
    else:
        print("\033[1;31;48m" "That didn't make any sense, can you actually read please? Or let me know that there is something wrong with my code")

#  "\033[1;31;48m" Red
#  "\033[1;32;48m" Green
#  "\033[1;33;48m" Yellow
#  "\033[1;34;48m" Blue
#  "\033[1;35;48m" Purple
#  "\033[1;36;48m" Cyan