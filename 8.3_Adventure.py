'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

# room setup: Room Description, North, East, South, West,
import random

room_list = []
room = ['You stand in the castle entrance.  The main courtyard lies to the south, and the guard tower is to the West.',
        None, None, 1, 2]
room_list.append(room)
room = ['The courtyard is connects to many parts of the castle.  The entrance is to the north, the Kitchen is to the '
        'east, the Grand Hall is to the south, and the West wall is to the west.', 0, 5, 6, 3]
room_list.append(room)
room = ['From the top of the tower, you can see most of the castle.  The entrance is to the east, and the West wall is '
        'to the south.', None, 0, 3, None]
room_list.append(room)
room = ['The West wall is wide and straight.  There are plenty of crates to hide behind.  The tower is to the north, '
        'and the courtyard is to the East, and the South wall is to the south.', 2, 1, 4, None]
room_list.append(room)
room = ['The South wall is a small and cramped corridor.  The West wall is to the north.  There is a hidden passage to '
        'the Throne room to the east.', 3, 7, None, None]
room_list.append(room)
room = ['The kitchen is filled with smoke, and it smells of fresh bread.  The only way out is to the west, into '
        'the courtyard.', None, None, None, 1]
room_list.append(room)
room = ['You feel small next to the towering pillars in the Grand Hall.  One set of stairs to the west leads to the '
        'Throne room, and another set to the east leads to the Royal Bedroom.  The courtyard is also to the north.',
        1, 8, None, 7]
room_list.append(room)
room = ['The large golden throne dominates the Throne room.  Strangely, there are no guards here.  A doorway to the '
        'east leads to the Grand Hall.  There is also a hidden passage to the west.', None, 6, None, 4]
room_list.append(room)
room = ['The heavy curtains make the Royal bedroom feel dark yet spacious.  The only exit is to the west, into the '
        'Grand Hall.', None, None, None, 6]
room_list.append(room)

# print(room_list)

current_room = 0

done = False
next_room = None

timer = None

royal_crown = False  # In order to win, you must escape with the crown

coin_sack = False       # bribe guards
bread = False           # bribe peasant
rope = False            # escape over wall
sword = False           # fight guards
armor = False           # fight guards
royal_clothing = False      # disguise self
peasants_clothing = False   # disguise self

armor_equipped = False  # when fighting guards, user must have armor equipped


def investigate():
    print('\nYou investigate the room.')
    global royal_crown, coin_sack, bread, rope, sword, royal_clothing, peasants_clothing, armor, timer

    if current_room == 7 and royal_crown is False:                      # first check for location dependent items
        print('\nYou find the royal crown resting upon the throne, and you quickly snatch it and put it in your bag.  '
              'It has a large sapphire crystal embedded on the front.')
        royal_crown = True
        timer = 7
    elif current_room == 8 and royal_clothing is False:
        print('\nYou find a set of royal clothing in the closet.')
        royal_clothing = True
    elif current_room == 5 and bread is False:
        print('\nYou steal a piece of bread from the kitchen.  It is still warm and fresh.')
        bread = True
    elif coin_sack is False and (current_room == 4 or current_room == 2) and coin_sack is False and \
            random.randrange(0, 2) == 1:
        print('\nYou find a coin sack hidden underneath a loose floorboard.')
        coin_sack = True
    elif random.randrange(0, 4) == 1 and rope is False:                 # then check for general random items
        print('\nYou find a thick and long coil hempen rope.  It looks like it can support your weight.')
        rope = True
    elif random.randrange(0, 5) == 1 and peasants_clothing is False:
        print("\nYou find a set of peasant's clothing.")
        peasants_clothing = True
    elif random.randrange(0, 5) == 1 and sword is False:
        print('\nYou find a sword hidden inside of a crate.  The blade has the signature of the ruined king')
        sword = True
    elif random.randrange(0, 4) == 1 and armor is False:
        print('\nYou find a set of armor.  There are large iron thorns embedded in the chest plate.')
        armor = True
    else:
        print('\nYou do not find anything in your investigation.')


def inventory():
    print('\nCurrent backpack items:')
    if coin_sack is True:
        print('Sack of coins')
    if bread is True:
        print('Bread')
    if rope is True:
        print('Rope')
    if sword is True:
        print('Sword')
    if royal_clothing is True:
        print('Royal Clothing')
    if peasants_clothing is True:
        print("Peasant's Clothing")
    if armor is True:
        print('Armor')

        if armor_equipped is False:
            print('\nYou have not equipped your armor.')
        else:
            print('\nYou have equipped your armor.')

    action = input('\nWould you like to use an item? (Y/N): ')
    if action.upper() == 'Y' or action.upper() == 'YES':
        use_item()

    elif action.upper() == 'N' or action.upper() == 'NO':
        print('\nYou do not use an item.')


