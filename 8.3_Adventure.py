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

time.sleep(0)
#seconds = time.time()

total_time = 0
room_list = []
item_list = []
key = 'This key smells faintly of AXE deoderant.'
room = ["You are in your bedroom. There is a box with an unknown object.", 2, None, None, None] # 3 IS MEANT FOR STAIRS
room_list.append(room)
room = ["Bedroom 2, this room is silent and very dark, weirdly dark.", None, 4, 1, 3]
room_list.append(room)
room = ["Bedroom 3, this room sounds sounds of a train, also known as your dad's snoring.",None, 2, None, None]
room_list.append(room)
room = ["Bedroom 4, this room has a fan which is on and there is someone sleeping in the bedroom.",None, None, None, 2]
room_list.append(room)
room = ["Bathroom, this room is what it says it is. don't bother going there because there is nothing of interest for you there.",None, None, 2, None]
room_list.append(room)
room = ["You have done it, this is the stairs to the ground floor. You are relieved and now have the ability to go and get the sacred ice juice.",3, None, None, None]
room_list.append(room)

current_room = 0

done = False
while not done:

    print()
    print("\033[1;32;48m",room_list[current_room][0])
    bing = input("\033[1;33;48m" "Type \nN \nE \nW \nS \nP for backpack \nQ to quit \nX to search")

    #NORTH
    if bing.lower()=="n" or bing.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go there.")
        else:
            current_room = next_room
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
            print("You can't go there.")
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
        print("You are searching for a key.")
        item_list.append(key)
    #elif bing.lower() == "u" or bing.lower() == "use":
    #STUID
    else:
        print("That didn't make any sense, can you actually read please? Or let me know that there is something wrong with my code")


#  "\033[1;31;48m" Red
#  "\033[1;32;48m" Green
#  "\033[1;33;48m" Yellow
#  "\033[1;34;48m" Blue
#  "\033[1;35;48m" Purple
#  "\033[1;36;48m" Cyan