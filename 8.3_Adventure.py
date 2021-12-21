'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game
'''
k=0
a=0
c=0
d=0
e=0
f=0
g=0
j=0
l=0
m=0
n=0
p=0
r=0
s=0
u=0
v=0
w=0
x=0
y=0
z=0


class bcolors:
    GUARDIANS = '\033[0;34m'
    JESSICA = '\033[0;31m'
    SIMON = '\033[1;35m'
    JOHN = '\033[1;36m'
    ARISIA = '\033[93m'
    GUY = '\033[1;37m'
    KYLE= '\033[0;33m'
    HAL='\033[0;30m'
    HIM2='\033[3m'
    HIM = '\033[2;31m'
b=0
print("You aren't exactly sure where you are, or how you got there.")
print("You have seven options. North, South, East, West, List of Items, Interact, and Quit.(n,s,e,w,l,i,q)")
print("Find you way around the ship and try to regain your memory. Something bad happened here.")
print("There's a hole in the side of the ship. You have thirty minutes before it collapses.")
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
print(bcolors.ARISIA + "WAKE UP GUY.")
print()
print()
print(bcolors.GUARDIANS + "THE MISSION WAS A FAILURE.")
print()
print()
print(bcolors.GUARDIANS + "WHERE ARE THE OTHER FIVE. WHERE IS CORPS LEADER STEWART.")
print()
print()
print("HAVE YOU SEEN 2814.5 AND 2814.6 ANYHWERE.")
print()
print()
print("WE CAN'T AFFORD TO LOSE THE TORCHBEARER. RAYNER IS TOO IMPORTANT.")
print()
print()
print(bcolors.ARISIA + "GUY. I NEED YOU TO ANSWER ME.")
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
print("WHERE IS HAL......")
print(bcolors.GUY + "    ")


current_room=0
done=False

room_list=[]
room=["You are in the control room of the ship.. There appears to be a panel loose on the wall."]
room_list.append(room)
room=["You are now in the central room of the ship. There is a ring on the floor, but you can't access it yet. "]
room_list.append(room)
room=["You are now in the navigation room. You could find something useful in hear."]
room_list.append(room)
room=["You have entered the crew's quarters of the ship. There is a box of stuff belonging to the crew."]
room_list.append(room)
room=["You have entered the armory of the ship. There are lots of weapons, but there is also a box of tools on the wall."]
room_list.append(room)
room=["You are now in the observation deck of the ship. What you see through the glass shocks you. You are in space."]
room_list.append(room)
room=["You have entered the medical bay of the ship. There's records on the table. One of them looks like you."]
room_list.append(room)
print()
print()
print()
print()
print()
item_list=[]
print(room_list[0])

while done==False:
    user_input=str(input("What would you like to do: n,s,e,w,i,e,q"))
    if user_input.lower()=="n" and current_room==0:
        current_room+=1
        if x==0:
            print()
            print()
            print(bcolors.GUARDIANS + "CAN WE TRUST YOU TO WORK WELL WITH YOUR FELLOW CORPS MEMEBERS GARDENER?")
            print()
            print()
            print(bcolors.GUY + "YEAH YEAH, KEEP YOUR WHITE WIG ON YOUR BLUE BOBBLEHEAD GANTHET")
            print()
            print()
            x+=1
        print()

    if user_input.lower()=="e" and current_room==1:
        current_room+=100
        print(room_list[5])
        if d==0:
            print()
            print()
            print("THOSE BLUE WEIRDOS ALWAYS GIVE YOU THE EXCITING STUFF JORDAN.")
            print()
            print()
            print(bcolors.HAL + "WE ALL GO ON THIS ONE GUY.")
            print()
            print()
            print(bcolors.GUY + "YEAH, BUT I HAVE TO BABYSIT THE NEWCOMERS WHILE YOU GET GUARD DUTY.")
            print()
            print()
            print(bcolors.HAL + "SIMON AND JESSICA ARE SHOWING MORE PROMISE AS NEW CORPS MEMBERS THAN YOU EVER DID.")
            print()
            print()
            print(bcolors.GUY + "NOBODY IS MORE PROMISING THAN A GARDNER, JORDAN.")
            print()
            print()
            print(room_list[5])
            print()
            d+=1
            l+=1
        print()
    if user_input.lower()=="w" and current_room==1:
        print(room_list[4])
        current_room-=30
        if c==0:
            print()
            print()
            print(bcolors.GUY + "JOHNNY BOY, HOW'S IT FEEL TO BE STUCK WITH ME ON BABBYSITTING DUTY")
            print()
            print()
            print(bcolors.JOHN + "I DO MY DUTY TO THE CORPS GUY. YOU SHOULD TOO.")
            print()
            print()
            print(bcolors.GUY + "I DO I DO. I JUST LIKE SOME ACTION TO KEEP ME ENTERTAINED.")
            print()
            print()
            print(bcolors.JOHN + "THE GUARDIANS PUT ME WITH YOU TO KEEP YOU IN LINE GUY. NOT SIMON AND JESSICA.")
            print()
            print()
            print(bcolors.GUY + "IF THERE'S ANYONE WHO NEEDS SUPERVISION, JOHN, IT'S JORDAN. REMEMBER COAST CITY?")
            print()
            print()
            print(bcolors.JOHN + "WATCH YOUR MOUTH GUY.")
            print(bcolors.GUY + "   ")
            print()
            print()
            print(room_list[4])
            c+=1
            l+=1
        print()
    if user_input.lower()=="e" and current_room==-29:
        print()
        print(room_list[1])
        current_room+=30
        l+=1
    if user_input.lower()=="w" and current_room==101:
        print()
        print(room_list[1])
        current_room-=100
        l+=1
    if user_input.lower()=="n" and current_room==101:
        print()
        print(room_list[3])
        current_room+=1
        l+=1
        if e==0:
            print()
            print()
            print("SO NEWBIES, EXCITED FOR YOUR FIRST MISSION?")
            print()
            print()
            print(bcolors.SIMON + "IT'S NOT OUR FIRST MISSION GUY.")
            print()
            print()
            print(bcolors.GUY + "YEAH SIMON, BUT IT'S YOUR FIRST MISSION WITH ME.")
            print()
            print()
            print(bcolors.JESSICA + "IS THAT SUPPOSED TO BE A WARNING.")
            print()
            print()
            print(bcolors.SIMON + "BE NICE JESSICA.")
            print()
            print()
            print(bcolors.GUY + "OH, YOU TWO HAVE NO IDEA WHAT YOU'RE IN FOR.")
            print()
            print()
            print(room_list[3])
            print()
            e+=1
        print()
    if user_input.lower()=="n" and current_room==-29:
        print()
        print(room_list[2])
        l+=1
        current_room+=1
        if j==0:
            print()
            print()
            print(bcolors.KYLE + "GUY, I WANT YOU TO TRY REALLY HARD TO BE GOOD TO SIMON AND JESSICA.")
            print()
            print()
            print(bcolors.GUY + "AWW, YOU KNOW ME KYLE. ALWAYS STAYING OUT OF TROUBLE.")
            print()
            print()
            print(bcolors.KYLE + "SURE. WHAT ABOUT THAT TIME WITH GNORT?")
            print()
            print()
            print(bcolors.GUY + "OKAY, I DIDN'T ASK FOR HIM.")
            print()
            print()
            print("PLUS, YOU HAVE A DIFFERENT PERSPECTIVE WHEN YOU NEVER DO ANYTHING WRONG. YOU'RE THE TORCHBEARER!")
            print()
            print()
            print(bcolors.KYLE + "NO, I JUST DON'T GO LOOKING FOR PROBLEMS.")
            print()
            print()
            print(bcolors.GUY + "HEY, I TRY, BUT PROBLEMS SEEM TO FIND ME ANYWAY.")
            print()
            j+=1
    if user_input.lower()=="s" and current_room==-28:
        print()
        print(room_list[4])
        current_room-=1
        l+=1
    if user_input.lower()=="s" and current_room==102:
        print()
        print(room_list[5])
        current_room-=1
        l+=1
    if user_input.lower()=="s" and current_room==0:
        print()
        print("You can't access this room yet.")
    if user_input.lower()=="s" and current_room==1:
        print()
        print(room_list[0])
        current_room-=1
        l+=1
    if user_input.lower()=="i" and current_room==1:
        print()
        print("You picked up the ring, but you still can't access it.")
        item=["Strange ring. There's a symbol carved onto it."]
        item_list.append(item)
        g+=1
        print()
        print()
        print("I TOLD YOU THERE WAS NO REASON TO ESCORT THIS SHIP.")
        print()
        print()
        print(bcolors.JOHN + "IF THE GUARDIANS WANT US ON THIS SHIP, THEN THAT'S WHERE WE'LL BE.")
        print()
        print()
        print(bcolors.JESSICA + "I REALLY DON'T THINK I NEED YOU TWO TO WATCH US. SIMON AND I ARE PERFECTLY CAPABLE OF HANDLING OURSELVES.")
        print()
        print()
        print(bcolors.GUY + "SHE'S RIGHT JOHN. THIS IS BORING WITH A PLANET SIZED B.")
        print()
        print()
        print(bcolors.JOHN + "I'M NOT GOING OVER THIS AGAIN. WE'RE STAYING RIGHT WHERE WE ARE.")
        print()
        print()
        print(bcolors.SIMON + "I BET HAL AND KYLE ARE HAVING A GREAT TIME FLOATING ON GUARD DUTY. THEY MIGHT ACTUALLY BE MORE BORED THAN US.")
        print()
        print()
        print(bcolors.GUY + "NAH. KYLE'S DRAWING AND HAL FOUND AN ALIEN GIRL.")
        print()
        print()
    if user_input.lower()=="i" and current_room==101:
        print()
        print("There's a key-card on the floor. It looks like it belonged to the ships maintenance.")
        print("You pick the key-card up.")
        item=["Key-card. Could be used to open something."]
        item_list.append(item)
        b+=1
        print()
        print()
        print(bcolors.GUY + "WE'VE LOST THE NEWBIES.")
        print()
        print()
        print(bcolors.JOHN + "WE'LL FIND THEM LATER. OUR FIRST PRIORITY IS PROTECTING THE KORUGIAN LEADERS.")
        print()
        print()
        print(bcolors.GUY + "BUT....")
        print()
        print()
        print(bcolors.JOHN + "GUY, WE CAN'T WASTE ANY TIME RIGHT NOW.")
        print()
        print()
        print(bcolors.GUY + "HOW DID THEY FIND US?")
        print()
        print()
    if user_input.lower()=="i" and current_room==-29:
        if b==0:
            print("The box of tools is locked. It's sealed electronically.")
        if b==1:
            print("You opened the box of tools. The only thing of value in it was a crowbar.")
            item=["A crowbar. Not to be used on robins."]
            item_list.append(item)
            k+=1
            print()
            print()
            print(bcolors.KYLE + "THEY JUST KEEP COMING. WE CAN'T MAKE A DENT IN THEIR RANKS.")
            print()
            print()
            print(bcolors.HAL + "I DON'T THINK OUR FIGHT'S GOING TO LAST MUCH LONGER.")
            print()
            print()
            print(bcolors.KYLE + "IT'S HIM. YOU GOING TO BE OKAY?")
            print()
            print()
            print(bcolors.HIM + bcolors.HIM2 + "I REQUIRE BOTH OF YOU.")
            print(bcolors.JOHN + "   ")
            print()
            print(bcolors.HAL + "WE'RE NOT WINNING HERE. WE'RE GOING WITH HIM.")
            print()
            print()
            print(bcolors.KYLE + "YOU REALLY THINK IT'S A GOOD IDEA?")
            print()
            print()
            print(bcolors.HIM + bcolors.HIM2 + "KNOW THAT YOU LEAVE THE OTHERS TO DIE.")
            print()
            print(bcolors.JOHN + "    ")
            print(bcolors.HAL + "I CAN GURANTEE THEY WON'T")
            print(bcolors.GUY + "   ")
            print()
    if user_input.lower()=="i" and current_room==102:
        if k==0:
            print()
            print("The box is sealed shut. It will only open by force.")
        if k==1:
            print()
            print("You opened the box with the crowbar. You take the ship's naivgators id card.")
            n+=1
            print()
            print()
            print(bcolors.SIMON + "I CAN'T SEE." )
            print()
            print()
            print(bcolors.JESSICA + "SIMON?")
            print()
            print()
            print(bcolors.JESSICA + "WHERE ARE WE?")
            print()
            print()
            print(bcolors.SIMON + "RING. IDENTIFY LOCATION.")
            print()
            print()
            print(bcolors.SIMON + "OUT OF POWER. YOURS?")
            print()
            print()
            print(bcolors.JESSICA + "NOT RESPONDING. CAN YOU SEE ANYTHING?")
            print()
            print()
            print(bcolors.SIMON + "LOTS OF OVERGROWN JUNGLE.")
            print()
            print()
            print(bcolors.JESSICA + "BASED ON THE STARS, I WOULD SAY WE'RE IN THE VEGA SYSTEM.")
            print()
            print()
            print(bcolors.SIMON + "OVERGROWN JUNGLE, VEGA SYSTEM. NOT GOOD.")
            print(bcolors.GUY + "    ")
            item=["An ID card from the ships captain. Gives you higher security clearance."]
            item_list.append(item)
    if user_input.lower()=="i" and current_room==-28:
        if n==0:
            print()
            print("You need proper clearance to access the navigation systems and ship logs.")
        if n==1:
            print()
            print()
            print()
            print(bcolors.JOHN + "GUY? GUY?")
            print()
            print()
            print("I MUST HAVE BEEN THROWN INTO SPACE BY THE MANHUNTERS.")
            print()
            print()
            print("RING. IDENTIFY LOCATION.")
            print()
            print()
            print("SECTOR 1313. FIGURES.")
            print()
            print()
            print("EVERYTIME SOMETHING HAPPENS I ALWAYS END UP RIGHT BACK HERE.")
            print()
            print()
            print("WAIT A MINUTE, THERE'S NOT SUPPOSED TO BE ANY SETTLEMENTS HERE. THIS PLANETS DEVOID OF LIFE.")
            print()
            print()
            print("COME IN GURADIANS. DO YOU READ ME?")
            print()
            print()
            print("NO ANSWER.")
            print()
            print()
            print()
            print()
            print(bcolors.GUY + "   ")
            print()
            print("The ships navigation systens are pretty much broken, but you did learn one thing. 195922. Must be a code.")
            print("You write it down on a piece of paper.")
            item=["A piece of paper with a code. 195922."]
            item_list.append(item)
    if user_input.lower()=="l":
        print()
        print(item_list)
        print()
    if user_input.lower()=="i" and current_room==0:
        code_input=float(input("What is the code for this room?"))
        if code_input==195922:
            print()
            print(room_list[6])
            current_room-=1000
    if user_input.lower()=="i" and current_room==-1000:
        print("Name:GUY GARDNER")
        print("Height: 6 feet")
        print(" Weight: 184 lbs")
        print("Age: 38 Earth years")
        print("Raised in Baltimore by Peggy and Roland.")
        print("Alcoholic father who was prone to violent outbursts")
        print("Younger brother to Mace Gardener.")
        print("Grew up a delinquent before his brother inspired him to go to college and play football.")
        print("Suffered a career ending injury.")
        print("Then worked in rehabilitation of inmates before becoming a teacher for kids with disabilites.")
        print("Tends to be distant and sarcastic.")
        print("Was a second choice. Is not happy about it.")
        print()
        print()
        print("The ring starts glowing in your pocket. Head back to the central room to activate it.")
        v+=1
    if user_input.lower()=="n" and current_room==-1000:
        print()
        print(room_list[0])
        current_room+=1000
        print()
        l+=1
    if current_room==1 and v==1:
        print("You take out the ring and put it on your finger.")
        print()
        print()
        print(bcolors.GUY + "JOHN, I HAVE AN IDEA.")
        print()
        print()
        print(bcolors.JOHN + "WE'VE LOST THE KORUGIANS. I'M WILLING TO TRY ANYTHING.")
        print()
        print()
        print(bcolors.GUY + "IT GOES I PUSH YOU OUT OF THE SHIP AND I BLOW THE FUEL TANK.")
        print()
        print()
        print(bcolors.JOHN + "I DON'T HAVE A SAY IN THIS DO I?")
        print()
        print()
        print(bcolors.GUY + "BYE JOHN")
        print()
        print()
        print("The explosion must have given you some sort of amnesisa.")
        print("You fly out of the ship, going to find the others.")
        done=True
    if user_input.lower()=="q":
        print("You never found your way out of the ship.")
        break
    if l==30:
        print("The ship has collapsed and you have died. The corps just lost a valuable member.")
        break