def use_item():
    item = input('\nWhich item would you like to use?  (Please enter the full item name): ')
    global armor_equipped, done
    if item.upper()[:3] == 'ARM' and armor is True and armor_equipped is False:
        print('\nYou equip the armor.')
        armor_equipped = True
    elif armor_equipped is True:
        print('\nYou have already equipped your armor.')

    if item.upper()[:3] != 'ARM' and royal_crown is False:
        print('\nEither that is not a valid item, or you cannot use it right now.  Make sure to find the crown '
              'before trying to escape from the castle.')

    elif item.upper()[:3] == 'COI' and coin_sack is True and royal_crown is True and (current_room == 0 or
                                                                                      current_room == 1):
        print('\nYou give the guards the coin sack as a bribe, and they agree to look the other way as you escape with '
              'the crown.')
        done = True
    elif item.upper()[:3] == 'BRE' and bread is True and royal_crown is True and (current_room == 0 or current_room == 1):
        print('\nYou give the bread to a peasant farmer, who agrees to hide you in his wagon when he leaves the castle.'
              ' You hide underneath several bags of seed, and you escape from the castle, undetected.')
        done = True
    elif item.upper()[:3] == 'ROP' and rope is True and royal_crown and (current_room == 2 or current_room == 3 or
                                                                         current_room == 4):
        print('\nYou tie the rope to a castle wall, and you use the rope to repel down the side of castle.  You escape '
              'with the crown, undetected.')
        done = True
    elif item.upper()[:3] == 'ROY' and royal_clothing is True and royal_crown is True:
        print('\nYou hide and put on the royal clothing to disguise yourself as a noble.  You simply walk out the front'
              ' entrance with the crown, and nobody stops you.')
        done = True
    elif item.upper()[:3] == 'SWO' and sword is True and royal_crown is True:
        print('\nYou decide to fight your way out of the castle, so you start running towards the main entrance with '
              'your sword in hand. ')
        fight()


def fight():
    global done
    if sword is True and armor_equipped is True:
        print("\nYou use your sword to slice through the guard's armor.  One tries to counterattack, but his spear is "
              "deflected by your armor with a deep 'clang!'  The guards cannot stop you, and you escape out of the "
              "castle with the crown.  ")
    elif sword is False and armor_equipped is True:
        print('\nYou try to attack the guards, but you have no weapon to fight them with.  You try to use your fists, '
              'but you cannot land a solid hit.  You are unable to take the guards down, and you are captured.')
    elif sword is True and armor_equipped is False:
        print("\nYou use your sword to slice through the guard's armor.  Another guard counterattacks with his "
              "spear, and he stabs right into your gut.  You fall to the ground and are captured by the guards.")
    else:
        print('\nYou try to fight back, but you have no tools to do so.  You are quickly outnumbered and captured by '
              'the guards.')
    done = True


while not done:
    print()
    print(room_list[current_room][0])
    choice = input('Would you like to go North, South, East, or West?  You can also investigate the current room (I) '
                   'or check your backpack (B).  Enter Q to quit: ')
    if choice.upper() == 'N' or choice.upper() == 'NORTH':
        next_room = room_list[current_room][1]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the north.')
    elif choice.upper() == 'E' or choice.upper() == 'EAST':
        next_room = room_list[current_room][2]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the east.')
    elif choice.upper() == 'S' or choice.upper() == 'SOUTH':
        next_room = room_list[current_room][3]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the south.')
    elif choice.upper() == 'W' or choice.upper() == 'West':
        next_room = room_list[current_room][4]
        if next_room is None:
            print('\nThere is no room there.')
        else:
            current_room = next_room
            print('\nYou enter the room to the west.')
    elif choice.upper()[:1] == 'Q':
        done = True
        print('Better luck next time.')
        continue

    elif choice.upper()[:1] == 'I':
        investigate()

    elif choice.upper()[:1] == 'B':
        inventory()

    if type(timer) is int:
        timer -= 1
        if timer == 3:
            print('\nYou hear bells signaling an alarm.  The guards are now looking for you.  Try to escape quickly.')
        elif timer == 0:
            encounter = True
            while encounter is True:
                choice = input('\nThe guards catch up and surround you.  Would you like to fight? (Y/N): ')
                if choice.upper()[:1] == 'Y':
                    fight()
                    encounter = False
                elif choice.upper()[:1] == 'N':
                    print('\nYou have no choice but to surrender.  You are thrown into the dungeon deep beneath the '
                          'castle, from where you will never escape.')
                    encounter = False
                    done = True
                else:
                    print('\nThat is not a valid response.')

# mechanic to search from the tower?
