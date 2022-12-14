'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import time
import random

room_list = []
# create rooms and add to room_list
room = ['''
You are in the Main hall. There are stairs going to the North going out of the building and stairs going up, leading to 
more of the building. To the East there's hallway labeled West and to the East there is a hallway labeled West. 
Whoever designed this place must've been pretty stupid. \n''', None, 1, None, 2, None]
room_list.append(room)
room = ['''
You are in the West Hallway. There's not much here so you continue walking and realise it leads to another room around 
the corner. There's really nothing to do in here so you should probably just keep going to the next room. \n''', None,
        None, 3, 0, None]
room_list.append(room)
room = ['''
You are in the East Hallway. At the end of the hallway there's a well done painting of Dust II from CSGO. Around the 
corner there is another room. Doesn't seem like there's much to do in this room, maybe the next room will be exiting.
\n''', None, 0,
        4, None, None]
room_list.append(room)
room = ['''
You are in a room with a guarded door. On either side of the door there is two stone statues on either side of the 
double doors. You start to reach for the door and you see the statue on the left turn it's head slowly. \n''',
        1, None, None, None, '''
Would you like to reach for the door?''']
room_list.append(room)
room = ['''
You are in what looks to be the Harry Potter Dining Hall. There are four differently colored tables, each full of kids 
wearing matching robes. At the front of the dining hall there's a row of old people all watching as kids go up and put a
hat on their head. As you walk past the evil looking kids you question how good of a school a place like this could be.
\n''', 2, None, 7, None, '''
Do you wish to be sorted into one of the four houses? \n''']
room_list.append(room)
room = ['''
You take a step into the void. There's nothing that you can see around you except nothingness in every direction.\n''',
        None, None, None, 6, '''
You step farther into the void hesitantly, unsure what to make of this room.As soon as you take your third step Ninja 
Tyler Blevins appears, clearly having just eaten a Takis as fire spirals around him. You realise you are not in any 
simple void, you have entered the Takis dimension and it's seriously intense. So intense you are blown back into the 
hallway. The door you just came out of disappears in a fiery swirl of intensity. It's hard to know if you'll ever 
experience something so intense ever again.''']
room_list.append(room)
room = ['''
You are in the Intersecting Hallway A. You see rooms to the North, South, and East. To the West you see a river that 
goes to the other intersecting hallway.\n''', 6, 5, 9, 7, None]
room_list.append(room)
room = ['''
You are in the Intersecting Hallway B. You see rooms to the North, South, and West. To the East you see a river that 
goes to the other intersecting hallway but it's locked right now.\n''', 4, None, 10, 8, None]
room_list.append(room)
room = ['''
You are in the NFT Room. All around you are pictures of gross monkeys and other weird pieces of "art." As you look 
around, you can't help but think, "Why would anyone pay for this?"\n''', None, 7, None, None, '''
There's really not you can do in this room, it's pretty useless. Just pointlessly large amounts of money being wasted on
bad art. But before you leave, you take out your phone and take a picture of the room, it's a free way to get the same 
thing so why not.''']
room_list.append(room)
room = ['''
You are in a warehouse with a kids ball pit in the middle. The smell of sadness and despair wafts towards you and causes
you to take a step back. As you approach the ball pit, you see a fine layer of dust across the balls, clearly never 
being touched in the last several years.\n''', 6, None, None, None, '''
You jump into the ball pit without a second of thought. It's not very deep so you heart your legs a little bit.''']
room_list.append(room)
room = ['''
You are in the Sun Room. There is a couch with a coffee table in front of it and a dinner table set for four beside it. 
The room seems like a nice calming place to sit and relax. Outside the windows on every wall, you see an unmoving forest
full of trees but with no wildlife.\n''', 7, None, None, 11, '''
Would you like to take a nap on the comfortable looking couch?''']
room_list.append(room)
room = ['''
You walk into the woods. But as soon as you take your first step out you realise this isn't actually a forest, it's 
Dust II, the map from the hit game CSGO. The door that was just there behind you is gone and you are left in this desert
hell-scape alone. Off in the distance you can hear some incomprehensible screaming drawing closer.\n''',
        None, None, None, None, '''
You run behind a box to take cover
        ''']
