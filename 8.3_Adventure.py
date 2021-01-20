'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import random
import time

# Creates each room
room_list = []
# Room parameters - ["Description", N, S, E, W]
# 0
room = ["grungy stairwell", 3, None, None, None]
room_list.append(room)
# 1
room = ["washroom", 4, None, None, None]
room_list.append(room)
# 2
room = ["torture hall", 7, None, None, None]
room_list.append(room)
# 3
room = ["main corridor", 9, 0, 4, 7]
room_list.append(room)
# 4
room = ["east corridor", 8, 1, 5, 3]
room_list.append(room)
# 5
room = ["storage closet", None, None, None, 4]
room_list.append(room)
# 6
room = ["keepers quarters", 12, 11, 7, None]
room_list.append(room)
# 7
room = ["west corridor", None, 2, 3, 6]
room_list.append(room)
# 8
room = ["desolate kitchen", None, 4, None, None]
room_list.append(room)
# 9
room = ["prisoners quarters", None, 3, 10, None]
room_list.append(room)
# 10
room = ["secret passage to closet", None, 5, None, None]
room_list.append(room)
# 11
room = ["secret passage to stairwell", None, None, 0, None]
room_list.append(room)
# 12
room = ["keepers hall", None, 6, 13, None]
room_list.append(room)
# 13
room = ["private washroom", None, 6, None, 12]
room_list.append(room)


# Class for creation of items
class Item:

    def __init__(self, item_type, name, description="", damage=0, tier=0, uses=-1, effect="None"):
        self.item_type = item_type
        self.name = name
        self.description = description
        self.damage = damage
        self.tier = tier
        self.uses = uses

    def properties(self, damage, tier, uses):
        self.damage = damage
        self.tier = tier
        self.uses = uses



class Loot:

    def __init__(self, rooml):
        self.room = rooml
        self.loot = []
        self.item = []
        self.one = None

    def add(self, item):
        if type(item) == list:
            self.item = item
            for x in self.item:
                self.one = self.item[self.item.index(x)]
                self.loot.append(self.one)
        else:
            self.loot.append(item)
        rooms_loot.append(self.loot)
        room_list[self.room].append(self.loot)

    def list(self):
        for z in self.loot:
            print(z.name)


# sets variables equal to string values of weapon types for easier access
weapon = "weapon"
consumable = "consumable"
junk = "junk"
material = "material"
any_item = "any"

# Creation of Junk
hairbrush = Item(junk, "Plastic Hairbrush", "It's Sticky. You run it through your hair")
screwdriver = Item(junk, 'Broken Screwdriver', "Now what are you gonna do with a broken screwdriver, huh?")
battery = Item(junk, 'AAA battery', "Too bad you don't have a flashlight...")
bandage = Item(junk, 'Used Bandage', 'It may be used, but you can still use it again!')
eyepatch = Item(junk, 'Bloody Eyepatch', "I wonder how the blood got there...")
femur = Item(junk, "Cracked Femur", "Finders keepers!")
plank = Item(junk, "Rotted Wooden Plank", "Hit yourself over the head with it! Maybe this is all just a dream...")
pen = Item(junk, "Ballpoint Pen", "Better start writing your obituary.")
letteropen = Item(junk, "Wooden Letter Opener", "You know the mail doesnt get delivered to dungeons right?")
rubberband = Item(junk, "Rubber Band", "Strike down your enemies!")
hair = Item(junk, "Ball of Hair", "Did you cough that up? Gross.")
mirror = Item(junk, "Broken Mirror", "It may be broken, but you can still see how ugly you are!")
gameboy = Item(junk, "Gameboy Advanced", "You'll need a way to stay entertained down here!")
soap = Item(junk, "Used Bar Of Soap", "Should you eat it...? No.")
# add junk to list
junks = [hair, hairbrush, screwdriver, battery, bandage, eyepatch, femur, plank, pen, letteropen, rubberband, hair,
         mirror, gameboy]

# Creation of Weapons
swiss = Item(weapon, "Swiss Army Knife", "Maybe you can use it to cut swiss cheese?", 3, 1, 5)
switchblade = Item(weapon, "Rusty Switchblade", "Better hope you have your tetanus vaccine...", 2, 0, 3)
chefknife = Item(weapon, "Dull Chef's Knife", "Maybe you should prepare a meal before you become one.", 3.5)
machette = Item(weapon, "16 inch Machete", "Too bad you arent trapped in a jungle!", 5, 2, 8)
pencil = Item(weapon, "#2 Pencil", "Sharper than your wits!", 1, 0, 1)
fork = Item(weapon, "Bent Fork", "Try and bend it back, then you'll just have a fork", 1, 0)
nail = Item(weapon, "6 inch Iron Nail", "Quick! Drive it through your skull and end the harsh reality that is your life!")
woodenstake = Item(weapon, "Wooden Stake", "You can protect yourself from vampires!")
# add weapons to list
weapons = [swiss, switchblade, chefknife, machette, pencil, fork, nail, woodenstake]

# Materials
nails = Item(material, "Box of Nails", "Maybe you can build something...")
matches = Item(material, "Soggy Box of Matches", "Better hope they still work...")
stones = Item(material, "Pile of Stones", "This could be used for something!")
gauze = Item(material, "Fresh Gauze", "I have a feeling you'll be needing this...")
rope = Item(material, "Knotted Rope", "Undo the knots and you can make a noose!")
hammer = Item(material, "Small Hammer", "Are you strong enough to lift that?")
# add materials to list
materials = [nails, matches, stones]

