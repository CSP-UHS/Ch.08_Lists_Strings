'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
s="ok"
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
room=["You are in the Testing Lab",None,None,6,4]
room_list.append(room)
room=["You are in the Igloo",5,None,None,1]
room_list.append(room)
room=["You are on the Roof",None,None,4,None]
room_list.append(room)
room=[""]
current_room=0
fish=False
done=False
firstentrytoseal=False
sealkey=False
health=20
inventory=""
fishuse=False
while not done:
    print()
    print(room_list[current_room][0])
    bing=input("Type N,E,S,W for directions, I to interact,C to check condition, or Q to rage quit")

    #NORTH
    if bing.lower()=="n" or bing.lower()=="north":
        nextroom=room_list[current_room][1]
        if nextroom== None:
            print()
            print("You cant go there dummy")
        else:
            current_room=nextroom

        # EAST
    elif bing.lower()=="e" or bing.lower()=="east":
        nextroom = room_list[current_room][2]
        if nextroom == None:
            print()
            print("You cant go there dummy")
        else:
            current_room = nextroom

        # SOUTH
    elif bing.lower() == "s" or bing.lower() == "south":
        nextroom = room_list[current_room][3]
        if nextroom == None:
            print()
            print("You cant go there dummy")
        else:
            current_room = nextroom

        # WEST
    elif bing.lower() == "w" or bing.lower() == "west":
        nextroom = room_list[current_room][4]
        if nextroom == None:
            print()
            print("You cant go there dummy")
        else:
            current_room = nextroom

        #QUIT

    elif bing.lower() == "q" or bing.lower() == "quit":
        done=True

        #Status Check
    elif bing.lower()=="c" or bing.lower()=="condition":
        print()
        print(health,"/ 20")
        print()
        print(inventory)
        #INTERACT
    elif bing.lower()=="i" and current_room==0 or bing.lower()=="interact" and current_room==0:
        print()
        print("Nothing to see here just a few penguin beaks")
    elif bing.lower()=="i" and current_room==1 and fish==False or bing.lower()=="interact" and current_room==1 and fish==False:
        print()
        ans1=input(str("You look into the fish tanks and see one fish still on the bottom and notice it's colored differently than the others, do you grab it? (y/n)"))
        if ans1.lower()=="y" or ans1.lower()=="yes":
                    print()
                    print("The fish grows a pair of legs upon touch and leaps out of the water and walks into the seal room")
                    print()
                    fish=True
    elif bing.lower() == "i" and current_room == 1 and fish == True or bing.lower() == "interact" and current_room == 1 and fish == True:
        print()
        print("You've already done everything in this room")
    if current_room == 2 and bing.lower()!="i" and sealkey==False:
        print()
        print("As you enter the room you notice multiple seel underneath the water in front of you however, one of the seal seems to have a key in its mouth")
    elif bing.lower() == "i" and current_room == 2 and sealkey==False or bing.lower() == "interact" and current_room == 2 and sealkey==False:
        print()
        s=(input("You ponder a few options to try to reach the key. A.Reach into it's mouth B. Pep talk the walking fish C. Back out"))
    elif bing.lower() == "i" and current_room == 2 and sealkey == True or bing.lower() == "interact" and current_room == 2 and sealkey == True:
        print()
        print("You've already done everything in this room")
    if s.lower() == "a" and sealkey==False:
        print()
        print("You attempt to slowly reach your hand towards the key but are abruptly startled by the seals barking causing you to fall into the freezing water")
        print()
        print("You try to swim back up to the surface but the seals block your path up to the surface and you slowly die")
        done = True
    elif s.lower()=="b" and fish==True and sealkey==False:
        print()
        print("After enough persuasion the fish distracts the seals and knocks the key right to your feet that you promplty pick up")
        print()
        print("KEY ITEM ACQUIRED")
        inventory+="Key,"
        sealkey=True
    elif s.lower()=="b" and fish==False:
        print()
        print("There are no fish to pep talk")
    if fish==True and sealkey==True and fishuse==False:
        print()
        print("The fish walks back and hops into it's tank")
        fishuse=True
    #stupid
    elif current_room==3:
        print("You enter what appears to be a bedroom for.... a penguin")
        print()
    elif current_room==3 and sealkey==True and bing.lower()=="i" or current_room==3 and sealkey==True and bing.lower()=="interact":
        keyanswer=(input("You see a box with a keyhole perfectly fitting the key you have, do you use it? (y/n)"))
    if keyanswer.lower()=="y" or keyanswer.lower()=="yes":
       sealkey==False
       pingubedanswer=(input("you open the box only to find a 8 letter, 2 word phrase needed to unlock another box, do you try to attempt it? (y/n)"))
    if pingubedanswer.lower()=="noot noot":
        print()
        print("The box swings open and reveals a vile of blue dense liquid")
        print()
        print("BLUE VILE ITEM ACQUIRED")
        inventory+="Blue Liquid"


print()
print("You're welcome for experiencing the best game")