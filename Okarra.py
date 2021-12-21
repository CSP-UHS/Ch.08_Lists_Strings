import random
import arcade
class bcolors:
    MANHUNTERS = '\033[0;34m'
    JESSICA = '\033[0;31m'
    SIMON = '\033[1;35m'
    JOHN = '\033[1;36m'
    LARFLEEZE = '\033[93m'
    GUY = '\033[1;37m'
    KYLE= '\033[0;33m'
    HAL='\033[0;30m'
    HIM2='\033[3m'
    HIM = '\033[2;31m'
SW=245
SH=245
a=0
b=2
c=-2
d=-2
e=-1
f=0
g=0
h=0
i=0
k=0
l=0
m=0
n=0
red=0
orange=0
yellow=0
green=0
blue=0
purple=0
darkstar=0
jessica_health=2
simon_health=2
print("The sky's rise over the planet Okkara. Our heroes are trapped with little power in their rings.")
print()
print()
print(bcolors.SIMON + "I'm suprised hasn't come to find us. ")
print()
print(bcolors.LARFLEEZE + "What are you doing?!. This planet is mine! MINE MINE MINE!")
print()
print(bcolors.JESSICA + "We were attacked by the manhunters. We're stranded here and our rings are damaged")
print()
print(bcolors.LARFLEEZE + "Hmmm. Well, is suppose that's not your fault. But I won't help you!. My ring's power is all mine!")
print()
print(bcolors.SIMON + "But that's..... sounds good Larfleeze.")
print()
print(bcolors.LARFLEEZE + "Now get out of my sight! Don't try taking anything either. It's mine!")
print()
print()
print()
print(bcolors.GUY + "  ")
print("Suddenly, a creature jumps out at you from behind the bush. There are a few rocks to take cover behind.")
print("This game takes a strategy approach. Move each character left, right, back, or forward. You can also attack or use an item.")
print("Type the lowercase letter of the start of each action. Type s or j to switch characters. Type m for a map. You will always start as Jessica.")
print("When next to a rock, press j to climb on top of it and press a to attack a creature if it is next to the rock.")
done=False
while done==False:
    action_input=str(input("What action would you like to take?"))
    if action_input.lower()=="s" and a==0:
        print()
        print("You have switched to Simon")
        a += 1
    if action_input.lower()=="s" and a==1:
        print()
        print("You are already playing as Simon.")
    if action_input.lower()=="j" and a==0:
        print()
        print("You are already playing as Jessica.")
    if action_input.lower()=="j" and a==1:
        print()
        a-=1
        print("You have switched to Jessica")
    if action_input.lower()=="l" and a==0:
        print()
        d-=1
        print("Jessica has moved to the left")
    if action_input.lower()=="r" and a==0:
        print()
        d+=1
        print("Jessica has moved to the right")
    if action_input.lower()=="f" and a==0:
        print()
        e+=1
        print("Jessica has moved forward")
    if action_input.lower()=="b" and a==0:
        print()
        e-=1
        print("Jessica has moved backward")
    if action_input.lower()=="l" and a==1:
        print()
        b-=1
        print("Simon ahs moved to the left")
    if action_input.lower()=="r" and a==1:
        print()
        b+=1
        print("Simon has moved to the right")
    if action_input.lower()=="f" and a==1:
        print()
        c+=1
        print("Simon has moved forward")
    if action_input.lower()=="b" and a==1:
        print()
        c-=1
        print("Simon has moved backwards.")
    if action_input.lower()=="b" and a==1 and c==-3:
        print()
        print("Simon can't move any farther backwards")
    if action_input.lower()=="f" and a==1 and c==3:
        print()
        print("Simon can't move any farther forwards")
    if action_input.lower()=="r" and a==1 and b==3:
        print()
        print("Simon can't move any farther to the right")
    if action_input.lower()=="l" and a==1 and b==-3:
        print()
        print("Simon can't move any farther to the left")
    if action_input.lower()=="b" and a==0 and e==-3:
        print()
        print("Jessica can't move any farther backwards")
    if action_input.lower()=="f" and a==0 and e==3:
        print()
        print("Jessica can't move any farther forward.")
    if action_input.lower()=="r" and a==0 and d==3:
        print()
        print("Jessica can't move any farther to the right")
    if action_input.lower()=="l" and a==0 and d==-3:
        print()
        print("Simon can't move any farther to the left")
    if b==2 and c==0:
        print()
        print("The creature attacks!")
        simon_health-=1
    if b==3 and c==-1:
        print()
        print("The creature attacks!")
        simon_health-=1
    if b==1 and c==1:
        print()
        print("The creature attacks!")
        simon_health-=1
    if c>=-1 and b==0:
        print()
        print("The creature attacks!")
        simon_health-=1
    if c==2 and b>=1:
        print()
        print("The creature attacks!")
        simon_health-=1
    if c==1 and b==-1:
        print()
        print("The creature attacks!")
        simon_health-=1
    if d==2 and e==0:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if d==3 and e==-1:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if d==1 and e==1:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if e>=-1 and d==0:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if e==2 and d>=1:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if e==1 and d==-1:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if c==3 and b==-1:
        print()
        print("The creature attacks!")
        simon_health-=1
    if c==3 and b==1:
        print()
        print("The creature attacks!")
        simon_health-=1
    if e==3 and d==-1:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if e==3 and d==1:
        print()
        print("The creature attacks!")
        jessica_health-=1
    if simon_health==0:
        print()
        print("Simon has died. You have failed.")
        break
    if jessica_health==0:
        print()
        print("Jessica has died. You have failed.")
        break
    if b==3 and c==1:
        print()
        print("You are on a rock and the creature can't see you.")
    if b==0 and c==-2:
        print()
        print("You are on a rock and the creature can't see you")
    if b==-2 and c==0:
        print()
        print("You are on a rock and the creature can't see you")
    if b==-1 and c==2:
        print()
        print("You are on a rock and the creature can't see you")
    if d==3 and e==1:
        print()
        print("You are on a rock and the creature can't see you")
    if d==0 and e==-2:
        print()
        print("You are on a rock and the creature can't see you")
    if d==-2 and e==0:
        print()
        print("You are on a rock and the creature can't see you")
    if d==-1 and e==2:
        print()
        print("You are on a rock and the creature can't see you")
    if action_input.lower()=="a" and b==-1 and c==2:
        print()
        print("Simon attacked the creature. It died in one hit.")
        done=True
    if action_input.lower()=="a" and d==-1 and e==2:
        print()
        print("Jessica attacked the creature. It died in one hit.")
        done=True
