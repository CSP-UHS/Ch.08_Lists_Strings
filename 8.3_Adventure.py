'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[]
#create room list
room=["You are on the front porch",2,None,None,None]
room_list.append(room)
room=["You are in Bedroom 2",4,2,None,None]
room_list.append(room)
room=["You are in the South Hall",5,3,0,1]
room_list.append(room)
room=["You are in the dining room",6,None,None,2]
room_list.append(room)

current_room=0
done=False
while not done:
    print()
    print(room_list[current_room][0])
    bing=input("Type N,E,S,W for directions or Q to rage quit")

    #NORTH
    if bing.lower==("n") or bing.lower==("north"):
        nextroom=room_list[current_room][1]
    if nextroom== None:
        print("You cant go there dummy")
    else:
        current_room=nextroom

        # EAST
    elif bing.lower==("e") or bing.lower==("east"):
        nextroom = room_list[current_room][2]
    if nextroom == None:
        print("You cant go there dummy")
    else:
        current_room = nextroom

        # SOUTH
    elif bing.lower == ("s") or bing.lower == ("south"):
        nextroom = room_list[current_room][3]
    if nextroom == None:
        print("You cant go there dummy")
    else:
        current_room = nextroom

        # WEST
    elif bing.lower == ("w") or bing.lower == ("west"):
    nextroom = room_list[current_room][4]
    if nextroom == None:
    print("You cant go there dummy")
    else:
        current_room = nextroom

        #QUIT

    elif bing.lower == ("q") or bing.lower == ("quit"):
    done=True

    #stupid
    else: print("Invalid answer bud")

print("You're welcome for experiencing the best game")