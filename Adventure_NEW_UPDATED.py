'''
BRAND NEW IDEA... FUCK STAR WARS WE GOING GREEK MYTHOLOGY IN THIS BITCH
okay but the game is more of a game
GAMEPLAY: You enter proceduraly generated rooms (still choose between 4) with random number of enemies. Write a super
long algorithm for whether or not the room is cleared, gain 1 soul for every enemy cleared. When you die you go back
to the beginning and can spend souls to upgrade stats. If you clear a room with a certain number of enemies you gain a
special weapon point, which you can spend on new weapons with better stats.
WEAPONS: Weapons are situational, some may be better at AOE clearing, some may be better at single target clearing,
some may benefit from long range, some short.
ATTRIBUTES: Every character, mob, and boss have health, damage, dps, and range. Depending on stats a character will be
victorious
IMPORTANT THINGS TO REMEMBER: The game should not be SUPER luck based, should not take forever, and should not require
a single threshold to win (there should not be one combination of attributes and weapons in order to win).
ROOMS: After clearing a room, you have 4 options for the next, depending on the room, the amount of enemies will
increase, as well as difficulty. The main hub area has a spot for upgrading attributes, unlocking weapons,
and changing what weapon you use for the next run. After clearing 5 rooms in a run, a
random boss with set stats (for instance, one run could be a minotaur, the next could be medusa, but the stats will
remain the sames so that the clear is not based on RNG)

The player character will have a base health and damage, weapons will determine DPS and range, as well as buffing or
nerfing the players base stats. Mobs and bosses will have all 4 stats default. The only portion of the game that is
based on RNG is the number of enemies that are in a room, all bosses will be beatable once you cross their threshold.
When the player dies, give information about the boss and the player, so that they know what they need to level.

3 mini bosses leading up to Hades, aiming for a total of 5 runs, maybe a total game time of 20 minutes or so.
'''
import random


class Character:
    def __init__(self, name, health, damage, dps, intro, outro):
        self.name = name
        self.health = health
        self.damage = damage
        self.dps = dps
        self.intro = intro  # To allow for easier intro of bosses
        self.outro = outro


class Weapon:
    def __init__(self, name, hpbuff, dmgbuff, dps, unlocked):
        self.name = name
        self.hpbuff = hpbuff
        self.dmgbuff = dmgbuff
        self.dps = dps
        self.unlocked = unlocked


class Item:
    def __init__(self, name, hpbuff, dmgbuff, dpsbuff, unlocked):
        self.name = name
        self.hpbuff = hpbuff
        self.dmgbuff = dmgbuff
        self.dpsbuff = dpsbuff
        self.unlocked = unlocked


class Room:
    def __init__(self, emin, damage, dps, health, diff, desc):
        self.emin = emin
        self.dps = dps
        self.diff = diff
        self.desc = desc
        self.health = health
        self.damage = damage


# Creating characters and levels and weapons
zag = Character("Zagreus", 200, 200, 20, "Unimportant", "Still unimportant")  # Creating the main character and bosses
zag_base = Character("Zagreus", 200, 200,
                     20, "Even less important",
                     "And less important still")  # These values are the base values, the zag values will be changed during the game
hades = Character("Hades", 8000, 115, 45,
                  "\033[33mAs you make your final steps to the surface, a familiar booming voice can "
                  "be heard mocking you. Your dad, Hades, is the final challenge you must "
                  "conquer on your quest.\033[0m\n",
                  "\033[33mYour dad slumps over lifeless, you are finally free...\033[0m\n")
bhyd = Character("Bone Hydra", 3000, 70, 30, "\033[33mJust as you were about to exit tartarus, a 3 headed bone "
                                             "hydra blocked your path. You must defeat him to move on\033[0m\n",
                 "\033[33mYou defeat the bone hydra and make your "
                 "way to Elysium\033[0m\n")
meg = Character("Megaera", 2000, 40, 20, "\033[33mYou fight against Megaera\033[0m\n",
                "\033[33mWith the Fury slain you move ever close "
                "toward your goal, and step into Ashpodel.\033[0m\n")