# Consumables
cheese = Item(consumable, "Swiss Cheese", "It's got holes in it!")
flesh = Item(consumable, "Rotten Flesh", "Wait, this isn't minecraft!")
apple = Item(consumable, "Bruised Apple", "Watch your back, before you get bruised too...")
mouse = Item(consumable, "Mutilated Mouse", "Not very appetizing... yet.")
bread = Item(consumable, "Stale loaf of Bread", "This could do some damage... Or you could eat it")
medicine = Item(consumable, "Mysterious Bottle Of Medicine", "At least you have a painless way out...")
# add consumables to list
consumables = [cheese, flesh, apple, mouse, bread, medicine]
item_types = ["consumable", "material", "junk", "weapon"]
# add all items to loot pool
loot_pool = [consumables, materials, junks, weapons]
rooms_loot = []


# loot generation
def gen_loot(count, tier, itemtype):
    nums = [0, 1, 2, 3]
    # if item generation is set to any, run random generation
    if itemtype == "any":
        # different odds for each tier of loot, 0 is the worst, 3 is the highest
        # mostly junk, some consumables and materials, no weapons
        if tier == 0:
            index = random.choices(nums, weights=[2, 2, 6, 0], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
        # even amount of consumables, materials, and weapons, but mostly junk
        elif tier == 1:
            index = random.choices(nums, weights=[2, 2, 5, 2], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
        # even amount of all items
        elif tier == 2:
            index = random.choices(nums, weights=[3, 3, 3, 3], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
        # almost no junk, mostly weapons and materials, some consumables
        elif tier == 3:
            index = random.choices(nums, weights=[3, 4, 1, 5], k=count)
            room_loot = random.choices(loot_pool[index[0]], k=count)
    # if loot type is specified, pick random items from that item's loot pool
    elif itemtype in item_types:
        room_loot = random.choices(loot_pool[item_types.index(itemtype)], k=count)
    else:
        print("No items generated")
    # add loot data to the room
    rooms_loot.append(room_loot)

    return room_loot


# probability simulation for loot generation
def probsim(tier, runs, ipr=1):
    junkcount = 0
    weaponcount = 0
    materialcount = 0
    consumablecount = 0

    for x in range(0, runs):
        loot = gen_loot(ipr, tier, any_item)
        for i in range(0, len(loot)):
            if loot[i].item_type == junk:
                junkcount += 1
            elif loot[i].item_type == weapon:
                weaponcount += 1
            elif loot[i].item_type == material:
                materialcount += 1
            elif loot[i].item_type == consumable:
                consumablecount += 1

    print(f"Junk: {junkcount}\n weapons: {weaponcount}\n consumable: {consumablecount}\n material: {materialcount}")


dev = False
if dev is True:
    print("\ntier 0")
    probsim(0, 100)
    print("\ntier 1")
    probsim(1, 100)
    print("\ntier 2")
    probsim(2, 100)
    print("\ntier 3")
    probsim(3, 100)


# sets up enemies
def enemies():
    def add_enemy():
        print("hey")


# sets up health system
def health():
    global health

    def damage(amount):
        health -= amount

    def regen(amount):
        health += amount


# Prints location of player
def loc():
    playerpos = room_list[current_room]
    print(f"You are in the {playerpos[0]}")


def open_inv():
    print("Your inventory contains:")
    for z in playerinv:
        print(z.name)


# Takes various forms of user input
def user_input(userinput="none"):
    inp = None
    while inp is None:
        if userinput == "none":
            cmd = input(f"Please enter a command:").upper()
            if cmd.upper()[0] in controls[1:5]:
                inp = cmd[0]
                travel(current_room, inp)
            elif cmd.upper()[0] in controlkeys:
                open_inv()
            else:
                print(f"Invalid Command. Valid Commands: {controls + controlkeys}")
                continue
        elif userinput == "direction":
            direct = input("Please input a direction:").upper()
            inp = direct[0]
        return inp


# Allows the player to travel to different rooms
def travel(current, direction):
    global current_room
    global last_room
    d = None
    while d is None:
        d = controls.index(direction)
        next_room = room_list[current][d]
        if next_room is not None:
            last_room = current_room
            current_room = next_room
            loc()
        else:
            print("You cant go that direction.")


# spawn player, set starting variables
current_room = 0
last_room = 0
done = False
first = True
controls = None
health = 100
hunger = 100
energy = 10
controlkeys = ['Q', 'E']
keys = ['directional keys', 'W', 'S', 'D', 'A']
directions = ['cardinal letters/words', 'N', 'S', 'E', 'W']
playerinv = []


# Configures settings
def settings():
    global controls
    cont = input(f"Would you like to use: {keys[0]} (W,A,S,D) or {directions[0]} (N,S,E,W)? type [d/c]")
    if cont.lower() == "d":
        controls = keys
    elif cont.lower() == "c":
        controls = directions
    print(f"Controls are set to: {controls[0]}")


# main game loop
while done is False:
    if first is True:
        settings()
        print("Generating terrain...")
        time.sleep(.25)
        print("Randomizing loot...")
        # room1 = Loot(3)
        # room1.add(gen_loot(3, 1, any_item))
        time.sleep(.25)
        for each in room_list:
            room = int(room_list.index(each))
            Loot(room).add(gen_loot(3, random.randint(0,3), any_item))
            Loot(room).list()
            print()

        print("Spawning monsters...")
        time.sleep(.25)
        print("Tending the garden...")
        time.sleep(.25)
        print("Welcome to adventure game!")
        time.sleep(.25)
        loc()
        travel(current_room, user_input("direction"))
        first = False

    user_input()




