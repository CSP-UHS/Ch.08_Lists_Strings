'''
Be creative and see how far you can expand this game.
'''

import time
import random
import arcade
room_list=[]
#create rooms and add to room list
room0 = ["You are outside the mansion, looking at the front door.", 2,None,None,None]
room_list.append(room0)
room1 = ["You are in the dining room.", 4,2,None,None]
room_list.append(room1)
room2 = ["You are in the entry way.",5,3,0,1]
room_list.append(room2)
room3 = ["You are in the kitchen.", 6,None,None,2]
room_list.append(room3)
room4 = ["You are in lab.", None,5,1,None]
room_list.append(room4)
room5 = ["You are in the hallway.", 7,6,2,4]
room_list.append(room5)
room6 = ["You are in the library.", None,None,3,5]
room_list.append(room6)
room7 = ["You are in the Balcony.", None,None,5,None]
room_list.append(room7)

current_room = 0
player_health = 100
mysterio = 0
rhino = 0
sanity = 0
lizard = 0
venom = 0
green_goblin = 0
doc_oc = 0
scorpion = 0

print("You are Spiderman. You are New York's greatest superhero.")
print("But not everything about the superhero life is so great.")
print("You have to live two separate lives. If you mix them together... that's when people get hurt.")
print("And they always know exactly who to hurt.")
print("Your girlfriend and fiancee, Mary Jane, was killed.")
print("You are driven insane by a desperate drive for revenge. The only problem?")
print("You don't know who did it.")
print()
print("You have narrowed it down to seven suspects:")
print("Green Goblin, Doc Oc, Venom, Rhino, Lizard, Mysterio, and Scorpion.")
print("You have caught word of a mysterious meeting going on in a mansion on the outskirts of Pennsylvania.")
print("Your goal will be to find whoever killed your girlfriend and make them pay.")
print()
done = False
endgame = True
boss_fight = True
while not done:
    print()
    print(room_list[current_room][0])
    user_choice1 = input("Type N,S,E, or W for directions or Q to quit: ")
    if user_choice1.lower() == "cheat":
        done = False
        endgame = False
    elif user_choice1.lower() == "n" or user_choice1.lower() == "north":
        next_room = room_list[current_room][1]
        if next_room == None:
            print("You can't go that way!")
        #mysterio
        elif next_room == 2 and mysterio == 0:
            current_room = next_room
            time.sleep(.25)
            print("Mysterio is standing in the the entryway, watching you, as if he were expecting you.")
            time.sleep(.25)
            print("Mysterio: 'Hello, Peter.'")
            time.sleep(.25)
            print("He knew your first name, and your secret identity. You feel rage build up inside you.")
            time.sleep(.25)
            print("Mysterio: 'I have to say, I am truly sorry about your loss.'")
            time.sleep(.25)
            print("You: 'Shut up! I didn't come here for your sympathy! Tell me everything you know about it!")
            time.sleep(.25)
            print("He snorts.")
            time.sleep(.25)
            print("Mysterio: 'And why should I? Seriously there is no reason for me to help you.'")
            time.sleep(.25)
            print("You could force the information out of him right now (a)")
            print("Or you could ignore him and move on (b)")
            time.sleep(.25)
            user_choice2 = input("What do you do?: ")
            if user_choice2.lower() == "a":
                print("You attack Mysterio")
                time.sleep(.25)
                print("He fights back, but you are stronger. You kill him, but lose a bit of your health and sanity.")
                time.sleep(.25)
                print("But you learn that whoever killed MJ was friends with Mysterio and Venom.")
                mysterio += 1
                sanity += 1
                player_health -= 10
            else:
                print("You move on.")
                mysterio += 1
            #Mysterio encouter code\
        #venom
        elif next_room == 4 and venom == 0:
            current_room = next_room
            print("The laboratory is full of insects and viles of venom.")
            time.sleep(.25)
            print("But not the Venom you are looking for.")
            time.sleep(.25)
            print("It is an eerie quiet in the room.")
            time.sleep(.25)
            print("You : 'I know you are here, Eddie. I can sense you.'")
            time.sleep(.25)
            print("The hair on the back of your neck stands up.")
            time.sleep(2)
            print()
            time.sleep(.2)
            print()
            time.sleep(.2)
            print()
            time.sleep(.25)
            print("Venom pounces from the ceiling.")
            time.sleep(.25)
            arcade.open_window(500, 500, "Venom", True)
            arcade.set_background_color(arcade.color.WHITE)
            arcade.start_render()
            arcade.draw_lrtb_rectangle_filled(200, 300, 100, 0, (0, 0, 0))
            arcade.draw_ellipse_filled(250, 150, 250, 350, (0, 0, 0))
            arcade.draw_arc_filled(200, 200, 50, 100, (255, 255, 255), 120, 320, )
            arcade.draw_arc_filled(300, 200, 50, 100, (255, 255, 255), 45, 245, 180)
            arcade.draw_triangle_filled(175, 120, 185, 120, 185, 90, (255, 255, 255))
            arcade.draw_triangle_filled(195, 110, 205, 110, 205, 80, (255, 255, 255))
            arcade.draw_triangle_filled(215, 100, 225, 100, 220, 60, (255, 255, 255))
            arcade.draw_triangle_filled(240, 100, 250, 100, 245, 60, (255, 255, 255))
            arcade.draw_triangle_filled(265, 100, 275, 100, 270, 60, (255, 255, 255))
            arcade.draw_triangle_filled(285, 110, 295, 110, 285, 80, (255, 255, 255))
            arcade.draw_triangle_filled(305, 120, 315, 120, 305, 90, (255, 255, 255))
            arcade.draw_triangle_filled(175, 50, 185, 50, 185, 80, (255, 255, 255))
            arcade.draw_triangle_filled(195, 40, 205, 40, 205, 70, (255, 255, 255))
            arcade.draw_triangle_filled(215, 20, 225, 20, 220, 60, (255, 255, 255))
            arcade.draw_triangle_filled(240, 20, 250, 20, 245, 60, (255, 255, 255))
            arcade.draw_triangle_filled(265, 20, 275, 20, 270, 60, (255, 255, 255))
            arcade.draw_triangle_filled(285, 40, 295, 40, 285, 70, (255, 255, 255))
            arcade.draw_triangle_filled(305, 50, 315, 50, 305, 80, (255, 255, 255))
            arcade.draw_arc_filled(330, 60, 20, 175, (252, 11, 3), 45, 255, 80)
            arcade.finish_render()
            arcade.run()
            print("With seconds to think you jump to the side.")
            time.sleep(.25)
            print("Venom: 'You know, Scorpion was right about you! You are crazy now!'")
            time.sleep(.25)
            print("Venom throws a dagger at your head.")
            time.sleep(.25)
            print("You catch it with your webs and cast it to the side.")
            time.sleep(.25)
            print("Venom shifts into Eddie Brock.")
            time.sleep(.25)
            print("Eddie: 'What's up, Parker? You miss me?'")
            time.sleep(.25)
            print("You: 'How do you know my name?'")
            time.sleep(.25)
            print("Eddie: 'Don't you know? Green Goblin leaked it to all of us!'")
            time.sleep(.25)
            print("You notice the dagger still on the ground. It would be so easy to end Eddie right now.")
            if sanity > 2:
                time.sleep(.25)
                print("The temptation is too great, you web the dagger and stab Eddie in the heart.")
                sanity += 1
                venom += 1
            else:
                user_choice7 = input("Do you kill him? (Y/N): ")
                if user_choice7.lower() == "y" or user_choice7.lower() == "yes":
                    time.sleep(.25)
                    print("The temptation is too great, you web the dagger and stab Eddie in the heart.")
                    sanity += 1
                    venom += 1
                else:
                    time.sleep(.25)
                    print("You walk away from Eddie.")
                    venom +=1
        #green goblin
        elif next_room == 5 and green_goblin == 0:
            current_room = next_room
            print("You see the Green Goblin standing at the end of the hallway.")
            time.sleep(.25)
            print("He hovers on his glider, a grenade in hand.")
            time.sleep(.25)
            print("A. What have you done?")
            print("B. How did you get here?")
            print("C. Why did you kill MJ?")
            time.sleep(.25)
            user_choice8 = input("What do you say?:")
            if user_choice8.lower() == "a" or user_choice8.lower() == "what have you done?":
                time.sleep(.25)
                print("You: 'What have you done?'")
                time.sleep(.25)
                print("Green Goblin: 'I just leveled the playing field a little bit.'")
                time.sleep(.25)
                print("Green Goblin: 'You know that I am Norman Osborne, why shouldn't we know that you are Peter Parker?'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "b" or user_choice8.lower() == "how did you get here?":
                print("You: 'How did you get to this mansion?'")
                time.sleep(.25)
                print("Green Goblin: 'Come on, Peter. You should know this by now.'")
                time.sleep(.25)
                print("Green Goblin: 'Someone using the allias Otto Octavius invited each one of us here.'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "c" or user_choice8.lower() == "why did you kill mj":
                print("You: 'Why did you kill Mary Jane!'")
                time.sleep(.25)
                print("Green Goblin just laughs demonically.")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            else:
                print("Answer with one of the input options.")
        #scorpion
        elif next_room == 6 and scorpion == 0:
            time.sleep(1)
            print("The door is locked.")
        #doc oc
        elif next_room == 7 and doc_oc == 0 and mysterio == 1 and rhino == 1 and lizard == 1 and venom == 1 and green_goblin == 1:
            current_room = next_room
            time.sleep(.25)
            print("Standing on the balcony, facing away from you, is Otto Octavius.")
            time.sleep(.25)
            print("Doc Oc: 'Hello, Peter.'")
            time.sleep(.25)
            if sanity >=4:
                print("Overcome with hate, you kill Doc Oc.")
                sanity += 1
                doc_oc += 1
                done = True
                endgame = False
            else:
                print("You: 'You killed her.'")
                time.sleep(.25)
                print("Doc Oc: 'Peter, I consider you a friend, why would I kill your fiancee?'")
                time.sleep(.25)
                print("You: '...'")
                time.sleep(.25)
                print("Doc Oc: 'Peter, she was posioned.'")
                time.sleep(.25)
                print("You: '...'")
                time.sleep(.25)
                print("Doc Oc: 'Peter...'")
                time.sleep(.25)
                print("You: 'Shut up!!'")
                time.sleep(.25)
                print("You: 'Don't try and reason with me!'")
                time.sleep(.25)
                print("Doc Oc: 'Then, Peter, who did it?'")
                time.sleep(.25)
                done = True
                endgame = False
        else:
            current_room = next_room

    #North

    elif user_choice1.lower() == "e" or user_choice1.lower() == "east":
        next_room = room_list[current_room][2]
        if next_room == None:
            print("You can't go that way!")
        #lizard
        elif next_room == 3 and lizard == 0:
            current_room = next_room
            print("As you enter the kitchen, Lizard immediately attacks you!")
            time.sleep(.25)
            attack = random.randrange(1,20)
            if attack == 7:
                print("He rakes his claws aganist your chest and you die.")
                time.sleep(.25)
                print("You never learn who killed Mary Jane.")
                done = True
            else:
                print("You sense him with your spider sense and duck under his claws.")
                time.sleep(.25)
                print("You attack him and he falls back, whipping you with his tail.")
                player_health -= 10
                time.sleep(.25)
                print("You fall down, losing sight of him.")
                time.sleep(.25)
                print("When you get back up, you don't see him anywhere.")
                time.sleep(.25)
                print("He must be hiding somewhere in the kitchen.")
                time.sleep(.25)
                print("There is a refrigerator (a), a snack cabinet (b), and an oven (c).")
                user_choice4 = input("Which do you check?: ")
                if user_choice4.lower() == "a" or user_choice4.lower() == "refrigerator":
                    print("You go to check the refrigerator.")
                    time.sleep(1)
                    print("There is nothing inside. Not even food. (Rhino must have raided it).")
                    time.sleep(.25)
                    print("You leave.")

                elif user_choice4.lower() == "b" or user_choice4.lower() == "snack cabinet":
                    print("You go to check the snack cabinet")
                    time.sleep(1)
                    print("There is nothing inside. Not even snacks. (Rhino must have raided it).")
                    time.sleep(.25)
                    print("You leave.")

                elif user_choice4.lower() == "c" or user_choice4.lower() == "oven":
                    print("You go to check the oven.")
                    time.sleep(1)
                    print("You open up the oven and Lizard flys out, ready to rip you to shreds.")
                    time.sleep(.25)
                    print("You narrowly dodge him, and make sure to jump over his tail this time.")
                    time.sleep(.25)
                    print("You are able to web him up to the fridge.")
                    time.sleep(.25)
                    print("Lizard: 'Let me go Spiderman! Make this a fair fight!'")
                    time.sleep(.25)
                    print("You: 'Answer this and I will consider it!'")
                    time.sleep(.25)
                    print("A. Who invited you to this mansion?")
                    print("B. Who are you friends with of the villians?")
                    print("C. Did you kill her?")
                    user_choice5 = input("What do you say?: ")
                    if user_choice5.lower() == "a" or user_choice5.lower() == "who invited you to this mansion?":
                        print("You: 'Who invited you to this mansion?'")
                        time.sleep(.25)
                        print("Lizard: 'Same who invited everyone. You are smart, you can figure it out.'")
                        time.sleep(.25)
                        print("You: 'I don't have time for your games! Give me a name!'")
                        time.sleep(.25)
                        print("You punch him.")
                        time.sleep(.25)
                        print("Lizard: 'Doc Oc! There! You got it! Now let me go!'")
                        time.sleep(.25)
                        print("You could kill him (a) or spare him (b).")
                        user_choice6 = input("What do you do?: ")
                        if user_choice6.lower() == "a":
                            print("You kill him.")
                            time.sleep(.25)
                            sanity += 1
                            lizard += 1
                        else:
                            lizard += 1
                            print("You spare him.")
                    elif user_choice5.lower() == "b" or user_choice5.lower() == "who are you friends with of the villians?":
                        print("You: 'Who are you friends with of the villians?'")
                        time.sleep(.25)
                        print("Lizard: 'What type of question is that?'")
                        time.sleep(.25)
                        print("You: 'One that you are going to answer!'")
                        time.sleep(.25)
                        print("You raise your fist.")
                        time.sleep(.25)
                        print("Lizard: 'Okay! Okay! I'll tell you! I hang out with Green Goblin and Rhino!'")
                        time.sleep(.25)
                        print("It is unlikly that Lizard killed your girlfriend.")
                        time.sleep(.25)
                        print("You could kill him (a) or spare him (b).")
                        user_choice6 = input("What do you do?: ")
                        if user_choice6.lower() == "a":
                            print("You kill him.")
                            time.sleep(.25)
                            sanity += 1
                            lizard += 1
                        else:
                            lizard += 1
                            print("You spare him.")
                    elif user_choice5.lower() == "c" or user_choice5.lower() == "did you kill her?":
                        print("You: 'Did you kill her?'")
                        time.sleep(.25)
                        print("Lizard: 'I wish I could be the one responsible for your suffering.'")
                        time.sleep(.25)
                        print("Not giving him any time you kill him.")
                        sanity += 1
                        lizard += 1
                    else:
                        lizard += 1
                else:
                    lizard += 1

        #green goblin
        elif next_room == 5 and green_goblin == 0:
            current_room = next_room
            print("You see the Green Goblin standing at the end of the hallway.")
            time.sleep(.25)
            print("He hovers on his glider, a grenade in hand.")
            time.sleep(.25)
            print("A. What have you done?")
            print("B. How did you get here?")
            print("C. Why did you kill MJ?")
            time.sleep(.25)
            user_choice8 = input("What do you say?:")
            if user_choice8.lower() == "a" or user_choice8.lower() == "what have you done?":
                time.sleep(.25)
                print("You: 'What have you done?'")
                time.sleep(.25)
                print("Green Goblin: 'I just leveled the playing field a little bit.'")
                time.sleep(.25)
                print("Green Goblin: 'You know that I am Norman Osborne, why shouldn't we know that you are Peter Parker?'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "b" or user_choice8.lower() == "how did you get here?":
                print("You: 'How did you get to this mansion?'")
                time.sleep(.25)
                print("Green Goblin: 'Come on, Peter. You should know this by now.'")
                time.sleep(.25)
                print("Green Goblin: 'Someone using the allias Otto Octavius invited each one of us here.'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "c" or user_choice8.lower() == "why did you kill mj":
                print("You: 'Why did you kill Mary Jane!'")
                time.sleep(.25)
                print("Green Goblin just laughs demonically.")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            else:
                print("Answer with one of the input options.")

        #scorpion
        elif next_room == 6 and scorpion == 0:
            time.sleep(1)
            print("The door is locked.")
        else:
            current_room = next_room
    #east

    elif user_choice1.lower() == "s" or user_choice1.lower() == "south":
        next_room = room_list[current_room][3]
        if next_room == None:
            print("You can't go that way!")
        #rhino
        elif next_room == 1 and rhino == 0:
            current_room = next_room
            print("You see Rhino in the dining room, eating chicken.")
            time.sleep(.25)
            print("You:'Aleksei.'")
            time.sleep(.25)
            print("Rhino jumps around, and looks at you.")
            time.sleep(.25)
            print("Rhino: 'Huh?'")
            time.sleep(.25)
            print("You don't think he would be smart enough to even figure out your real idenity, let alone kill MJ.")
            time.sleep(.25)
            print("But you have been wrong before.")
            time.sleep(.25)
            print("You: 'Why are you here?'")
            time.sleep(.25)
            print("Rhino: 'Spiderman!!")
            time.sleep(.25)
            print("He charges at you.")
            time.sleep(.25)
            print("You see it coming and jump over his head, then pin him aganist the wall using your webs.")
            time.sleep(.25)
            print("You: 'I'll only ask once more!'")
            time.sleep(.25)
            print("You: 'Why are you here?!")
            time.sleep(.25)
            print("Rhino: 'Doc Oc invited me. He said there would be lots of food and a chance to kill Spiderman.'")
            time.sleep(.25)
            print("You think Rhino's story is pretty believable, do you spare him (a)?")
            print("Or kill him (b)?")
            user_choice3 = input("What do you do?: ")
            if user_choice3.lower() == "b":
                print("You kill Rhino and move on. You feel your morals slipping away.")
                sanity += 1
                rhino += 1
            else:
                print("You continue your search.")
                rhino += 1

        #lizard
        elif next_room == 3 and lizard == 0:
            current_room = next_room
            print("As you enter the kitchen, Lizard immediately attacks you!")
            time.sleep(.25)
            attack = random.randrange(1,20)
            if attack == 7:
                print("He rakes his claws aganist your chest and you die.")
                time.sleep(.25)
                print("You never learn who killed Mary Jane.")
                done = True
            else:
                print("You sense him with your spider sense and duck under his claws.")
                time.sleep(.25)
                print("You attack him and he falls back, whipping you with his tail.")
                player_health -= 10
                time.sleep(.25)
                print("You fall down, losing sight of him.")
                time.sleep(.25)
                print("When you get back up, you don't see him anywhere.")
                time.sleep(.25)
                print("He must be hiding somewhere in the kitchen.")
                time.sleep(.25)
                print("There is a refrigerator (a), a snack cabinet (b), and an oven (c).")
                user_choice4 = input("Which do you check?: ")
                if user_choice4.lower() == "a" or user_choice4.lower() == "refrigerator":
                    print("You go to check the refrigerator.")
                    time.sleep(1)
                    print("There is nothing inside. Not even food. (Rhino must have raided it).")
                    time.sleep(.25)
                    print("You leave.")

                elif user_choice4.lower() == "b" or user_choice4.lower() == "snack cabinet":
                    print("You go to check the snack cabinet")
                    time.sleep(1)
                    print("There is nothing inside. Not even snacks. (Rhino must have raided it).")
                    time.sleep(.25)
                    print("You leave.")

                elif user_choice4.lower() == "c" or user_choice4.lower() == "oven":
                    print("You go to check the oven.")
                    time.sleep(1)
                    print("You open up the oven and Lizard flys out, ready to rip you to shreds.")
                    time.sleep(.25)
                    print("You narrowly dodge him, and make sure to jump over his tail this time.")
                    time.sleep(.25)
                    print("You are able to web him up to the fridge.")
                    time.sleep(.25)
                    print("Lizard: 'Let me go Spiderman! Make this a fair fight!'")
                    time.sleep(.25)
                    print("You: 'Answer this and I will consider it!'")
                    time.sleep(.25)
                    print("A. Who invited you to this mansion?")
                    print("B. Who are you friends with of the villians?")
                    print("C. Did you kill her?")
                    user_choice5 = input("What do you say?: ")
                    if user_choice5.lower() == "a" or user_choice5.lower() == "who invited you to this mansion?":
                        print("You: 'Who invited you to this mansion?'")
                        time.sleep(.25)
                        print("Lizard: 'Same who invited everyone. You are smart, you can figure it out.'")
                        time.sleep(.25)
                        print("You: 'I don't have time for your games! Give me a name!'")
                        time.sleep(.25)
                        print("You punch him.")
                        time.sleep(.25)
                        print("Lizard: 'Doc Oc! There! You got it! Now let me go!'")
                        time.sleep(.25)
                        print("You could kill him (a) or spare him (b).")
                        user_choice6 = input("What do you do?: ")
                        if user_choice6.lower() == "a":
                            print("You kill him.")
                            time.sleep(.25)
                            sanity += 1
                            lizard += 1
                        else:
                            lizard += 1
                            print("You spare him.")
                    elif user_choice5.lower() == "b" or user_choice5.lower() == "who are you friends with of the villians?":
                        print("You: 'Who are you friends with of the villians?'")
                        time.sleep(.25)
                        print("Lizard: 'What type of question is that?'")
                        time.sleep(.25)
                        print("You: 'One that you are going to answer!'")
                        time.sleep(.25)
                        print("You raise your fist.")
                        time.sleep(.25)
                        print("Lizard: 'Okay! Okay! I'll tell you! I hang out with Green Goblin and Rhino!'")
                        time.sleep(.25)
                        print("It is unlikly that Lizard killed your girlfriend.")
                        time.sleep(.25)
                        print("You could kill him (a) or spare him (b).")
                        user_choice6 = input("What do you do?: ")
                        if user_choice6.lower() == "a":
                            print("You kill him.")
                            time.sleep(.25)
                            sanity += 1
                            lizard += 1
                        else:
                            lizard += 1
                            print("You spare him.")
                    elif user_choice5.lower() == "c" or user_choice5.lower() == "did you kill her?":
                        print("You: 'Did you kill her?'")
                        time.sleep(.25)
                        print("Lizard: 'I wish I could be the one responsible for your suffering.'")
                        time.sleep(.25)
                        print("Not giving him any time you kill him.")
                        sanity += 1
                        lizard += 1
                    else:
                        lizard += 1
                else:
                    lizard += 1

        #green goblin
        elif next_room == 5 and green_goblin == 0:
            current_room = next_room
            print("You see the Green Goblin standing at the end of the hallway.")
            time.sleep(.25)
            print("He hovers on his glider, a grenade in hand.")
            time.sleep(.25)
            print("A. What have you done?")
            print("B. How did you get here?")
            print("C. Why did you kill MJ?")
            time.sleep(.25)
            user_choice8 = input("What do you say?:")
            if user_choice8.lower() == "a" or user_choice8.lower() == "what have you done?":
                time.sleep(.25)
                print("You: 'What have you done?'")
                time.sleep(.25)
                print("Green Goblin: 'I just leveled the playing field a little bit.'")
                time.sleep(.25)
                print("Green Goblin: 'You know that I am Norman Osborne, why shouldn't we know that you are Peter Parker?'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "b" or user_choice8.lower() == "how did you get here?":
                print("You: 'How did you get to this mansion?'")
                time.sleep(.25)
                print("Green Goblin: 'Come on, Peter. You should know this by now.'")
                time.sleep(.25)
                print("Green Goblin: 'Someone using the allias Otto Octavius invited each one of us here.'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "c" or user_choice8.lower() == "why did you kill mj":
                print("You: 'Why did you kill Mary Jane!'")
                time.sleep(.25)
                print("Green Goblin just laughs demonically.")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            else:
                print("Answer with one of the input options.")
        else:
            current_room = next_room
    #south

    elif user_choice1.lower() == "w" or user_choice1.lower() == "west":
        next_room = room_list[current_room][4]
        if next_room == None:
            print("You can't go that way!")
        #rhino
        elif next_room == 1 and rhino == 0:
            current_room = next_room
            print("You see Rhino in the dining room, eating chicken.")
            time.sleep(.25)
            print("You:'Aleksei.'")
            time.sleep(.25)
            print("Rhino jumps around, and looks at you.")
            time.sleep(.25)
            print("Rhino: 'Huh?'")
            time.sleep(.25)
            print("You don't think he would be smart enough to even figure out your real idenity, let alone kill MJ.")
            time.sleep(.25)
            print("But you have been wrong before.")
            time.sleep(.25)
            print("You: 'Why are you here?'")
            time.sleep(.25)
            print("Rhino: 'Spiderman!!")
            time.sleep(.25)
            print("He charges at you.")
            time.sleep(.25)
            print("You see it coming and jump over his head, then pin him aganist the wall using your webs.")
            time.sleep(.25)
            print("You: 'I'll only ask once more!'")
            time.sleep(.25)
            print("You: 'Why are you here?!")
            time.sleep(.25)
            print("Rhino: 'Doc Oc invited me. He said there would be lots of food and a chance to kill Spiderman.'")
            time.sleep(.25)
            print("You think Rhino's story is pretty believable, do you spare him (a)?")
            print("Or kill him (b)?")
            user_choice3 = input("What do you do?: ")
            if user_choice3.lower() == "b":
                print("You kill Rhino and move on. You feel your morals slipping away.")
                sanity += 1
                rhino += 1
            else:
                print("You continue your search.")
                rhino += 1

        #venom
        elif next_room == 4 and venom == 0:
            current_room = next_room
            print("The laboratory is full of insects and viles of venom.")
            time.sleep(.25)
            print("But not the Venom you are looking for.")
            time.sleep(.25)
            print("It is an eerie quiet in the room.")
            time.sleep(.25)
            print("You : 'I know you are here, Eddie. I can sense you.'")
            time.sleep(.25)
            print("The hair on the back of your neck stands up.")
            time.sleep(2)
            print()
            time.sleep(.2)
            print()
            time.sleep(.2)
            print()
            time.sleep(.25)
            print("Venom pounces from the ceiling.")
            time.sleep(.25)
            arcade.open_window(500, 500, "Venom", True)
            arcade.set_background_color(arcade.color.WHITE)
            arcade.start_render()
            arcade.draw_lrtb_rectangle_filled(200, 300, 100, 0, (0, 0, 0))
            arcade.draw_ellipse_filled(250, 150, 250, 350, (0, 0, 0))
            arcade.draw_arc_filled(200, 200, 50, 100, (255, 255, 255), 120, 320, )
            arcade.draw_arc_filled(300, 200, 50, 100, (255, 255, 255), 45, 245, 180)
            arcade.draw_triangle_filled(175, 120, 185, 120, 185, 90, (255, 255, 255))
            arcade.draw_triangle_filled(195, 110, 205, 110, 205, 80, (255, 255, 255))
            arcade.draw_triangle_filled(215, 100, 225, 100, 220, 60, (255, 255, 255))
            arcade.draw_triangle_filled(240, 100, 250, 100, 245, 60, (255, 255, 255))
            arcade.draw_triangle_filled(265, 100, 275, 100, 270, 60, (255, 255, 255))
            arcade.draw_triangle_filled(285, 110, 295, 110, 285, 80, (255, 255, 255))
            arcade.draw_triangle_filled(305, 120, 315, 120, 305, 90, (255, 255, 255))
            arcade.draw_triangle_filled(175, 50, 185, 50, 185, 80, (255, 255, 255))
            arcade.draw_triangle_filled(195, 40, 205, 40, 205, 70, (255, 255, 255))
            arcade.draw_triangle_filled(215, 20, 225, 20, 220, 60, (255, 255, 255))
            arcade.draw_triangle_filled(240, 20, 250, 20, 245, 60, (255, 255, 255))
            arcade.draw_triangle_filled(265, 20, 275, 20, 270, 60, (255, 255, 255))
            arcade.draw_triangle_filled(285, 40, 295, 40, 285, 70, (255, 255, 255))
            arcade.draw_triangle_filled(305, 50, 315, 50, 305, 80, (255, 255, 255))
            arcade.draw_arc_filled(330, 60, 20, 175, (252, 11, 3), 45, 255, 80)
            arcade.finish_render()
            arcade.run()
            print("With seconds to think you jump to the side.")
            time.sleep(.25)
            print("Venom: 'You know, Scorpion was right about you! You are crazy now!'")
            time.sleep(.25)
            print("Venom throws a dagger at your head.")
            time.sleep(.25)
            print("You catch it with your webs and cast it to the side.")
            time.sleep(.25)
            print("Venom shifts into Eddie Brock.")
            time.sleep(.25)
            print("Eddie: 'What's up, Parker? You miss me?'")
            time.sleep(.25)
            print("You: 'How do you know my name?'")
            time.sleep(.25)
            print("Eddie: 'Don't you know? Green Goblin leaked it to all of us!'")
            time.sleep(.25)
            print("You notice the dagger still on the ground. It would be so easy to end Eddie right now.")
            if sanity > 2:
                time.sleep(.25)
                print("The temptation is too great, you web the dagger and stab Eddie in the heart.")
                sanity += 1
                venom += 1
            else:
                user_choice7 = input("Do you kill him? (Y/N): ")
                if user_choice7.lower() == "y" or user_choice7.lower() == "yes":
                    time.sleep(.25)
                    print("The temptation is too great, you web the dagger and stab Eddie in the heart.")
                    sanity += 1
                    venom += 1
                else:
                    time.sleep(.25)
                    print("You walk away from Eddie.")
                    venom +=1

        #green goblin
        elif next_room == 5 and green_goblin == 0:
            current_room = next_room
            print("You see the Green Goblin standing at the end of the hallway.")
            time.sleep(.25)
            print("He hovers on his glider, a grenade in hand.")
            time.sleep(.25)
            print("A. What have you done?")
            print("B. How did you get here?")
            print("C. Why did you kill MJ?")
            time.sleep(.25)
            user_choice8 = input("What do you say?:")
            if user_choice8.lower() == "a" or user_choice8.lower() == "what have you done?":
                time.sleep(.25)
                print("You: 'What have you done?'")
                time.sleep(.25)
                print("Green Goblin: 'I just leveled the playing field a little bit.'")
                time.sleep(.25)
                print("Green Goblin: 'You know that I am Norman Osborne, why shouldn't we know that you are Peter Parker?'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "b" or user_choice8.lower() == "how did you get here?":
                print("You: 'How did you get to this mansion?'")
                time.sleep(.25)
                print("Green Goblin: 'Come on, Peter. You should know this by now.'")
                time.sleep(.25)
                print("Green Goblin: 'Someone using the allias Otto Octavius invited each one of us here.'")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            elif user_choice8.lower() == "c" or user_choice8.lower() == "why did you kill mj":
                print("You: 'Why did you kill Mary Jane!'")
                time.sleep(.25)
                print("Green Goblin just laughs demonically.")
                time.sleep(.25)
                if sanity > 2:
                    print("Green Goblin: 'I can smell blood on you, Spiderman. You are no better than any of us.'")
                    time.sleep(.25)
                    print("You: 'You took something from me!'")
                    time.sleep(.25)
                    print("You kill Green Goblin. You feel yourself filling with more and more hate.")
                    sanity += 1
                    green_goblin += 1
                else:
                    print("Green Goblin throws a grenade at you!")
                    time.sleep(1)
                    print("You dodge it but it still does a little bit of damage.")
                    time.sleep(.25)
                    player_health -= 5
                    user_choice9 = input("Do you kill him (a) or turn the other way (b)?: ")
                    if user_choice9.lower() == "a":
                        time.sleep(.25)
                        print("You kill him.")
                        sanity += 1
                        green_goblin += 1
                    else:
                        time.sleep(.25)
                        print("You ignore him. You are better than him.")
                        time.sleep(1)
                        print("Or are you?")
                        green_goblin += 1
            else:
                print("Answer with one of the input options.")
        else:
            current_room = next_room
    #west

    elif user_choice1.lower() == "q" or user_choice1.lower() == "quit":
        print("Thanks for playing!")
        done=True
    #quit

    else:
        print("Not sure you understand what you are doing?!")

while not endgame:
    final_choice = input("Who killed Mary Jane?(Answer with: Doc Oc, Venom, Green Goblin, Scorpion, Lizard, Mysterio, or Rhino): ")
    if sanity > 5:
        print("You have lost your mind to the violence.")
        endgame = True
    elif final_choice.lower() == "venom":
        print("Venom was friends with the killer, but he was not the killer.")
        endgame = True
    elif final_choice.lower() == "mysterio":
        print("Mysterio was friends with the killer, but he was not the killer.")
        endgame = True
    elif final_choice.lower() == "rhino":
        print("Rhino is too stupid to kill Mary Jane.")
        endgame = True
    elif final_choice.lower() == "green goblin":
        print("Green Goblin leaked your identity, but he did not kill Mary Jane.")
        endgame = True
    elif final_choice.lower() == "doc oc":
        print("Doc Oc invited everyone to the party, but the killer posioned Mary Jane,and that is not Doc Oc's style. He did not kill Mary Jane.")
        endgame = True
    elif final_choice.lower() == "scorpion":
        print("Scorpion was in fact the killer.")
        time.sleep(.25)
        print("You hear the library doors unlock.")
        time.sleep(.25)
        user_choice10 = input("Do you want to enter? (Y/N): ")
        if user_choice10.lower() == "y":
            endgame = True
            boss_fight = False
        else:
            endgame = True
    else:
        print("Enter one of the choices.")
scorpion_health = 1000
while not boss_fight:
    time.sleep(.25)
    print("You enter the library and see Scorpion waiting for you, tail dripping with venom.")
    time.sleep(.25)
    print("You: 'You took my world from me!'")
    time.sleep(.25)
    print("Scorpion: 'Oh I know, and it is glorious!'")
    time.sleep(.25)
    print("You: 'Mark my words, you will pay!'")
    time.sleep(.25)
    print("Scorpion: 'Soon you will also feel the fatal sting!'")
    break
while not boss_fight:
    if player_health > 0 and scorpion_health > 0:
        print("Player Health: ", player_health)
        print("Scorpion Health: ", scorpion_health)
        if scorpion_health <= 500:
            time.sleep(.25)
            screwed = random.randrange(1,2)
            if screwed == 1:
                print("Scorpion attacks you!")
                player_health -= 20
            user_choice11 = input("Do you attack? (Y/N): ")
            if user_choice11.lower() == "y":
                attack = random.randrange(50, 100)
                scorpion_health -= attack
                print("You did ", attack, "damage!")
            else:
                print("You did not attack!")
        else:
            time.sleep(.25)
            screwed = random.randrange(1,5)
            if screwed == 3:
                print("Scorpion attacks you!")
                player_health -= 10
            user_choice11 = input("Do you attack? (Y/N): ")
            if user_choice11.lower() == "y":
                attack = random.randrange(50,200)
                scorpion_health -= attack
                print("You did ", attack, "damage!")
            else:
                print("You did not attack!")
    elif scorpion_health <= 0 and player_health > 0:
        print("You win!!!!")
        boss_fight = True
    else:
        print("Scorpion killed you!")
        boss_fight = True