theseus = Character("Theseus", 5000, 90, 40,
                    "\033[33mTheseus, a hero of old, is blocking your path. In order to move on you "
                    "must defeat him in combat\033[0m\n", "\033[33mWith the fallen legend behind you, you "
                                                          "can taste the fresh air and smell the "
                                                          "flowers blooming on the surface.\033[0m\n")

hub = Room(0, 0, 0, 0, 0, "House of Hades")
lvl_1 = Room(7, 15, 10, 1000, 1, "Tartarus")  # Creating rooms
lvl_2 = Room(11, 15, 15, 2000, 2, "Ashpodel")
lvl_3 = Room(15, 20, 20, 3000, 3, "Elysium")

styg = Weapon("Stygius", 0, 0, 20, True)  # Creating weapons # Sword
aegis = Weapon("Aegis", 150, 100, 15, False)  # Shield
varatha = Weapon("Veratha", 0, 120, 30, False)  # Javelin
coronacht = Weapon("coronacht", -5, 130, 15, False)  # Bow
malphon = Weapon("Malphon", 200, 80, 20, False)  # Gloves
exagryph = Weapon("Exagryph", -10, 150, 40, False)  # Gun

collar = Item("Cerberus' collar", 1000, 0, 0, False)
shawl = Item("Black Shawl", 0, 1000, 0, False)
plume = Item("Lambent Plume", 0, 0, 40, False)

souls = 0
soul_bar = 40


def hub_func():
    '''
    print("this is where you upgrade attributes\n")
    print("This is where you unlock weapons\n")
    print("this is where you change weapons and items\n")
    print("You have", souls, "souls\n")
    if input("would you like to start a run? Y or N\n").upper() == "Y":
        game_play()
    else:
        print("You go back to your room\n")
    '''
    print("1. Access attribute menu\n2. Access weapons menu\n3. Access item menu\n4. Begin run\n")
    menmove = int(input("What would you like to do?\n"))
    if menmove == 1 or menmove == 2 or menmove == 3 or menmove == 4:
        if menmove == 1:
            att_menu()
        elif menmove == 2:
            calcstat(weapon_menu())
            print(zag.health, zag.damage, zag.dps)
        elif menmove == 3:
            item_menu()
        else:
            game_play()


def att_menu():  # Creates menu for attribute improvement
    global souls
    global soul_bar
    print("Current Stats\n")
    print("Health:", zag_base.health)
    print("Damage:", zag_base.damage, "\n")
    print("souls:", souls, "\n")
    if souls >= soul_bar:
        print("You can upgrade either your health or damage.\n")
        print("1. Health\n2. Damage\n")
        answer = int(input("Which would you like to upgrade? 1 or 2\n"))
        if answer == 1:
            zag_base.health += 200
            print("Health upgraded. New health: ", zag_base.health, "\n")
        else:
            zag_base.damage += 200
            print("Damage upgraded. New damage: ", zag_base.damage, "\n")
        souls -= soul_bar
        if soul_bar < 200:
            soul_bar += 40


def weapon_menu():
    print("Available Weapons\n")
    print("1. Stygius")
    print("Extra Health: 0", "Extra Damage: 0", "DPS: 20\n")
    if aegis.unlocked:
        print("2. Aegis")
        print("Extra Health: 150", "Extra Damage: 100", "DPS: 15\n")
    if varatha.unlocked:
        print("3. Varatha")
        print("Extra Health: 0", "Extra Damage: 120", "DPS: 30\n")
    if coronacht.unlocked:
        print("4. Coronacht")
        print("Extra Health: -5", "Extra Damage: 130", "DPS: 30\n")
    if malphon.unlocked:
        print("5. Malphon")
        print("Extra Health: 200", "Extra Damage: 80", "DPS: 20\n")
    if exagryph.unlocked:
        print("6. Exagryph")
        print("Extra Health:", exagryph.hpbuff, "Extra Damage:", exagryph.dmgbuff, "DPS:", exagryph.dps, "\n")
    select = int(input("Which would you like to equip? 1 through 6\n"))
    if select == 1:
        print("You equipped Stygius\n")
        return styg.hpbuff, styg.dmgbuff, styg.dps
    elif select == 2 and aegis.unlocked:
        print("You equipped Aegis\n")
        return aegis.hpbuff, aegis.dmgbuff, aegis.dps
    elif select == 3 and varatha.unlocked:
        print("You equipped Varatha\n")
        return varatha.hpbuff, varatha.dmgbuff, varatha.dps
    elif select == 4 and coronacht.unlocked:
        print("You equipped Coronacht\n")
        return coronacht.hpbuff, coronacht.dmgbuff, coronacht.dps
    elif select == 5 and malphon.unlocked:
        print("You equipped Malphon\n")
        return malphon.hpbuff, malphon.dmgbuff, malphon.dps
    elif select == 6 and exagryph.unlocked:
        print("You equipped Exagryph\n")
        return exagryph.hpbuff, exagryph.dmgbuff, exagryph.dps
    else:
        print("something went wrong. Oops.\n")