if done==True:
    print()
    print(bcolors.JESSICA + "This would be a lot easier if we had our rings")
    print()
    print(bcolors.SIMON + "Speaking of rings, where did Larfleeze go?")
    print()
    print(bcolors.LARFLEEZE + "I havn't left idiots!")
    print()
    print(bcolors.JESSICA + "Ah there you are. Is there any way you could help us get off Okkara?")
    print()
    print(bcolors.LARFLEEZE + "Only if you have something I want.")
    print()
    print(bcolors.SIMON + "How about a yacht?")
    print()
    print(bcolors.LARFLEEZE + "What's a yacht? I want it!")
    print()
    print(bcolors.JESSICA + "Or, how about some manhunters for your collection?")
    print()
    print(bcolors.LARFLEEZE + "Only if i get a yacht as intrest.")
    print()
    print(bcolors.SIMON + "Alright then lets go.")
    print()
    print(bcolors.LARFLEEZE + "Actually a couple of my constructs have gotten loose. I want him back. He's mine!")
    print()
    print(bcolors.SIMON + "Then why don't you just go get them back?")
    print()
    print(bcolors.LARFLEEZE + "Simple. Because I don't want to.")
    print()
    print(bcolors.JESSICA + "You're useless.")
    print()
    print(bcolors.LARFLEEZE + "Well go get them!")
    construct=False
    print()
    print(bcolors.GUY + "Simon and Jessica delve into the caves of Okkara, looking for Larfleeze's rebellious constructs.")
    print()
    print("As they enter the largest tunnel on the planet, they find technology belonging to the controllers during their brief stay on Okkara.")
    print()
    print(bcolors.SIMON + "We could use this you know.")
    print()
    print(bcolors.JESSICA + "There's nothing here that could be used as a weapon or a means of escape.")
    print()
    print(bcolors.SIMON + "I don't know about that. Looks like some Darkstar equipment.")
    print()
    print(bcolors.JESSICA + "We still need a way to power it.")
    print()
    print(bcolors.SIMON  + "There's a Darkstar battery over there, but it looks old. Really old.")
    print()
    print(bcolors.JESSICA + "You realize that if we make on wrong move the whole thing blows.")
    print()
    print(bcolors.SIMON + "Never stopped us before.")
    print()
    print()
    print(bcolors.HAL + "   ")
    while construct==False:
        print("There are multiple buttons on the battery. There is also a name. Donna Troy.")
        print("Type 1,2,3,4, or 5 to press the buttons, or type 6 for a description of the buttons.")
        power_input = int(input("How would you like to activate the power battery?"))
        if power_input==6:
            print("The first button has images of an arrow, waves, lightning, and a bird.")
            print("The second button has an image of a face that is half old and half young")
            print("The third button's image has the Darkstar logo on it")
            print("The fourth button has the face of corps member Rayner on it.")
            print("The fifth button has an image of a question mark and a clock.")
        if power_input==2:
            if orange==0:
                print()
                print("You have correctly selected the first button in sequence")
                orange+=1
            if orange==1:
                print("This button has already been selected.")
        if power_input==1:
            if orange==1:
                print()
                print("You have correctly selected the second button in sequence")
                yellow+=1
            if orange==0:
                print()
                print("You have selected the wrong button and have died.")
                print("The corps just lost two valuable members.")
                break
            if yellow==1:
                print()
                print("This button has already been selected")
        if power_input==4:
            if yellow==1:
                print()
                print("You have correctly selected the third button in sequence.")
                green+=1
            if yellow==0:
                print()
                print("You have selected the wrong button and have died.")
                print("The corps just lost two valuable members.")
                break
            if green==1:
                print()
                print("This button has already been selected.")
        if power_input==3:
            if green==1:
                print()
                print("You have correctly selected the fourth button in sequence.")
                blue+=1
            if green==0:
                print()
                print("You have selected the wrong button and have died.")
                print("The corps just lost two valuable members.")
                break
            if blue==1:
                print()
                print("This button has already been selected.")
        if power_input==5:
            if blue==1:
                print()
                print("You have correctly selected the final button in sequence.")
                darkstar+=1
                construct=True
            if blue==0:
                print()
                print("You have selected the wrong button and have died.")
                print("The corps just lost two valuable members.")
                break
    if construct==True:
        print("The Darkstar battery powered up!")
        print()
        print(bcolors.JESSICA + "Alright, let's get these suits on.")
        print()
        print(bcolors.SIMON + "We're going to have to be careful of Larfleeze though.")
        print()
        print("This stuff is on his planet and we didn't actually find his constructs.")
        print()
        print(bcolors.JESSICA + "Good point. Lets leave through these caves. The opposite way we came out.")
        print()
        print(bcolors.GUY + "The two have almost made it out of the planets atmosphere when they are stopped by Larfleeze.")
        print()
        print(bcolors.LARFLEEZE + "What are you doing?! I told you not to touch anything! It's all mine!!!")
        print()
        print(bcolors.SIMON + "Sorry Larfleeze, but we're needed somewhere else.")
        print()
        print(bcolors.LARFLEEZE + "I dont care! Give me those suits now!")
        print()
        print(bcolors.GUY + "Larfleeze attacks!")
        fight=False
        larfleeze_health = 400
        lantern_health = 100
        while fight==False:
            fight_input=str(input("Will you attack Larfleeze? (y/n)"))
            if fight_input.lower()=="y":
                print()
                larfleeze_damage = random.randint(12, 30)
                lantern_damage = random.randint(50, 75)
                larfleeze_health-=lantern_damage
                lantern_health-=larfleeze_damage
                print("Larfleeze's health is at", larfleeze_health)
                print("Simon and Jessica's health is at", lantern_health)

                print()
                print()
                larfleeze_anger = random.randint(25, 35)
                lantern_regain = random.randint(5, 10)
                larfleeze_chance = random.randint(1, 10)
                if larfleeze_chance >= 5:
                    larfleeze_health -= larfleeze_anger
                    print("In his anger, Larfleeze slams into an asteriod")
                lantern_chance = random.randint(1, 10)
                if lantern_chance >= 5:
                    lantern_health += lantern_regain
                    print("Simon and Jessica gained some health")
                print("Larfleeze's health is at", larfleeze_health)
                print()
                print("Simon and Jessica's health is at", lantern_health)
            if lantern_health <= 0:
                print()
                print("Simon and Jessica have died.")
                break
            if larfleeze_health <= 0:
                print()
                print("Simon and Jessica have defeated Larfleeze.")
                fight = True
            if fight_input.lower()=="n":
                print()
                print("Simon and Jessica avoided fighting Larfleeze")
                print()

    if fight==True:
        print()
        print(bcolors.SIMON + "We're leaving now Larfleeze.")
        print()
        print(bcolors.LARFLEEZE + "No! NO! Give them back! MINE! MINE MINE MINE!")
        print()
        print(bcolors.JESSICA + "Simon come on.")
        print()
        print(bcolors.SIMON + "We have no idea where they are.")
        print()
        print(bcolors.JESSICA + "If this is actually Donna's battery then it might know where Kyle is. ")
        print()
        print("I just hope their okay.")
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print(bcolors.HIM + bcolors.HIM2 + "Manhunters, are the lanterns almost ready?")
        print()
        print(bcolors.MANHUNTERS + "A few more hours master.")
        print()
        print(bcolors.HIM+ bcolors.HIM2 + "Good. Things are going as planned then.")







