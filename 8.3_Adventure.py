'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random

done = False
currRoomNum = 0
movesMade = 0
maxHealth = 100
health = 100
damage = 14
money = 0
roomsUninfected = 0

stage = 0

roomLetters = ["A","B","C","D","E","F","G","H"]

mapStr = ("      ┌─────┐\n"
           "      │  G  │\n"
           "      ├─────┼─────┬─────┐\n"
           "      │  D  │  E  │  F  │\n"
           "┌─────┼─────┼─────┼─────┘\n"
           "│  A  │  B  │  C  │\n"
           "└─────┼─────┼─────┘\n"
           "      │  H  │\n"
           "      └─────┘\n")

zombieStr = ("🧟")

class room:
    def __init__(self, rn, rd, ri, n, e, s, w, inf, tres):
        self.room_number = rn
        self.room_desc = rd
        self.room_info = ri
        self.n_room = n
        self.e_room = e
        self.s_room = s
        self.w_room = w
        self.infected = inf
        self.treasure = tres


'''
ROOM MAP:

   [6]
   [3][4][5]
[0][1][2]
   [7]

'''

room_list = [
    room(0,"Bedroom","You woke up here to banging on your doors. Maybe see what's going on?",None,1,None,None,False,False),
    room(1,"Downstairs","The walls are all scratched. Something has been here.",3,2,7,0,1,False),
    room(2,"Living Room","The couch is completely ruined and your TV is shattered.",4,None,None,1,3,False),
    room(3,"Kitchen","Something smells burnt. The zombies turned the stove on.",6,4,1,None,3,False),
    room(4,"Dinner Table","Blood is all over the dinner table. Disgusting.",None,5,2,3,2,False),
    room(5,"Deck","You look out from your deck and see even more zombies. This can't be good.",None,None,None,4,4,False),
    room(6,"Backyard","The grass is dead. The sky above is completely dark. At least a very convenient treasure chest is there.",None,None,3,None,False,True),
    room(7,"Driveway","Your driveway is massacred. Your car is completely smashed in. But you don't have time to call insurance.",1,None,None,None,3,False)
]

def get_room_obj(n):
    for r in room_list:
        if r.room_number == n:
            return r

def movable_dir_list():
    currRoomObj = get_room_obj(currRoomNum)

    if currRoomObj.n_room is not None:
        print("\033[93m*\033[0m North (n)")
    if currRoomObj.e_room is not None:
        print("\033[93m*\033[0m East (e)")
    if currRoomObj.s_room is not None:
        print("\033[93m*\033[0m South (s)")
    if currRoomObj.w_room is not None:
        print("\033[93m*\033[0m West (w)")

def move_in_dir(d):
    dir = d.lower().strip()
    currRoomObj = get_room_obj(currRoomNum)

    if (dir == "n" or dir == "north") and (currRoomObj.n_room is not None):
        return currRoomObj.n_room
    elif (dir == "e" or dir == "east") and (currRoomObj.e_room is not None):
        return currRoomObj.e_room
    elif (dir == "s" or dir == "south") and (currRoomObj.s_room is not None):
        return currRoomObj.s_room
    elif (dir == "w" or dir == "west") and (currRoomObj.w_room is not None):
        return currRoomObj.w_room
    else:
        return None


def treasure_room():
    get_room_obj(random.randint(0,7)).treasure = True