def item_menu():
    if not collar.unlocked and not shawl.unlocked and not plume.unlocked:
        print("You don't have any items")
    if collar.unlocked:
        print("1.", collar.name, "\nThis item grants 1000 extra health\n")
    if plume.unlocked:
        print("2.", plume.name, "\nThis item grants 1000 extra damage\n")
    if shawl.unlocked:
        print("3.", shawl.name, "\nThis item grants 40 extra DPS\n")


def calcstat(response):
    if collar.unlocked:
        zag.health = zag_base.health + response[0] + collar.hpbuff
    else:
        zag.health = zag_base.health + response[0]
    if shawl.unlocked:
        zag.damage = zag_base.damage + response[1] + shawl.dmgbuff
    else:
        zag.damage = zag_base.damage + response[1]
    if plume.unlocked:
        zag.dps = response[2] + plume.dpsbuff
    else:
        zag.dps = response[2]


def game_play():
    global playing
    if room_play(first_room(), lvl_1.emin, lvl_1.damage,
                 lvl_1.dps):  # Does room one with the difficulty selected by the player
        if boss(meg.health, meg.damage, meg.dps, meg.intro, meg.outro):
            if room_play(room_choose(), lvl_2.emin, lvl_2.damage, lvl_2.dps):
                if boss(bhyd.health, bhyd.damage, bhyd.dps, bhyd.intro, bhyd.outro):
                    room_play(room_choose(), lvl_3.emin, lvl_3.damage, lvl_3.dps)
                    if boss(theseus.health, theseus.damage, theseus.dps, theseus.intro, theseus.outro):
                        if boss(hades.health, hades.damage, hades.dps, hades.intro, hades.outro):
                            print("Congrats you beat the game!")
                            playing = False


def first_room():  # Handles the first room because it is different from the rest
    print("You enter the dungeon, the only way to return is to perish.\n")
    move = int(input("Which way would you like to start? 1 through 4\n"))
    if 1 <= move <= 4:
        return move


def room_play(difficulty, enemy_min, damage, dps):  # Handles rooms for the first level
    game_diff = difficulty
    global souls
    for i in range(5):
        wpnunlock()
        itemunlock()
        print("There are", enemy_min + game_diff, "enemies in this room\n")
        if fight_room(game_diff, damage, dps):
            print("\033[32mYou cleared the room\033[0m\n")
            souls += (enemy_min + game_diff)
            game_diff = room_choose()
        else:
            print("\033[31mYou died trying to clear the room, you have been sent back to the House of Hades\033[0m\n")
            return False
    return True


def wpnunlock():
    randomnumber = random.randint(0, 50)
    if randomnumber == 1 and not aegis.unlocked:
        aegis.unlocked = True
        print("\033[94mYou unlocked a new weapon!\033[0m")
    elif randomnumber == 2 and not varatha.unlocked:
        varatha.unlocked = True
        print("\033[94mYou unlocked a new weapon!\033[0m")
    elif randomnumber == 3 and not malphon.unlocked:
        malphon.unlocked = True
        print("\033[94mYou unlocked a new weapon!\033[0m")
    elif randomnumber == 4 and not exagryph.unlocked:
        exagryph.unlocked = True
        print("\033[94mYou unlocked a new weapon!\033[0m")
    elif randomnumber == 5 and not coronacht.unlocked:
        coronacht.unlocked = True
        print("\033[94mYou unlocked a new weapon!\033[0m")


