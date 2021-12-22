'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
room_list=[]
#create room list
room=["You are in the Front Entrance",1,None,None,None]
room_list.append(room)
room=["You are in the Fishy Boi room",4,6,0,2]
room_list.append(room)
room=["You are in the Seal room",3,1,None,None]
room_list.append(room)
room=["You are in Pingus bedroom",None,4,2,None]
room_list.append(room)
room=["You are in the Polar Bear room",7,5,1,3]
room_list.append(room)
room=["You are in the Kitchen",None,None,6,4]
room_list.append(room)
room=["You are in the Igloo",5,None,None,1]
room_list.append(room)
room=["You are on the Roof",None,None,4,None]
room_list.append(room)
room=[""]
current_room=0
fish=False
done=False
while not done:
    print()
    print(room_list[current_room][0])
    bing=input("Type N,E,S,W for directions, I to interact or Q to rage quit")

    #NORTH
    if bing.lower()=="n" or bing.lower()=="north":
        nextroom=room_list[current_room][1]
        if nextroom== None:
            print("You cant go there dummy")
        else:
            current_room=nextroom

        # EAST
    elif bing.lower()=="e" or bing.lower()=="east":
        nextroom = room_list[current_room][2]
        if nextroom == None:
            print("You cant go there dummy")
        else:
            current_room = nextroom

        # SOUTH
    elif bing.lower() == "s" or bing.lower() == "south":
        nextroom = room_list[current_room][3]
        if nextroom == None:
            print("You cant go there dummy")
        else:
            current_room = nextroom

        # WEST
    elif bing.lower() == "w" or bing.lower() == "west":
        nextroom = room_list[current_room][4]
        if nextroom == None:
            print("You cant go there dummy")
        else:
            current_room = nextroom

        #QUIT

    elif bing.lower() == "q" or bing.lower() == "quit":
        done=True

        #INTERACT
    elif bing.lower()=="i" and current_room==0 or bing.lower()=="interact" and current_room==0:
        print()
        print("Nothing to see here just a few penguin beaks")
    elif bing.lower()=="i" and current_room==1 and fish==False or bing.lower()=="interact" and current_room==1 and fish==False:
        print()
        ans1=input(str("You look into the fish tanks and see one fish still on the bottom and is colored differently to the others, do you grab it? (y/n)"))
        if ans1.lower()=="y" or ans1.lower()=="yes":
                    print()
                    print("The fish grows a pair of legs the second it gets out of water and walks into the seal room")
                    print()
                    fish=True
    #stupid
    elif nextroom==current_room:
        print("Invalid answer bud")
    else:
        print("Invalid answer bud")

print("You're welcome for experiencing the best game")