def battle_sequence():
    global health, maxHealth, roomsUninfected
    print("\n"*15)
    print("You stepped into an infected room!\n")
    infectedNum = get_room_obj(currRoomNum).infected
    zombieMaxHealth = infectedNum^2 + infectedNum * 6 + 20  # x^2 + 6x + 20
    zombieCurrHealth = zombieMaxHealth
    while True:
        print("\033[91mLvl. {}\033[0m Zombie 🧟 ({} / {} HP)".format(infectedNum, zombieCurrHealth, zombieMaxHealth))
        print("YOU ☺ ({} / {} HP)\n".format(health, maxHealth))
        print("\033[93m1.\033[0m Attack")
        print("\033[93m2.\033[0m Surrender")
        userInput = input("> ").strip().lower()
        print("\n"*15)
        if userInput == "1" or userInput == "attack":

            dmg = random.randint(int(damage*0.8),int(damage*1.2))
            zombieCurrHealth -= dmg
            if zombieCurrHealth <= 0:
                roomsUninfected += 1
                print("\033[36mZombie defeated! The room is now uninfected!\033[0m")
                print("\033[36mTotal rooms uninfected: {}\033[0m\n".format(roomsUninfected))
                get_room_obj(currRoomNum).infected = 0
                break
            else:
                print("\033[36mYou dealt -{} dmg!\033[0m".format(dmg))

            zombieDmg = int((infectedNum^2 + infectedNum*2 + 2) * (random.randint(8,12) / 10))  # x^2 + 2x + 2
            health = health - zombieDmg
            print("\033[91mYou took -{} dmg!\033[0m\n".format(zombieDmg))
            if health <= 0:
                print("\033[91mYou've died lol! Try better next time loser!!\033[0m")
                exit()
                break

def found_treasure():
    global damage, money, health, maxHealth
    moneyFound = int(random.randint(10, 20) * (stage + 1))
    money += moneyFound
    damage *= 1.2
    maxHealth = int(maxHealth * 1.2)
    health = maxHealth
    print("\033[93mYou found a treasure chest!\033[0m")
    print("\033[93mItems recovered:\033[0m")
    print("\033[93m- Health Replenished\033[0m")
    print("\033[93m- x1.2 Max Health Bonus\033[0m")
    print("\033[93m- x1.2 Damage Boost\033[0m")
    print("\033[93m- +${}\033[0m\n".format(moneyFound))
    get_room_obj(currRoomNum).treasure = False



def print_map():
    printStr = mapStr

    printStr = printStr.replace(roomLetters[currRoomNum], "\033[92m☺\033[0m")

    for r in room_list:
        if r.infected:
            printStr = printStr.replace(roomLetters[r.room_number], "\033[91m" + roomLetters[r.room_number] + "\033[0m")
        if r.treasure:
            printStr = printStr.replace(roomLetters[r.room_number], "\033[93m" + roomLetters[r.room_number] + "\033[0m")


    print(printStr)


print("Welcome to the adventure game!")
print("In your bedroom one saturday morning, you hear banging on your door")
print("Zombies have infested your home and now you have to eradicate them")
print("Each room in your house is infected with a zombie with varying levels of strength")
print("When you defeat a zombie in a room, that room becomes uninfected")
print("The goal is to uninfect all rooms")
print("You won't need a paper map, the map is included in the gameplay")
print("-"*25)
print("White Rooms are perfectly safe.")
print("\033[91mRed Rooms\033[0m are infected with zombies.")
print("\033[93mYellow Rooms\033[0m have a special surprise")
print("-"*25)
input("Press any key to begin\n >")
print("\n"*20)

while True:
    currRoomObj = get_room_obj(currRoomNum)

    #if movesMade % 4 == 2:
        #infect_room()

    if currRoomObj.infected:
        battle_sequence()

    if currRoomObj.treasure:
        found_treasure()

    print("Current room: \033[92m{}\033[0m [{}]".format(currRoomObj.room_desc,roomLetters[currRoomNum]))
    print("Room Description: {}".format(get_room_obj(currRoomNum).room_info))
    print("\033[92m☺\033[0m - YOU ARE HERE:\n")

    print_map()

    if roomsUninfected >= 6:
        print("\nAll 6 rooms have been uninfected! You win!")

    print("Select a direction to move:")
    movable_dir_list()
    userDir = input("> ")
    print("\n"*15)

    if move_in_dir(userDir) is not None:
        currRoomNum = move_in_dir(userDir)
        movesMade += 1
    else:
        print("\033[91m// You can't move in that direction! //\033[0m")