def itemunlock():
    randomnumber = random.randint(1, 100)
    if randomnumber == 1 and not collar.unlocked:
        print("\033[35mYou got an item!\033[0m\n")
        collar.unlocked = True
    elif randomnumber == 2 and not shawl.unlocked:
        print("\033[35mYou got an item!\033[0m\n")
        shawl.unlocked = True
    elif randomnumber == 2 and not plume.unlocked:
        print("\033[35mYou got an item!\033[0m\n")
        plume.unlocked = True


def fight_room(enemies, damage, dps):  # Handles whether or not a room has been cleared
    ttkp = zag.health / (damage * dps)  # Figures out how quickly the enemies can kill the player
    ttcr = (lvl_1.health + (1500 * enemies)) / (
            zag.damage * zag.dps)  # Figures out how quickly the player can kill the enemies
    print("Time to kill player: ", ttkp)
    print("Time to clear room: ", ttcr, "\n")
    if ttcr <= ttkp:  # If the player can kill the enemies faster than they can kill him, he moves on
        return True
    else:
        return False


def fight_boss(boss_health, boss_damage, boss_dps):  # Fight algorithm for bosses
    ttkp = zag.health / (boss_damage * boss_dps)  # Figures out how quickly the boss can kill the player
    ttkb = boss_health / (zag.damage * zag.dps)  # Figures how quickly player can kill boss
    print("Time to kill player: ", ttkp)
    print("Time to kill boss: ", ttkb, "\n")
    if ttkb <= ttkp:  # If the player can kill the boss faster than they can kill him, he moves on
        return True
    else:
        return False


def room_choose():  # Choosing rooms
    return int(input("Which room would you like to go to? 1 through 4\n"))


def boss(health, damage, dps, intro, outro):  # Boss fights
    print(intro)
    if fight_boss(health, damage, dps):
        print(outro)
        return True
    else:
        print("\033[31mYou were conquered in battle, and are returned to your home.\033[0m\n")
        return False


def intro():
    print("\nWelcome to hell.")
    print("In this stupid adventure game you play as Zagreus, son of Hades, the god of the dead.")
    print("His whole life Zagreus have been trapped in the underworld, maybe with you at the controls he can finally "
          "make the long journey to the surface.")
    print("You must battle your way through 3 layers of the underworld, fighting enemies around every corner")
    print("As you slay enemies in each room, you will gain souls, which you can use to upgrade your attributes in the "
          "main menu")
    print("In each room you will have a choice between where you want to go next, your choice will determine the "
          "danger you face.")
    print("The higher difficulty rooms will have more enemies, but grant more souls.")
    print("At the end of each layer you will face a boss, who will be much stronger than the previous rooms")
    print("After every room cleared you will see two numbers, Time to kill player and time to clear room/kill boss.")
    print("These numbers determine whether or not you clear the room or beat the boss.")
    print("Increasing your damage will decrease your time to clear/kill rooms/bosses, and increasing your health will "
          "increase the time to kill the player.")
    print("Keep an eye on these numbers to decide how you want to play the game!")
    print("On occasion you will receive new weapons (1 in 20 chance per room cleared), and on very rare occasions "
          "(1 in 100) you will receive special items that increase your stats and make you stronger")
    print("In the main menu, you can look at weapons and equip them.")
    print("You can also look at items, if you got any, and see the stats they give, but you do not need to equip "
          "them to get their benefits.")
    print("\n\033[31mIMPORTANT:\033[0m Implementing features to save the game if you input something wrong was not "
          "something I had the time or patience to do.\nSome wrong inputs will break the game, some will not.\nSo do "
          "not test to see if my code is bullet proof, it is not, and if you do, thats on you...")
    print("\nEnjoy the game!\n")


def main():  # main function
    global playing
    intro()
    calcstat([0, 0, 20])
    playing = True
    while playing:
        hub_func()


if __name__ == "__main__":
    main()
