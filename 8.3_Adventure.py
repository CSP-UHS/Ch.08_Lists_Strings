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
room=["You are in the Attic Room",None,None,4,None]
room_list.append(room)
room=[""]
current_room=0
fish=False
done=False
firstentrytoseal=False
sealkey=False
health=15
inventory=""
fishuse=False
keyanswer=""
pingubedanswer=""
firstentrytopinger=False
backtrack=False
pingucodeanswer="ok"
walrusrushanswer="c"
okay="w"
crafting="a"
dial="b"
trapdoor="r"
trapans="t"
sealitem="g"
beak=False
vile=False
bleeding=False
syringe=False
fullsyringe=False
tranq=False
bait=False
roomsmoved=5
while not done:
    print()
    print(room_list[current_room][0])
    bing=input("Type N,E,S,W for directions, I to interact,C to check condition, or Q to rage quit")

    #NORTH
    if bing.lower()=="n" or bing.lower()=="north":
        roomsmoved += 1
        nextroom=room_list[current_room][1]
        if nextroom== None:
            print()
            print("You cant go there dummy")
        else:
            current_room=nextroom

        # EAST
    elif bing.lower()=="e" or bing.lower()=="east":
        roomsmoved+=1
        nextroom = room_list[current_room][2]
        if nextroom == None:
            print()
            print("You cant go there dummy")
        else:
            current_room = nextroom


        # SOUTH
    elif bing.lower() == "s" or bing.lower() == "south":
        roomsmoved += 1
        nextroom = room_list[current_room][3]
        if nextroom == None:
            print()
            print("You cant go there dummy")
        else:
            current_room = nextroom

        # WEST
    elif bing.lower() == "w" or bing.lower() == "west":
        roomsmoved += 1
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
        print("HP",health,"/ 15")
        print()
        print(inventory)
        #INTERACT
    elif bing.lower()=="i" and current_room==0 and backtrack==False or bing.lower()=="interact" and current_room==0 and backtrack==False:
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
    if bing.lower() == "i" and current_room == 2 and sealkey==False or bing.lower() == "interact" and current_room == 2 and sealkey==False:
        print()
        s=(input("You ponder a few options to try to reach the key. A.Reach into it's mouth B. Pep talk the walking fish C. Back out"))
    if bing.lower() == "i" and current_room == 2 and sealkey == True and backtrack==False or bing.lower() == "interact" and current_room == 2 and sealkey == True and backtrack==False:
        print()
        print("You've already done everything in this room")
    if s.lower() == "a" and sealkey==False:
        print()
        print("You attempt to slowly reach your hand towards the key but are abruptly startled by the seals barking causing you to fall into the freezing water")
        print()
        print("You try to swim back up to the surface but the seals block your path up to the surface and you slowly die")
        done = True
    if s.lower()=="b" and fish==True and sealkey==False:
        print()
        print("After enough persuasion the fish distracts the seals and knocks the key right to your feet that you promplty pick up")
        print()
        print("KEY ITEM ACQUIRED")
        inventory+="Key,"
        sealkey=True
    if s.lower()=="b" and fish==False:
        print()
        print("There are no fish to pep talk")
    if fish==True and sealkey==True and fishuse==False:
        print()
        print("The fish walks back and hops into it's tank")
        fishuse=True
    #stupid
    elif current_room==3 and firstentrytopinger==False:
        print("You enter what appears to be a bedroom for.... a penguin")
        print()
        firstentrytopinger=True
    if current_room==3 and sealkey==True and bing.lower()=="i" or current_room==3 and sealkey==True and bing.lower()=="interact":
        keyanswer=(input("You see a box with a keyhole perfectly fitting the key you have, do you use it? (y/n)"))
    if keyanswer.lower()=="y" and vile==False and current_room==3  or keyanswer.lower()=="yes" and vile==False and current_room==3:
       pingubedanswer=(input("you open the box only to find a code needed to unlock another box, possibly a backtrack might help you find the answer, do you attempt it?"))
       backtrack=True
    if pingubedanswer.lower()=="y" and vile==False or pingubedanswer.lower()=="yes" and vile==False:
        pingucodeanswer=(input("Enter the code"))
    if pingucodeanswer=="74GBHL" and vile==False:
        print()
        print("The box swings open and reveals a vile of blue dense liquid")
        print()
        print("BLUE VILE ITEM ACQUIRED")
        inventory+="Blue Liquid"
        vile=True
    elif pingucodeanswer!="74GBHL" and pingucodeanswer!="ok":
        print()
        print("WRONG! plays out of a speaker from the box and you get sent an electric shock taking half your hp!")
        health/=2
    if current_room==3 and sealkey==False and bing.lower()=="i" or current_room==3 and sealkey==False and bing.lower()=="interact":
        print()
        print("You see a box with a keywhole however you don't seem to have a key, maybe theres one nearby?")
    if health==0 or health<0:
        print()
        print("You die from your wounds")
        done=True
    elif current_room==4 and bing.lower()!="i":
        print()
        print("You enter the room only to be immediatdely attacked by a polar bear dealing 1 bleed damage per room for the rest of the game!")
        bleeding=True
    if bleeding==True and bing.lower()=="n" or bleeding==True and bing.lower()=="e" or bleeding==True and bing.lower()=="s" or bleeding==True and bing.lower()=="w":
       health-=1
    if current_room==4 and bing.lower()=="i" and backtrack==False:
        print()
        print("There doesn't seem to be anything to do in here currently other than being attacked by polar bears")
    if current_room==5 and syringe==False:
       okay=input("Across the lab table you see a walrus staring at you menacingly, across the table you see a empty syringe do you try and grab it? (y/n)")
    if okay=="y" and bleeding==True and syringe==False:
        print("You reach over only for the walrus to recognize the smell of blood and pounce on you dealing 10 damage!")
        health-=10
    if okay=="y" and bleeding==False and syringe==False:
        print()
        walrusrushanswer=(input("You get closer to the syringe but the walrus seems more nervous, do you, A. Grab the syringe quick OR B. Continue to take it slow?"))
    if walrusrushanswer.lower()=="a" and syringe==False:
        print()
        print("You reach for the syringe but before you can even touch it the walrus pounces on you and starts mauling you causing your demise")
        done=True
    if walrusrushanswer.lower()=="b" and syringe==False:
        print()
        print("The walrus relaxes as you grab the syringe and slowly back out to the corner")
        print()
        print("SYRINGE ITEM ACQUIRED")
        inventory+=",Syringe"
        syringe=True
    if current_room==5 and syringe==True and bing.lower()=="i":
        print()
        print("It's hard to find something useful with a menacing walrus staring at you")
    if current_room==5 and syringe==True and vile==True and bing.lower()=="i" and fullsyringe==False:
        print()
        crafting=input("You go to the table to craft an item, you think about using the syringe and the vile, do you? (y/n)")
    if crafting=="y" and fullsyringe==False:
        print()
        print("ITEM ACQUIRED FULL SYRINGE")
        print()
        print("As time goes by you hear the speedy boats of the Malta army get closer, you don't have much more time to escape")
        inventory="Full syringe"
        fullsyringe=True
    if current_room==7:
        print()
        dial=(input("There seems to be a dial on the wall do you turn it? (y/n)"))
    if current_room==6 and bing.lower()=="i":
        print()
        print("The igloo seems useless as theres nothing inside or anything unusual about it")
    if dial=="y":
        roomsmoved=0
    if roomsmoved<4 and current_room==6 and bing.lower()=="i":
        print()
        trapdoor=(input("A trap door reveals itself do you enter it? (y/n)"))
    if trapdoor=="y":
        trapans=(input("You go down the trapdoor only to be pushed down to a slide nearing water do you use the syringe?(y/n)"))
    if trapans=="y" and fullsyringe==True:
        print("You inject the syringe into your veins and turn back into a penguin!, You land into the water to swim away to recooperate, this may be the end of the battle, but not the war")
        print()
        print("YOU'VE WON CONGRAGTULATIONS")
    if trapans=="y" and fullsyringe==False:
        print()
        print("As you hit the water you feel the sudden temperature drop and despite your swimming experience you freeze to death")
        done=True
    if current_room==0 and bing.lower()=="i" and backtrack==True:
        print()
        print("Upon further inspection you see a letter engraved inside one of the beaks but the lighting makes it too dark to make out the rest")
        print("ITEM AQUIRED Engraved Beak")
        inventory+=",Engraved beak"
        beak=True
    if current_room==2 and bing.lower()=="i" and sealkey==True and backtrack==True and bait==False or current_room==2 and bing.lower()=="i" and sealkey==True and backtrack==True and tranq==False :
        sealitem=(input("You notice a tranquilizer gun and bait which do you pick up?, A.Tranquilizer Gun B.Bait"))
    if sealitem.lower()=="a" and tranq==False:
        print()
        print("ITEM ACQUIRED TRANQ GUN")
        inventory+=",Tranq Gun"
        tranq=True
    if sealitem.lower()=="b" and bait==False:
        print()
        print("ITEM ACQUIRED BAIT")
        inventory+=",Bait"
        bait=True
    if current_room==4 and bing.lower()=="i" and sealitem.lower()=="b" and beak==True:
        print()
        print("You use the bait on the bear to put it on a desk as you stand across from the other side to use the flashlight to reveal the code 74GBHL")
    if current_room==4 and bing.lower()=="i" and sealitem.lower()=="a" and beak==True:
        print()
        print("You use the tranq gun on the bear only to realize theres no ammo!, the bear doesn't appreciate the attempt and mauls you til death")
        done=True
    if beak==True and current_room==4 and bing.lower()=="i" and bait==False:
        print()
        print("You notice that one of the bears has something inside it's mouth, if only you could get it still")
    if current_room==4 and bing.lower()=="n":
        print()
        print("You are in the attic")
print()
print("You're welcome for experiencing the best game ever")
