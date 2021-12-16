import random
import arcade
class bcolors:
    GUARDIANS = '\033[0;34m'
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
    print(bcolors.GUY + "Simon and Jessica eventually find Glo")




