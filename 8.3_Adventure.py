'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
print("Welcome to sneaking into your kitchen simulator!")
print("You are thirsty at 3 AM and everybody in your house is sleeping")
print("You must find a way to get into the kitchen and drink the sacred ice juice")
print("Waking anybody up will fail you, god help you if you wake up h̷͚͝ì̴̝m̷̼͝")

room_list = []
item_list = []

room = ["You are in your bedroom. There is a box"]
room_list.append(room)
room = ["Bedroom 2", None, None, None]
room_list.append(room)
room = ["Bedroom 3",None,None,None,None]
room_list.append(room)
room = ["Bedroom 4",None , None, None , None]
room_list.append(room)
room = ["Bathroom",None, None, None , None]
room_list.append(room)

current_room = 0

done = False
while not done:
    print()
    print(room_list[0])
    bing = input("Type N, E, W, S, P for backpack, Q to quit or S to search")

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
    #elif bing.lower() == "s" or bing.lower() == "search":
        #if room_list ==

    #STUID
    else:
        print("That didn't make any sense, can you actually read please? Or let me know that there is something wrong with my code")


#  "\033[1;31;48m" Red
#  "\033[1;32;48m" Green
#  "\033[1;33;48m" Yellow
#  "\033[1;34;48m" Blue
#  "\033[1;35;48m" Purple
#  "\033[1;36;48m" Cyan