'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random
room_list=[]
room=["This is your starting room", 1, 2, 3, 4, None, 69]
room_list.append(room)
room=["This is the dining hall", None, None, 0, 6, None, 69]
room_list.append(room)
room=["This is the basement", None, None, None, 0, None, 69]
room_list.append(room)
room=["This is the west hallway", 0, None, None, 9, None, 69]
room_list.append(room)
room=["This is your bedroom", None, 0, None, None, None, 69]
room_list.append(room)
room=["This is the porch", 10, None, None, None, None, 69]
room_list.append(room)
room=["This is the east hallway", 7, 1, None, 10, 11, 69]
room_list.append(room)
room=["This is the kitchen", None, 8, 6, None, None, 69]
room_list.append(room)
room=["This is the kitchen freezer", None, None, None, 7, None, 69]
room_list.append(room)
room=["This is your bathroom", None, 3, None, None, None, 69]
room_list.append(room)
room=["This is the living room", None, 6, 5, None, None, 69]
room_list.append(room)
room=["This is the attic", None, None, None, None, 6, 69]
room_list.append(room)
r1t="no"
r4t="no"
r3t="no"
r2t="no"
r5t="no"
r6t="no"
r7t="no"
r8t="no"
r9t="no"
r10t="no"
r11t="no"
key = False
key2 = False
melatonin = False
current_room=0
next_room = 0
done=False
pills=False
codeNum=False
candy=False
gun=False
knife=False
code = False
codeNumB = random.randrange(1000, 10000)
print("POP ESCAPE!")
print("")
print("!!GAME MAY CONTAIN IMPLIED GORE/DEATH!!")
print("<<<Player discretion advised>>>")
print("")
print("You are a teenager on your way to dinner with your friends, but first you must get out of your house")
while done != True:
    print(" ")
    print(room_list[current_room][0])
    pIn = str(input("Do you wish to go North, South, West, East, Up/Down, or quit? Type I to check your inventory or DE for decrypt"))
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
    elif pIn.upper() == "ACCESSCODE4126":
        next_room = room_list[current_room][6]
    if next_room == None:
        print("You can't go that way")
    else:
        current_room = next_room

    if pIn.upper() == "Q" or pIn.upper() == "QUIT":
        print("Goodbye player!")
        done = True
    elif pIn.upper() == "I" or pIn.upper() == "Inventory":
        print("Your inventory:")
        if pills==True:
            print("Pills")
        if candy==True:
            print("Candy Bar")
        if gun==True:
            print("Gun")
        if knife==True:
            print("Knife")
        if code == True:
            print(codeNumB)
        if key2 == True:
            print("Porch Key")
        if key == True:
            print("Cabinet Key")
    elif pIn.upper() == "DECRYPT" or pIn.upper() == "DE":
        dInput = str(input("What would you like to decrypt"))
        for i in range(-30, 31):
            decrypt = ""
            for c in dInput:
                num = ord(c) + i
                newCh = chr(num)
                decrypt += newCh
            print(decrypt)
        print("Here are possible decryption options")
    #if code == True:
        #room_list[current_room][4] = 9
    #if next_room == None:
        #print("You can't go that way")
    #else:
        #current_room = next_room
    #if codeNum == True:
        #room_list[current_room][4] = 9

    if current_room == 4 and r4t=="no":
        print("You have entered the bedroom")
        r4 = str(input("Do you wish do search the dresser?"))
        if r4.upper() == "Y" or r4.upper() == "YES":
            r4t="yes"
            print("You discover a note that says among us with a small drawing on it, strange.")
            print("*CREEEK*")
            print("A big red figure appears behind you, it slaughters you with a knife and slips into the vent to escape")
            done = True
        elif r4.upper() == "N" or r4.upper() == "NO":
            print("You leave the dresser closed, and feel a feeling of regret")
    if current_room == 1 and r1t=="no":
        print("You have entered the Dining room")
        r1 = str(input("You find a big family meal set out in front of you, yet you don't have any family members, do you wish to partake?"))
        if r1.upper() == "Y" or r1.upper() == "YES":
            r1t="yes"
            print("You begin to eat the food when you start to hear a deep voice")
            print("'Homie?'")
            print("Marge simpson jumps out of the shadows, with a butchers knife in her hand")
            r1c = str(input("What do you wish to do? 1. run 2. give up hope 3. Compliment her cooking"))
            if r1c.upper() == "1" or r1c.lower() == "run":
                print("You attempt to run from marge simpson but she's too fast, she impales you with her big blue hair and you die")
                done=True
            if r1c.upper() == "2" or r1c.lower() == "give up hope":
                print("You crawl in a ball and start to cry, marge picks you up like the little piss baby you are and gives you a bottle of milk")
                print("You have been humiliated but you survive")
            if r1c.upper() == "3" or r1c.lower() == "compliment":
                print("Marge gives you a big hug and runs away joyfully")
        elif r1.upper() == "N" or r1.upper() == "NO":
            print("You walk away from the cooking, starting to feel famished")
    if current_room == 2:
        r2 = str(input("You walk down the stairs into the basement, and see a bunch of torn up training dolls, do you wish to inspect them?"))
        if r2.upper() == "Y" or r2.upper() == "YES" and r2t == "no":
            print("Naruto uzamaki pops out of the corner and assaults you")
            r2t = "yes"
            nDeath = random.randrange(0, 51)
            if nDeath >= 25:
                print("Luckily naruto is mid, you survived")
            elif nDeath < 25:
                print("Naruto solo'd you bozo #mid #solo #yourmom")
                done = True
        elif r2.upper() == "N" or r2.upper() == "NO":
            print("You avoid the training dolls and find a key!")
            key = True
    if current_room == 3 and r3t == "no":
        r3 = str(input("You walk into the west hallway, green slime is dripping from the walls, you sense danger, do you wish to go back?"))
        if r3.upper() == "Y" or r3.upper() == "YES":
            current_room = room_list[current_room][1]
        elif r3.upper() == "N" or r3.upper() == "NO":
            code = False
            print("You walk through the slimy halls")
            print("The green ooze drips from the ceiling and walls as you slowly make your way through the corridor")
            print("At the end of the hall is a keypad")
            r3 = str(input("Do you attempt to solve the code?"))
            if r3.upper() == "Y" or r3.upper() == "YES":
                r3 = int(input("Code:"))
                if r3!=codeNumB:
                    done = True
                    print("Pepe the green frog gave you a wet willy while you were attempting the code, you died from shock")
                elif r3==codeNumB:
                    print("You opened the door to the bathroom!")
                    r3t = "yes"
                    codeNum = True
            elif r3.upper() == "N" or r3.upper() == "NO":
                print("You walk away from the keypad and leave the room... for now")
                current_room = room_list[current_room][1]
    if current_room == 9 and codeNum == True:
        print("The bathroom is cold and covered in stuffed animals")
        print("A decapitated zebra plushie sits in the ice filled bath tub")
        print("the door SLAMS shut behind you... it's locked")
        r9 = str(input("What do you wish to do? 1. Check bath tub 2. Have a mental breakdown 3. Check the medicine cabinet"))
        if r9 == "1" and r9t=="no":
            r9t = "yes"
            print("You check the tub")
            print("As the cold ice fills your hands an angry red stuffed animal jumps onto your face")
            print("FIGHT IT OFF")
            elmo = 10
            playHp = 10
            while elmo > 0:
                r9 = str(input("Action: P = punch, G = grab, S = scratch"))
                if r9.upper() == "P":
                    elmo = elmo - 3
                    playHp = playHp - 3
                    print("You punched the stuffed animal")
                    print("'Elmo wants a hug!'")
                elif r9.upper() == "G":
                    elmo = elmo - 2
                    playHp = playHp - 3
                    print("You grabbed the stuffed animal and threw it")
                    print("'Hehe! Elmo is having fun")
                elif r9.upper() == "S":
                    elmo = elmo - 4
                    playHp = playHp - 3
                    print("You scratched the stuffed animal")
                    print("'Ow. That hurt elmo!")
                if playHp <= 0:
                    print("The stuffed animal killed you and played with your organs")
                    done = True
                if elmo <= 0 and playHp > 0:
                    print("You fought off the stuffed animal and survived, but you're feeling weak")
        if r9 == "2" and r9t=="no":
            print("You curl up on the floor and start to cry")
            print("A red stuffed animal crawls out of the icy tub")
            print("'Elmo wants to give hugs!'")
            print("The stuffed animal attacks you with its claws")
            print("You died")
            done = True
        if r9 == "3":
            if key == True and r9t == "no":
                print("You look at the glass mirror on the cabinet, a lock sits right in between the seperate glass panels.")
                r93 = str(input("You have a key, do you wish to open the cabinet?"))
                if r93.upper() == "Y" or r93.upper() == "YES":
                    r9t = "yes"
                    print("You stick the key into the lock, and open the door")
                    print("Inside the cabinet you find a bottle of pills, a knife, a gun, and candy.")
                    r93i = str(input("What do you do? 1. Grab the pills 2. Grab the knife 3. Grab the gun 4. Grab the candy"))
                    if r93i == "1":
                        print("You grabbed the pills")
                        pills = True
                    elif r93i == "2":
                        print("You grabbed the knife")
                        knife = True
                    elif r93i == "3":
                        print("You grabbed the gun")
                        gun = True
                    elif r93i == "4":
                        print("You grabbed the candy")
                        candy = True
                if r93.upper() == "N" or r93.upper() == "NO":
                    print("You walk away from the cabinet, and return to the center of the room")
            elif key == False:
                print("You do not have a key to open the cabinet")
    if current_room == 6 and r6t == "no":
        print("You walk down the eastern hallway, you hear a buzzing noise")
        print("Yellow-ish orange ooze is on the floor and walls")
        r6 = str(input("Do you continue to walk the passage?"))
        if r6.upper() == "Y" or r6.upper() == "YES":

            print("You continue to walk down the passage")
            print("*BZZZZ*")
            print("You begin to hear jazz music... from the ceiling?")
            r6 = str(input("Do you wish to investigate?"))
            if r6.upper() == "Y" or r6.upper() == "YES":
                print("You open the ceiling and crawl into the attic where you hear the music")
                current_room = room_list[current_room][5]
            elif r6.upper() == "N" or r6.upper() == "NO":
                print("You continue to walk through the hall")
                nDeath = random.randrange(0, 2)
                if nDeath == 0 :
                    print("'Ya like jazz?'")
                    print("Barry Bee Benson stings you in the jugular")
                    print("You have passed out and been brought back to start")
                    current_room = room_list[current_room][2]
                    current_room = room_list[current_room][3]
                elif nDeath == 1:
                    print("Nothing strange happens in the halls... somehow that itself is strange huh?")
        elif r6.upper() == "N" or r6.upper() == "NO":
            print("You return to the dining hall... could enjoy a snack while you wait to be brave right?")
            current_room = room_list[current_room][2]
    if current_room == 11 and r11t == "no":
        print("You have entered the attic")
        print("The floor creaks as you walk around")
        print("B,60 @;")
        r11 = str(input("Do you wish to investigate the room further?"))
        if r11.upper() == "YES" or r11.upper() == "Y":
            r11t="yes"
            r6t="yes"
            print("You walk further into the attic")
            print("@45?5?:@>1-8")
            print("You look around the dusty room")
            print("Numbers are written down on a piece of paper in the corner")
            print(codeNumB)
            code = True
        elif r11.upper() == "NO" or r11.upper() == "N":
            print("You leave the room... /;9- ")
            current_room = room_list[current_room][5]
    if current_room == 10 and r10t == "no":
        r10t = "yes"
        print("You walk into the living room")
        print("Pig guts are strung across the ceiling and walls")
        print("7CED=KI")
        print("The whole room is a crime scene")
        r10 = str(input("It is up to you to solve the crime, who did it? 1. Spider man 2. Carry 3. Peppa pig 4. Your mom"))
        if r10 == "1":
            print("Spider man...Really bro?")
            print("Now you're dumb AND dead")
            done = True
        elif r10 == "2":
            print("This answer makes sense")
            print("Not right tho")
            done = True
        elif r10 == "3":
            print("Good job you got it right")
            print("You'll live for now")
            print("You run towards the door and attempt to turn the handle")
            if key2==True:
                print("YES THE DOOR IS OPEN")
                current_room = room_list[current_room][3]
            elif key2 == False:
                print("The door is locked... you need a key")
                print("You turn around and Peppa pig is blocking your escape")
                print("*OINK OINK* IM PEPPA PIG")
                print("Your screams fill the living room as Peppa adds your guts to her collection on the wall")
                done = True
        elif r10 == "4":
            print("HAHAHAHAHAHA funny :|")
            print("Die bozo smh XD")
            done = True
    if current_room == 8 and r8t == "no":
        print("You walk into the cold kitchen freezer")
        print("Ice sticks to the freezer walls, you get chills up your spine")
        r8 = str(input("Do you wish to leave the desolate freezer?"))
        if r8.upper() == "Y" or r8.upper() == "YES":
            print("You walk out of the freezer, the chills still hitting your spine")
            current_room = room_list[current_room][4]
        elif r8.upper() == "N" or r8.upper() == "NO":
            print("You walk farther into the long freezer")
            print("You hear smacking noises, the sound echoing throughout the cold cavern")
            print("HO HO")
            r8 = str(input("Do you wish to investigate the noise"))
            if r8.upper() == "Y" or r8.upper() == "YES":
                print("You creep farther into the freezer")
                print("HO HO")
                print("You creep around the corner, you see MICKEY MOUSE")
                print("practicing his right hook, on a Sony printed punching bag")
                r8 = str(input("Mickey attacks, do you 1. defend yourself 2. scream 3. compliment sony"))
                if r8 == "1":
                    print("You block mickey's INSANE right hook")
                    print("He is not impressed and finishes you off")
                    done = True
                elif r8 == "2":
                    print("You begin to scream")
                    print("Mickey has no mercy...")
                    done = True
                elif r8 == "3":
                    print("You compliment sony's amazing products")
                    print("MICKEY IS ANGRY")
                    print("He screams and attacks the punching bag")
                    print("A key drops out of his pocket")
                    print("You grab it and run")
                    key2 = True
            if r8.upper() == "N" or r8.upper() == "NO":
                print("You escape the room and walk back to the kitchen")
                current_room = room_list[current_room][4]
    if current_room == 5:
        print("Finally! You have escaped your house!")
        print("Wait... somethings off")
        print("Hello business partner")
        print("Boss baby, as giant as the empire state building, stands in front of you and your house")
        if pills == True:
            print("In desperation, you take the pills in the bottle")
            print("You pass out...")
            print("You wake up, lights glaring into your eyes")
            print("It's a hospital...")
            print("You were in a coma")
            print("Your friends and family surround you... you WIN")
            print("...")
            print("799;II9E:;*'(,")
            done = True
        elif candy == True:
            print("You take out the candy bar")
            print("You open it, and have your last meal")
            print("*SPLAT")
            print("You died")
            done = True
        elif gun == True:
            print("You take out your gun, and shoot desperately at the baby")
            print("Your bullets do not phase it")
            print("You have failed... your friends will never see you at dinner")
            print("*SPLAT")
            print("You died")
            done = True
        elif knife == True:
            print("You take out your knife, and run at the baby, waving your knife in the air")
            print("The blade does not phase it")
            print("You have failed... your friends will never see you at dinner")
            print("*SPLAT")
            print("You died")
            done = True
        else:
            print("You died")
            done = True
    if current_room == 69:
        print("ACCESS CODE ACCEPTED")
        print("If you have wandered upon this message, run")
        print("It's coming")
        print("It will never stop")
        print("Escape while you can")
        print("Nobody can escape the static")
        print("...")
        print("...")
        print("...")
        print("Message deleted.")
        done = True
    if current_room == 7 and r7t == "no":
        print("You walk into the kitchen, the dim lights flicker as you walk across the cold tile")
        print("The fridge is cracked open, the frosty air seeping out")
        r7 = str(input("Do you wish to investigate the fridge"))
        if r7.upper() == "N" or r7.upper() == "NO":
            print("You walk away from the fridge, being too scared to take any of the objects")
            print("You're safe... for now")
        elif r7.upper() == "Y" or r7.upper() == "YES":
            print("You grab the fridge door and pull it fully open, the frosty air releases onto your bare arms")
            print("Inside the fridge are 3 cans of mountain dew, an among us brand pop it toy, and 3 months worth of melatonin")
            r7 = str(input("What do you wish to take, N for none, 1. Mountain dew, 2. pop it, 3. Melatonin"))
            if r7 == "1":
               print("You grab the mountain dew and continue your travels through the kitchen")
               print("suddenly you smell something...it has a scent of sweat and cheese")
               print("A shadowy figure appears in front of the kitchen doorway")
               print("DID YOU TOUCH MY DEWWW")
               print("A sweaty gamer boy who hasn't showered in weeks attacks you")
               print("You suffer a long BO filled death, as the gamer beats you to death with the DEWWWW")
               done = True
            elif r7 == "2":
                print("You snatch the pop it from the fridge")
                print("As you begin to pop the pop it, you hear children laughing")
                r7 = str(input("Do you check out the laughter?"))
                if r7.upper() == "YES" or r7.upper() == "Y":
                    print("You walk towards the laughter")
                    print("It's coming from behind the kitchen island")
                    print("You find a ginger hair dolled")
                    print("Theres...Blood on the doll")
                    print("The doll JUMPS onto your face and ends your bloodline with one swift strike")
                    done = True
            elif r7.upper() == "N" or r7.upper() == "NO":
                print("You walk away from the fridge... a feeling of emptiness fills you")
                #current_room = room_list[current_room][3]
            elif r7 == "3":
                print("You pick up the melatonin and decide to take all of it")
                print("You start to feel... dizzy")
                print("Your head hits the floor with a bang, you've passed out")
                current_room = room_list[current_room][3]
                current_room = room_list[current_room][2]
                current_room = room_list[current_room][3]
                melatonin=True
                while melatonin == True:
                    room_list = []
                    room = ["This is your starting room", 1, 2, 3, 4, None]
                    room_list.append(room)
                    room = ["This is the dining hall", None, None, 0, 6, None]
                    room_list.append(room)
                    room = ["This is the basement", None, None, None, 0, None]
                    room_list.append(room)
                    room = ["This is the west hallway", 0, None, None, 9, None]
                    room_list.append(room)
                    room = ["This is your bedroom", None, 0, None, None, None]
                    room_list.append(room)
                    room = ["This is the porch", 10, None, None, None, None]
                    room_list.append(room)
                    room = ["This is the east hallway", 7, 1, None, 10, 11]
                    room_list.append(room)
                    room = ["This is the kitchen", None, 8, 6, None, None]
                    room_list.append(room)
                    room = ["This is the kitchen freezer", None, None, None, 7, None]
                    room_list.append(room)
                    room = ["This is your bathroom", None, 3, None, None, None]
                    room_list.append(room)
                    room = ["This is the living room", None, 6, 5, None, None]
                    room_list.append(room)
                    room = ["This is the attic", None, None, None, None, 6]
                    room_list.append(room)
                    r1t1 = "no"
                    r4t1 = "no"
                    r3t1 = "no"
                    r2t1 = "no"
                    r5t1 = "no"
                    r6t1 = "no"
                    r7t1 = "no"
                    r8t1 = "no"
                    r9t1 = "no"
                    r10t1 = "no"
                    r11t1 = "no"
                    key1 = False
                    key21 = False
                    current_room = 0
                    next_room = 0
                    dead = False
                    pills1 = False
                    codeNum1 = False
                    candy1 = False
                    gun1 = False
                    knife1 = False
                    code1 = False
                    codeNumB1 = random.randrange(1000, 10000)
                    while dead != True:
                        print(" ")
                        print(room_list[current_room][0])
                        pIn1 = str(input(
                            "Do you wish to go North, South, West, East, Up/Down, or quit? Type I to check your inventory or DE for decrypt"))
                        if pIn1.upper() == "N" or pIn1.upper() == "NORTH":
                            next_room = room_list[current_room][4]

                        elif pIn1.upper() == "S" or pIn1.upper() == "SOUTH":
                            next_room = room_list[current_room][2]

                        elif pIn1.upper() == "E" or pIn1.upper() == "EAST":
                            next_room = room_list[current_room][1]

                        elif pIn1.upper() == "W" or pIn1.upper() == "WEST":
                            next_room = room_list[current_room][3]
                        elif pIn1.upper() == "U" or pIn1.upper() == "UP" or pIn.upper() == "D" or pIn.upper() == "DOWN":
                            next_room = room_list[current_room][5]
                        elif pIn.upper() == "ACCESSCODE4126":
                            next_room = room_list[current_room][6]
                        if next_room == None:
                            print("You can't go that way")
                        else:
                            current_room = next_room

                        if pIn1.upper() == "Q" or pIn1.upper() == "QUIT":
                            print("Goodbye player!")
                            melatonin = False
                            dead = True
                            done = True
                        elif pIn1.upper() == "I" or pIn1.upper() == "Inventory":
                            print("Your inventory:")
                            if pills1 == True:
                                print("Pills")
                            if candy1 == True:
                                print("Candy Bar")
                            if gun1 == True:
                                print("Gun")
                            if knife1 == True:
                                print("Knife")
                            if code1 == True:
                                print(codeNumB1)
                            if key21 == True:
                                print("Porch Key")
                            if key1 == True:
                                print("Cabinet Key")
                        elif pIn.upper() == "DECRYPT" or pIn.upper() == "DE":
                            dInput = str(input("What would you like to decrypt"))
                            for i in range(-30, 31):
                                decrypt = ""
                                for c in dInput:
                                    num = ord(c) + i
                                    newCh = chr(num)
                                    decrypt += newCh
                                print(decrypt)
                            print("Here are possible decryption options")
                        #if codeNum1 == True:
                            #room_list[current_room][4] = 9
                        # if next_room == None:
                        # print("You can't go that way")
                        # else:
                        # current_room = next_room
                        #if codeNum1 == True:
                            #room_list[current_room][4] = 9

                        if current_room == 4 and r4t1 == "no":
                            print("You have entered the bedroom")
                            r41 = str(input("Do you wish do search the dresser?"))
                            if r41.upper() == "Y" or r41.upper() == "YES":
                                r4t1 = "yes"
                                print("You found a note that says among us with a small drawing on it, strange.")
                                print("*CREEEK*")
                                print(
                                    "A big red figure appears behind you, it slaughters you with a knife and slips into the vent to escape")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][2]
                            elif r41.upper() == "N" or r41.upper() == "NO":
                                print("You leave the dresser closed, and feel a feeling of regret")
                        if current_room == 1 and r1t1 == "no":
                            print("You have entered the Dining room")
                            r11 = str(input(
                                "You find a big family meal set out in front of you, yet you don't have any family members, do you wish to partake?"))
                            if r11.upper() == "Y" or r11.upper() == "YES":
                                r1t1 = "yes"
                                print("You begin to eat the food when you start to hear a deep voice")
                                print("'Homie?'")
                                print("Marge simpson jumps out of the shadows, with a butchers knife in her hand")
                                r1c1 = str(input("What do you wish to do? 1. run 2. give up hope 3. Compliment her cooking"))
                                if r1c1.upper() == "1" or r1c1.lower() == "run":
                                    print("You attempt to run from marge simpson but she's too fast, she impales you with her big blue hair and you die")
                                    print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                    melatonin = False
                                    dead = True
                                    current_room = room_list[current_room][3]
                                if r1c1.upper() == "2" or r1c1.lower() == "give up hope":
                                    print("You crawl in a ball and start to cry, marge picks you up like the little piss baby you are and gives you a bottle of milk")
                                    print("You have been humiliated but you survive")
                                if r1c1.upper() == "3" or r1c1.lower() == "compliment":
                                    print("Marge gives you a big hug and runs away joyfully")
                            elif r11.upper() == "N" or r11.upper() == "NO":
                                print("You walk away from the cooking, starting to feel famished")
                        if current_room == 2:
                            r21 = str(input("You walk down the stairs into the basement, and see a bunch of torn up training dolls, do you wish to inspect them?"))
                            if r21.upper() == "Y" or r21.upper() == "YES" and r2t1 == "no":
                                print("Naruto uzamaki pops out of the corner and assaults you")
                                r2t1 = "yes"
                                nDeath1 = random.randrange(0, 51)
                                if nDeath1 >= 25:
                                    print("Luckily naruto is mid, you survived")
                                elif nDeath1 < 25:
                                    print("Naruto solo'd you bozo #mid #solo #yourmom")
                                    print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                    melatonin = False
                                    dead = True
                                    current_room = room_list[current_room][4]
                            elif r21.upper() == "N" or r21.upper() == "NO":
                                print("You avoid the training dolls and find a key!")
                                key1 = True
                        if current_room == 3 and r3t1 == "no":
                            r31 = str(input("You walk into the west hallway, green slime is dripping from the walls, you sense danger, do you wish to go back?"))
                            if r31.upper() == "Y" or r31.upper() == "YES":
                                current_room = room_list[current_room][1]
                            elif r31.upper() == "N" or r31.upper() == "NO":
                                code1 = False
                                print("You walk through the slimy halls")
                                print("The green ooze drips from the ceiling and walls as you slowly make your way through the corridor")
                                print("At the end of the hall is a keypad")
                                r31 = str(input("Do you attempt to solve the code?"))
                                if r31.upper() == "Y" or r31.upper() == "YES":
                                    r31 = int(input("Code:"))
                                    if r31 != codeNumB1:
                                        print("Pepe the green frog gave you a wet willy while you were attempting the code, you died from shock")
                                        print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                        melatonin = False
                                        dead = True
                                        current_room = room_list[current_room][1]
                                    elif r31 == codeNumB:
                                        print("You opened the door to the bathroom!")
                                        r3t1 = "yes"
                                        codeNum1 = True
                                elif r31.upper() == "N" or r31.upper() == "NO":
                                    print("You walk away from the keypad and leave the room... for now")
                                    current_room = room_list[current_room][1]
                        if current_room == 9 and codeNum1 == True:
                            print("The bathroom is cold and covered in stuffed animals")
                            print("A decapitated zebra plushie sits in the ice filled bath tub")
                            print("the door SLAMS shut behind you... it's locked")
                            r91 = str(input(
                                "What do you wish to do? 1. Check bath tub 2. Have a mental breakdown 3. Check the medicine cabinet"))
                            if r91 == "1" and r9t1 == "no":
                                r9t1 = "yes"
                                print("You check the tub")
                                print("As the cold ice fills your hands an angry red stuffed animal jumps onto your face")
                                print("FIGHT IT OFF")
                                elmo1 = 10
                                playHp1 = 10
                                while elmo1 > 0:
                                    r91 = str(input("Action: P = punch, G = grab, S = scratch"))
                                    if r91.upper() == "P":
                                        elmo1 = elmo1 - 3
                                        playHp1 = playHp1 - 3
                                        print("You punched the stuffed animal")
                                        print("'Elmo wants a hug!'")
                                    elif r91.upper() == "G":
                                        elmo1 = elmo1 - 2
                                        playHp1 = playHp1 - 3
                                        print("You grabbed the stuffed animal and threw it")
                                        print("'Hehe! Elmo is having fun")
                                    elif r91.upper() == "S":
                                        elmo1 = elmo1 - 4
                                        playHp1 = playHp1 - 3
                                        print("You scratched the stuffed animal")
                                        print("'Ow. That hurt elmo!")
                                    if playHp1 <= 0:
                                        print("The stuffed animal killed you and played with your organs")
                                        print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                        melatonin = False
                                        dead = True
                                        current_room = room_list[current_room][2]
                                        current_room = room_list[current_room][1]
                                    if elmo1 <= 0 and playHp1 > 0:
                                        print("You fought off the stuffed animal and survived, but you're feeling weak")
                            if r91 == "2" and r9t1 == "no":
                                print("You curl up on the floor and start to cry")
                                print("A red stuffed animal crawls out of the icy tub")
                                print("'Elmo wants to give hugs!'")
                                print("The stuffed animal attacks you with its claws")
                                print("You died")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][1]
                            if r91 == "3":
                                if key1 == True:
                                    print(
                                        "You look at the glass mirror on the cabinet, a lock sits right in between the seperate glass panels.")
                                    r931 = str(input("You have a key, do you wish to open the cabinet?"))
                                    if r931.upper() == "Y" or r931.upper() == "YES":
                                        r9t1 = "yes"
                                        print("You stick the key into the lock, and open the door")
                                        print("Inside the cabinet you find a bottle of pills, a knife, a gun, and candy.")
                                        r93i1 = str(input("What do you do? 1. Grab the pills 2. Grab the knife 3. Grab the gun 4. Grab the candy"))
                                        if r93i1 == "1":
                                            print("You grabbed the pills")
                                            pills1 = True
                                        elif r93i1 == "2":
                                            print("You grabbed the knife")
                                            knife1 = True
                                        elif r93i1 == "3":
                                            print("You grabbed the gun")
                                            gun1 = True
                                        elif r93i1 == "4":
                                            print("You grabbed the candy")
                                            candy1 = True
                                    if r931.upper() == "N" or r931.upper() == "NO":
                                        print("You walk away from the cabinet, and return to the center of the room")
                                elif key1 == False:
                                    print("You do not have a key to open the cabinet")
                        if current_room == 6 and r6t1 == "no":
                            print("You walk down the eastern hallway, you hear a buzzing noise")
                            print("Yellow-ish orange ooze is on the floor and walls")
                            r61 = str(input("Do you continue to walk the passage?"))
                            if r61.upper() == "Y" or r61.upper() == "YES":

                                print("You continue to walk down the passage")
                                print("*BZZZZ*")
                                print("You begin to hear jazz music... from the ceiling?")
                                r61 = str(input("Do you wish to investigate?"))
                                if r61.upper() == "Y" or r61.upper() == "YES":
                                    print("You open the ceiling and crawl into the attic where you hear the music")
                                    current_room = room_list[current_room][5]
                                elif r61.upper() == "N" or r61.upper() == "NO":
                                    print("You continue to walk through the hall")
                                    nDeath1 = random.randrange(0, 2)
                                    if nDeath1 == 0:
                                        print("'Ya like jazz?'")
                                        print("Barry Bee Benson stings you in the jugular")
                                        print("You have passed out and been brought back to start")
                                        current_room = room_list[current_room][2]
                                        current_room = room_list[current_room][3]
                                    elif nDeath1 == 1:
                                        print("Nothing strange happens in the halls... somehow that itself is strange huh?")
                            elif r61.upper() == "N" or r61.upper() == "NO":
                                print("You return to the dining hall... could enjoy a snack while you wait to be brave right?")
                                current_room = room_list[current_room][2]
                        if current_room == 11 and r11t1 == "no":
                            print("You have entered the attic")
                            print("The floor creaks as you walk around")
                            print("B,60 @;")
                            r111 = str(input("Do you wish to investigate the room further?"))
                            if r111.upper() == "YES" or r111.upper() == "Y":
                                r11t1 = "yes"
                                r6t1 = "yes"
                                print("You walk further into the attic")
                                print("@45?5?:@>1-8")
                                print("You look around the dusty room")
                                print("Numbers are written down on a piece of paper in the corner")
                                print(codeNumB1)
                                code1 = True
                            elif r111.upper() == "NO" or r111.upper() == "N":
                                print("You leave the room... /;9- ")
                                current_room = room_list[current_room][5]
                        if current_room == 10 and r10t1 == "no":
                            r10t1 = "yes"
                            print("You walk into the living room")
                            print("Pig guts are strung across the ceiling and walls")
                            print("7CED=KI")
                            print("The whole room is a crime scene")
                            r101 = str(input(
                                "It is up to you to solve the crime, who did it? 1. Spider man 2. Carry 3. Peppa pig 4. Your mom"))
                            if r101 == "1":
                                print("Spider man...Really bro?")
                                print("Now you're dumb AND dead")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                            elif r101 == "2":
                                print("This answer makes sense")
                                print("Not right tho")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                            elif r101 == "3":
                                print("Good job you got it right")
                                print("You'll live for now")
                                print("You run towards the door and attempt to turn the handle")
                                if key21 == True:
                                    print("YES THE DOOR IS OPEN")
                                    current_room = room_list[current_room][3]
                                elif key21 == False:
                                    print("The door is locked... you need a key")
                                    print("You turn around and Peppa pig is blocking your escape")
                                    print("*OINK OINK* IM PEPPA PIG")
                                    print("Your screams fill the living room as Peppa adds your guts to her collection on the wall")
                                    print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                    melatonin = False
                                    dead = True
                                    current_room = room_list[current_room][2]
                                    current_room = room_list[current_room][2]
                                    current_room = room_list[current_room][3]
                            elif r101 == "4":
                                print("HAHAHAHAHAHA funny :|")
                                print("Die bozo smh XD")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                        if current_room == 8 and r8t1 == "no":
                            print("You walk into the cold kitchen freezer")
                            print("Ice sticks to the freezer walls, you get chills up your spine")
                            r81 = str(input("Do you wish to leave the desolate freezer?"))
                            if r81.upper() == "Y" or r81.upper() == "YES":
                                print("You walk out of the freezer, the chills still hitting your spine")
                                current_room = room_list[current_room][4]
                            elif r81.upper() == "N" or r81.upper() == "NO":
                                print("You walk farther into the long freezer")
                                print("You hear smacking noises, the sound echoing throughout the cold cavern")
                                print("HO HO")
                                r81 = str(input("Do you wish to investigate the noise"))
                                if r81.upper() == "Y" or r81.upper() == "YES":
                                    print("You creep farther into the freezer")
                                    print("HO HO")
                                    print("You creep around the corner, you see MICKEY MOUSE")
                                    print("practicing his right hook, on a Sony printed punching bag")
                                    r81 = str(
                                        input("Mickey attacks, do you 1. defend yourself 2. scream 3. compliment sony"))
                                    if r81 == "1":
                                        print("You block mickey's INSANE right hook")
                                        print("He is not impressed and finishes you off")
                                        print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                        melatonin = False
                                        dead = True
                                        current_room = room_list[current_room][4]
                                        current_room = room_list[current_room][3]
                                        current_room = room_list[current_room][2]
                                        current_room = room_list[current_room][3]
                                    elif r81 == "2":
                                        print("You begin to scream")
                                        print("Mickey has no mercy...")
                                        print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                        melatonin = False
                                        dead = True
                                        current_room = room_list[current_room][4]
                                        current_room = room_list[current_room][3]
                                        current_room = room_list[current_room][2]
                                        current_room = room_list[current_room][3]
                                    elif r81 == "3":
                                        print("You compliment sony's amazing products")
                                        print("MICKEY IS ANGRY")
                                        print("He screams and attacks the punching bag")
                                        print("A key drops out of his pocket")
                                        print("You grab it and run")
                                        key21 = True
                                if r81.upper() == "N" or r81.upper() == "NO":
                                    print("You escape the room and walk back to the kitchen")
                                    current_room = room_list[current_room][4]
                        if current_room == 5:
                            print("Finally! You have escaped your house!")
                            print("Wait... somethings off")
                            print("Hello business partner")
                            print("Boss baby, as giant as the empire state building, stands in front of you and your house")
                            if pills1 == True:
                                print("In desperation, you take the pills in the bottle")
                                print("You pass out...")
                                print("You wake up, lights glaring into your eyes")
                                print("It's a hospital...")
                                print("You were in a coma")
                                print("Your friends and family surround you... you WIN... but still something feels off...")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][1]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                            elif candy1 == True:
                                print("You take out the candy bar")
                                print("You open it, and have your last meal")
                                print("*SPLAT")
                                print("You died")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][1]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                            elif gun1 == True:
                                print("You take out your gun, and shoot desperately at the baby")
                                print("Your bullets do not phase it")
                                print("You have failed... your friends will never see you at dinner")
                                print("*SPLAT")
                                print("You died")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][1]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                            elif knife1 == True:
                                print("You take out your knife, and run at the baby, waving your knife in the air")
                                print("The blade does not phase it")
                                print("You have failed... your friends will never see you at dinner")
                                print("*SPLAT")
                                print("You died")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][1]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                            else:
                                print("You died")
                                print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                melatonin = False
                                dead = True
                                current_room = room_list[current_room][1]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][2]
                                current_room = room_list[current_room][3]
                        if current_room == 69:
                            print("ACCESS CODE ACCEPTED")
                            print("If you have wandered upon this message, run")
                            print("It's coming")
                            print("It will never stop")
                            print("Escape while you can")
                            print("Nobody can escape the static")
                            print("...")
                            print("...")
                            print("...")
                            print("Message deleted.")
                            done = True
                        if current_room == 7 and r7t1 == "no":
                            print("You walk into the kitchen, the dim lights flicker as you walk across the cold tile")
                            print("The fridge is cracked open, the frosty air seeping out")
                            r71 = str(input("Do you wish to investigate the fridge"))
                            if r71.upper() == "Y" or r71.upper() == "YES":
                                print(
                                    "You grab the fridge door and pull it fully open, the frosty air releases onto your bare arms")
                                print(
                                    "Inside the fridge are 3 cans of mountain dew, an among us brand pop it toy, and 3 months worth of melatonin")
                                r71 = str(
                                    input("What do you wish to take, N for none, 1. Mountain dew, 2. pop it, 3. Melatonin"))
                                if r71 == "1":
                                    print("You grab the mountain dew and continue your travels through the kitchen")
                                    print("suddenly you smell something...it has a scent of sweat and cheese")
                                    print("A shadowy figure appears in front of the kitchen doorway")
                                    print("DID YOU TOUCH MY DEWWW")
                                    print("A sweaty gamer boy who hasn't showered in weeks attacks you")
                                    print("You suffer a long BO filled death, as the gamer beats you to death with the DEWWWW")
                                    print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                    melatonin = False
                                    dead = True
                                    current_room = room_list[current_room][3]
                                    current_room = room_list[current_room][2]
                                    current_room = room_list[current_room][3]

                                elif r71 == "2":
                                    print("You snatch the pop it from the fridge")
                                    print("As you begin to pop the pop it, you hear children laughing")
                                    r71 = str(input("Do you check out the laughter?"))
                                    if r71.upper() == "YES" or r71.upper() == "Y":
                                        print("You walk towards the laughter")
                                        print("It's coming from behind the kitchen island")
                                        print("You find a ginger hair dolled")
                                        print("Theres...Blood on the doll")
                                        print("The doll JUMPS onto your face and ends your bloodline with one swift strike")
                                        print("You wake up with a headache, a bottle of melatonin sits in your hand")
                                        melatonin = False
                                        dead = True
                                        current_room = room_list[current_room][3]
                                        current_room = room_list[current_room][2]
                                        current_room = room_list[current_room][3]
                                elif r71 == "3":
                                    print("You pick up the melatonin and decide to take all of it")
                                    print("You start to feel... dizzy")
                                    print("Your head hits the floor with a bang, you've passed out")
                                    current_room = room_list[current_room][3]
                                    current_room = room_list[current_room][2]
                                    current_room = room_list[current_room][3]
                                elif r71.upper() == "N" or r71.upper() == "NO":
                                    print("You walk away from the fridge, being too scared to take any of the objects")
                                    print("You're safe... for now")
                            elif r71.upper() == "N" or r71.upper() == "NO":
                                print("You walk away from the fridge... a feeling of emptiness fills you")
                                current_room = room_list[current_room][3]