room_list.append(room)
room = ['''
You are in a Basketball Court. In the center is basketball super star LeBron James from the hit movie Space Jam: A New 
Legacy. He's just standing there, dribbling his basketball. No words are spoken but you can feel his energy radiating 
off of him, challenging you to play him in basketball.\n''', 0, None, None, None, '''
One bounce, two bounce, big bounce, small bounce. Lebron is watching you carefully, waiting for your first move, 
what do you do?''']
room_list.append(room)
room = ['''
You are Free of the Building. Was it all worth it? You must now go back to your meaningless, non-miraculous, 
life. In the building you had adventure, excitement, and puzzlement, it is really worth leaving behind?''', None, None,
        None, None, "Do you wish to leave?"]
room_list.append(room)

rpsguard = True
secondguard = True
current_room = 0
done = False
napt = False
bball = False
exis = False
nftpic = False
exist = False
sort = False
print('''
                                                The Building
                                              by Gabe Van Haecke


Your story begins as many adventures do, lost and all alone in an unfamiliar place.''')
time.sleep(3)
while not done:
    bong = True
    print("\n \n", room_list[current_room][0])
    while bong:
        bing = input("Type N,E,W,S directions to move, I to interact, or Q to quit - ")

        # NORTH
        if bing.lower() == "n" or bing.lower() == "north":
            next_room = room_list[current_room][1]
            if next_room is None:
                print("\nyou can't go that way\n")
                continue
            else:
                current_room = next_room
                break

        # East
        elif bing.lower() == "e" or bing.lower() == "east":
            next_room = room_list[current_room][2]
            if next_room is None:
                print("\nyou can't go that way\n")
                continue
            else:
                current_room = next_room
                break

        # South
        elif bing.lower() == "s" or bing.lower() == "south":
            next_room = room_list[current_room][3]
            if next_room is None:
                print("\nyou can't go that way\n")
                continue
            else:
                current_room = next_room
                break

        # West
        elif bing.lower() == "w" or bing.lower() == "west":
            next_room = room_list[current_room][4]
            if next_room is None:
                print("\nyou can't go that way\n")
                continue
            else:
                current_room = next_room
                break

        # Quit
        elif bing.lower() == "q" or bing.lower() == "quit":
            bong = False
            done = True

        # Interact
        elif bing.lower() == "i" or bing.lower() == "interact":
            if room_list[current_room][5] is None:
                print("\nThere's not much to do in this so you just pace around for a little bit.\n")
                continue
            else:
                print(room_list[current_room][5])
                if current_room == 3 and rpsguard:
                    guard = input("- ")
                    if guard.lower() == "y" or guard.lower() == "yes":
                        win = 0
                        loss = 0
                        rpsg = True
                        while rpsg:
                            rps = input('''
The guard to your right looks at you as your approach the door. You can feel his energy forcing you away from the door 
as you see hold out an open palm and place his fist on top of it, the universal sign of Rock Paper Scissors.

Choose rock, paper, or scissors (1=rock, 2=paper, 3=scissors) or 4 to quit - ''')
                            if rps == "1" or rps == "rock" or rps == "r":
                                rps = int(1)
                            elif rps == "2" or rps == "paper" or rps == "p":
                                rps = int(2)
                            elif rps == "3" or rps == "scissors" or rps == "s":
                                rps = int(3)
                            elif rps == "4" or rps == "quit" or rps == "q":
                                rpsg = True
                            else:
                                print('''
Please choose rock, paper, or scissors, unless you wanna quit''')
                            if rps in range(1, 4):
                                com = random.randint(1, 3)
                                time.sleep(.5)
                                print("rock")
                                time.sleep(1)
                                print("paper")
                                time.sleep(1)
                                print("scissors")
                                time.sleep(.5)
                                print("shoot")
                                time.sleep(.25)
                                if com == 3:
                                    print("Guard: Scissors")
                                elif com == 2:
                                    print("Guard: Paper")
                                else:
                                    print("Guard: Rock")
                                # all the IF statements to determine victor
                                if rps == com:
                                    print("it was a tie")
                                    continue
                                elif (rps == 1 or com == 1) and (rps == 2 or com == 2):
                                    if rps > com:
                                        print("Paper cover rock, you win!")
                                        win += 1
                                    else:
                                        print("I'm sorry to inform you that paper covers rock, you lose")
                                        loss += 1
                                elif (rps == 2 or com == 2) and (rps == 3 or com == 3):
                                    if rps > com:
                                        print("Scissors cuts paper, you win!")
                                        win += 1
                                    else:
                                        print("I'm sorry to inform you that scissors cuts paper, you lose")
                                        loss += 1
                                else:
                                    if rps < com:
                                        print("Rock smashes scissors, you win!")
                                        win += 1
                                    else:
                                        print("I'm sorry to inform you that rock smashes scissors, you lose")
                                        loss += 1
                            elif rps == 4:
                                rpsg = False
                            else:
                                print("I don't think you quite understand what's going on.")
                            if win == 1:
                                print('''
Congratulations, you beat the guard. It bows it's head, recognizing your true mastery of the classic game of Rock Paper 
Scissors. It steps out of the way to the door.''')
                                rpsguard = False
                                rpsg = False
                                room_list[3][0] = '''
You are in a room with a guarded door. On either side of the door there is two stone statues on either side
of the double doors. You have already defeated the guard on the right who challenged you to Rock Paper Scissors.
You start to reach for the door and you see the statue on the left turn it's head slowly. \n'''
                            elif loss >= 2 + win:
                                print('''
The guard has defeated you. Knocked back by the force of it's Rock Paper Scissors skill, you stumble back from 
the guard.''')
                                current_room = 1
                                rpsg = False
                            else:
                                continue
                elif current_room == 3 and not rpsguard and secondguard:
                    guard2 = input("- ")
                    if guard2.lower() == "y" or guard2.lower() == "yes":
                        print('''
As you approach the door, the second guard turns it's head slowly towards you. You realise it's not actually looking at
you, it's looking at your pocket. Taking out your phone you start to think about what the guard might want to see. You
try pictures of yourself, your family and friends, some of your favorite memes, but nothing seems to work.
''')
                        if nftpic:
                            print('''
Then you remember the picture of the nft room, maybe a useless multi-billion dollar drawing of a monkey will satisfy the
guard. You scroll to the picture of the funny monkey and show it to the guard. It is pleased and steps out of the way,
letting you enter the door.''')
                            secondguard = False
                elif current_room == 3 and not rpsguard and not secondguard:
                    noguard = input("- ")
                    if noguard.lower() == "y" or noguard.lower() == "yes":
                        print('''
Now that there is guards in the way you push past the double doors. On the other side of the door is a couch with jeans
covering every inch. The label calls it a "Jouch." Sitting on the jouch is a scrawny kid with glasses, he tells you he
actually used to be a NBA player but people doubted his epic athletic expertise. He doesn't look like an athlete but he
says he's a unit on the basketball court. You sit with him on the jouch for a little bit, listening to his stories, but
the denim you're sitting on is quite uncomfortable and you move past the door to get to the hallway to the South.
                        ''')
                        current_room = 6
                        room_list[6][1] = 3
                        room_list[6][4] = 7
                        room_list[7][2] = 6
                        room_list[3][0] = '''
You are in the once guarded room. No more guards remain so you just come in and out as you please, always seeing the guy
who use to play basketball sitting on the jouch.
'''
                        room_list[3][5] = None
                        room_list[7][0] = '''
You are in the Intersecting Hallway B. You see rooms to the North, South, and West. To the East you see a river that 
goes to the other intersecting hallway.\n'''
                elif current_room == 4 and not sort:
                    hat = input("- ")
                    if hat.lower() == "y" or hat.lower() == "yes":
                        choice = input('''
You walk up to the line of students waiting their turn to put the sorting hat on. One-by-one each student goes up, wears
the hat, sits for a couple minutes, then goes and sits at a table. You wait your turn until you can finally go up and
put the hat on your head.

The hat speaks to you, not into your ears, but more like it put the thoughts directly into your brain. "Would you like
to be sorted into Gryffindor, Hufflepuff, Slytherin, Ravenclaw, or would you like me to surprise you? ''')
                        if choice.lower() == "gryffindor" or choice.lower() == "g" or choice.lower() == "1":
                            print('''
Wow, how brave of you, you must be a true hero to join the ranks of Harry Potter and the other ones.''')
                        elif choice.lower() == "hufflepuff" or choice.lower() == "h" or choice.lower() == "2":
                            print('''Why?''')
                        elif choice.lower() == "slytherin" or choice.lower() == "s" or choice.lower() == "3":
                            print('''
So you just really wanna be evil? Well, to each their own I guess. But also know you will be the first to be accused of
just about everything that goes wrong.''')
                        elif choice.lower() == "ravenclaw" or choice.lower() == "r" or choice.lower() == "4":
                            print('''
ooo your so smart and wise, I bet you try in all your classes.''')
                        else:
                            print("I'll just pick for you")
                            time.sleep(1)
                            house = random.randint(1, 4)
                            if house == 1:
                                print("Congratulations, you are a Gryffindor, you happy now")
                            elif house == 2:
                                print("Congratulations, you are a Hufflepuff, you happy now")
                            elif house == 3:
                                print("Congratulations, you are a Slytherin, you happy now")
                            else:
                                print("Congratulations, you are a Ravenclaw, you happy now")
                        time.sleep(2)
                        print('''
You step away from the hat, exactly as you were when you first put it on but now with a title that means nothing.''')
                        room_list[4][5] = '''
You're already sorted so there's not really any purpose unless you wanna sit with the other kids who were determined to
have the same personality as you by the talking hat.\n'''
                        sort = True
                elif current_room == 5:
                    exis = True
                    current_room = 6
                    room_list[6][2] = None
                elif current_room == 8:
                    current_room = 7
                    nftpic = 8
                    room_list[8][5] = "You already got your picture so now this room is even more useless."
                elif current_room == 9:
                    if napt:
                        print('''
You search through the ball pit and find a basketball, if only there was somewhere to play. Either way it sticks out to 
you and you take it with you.

Basketball acquired!''')
                        bball = True
                    else:
                        print("There are so many balls, you are too tired to look through them after wondering this"
                              "building for so long.")
                elif current_room == 10:
                    nap = input("- ")
                    if nap.lower() == "y" or nap.lower() == "yes":
                        if exis and nftpic:
                            print('''
You curl up for a nap on the couch, quickly you drift off to sleep, exhausted from exploring the building. Dreams of the
life you lived just yesterday float around in your head. You see the home, friends, and possessions you left behind.
But you also see all the stress and responsibility you left behind, you remember the days you spent working instead of
having fun or enjoying life. Then the dream shifts and you're watching yourself at a younger age working on a homework
assignment at your desk. At the angle you are you can see the kids outside playing. You try to reach out, to worn
yourself about worrying to much about school, but as you do everything fades away and you are suddenly conscious of the 
sun room around you. Slowly you get up and take a big stretch before continuing on your journey.''')
                            exist = True
                        else:
                            print('''
You lay down for a nice nap and wake up fully rested from your long journey.''')
                        napt = True
                elif current_room == 11:
                    print('''
As you start to get a glimpse of your surroundings, a big sign gets plasters on the sky


========================================================================================================================
        Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!!

                        You you have entered an unfinished part of the game 
            You will be returned to your previous locations with the necessary resources
                                Our deepest apologies for the inconvenience.

        Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!! Error!!
========================================================================================================================

You are returned back to the sun room, now with a comically large key in one hand and a pineapple in the other.
                    ''')
                    current_room = 10
                    room_list[10][4] = None
                    room_list[0][3] = None
                elif current_room == 12:
                    if not bball:
                        print('''
You want to challenge the master at his own game, but unfortunately you don't know if you could beat him, especially
since it doesn't seem like either of you have a basketball.
                        ''')
                    else:
                        game = input("Do you want to play basketball against superstar LeBron James?")
                        if game.lower() == "y" or game.lower() == "yes":
                            print('''
You take a your first few steps towards LeBron but before you can even make it to him your friend from the jouch appears
in front of you. He takes the ball from you and turns to face LeBron James himself. Before you can stop him he is on the
other side of the court where he does a fancy looking moves and shoots a quite impressive 3 pointer. LeBron James
instantly falls to his knees with tears streaming down his face. Nothing else happens but you just sense that the front
door is open now.
                            ''')
                            room_list[0][1] = 13
                elif current_room == 13:
                    if not exist:
                        leaving = True
                        while leaving:
                            leave = input("- ")
                            if leave.lower() == "y" or leave.lower() == "yes":
                                print('''
Unfortunately due to the limitations placed on me, this isn't an option yet. But you did win so congratulations I guess.
                                ''')
                                leaving = False
                            elif leave.lower() == "n" or leave.lower() == "no":
                                print('''
You leave and go back to the real world. Congratulations you won.
                                ''')
                                leaving = False
                            else:
                                print("Please answer the question.")
                    else:
                        print('''
You wake up from the strange dream you were having. As you start to lift up your head, you wipe the drool off your cheek
and realise it got all over the desk. You look up and see the homework assignment you were working on. Suddenly you
realise the dream you were having before inside the building was you at that very moment. Quickly you rush to the window
to look outside for the kids playing, and you see them still out there, just as you had dreamt. 
''')
                        input("Do you wish to go outside?")
                    bong = False
                    done = True
            break

        # Stupid
        else:
            print("\nNot sure you understand what you are doing\n")
            continue