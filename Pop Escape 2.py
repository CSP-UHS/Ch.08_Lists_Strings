import random
#0. Text 1. East 2. South 3. West 4. North 5. Up/Down 6. North east 7. South west
room_list=[]
room=["This is your starting room", None, 1, 3, None, None, None, None]
room_list.append(room)
room=["This is the south hallway of the hospital", None, None, 2, 0, None, None, None]
room_list.append(room)
room=["This is the hospital break room", 1, None, None, None, None, None, None]
room_list.append(room)
room=["This is the north hallway of the hospital", 0, 4, 5, None, None, None, None]
room_list.append(room)
room=["This is the hospital lobby", 6, None, None, 3, None, None, None]
room_list.append(room)
room=["This is the entrance to the hospital", 3, 8, None, None, None, None, 15]
room_list.append(room)
room=["This is the hospitals x-ray screening room", None, None, 4, None, None, None, None]
room_list.append(room)
room=["This is the northern street", 5, None, 26, None, None, None, None]
room_list.append(room)
room=["This is eastern street", None, 9, None, 5, None, None, None]
room_list.append(room)
room=["This is the entrance to the cafe", 10, None, None, 8, None, None, None]
room_list.append(room)
room=["This is the cafe seating area", None, 11, 9, None, None, None, None]
room_list.append(room)
room=["This is the cafe kitchen", None, None, 13, 10, None, None, None]
room_list.append(room)
room=["This is the cafe closet", 13, None, None, None, None, None, None]
room_list.append(room)
room=["This is the cafe's drive through control room", 11, None, 12, None, None, None, None]
room_list.append(room)
room=["This is the cross street", 5, 27, 27, 5, None, 5, 27]
room_list.append(room)
room=["This is the western street", None, 27, None, 26, None, None, None]
room_list.append(room)
room=["This is your houses basement", None, None, None, 17, None, None, None]
room_list.append(room)
room=["This is your houses family room", 18, 16, 19, 21, None, None, None]
room_list.append(room)
room=["This is your houses dining room", None, None, 17, 22, None, None, None]
room_list.append(room)
room=["This is your houses west hallway", 17, None, None, 20, None, None, None]
room_list.append(room)
room=["This is your houses bathroom", None, 19, None, None, None, None, None]
room_list.append(room)
room=["This is your houses bedroom", None, 17, None, None, None, None, None]
room_list.append(room)
room=["This is your houses east hallway", 23, 18, None, 25, None, None, None]
room_list.append(room)
room=["This is your houses kitchen", None, 24, 22, None, None, None, None]
room_list.append(room)
room=["This is your kitchens walk in freezer", None, None, None, 23, None, None, None]
room_list.append(room)
room=["This is your houses living room", None, 22, 27, None, None, None, None]
room_list.append(room)
room=["This is your houses attic", None, None, None, None, 22, None, None]
room_list.append(room)
room=["This is your houses porch", 25, None, None, None, None, None, None]
room_list.append(room)
room=["This is the gas station pumps", 14, 29, 30, 15, None, None, None]
room_list.append(room)
room=["This is the gas station store", None, None, None, 28, None, None, None]
room_list.append(room)
room=["This is the truck stop", 28, None, None, None, None, None, None]
room_list.append(room)
done = False
carrot = False
medmask = False
xrayKey = False
kitchenKey = False
crewmate = False
cubeS = False
flashlight = False
closetKey = False
current_room=0
next_room = 0
Eric = False
Marie = False
Sarah = False
Alex = False
hp = 0
intel = 0
stm = 0
r1t = "no"
r2t = "no"
r3t = "no"
r4t = "no"
r5t = "no"
r6t = "no"
r7t = "no"
r8t = "no"
r9t = "no"
r10t = "no"
r11t = "no"
r12t = "no"
r13t = "no"
r14t = "no"
r15t = "no"
r16t = "no"
r17t = "no"
r18t = "no"
r19t = "no"
r20t = "no"
r21t = "no"
r22t = "no"
r23t = "no"
r24t = "no"
r25t = "no"
r26t = "no"
r27t = "no"
r28t = "no"
r29t = "no"
r30t = "no"
codeNumB = random.randrange(1000, 10000)
print("POP ESCAPE: THE STATIC FATE")
print("")
print("!!GAME MAY CONTAIN IMPLIED GORE/DEATH!!")
print("<<<Player discretion advised>>>")
print("")
print("Eric - v1 Protag: 10 hp, 10 intelligence, 10 stamina")
print("Marie - Sister: 10 hp, 7 intelligence, 15 stamina")
print("Sarah Linn - Mom: 15 hp, 10 intelligence, 8 stamina")
print("Alex - Bestie: 6 hp, 15 intelligence, 10 stamina")
plySel = str(input("Chose your character: "))
if plySel.upper() == "ERIC":
    Eric = True
elif plySel.upper() == "MARIE":
    Marie = True
elif plySel.upper() == "SARAH" or plySel.upper() == "SARAH LINN":
    Sarah = True
elif plySel.upper() == "ALEX":
    Alex = True
if Eric == True:
    hp = 10
    intel = 10
    stm = 10
    print("You wake up in the hospital bed... you were in a coma, a deep sleep")
    print("Finally you and your family's lives can go back to normal")
    print("For now...")
if Marie == True:
    hp = 10
    intel = 7
    stm = 15
    print("You sit in the hospital room, eyes peeled open")
    print("The restless nights have been rough")
    print("But waiting for Eric to wake up is worth it")
    print("You glare across the room, when you see it")
    print("He's awake")
if Sarah == True:
    hp = 15
    intel = 10
    stm = 8
    print("The outside of the hospital room is lonely")
    print("The beeping of machines floods your ears")
    print("The door bursts open")
    print("'HES AWAKE'")
if Alex == True:
    hp = 6
    intel = 15
    stm = 10
    print("You're chilling in the hospital lobby")
    print("The light flickers as you stare at your dimmed phone screen")
    print("Suddenly, *BING* *BING* *BING*")
    print("All of them read")
    print("Eric is... awake.")
while done != True:
    print(" ")
    print(room_list[current_room][0])
    pIn = str(input("Do you wish to go North, South, West, East, Up/Down, South east, North east or quit? Type I to check your inventory "))
    if pIn.upper() == "N" or pIn.upper() == "NORTH":
        next_room = room_list[current_room][4]

    elif pIn.upper() == "S" or pIn.upper() == "SOUTH":
        next_room = room_list[current_room][2]

    elif pIn.upper() == "E" or pIn.upper() == "EAST":
        next_room = room_list[current_room][1]

    elif pIn.upper() == "W" or pIn.upper() == "WEST":
        next_room = room_list[current_room][3]
    elif pIn.upper() == "U" or pIn.upper() == "UP" or pIn.upper() == "D" or pIn.upper() == "DOWN":
        next_room = room_list[current_room][5]
    elif pIn.upper() == "SW" or pIn.upper() == "SOUTH WEST":
        next_room = room_list[current_room][7]
    elif pIn.upper() == "NE" or pIn.upper() == "NORTH EAST":
        next_room = room_list[current_room][6]
    if next_room == None:
        print("You can't go that way")
    else:
        current_room = next_room

    if pIn.upper() == "Q" or pIn.upper() == "QUIT":
        print("Goodbye player!")
        done = True
    if hp <= 0:
        print("You ran out of HP")
        print("Y O U    D I E D")
        done = True
    if current_room == 1 and r1t == "no":
        print("You walk into the southern hallway, you hear... static")
        print("The pink pattern on the walls begins to shift, forming distorted imagery")
        r1 = str(input("Do you continue down the hall? "))
        if r1.upper() == "Y" or r1.upper() ==  "YES":
            print("You creep down the halls, the static growing louder")
            print("'Whats up doc!' - A distorted voice says from the corner")
            print("A furry arm breaks through the wall, its grey fur is covered in... stuff?")
            if carrot == False:
                print("The arm grabs you by the leg, its claws digging into your skin")
                print("You scream as the terrible creature takes you into the wall")
                print("Y O U    D I E D")
                done = True
            if carrot == True:
                print("You grab the carrot out of your pocket and throw it across the hall")
                print("The arm directs itself towards it")
                print("A human sized bunny breaks through the wall, leaking out of its eyes are streams of static like fluid")
                print("It goes for the carrot")
                r1 = str(input("Do you wish to attack the bunny? "))
                if r1.upper() == "YES" or r1.upper() == "Y":
                    r1t = "yes"
                    print("You lunge for the bunny, you land on its back and start beating it senseless")
                    print("It screams as the liquid flows out of its mouth, faster and faster each second")
                    print("It throws you against the wall in an attempt to survive but fails")
                    print("You survived")
                    hp-=2
                elif r1.upper() == "N" or r1.upper() == "NO":
                    print("You run while the bunny is distracted")
                    current_room = room_list[current_room][4]
        elif r1.upper() == "N" or r1.upper() ==  "NO":
                print("You turn back, feeling something watching you.")
                current_room = room_list[current_room][4]
    if current_room == 2 and r2t == "no":
        print("You walk into the break room")
        print("The emptiness disturbs you")
        print("The dim lights on the ceiling flicker as the smell of cold coffee floods your nose")
        if medmask == False:
            print("Suddenly your eyes feel... heavy")
            print("You pass out, the room spinning around you")
            current_room = room_list[current_room][1]
            current_room = room_list[current_room][4]
        elif medmask == True:
            print("You start to feel woozy...")
            print("Something in the room is causing it")
            print("You put on the medical mask to lower your intake of the rooms air")
            r2 = str(input("Do you wish to investigate the room further? "))
            if r2.upper() == "YES" or r2.upper() == "Y":
                print("You look around the room")
                print("In the corner of the room lays a flask, half filled with liquid")
                r2 = str(input("Do you inspect the flask? "))
                if r2.upper() == "YES" or r2.upper() == "Y":
                    r2t = "yes"
                    print("You pick up the flask, the corroded metal lays in your hands, scratching your bare skin")
                    print("Suddenly you hear a growl...")
                    print("A white dog, walks out from the shadowed corner... on 2 feet?")
                    print("Its eyes are filled with the same substance as the rabbit")
                    print("It bares its teeth at you, and strikes you down, mercilessly")
                    print("Y O U      D I E D")
                    done = True
                elif r2.upper() == "NO" or r2.upper() == "N":
                    print("You avoid the flask, sensing danger from it")
                    print("The rest of the room is empty except for a drawer in the back")
                    print("You open the drawer and find a key labeled 'xray'")
                    xrayKey = True
            elif r2.upper() == "NO" or r2.upper() == "N":
                print("You walk out of the room, a feeling of regret fills you")
                current_room = room_list[current_room][1]
    if current_room == 3 and r3t == "no":
        print("You walk down the north hallway, the hospitals PA system blares")
        print("'EVERYONE LEAVE THE HOSPITAL, I REPEAT EVACUATE THE HOSPITAL'")
        print("'WE ARE UNDER A-'")
        print("The announcement cuts short, silence fills the halls")
        r3 = str(input("Do you continue to walk down the halls? "))
        if r3.upper() == "YES" or r3.upper() == "Y":
            print("You walk further down the halls")
            print("The PA system starts up again but, theres no noise")
            print("Scratching noises come from the speaker, followed by murmurs")
            print("You stare down at the end of the hall")
            print("A tall redish brown figure stands where your eyes lay")
            print("Its jaw is open, showing corroded metal teeth")
            print("Grey, static like liquid, is flowing from its eyes and mouth")
            r3 = str(input("It sits still, seemingly harmless, do you wish to investigate? "))
            if r3.upper() == "YES" or r3.upper() == "Y":
                r3t = "yes"
                print("You creep closer to the figure")
                print("As you approach, its arm SLAMS to the floor, the strange liquid covering it")
                print("In the things mouth is a key, slimy with the static goop")
                kitchenKey = True
            elif r3.upper() == "NO" or r3.upper() == "N":
                print("You stand back from the creature, its glowing red eyes staring at you")
                print("Suddenly, it dashes from its spot, coming towards you")
                print("It's claws scratch the floor")
                print("You scream as its metal body slams into you")
                print("Y O U      D I E D")
                done = True
        elif r3.upper() == "NO" or r3.upper() == "N":
            print("You walk back to the start room, fear filling you")
            current_room = room_list[current_room][1]
    if current_room == 4 and r4t == "no":
        print("You walk into the desolate lobby, warm air hits your skin")
        print("Photos of happy family's sit on the wall")
        print("The longer you stare, the more distorted they become")

        if Alex == True:
            print("Suddenly, one of portraits morphs into your family")
            print("The faces of everyone but you are crossed out")
            print("It wasn't your fault")
        else:
            print("Suddenly your family morphs onto one of the portraits")
            print("Creepy.")
        print("You look around the lobby, the desk is covered in pinkish ooze")
        print("It smells like copper")
        r4 = str(input("Medical masks sit on the counter, do you wish to take one? "))
        if r4.upper() == "YES" or r4.upper() == "Y":
            print("You take a mask from the counter")
            medmask = True
            r4t = "yes"
        if r4.upper() == "NO" or r4.upper() == "N":
            print("You leave the masks, feeling something odd")
        r4 = str(input("Do you wish to look behind the desk? "))
        if r4.upper() == "YES" or r4.upper() == "Y":
            print("You creep behind the desk, fear creeping into your mind")
            print("An orange blob sits behind the desk")
            print("Its about the size of a large dog")
            print("Suddenly, it jumps up, scared")
            print("A gash on its side seems to be the source of the pink stuff")
            print("The creature has a visor like object on its face")
            print("It gives you a carrot, a gift perhaps?")
            crewmate = True
            carrot = True
            print("You try to leave but it won't leave you alone, I guess you have a pet")
        if r4.upper() == "NO" or r4.upper() == "N":
            print("You avoid the desk, suddenly a red figure jumps out of the corner")
            print("AMONGUS")
            print("It stabs you and slips into a vent to escape")
            print("Y O U     D I E D")
            done = True
    if current_room == 5 and r5t == "no":
        print("You have reached the entrance / exit to the hospital")
        if crewmate == True:
            print("Your friend walks ahead of you, looking for danger")
            print("It jumps up and down in panic")
        else:
            print("You walk towards the door, fear filling you")
        r5 = str(input("Do you continue? "))
        if r5.upper() == "YES" or r5.upper() == "Y":
            print("You walk towards the door")
            print("A keypad sits on the doors handle")
            r5 = str(input("Do you attempt to solve the code?"))
            if r5.upper() == "YES" or r5.upper() == "Y":
                r5 = int(input("What is the code?: "))
                r5t = "yes"
                if r5 == codeNumB:
                    print("You opened the door!")
                elif r5!=codeNumB:
                    print("You failed to unlock the door")
                    print("Suddenly a short blonde girl with blue striped clothes appears")
                    print("Static liquid covers her arms and legs")
                    print("Her eyes glow blue")
                    print("She charges at you, a laser beam shoots out of her eyes and impales you")
                    print("Y O U     D I E D")
                    done = True
            elif r3.upper() == "NO" or r3.upper() == "N":
                print("You walk away from the door, and back into the hall")
                current_room = room_list[current_room][1]
        elif r5.upper() == "NO" or r5.upper() == "N":
            print("You walk away from the door, it's too risky")
            current_room = room_list[current_room][1]
    if current_room == 6:
        print("You approach the door to the hospitals x-ray room")
        print("You turn the handle, but its locked")
        if xrayKey == True:
            print("You have the key")
            print("Xrays paint the walls, images of broken bones fill your eyes")
            print("You walk further into the room")
            r6 = str(input("Do you wish to look through the xrays? "))
            if r6.upper() == "YES" or r6.upper() == "Y":
                print("You look through the past xrays")
                print("As you surf through them, one catches your eye")
                print("Its a full body xray, a suit shows up in the image, the bowtie gleaming")
                print("The lights in the room flicker")
                print("The xray image starts to bend and morph")
                print("Suddenly a tall figure crawls out")
                print("It smites you down with one quick strike")
                print("Y O U     D I E D")
                done = True
            elif r6.upper() == "NO" or r6.upper() == "N":
                print("You walk away from the images, on a white board you find written numbers")
                print(codeNumB)
                codeI = True
        elif xrayKey == False:
            print("You walk away from the door, you need the key")
            current_room = room_list[current_room][3]
    if current_room == 7:
        print("You walk into the northern street")
        streetDeath = random.randrange(1,3)
        if streetDeath == 1:
            print("You cross the street, impatience hits you and you don't look before you cross")
            print("A car zooms towards you, you have no time to think and get hit")
            print("Y O U     D I E D")
            done = True
        elif streetDeath == 2:
            print("You run quickly and make it across the street safely")
    if current_room == 8:
        print("You walk into the eastern street")
        streetDeath = random.randrange(1, 3)
        if streetDeath == 1:
            print("You cross the street, impatience hits you and you don't look before you cross")
            print("A car zooms towards you, you have no time to think and get hit")
            print("Y O U     D I E D")
            done = True
        elif streetDeath == 2:
            print("You run quickly and make it across the street safely")
    if current_room == 9 and r9t == "no":
        print("You walk into the local cafe")
        print("A gumball machine sits to the right of the entrance")
        r8 = str(input("Do you wish to use the machine? "))
        if r8.upper() == "YES" or r8.upper() == "Y":
            r9t = "yes"
            print("You put a quarter into the machine")
            print("Ticks and turns sound from the machines insides")
            print("A gumball slips out of the machine, into your hand")
            gumballC = random.randrange(1, 4)
            if gumballC == 1:
                print("You take the purple gumball and slip it into your mouth")
                print("You feel stronger...")
                hp +=5
            elif gumballC == 2:
                print("You take the yellow gumball and slip it into your mouth")
                print("You feel rejuvenated...")
                stm+=5
            elif gumballC == 3:
                print("A black gumball comes out of the machine... ")
                print("You hesitantly slip the gumball into your mouth")
                print("You begin to feel sick, your throat closes up")
                print("The air escapes your lungs and you collapse")
                print("Y O U      D I E D")
                done = True
        elif r8.upper() == "NO" or r8.upper() == "N":
            print("You avoid the machine and keep walking")
    if current_room == 10 and r10t == "no":
        r10t="yes"
        print("You walk into the seating area")
        print("Catchy music plays over the restaurant speaker")
        print("The cafe is oddly empty")
        print("Green fluid is poured over all the chairs")
        print("Missing pieces of clothing cover the room")
        r10 = str(input("Do you want to investigate? "))
        if r10.upper() == "YES" or r10.upper() == "Y":
            print("You walk behind the serving counter")
            print("Laying behind the counter is a passed out old man with spiky hair")
            print("Static liquid covers his eyes, it blends with the green fluid found on the chairs")
            print("He awakes, jerking up suddenly")
            if intel > 9:
                print("You throw a pan at him and run away")
                print("But you feel... woozy")
                print("The green fluid got on you")
                print("You fall over and hurt yourself")
                hp = 1
            else:
                print("He jumps at you, barfing the green fluid onto you")
                print("You choke on the ooze")
                print("Y O U      D I E D")
                done = True
        elif r10.upper() == "NO" or r10.upper() == "N":
            print("You decide not to look around further")
    if current_room == 11 and r11t == "no":
        print("You approach the kitchen door")
        print("But its locked")
        if kitchenKey == True:
            print("You unlock the door and enter the kitchen")
            print("The room is full of shiny pans and pots, all covered in liquid static")
            r11 = str(input("Do you wish to search the drawers? "))
            if r11.upper() == "YES" or r11.upper() == "Y":
                r11t = "yes"
                print("You open the drawers one by one, each filled with nothing")
                print("Until suddenly...")
                print("One of the drawers contains a silver cube, you hear static coming from it")
                cubeS = True
            if r11.upper() == "NO" or r11.upper() == "N":
                print("You avoid looking through the drawers")
                print("You walk away from the pans and begin to hear a clanging noise...")
                print("The pots and pans begin to shake")
                print("Suddenly, a bunch of tiny sea creatures pop out of the pots")
                print("They've been filled with water the whole time")
                print("A sponge and sea star start coming for you")
                print("They're harmless, but the pouring water from the ceiling and pots isn't...")
                print("The room fills with water, unable to breath you scream, but nobody can hear you")
                print("Y O U     D I E D")
                done = True
        elif kitchenKey == False:
            print("You do not have a key")
            current_room = room_list[current_room][4]
    if current_room == 12 and r12t == "no":
        print("You grab the closet door")
        print("It doesn't budge")
        if closetKey == True:
            print("You stick the key into the lock on the door")
            if stm < 10:
                print("The door still doesn't budge")
                current_room = room_list[current_room][1]
            elif stm >= 10:
                r12t = "yes"
                print("You turn the handle vigorously, somehow it opens")
                print("You open the door and walk your way into the closet")
                if flashlight == False:
                    print("The light is broken")
                    print("You are surrounded in darkness")
                    print("The feeling of terror fills you as the door slams shut behind you")
                    print("...")
                    print("A horrifying face meets your eyes, its twisted eyes stare at you")
                    print("The static fills its eyes, before it consumes you whole")
                    print("Y O U     D I E D")
                    done = True
                elif flashlight == True:
                    print("You grab out your flashlight, hearing the click as you turn it on")
                    print("As you scan the room, you see a horrifying face")
                    print("Its eyes meet yours, static rising from its open mouth")
                    print("It lunges at you!")
                    r12 = str(input("WHAT DO YOU DO? 1. Duck, 2. Punch, 3. Run: "))
                    if r12 == "1":
                        print("You attempt to duck the creatures attack, but it hits you anyway")
                        print("You feel your ribs break, pain fills your chest as you black out")
                        print("Y O U      D I E D")
                    elif r12 == "2":
                        print("You time yourself")
                        print("You must wait till the moments right")
                        print("Its face nears yours")
                        print("You punch the creature right in the face")
                        print("It stumbles back")
                        print("It stabs you, but is too weak to do much more and flees")
                        hp=hp-2
                    elif r12 == "3":
                        print("You attempt to escape the creature")
                        print("You run for the door but it won't budge")
                        print("It crushes you, your last breath leaving your body in silence")
                        print("Y O U     D I E D")
                        done = True
        elif closetKey == False:
            print("You don't seem to have the key to this door")
            current_room = room_list[current_room][1]
    if current_room == 13 and r13t == "no":
        print("You make your way into the drive thru center")
        print("The computers around the room are glitching, sounding endless loops of static")
        r13 = str(input("Do you wish do search the room? "))
        if r13.upper() == "YES" or r13.upper() == "Y":
            r13t = "yes"
            print("You walk over to one of the computers")
            print("Suddenly the screen shifts to a log in")
            print("Podrain.gov")
            print("'Public service announcement:'")
            print("'Static. Static. Static. ctiatS. iattcS.")
            print("'Don't touch the Static.'")
            print("Suddenly the screen goes blank...")
            print("Then. Static...")
            print("A creature crawls out of the static covered computer...")
            print("Q̸̣̗͎͚̺͙̝̞̙̗͛͝E̶̘̪̘̟͈̮̽̈̿̈́͋̾Ȩ̷̤̯̮̬͇̝̻̜̪̰̀̏̀̈́̈́͒̋̿̕Ŗ̸̩̦̲̖̮̖̬̦̽͜K̸̨̪̮̬͕͍̘̍́͗͑̅̐̊̈́̅͒̚A̴̹͍̙͔̳̔͑͑̊̏̄͌͜Ś̴̢̭̗͕̱̼̹͉̟̭̗͊͒̀̓̚͝F̶̺͕͚̦̤̥̟̗̘̩̎̒̀͌͒̂N̷̛̠̟̟͈̿G̷̣̖̣̮̳͉̲̯̉͒̃̂̕")
            r13 = str(input("What do you do: 1. Run, 2. Sacrifice"))
            if r13=="1":
                print("You attempt to run from the static beast, you hit the door, you desperately grasp at the handle")
                print("Its locked...")
                print("Ṣ̴̲̥̬̠̝͈͒̒̍̌̈́̽̇́̑͐̀͝͝ͅF̴͓̘̤̩̫̯̲̤̭̪̒̈̓͐͒̽̃͜͜H̸̰͊̃̐̀̔̊͐̋̌̋̄̕S̴̡̨̨̗̯̮̻͍̠̥̍̅͌̀̌̀͑̒́̚Ḧ̷̱͂F̶͔̺͓̜͙̮̱͈̺͙̗͇̤̲̼̅̒Ä̴̡̠̳͈̰͍̠̪̗̠̪͓͕́͆͒͑͝S̴̛̤̪̦̪͓̰͖̝̝̰̤̲͍̞̀̈̚͜͝O̷̢̢̧̨̗̗͉̪̞̬̻̝͔̊̇͋͋̄͊̏̈̊͋̾̑͘͝")
                print("Y O U     D I E D")
                done = True
            elif r13=="2":
                if crewmate == True:
                    print("You look down at your orange friend... you know what you have to do")
                    print("You grab him and throw him at the creature")
                    print("His screams fill the room as you escape the room")
                elif crewmate == False:
                    print("You have nothing to sacrifice to the creature, it strikes you down in an instance")
                    print("K̵̨̡̡̧̛̺̮̗̯̱̤̟̩̦̩̲̺̮͍͖̖͈͕̗̞̤̬̤̯̖̫̼͙̹̱̜̘̜̫͚̹͖̟̖͉̹̬̈́͒͂͂̿̊̓̈͊̀̃̽̈̾͐̔̃͘͜͠Ḑ̶̛̞̥̘͎͙̭̲̱̲͑̆̿̐͒͆̇̑̐̇̽̑́͗̓̉͛̅̒̑̽̓͛̋̔̉͒͑̏̂̊̊̌̎͗̓̀̋̃̓̑̎̃̚̕͘̚͝J̸̡̧̢̡̝̼̝̗̼̺̟̗͚̠̯̤͍̫̥̘̠̟̗̬̘͉̑͐̃͛Ǎ̷̯̪̲̈́͑͒͂̽̄͛͊́̀̈́̈͊̾̍̎̏̃́͒̊̑̽̌̍̏́̎̿̐̅͊͋̏́͛͂͐̄́̕̕̕͘͘͝͠͠F̵̜̣͌̇̃̆̾́͆͘N̶̢̨̛͖̖͎̰̅́̿͐̏͌̌̏̍͒̊́̈́́̓́͌̈͌͛̐̔̒̈́̃̓̊̈́͊̉̏̃̚̕̚͝͝͝͝͝͝Ş̶̨̧̧̲̗̝̬͎̰͙̝͙͚̘̱̤̲̦̮͙̜͔̩̞̭̟͇̟̖̝̟̟̺̙̤̣̥͚̺̾̿͗͆̊̂̋̉̅̓̇̈̂̊̋͐͊̉̔͐̃̔͐̊͋͑̂̈́͑̄̓̾͌̌̐͛͘͘̕͝͠͝͝͝ͅA̶̧̨̛̹̟̳̫̤̳͎̬̳̝̥̲̯͎͈̭̠͕̫͈͔̭͍̙̪̪͖̼̞̣̪̮̩̥̹̭͓̩͉̥̜̭͇̪͇͑̈́̓̽͋͜͝ͅṀ̸̛̹͇̯̝̜͉͕̐̾͆͒̓̈́͒̊͊͒̾́̀͗̾̊̋̒͗̀̐͒͌̊̌̽̐̈́́̓̾̎͆̃͛̎͌͑͊̀͘̚̚̕̕͘͠͝")
                    print("Y O U      D I E D")
                    done = True
            if r13.upper() == "NO" or r13.upper() == "N":
                print("You avoid the rooms contents, something mysterious looms here")
    if current_room == 14:
        print("You walk into the cross street")
        streetDeath = random.randrange(1, 101)
        if streetDeath > 1:
            print("You cross the street, impatience hits you and you don't look before you cross")
            print("A car zooms towards you, you have no time to think and get hit")
            print("Y O U     D I E D")
            done = True
        else:
            print("You run quickly and make it across the street safely")
    