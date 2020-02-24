'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

import random
room_list = []
room = ["You are outside. You are standing on a wooden porch.", 2, None, None, None]
room_list.append(room)
room = ["You are in the bathroom. There is a toilet, bathtub, sink, and a mirror.", 4, 2, None, None]
room_list.append(room)
room = ["You are in the living room. There is a TV, but the remote is missing. There is also a very comfy couch and a coffee table.", 5, 3, 0, 1]
room_list.append(room)
room = ["You are in the kitchen. There a multiple cabinets, an oven, fridge, stove, and microwave. There is also lots of counterspace.", 6, None, None, 2]
room_list.append(room)
room = ["You are in the master bedroom. There is a large bed in the middle of the room, with a nightstand on either side. There is a very small TV that you have completely lost the remote too.", None, 5, 1, None]
room_list.append(room)
room = ["You are in the guest room. It is very similar to the master bedroom with a large bed in the middle of the room and a nightstand on either side of it. There is not much else.", 7, 6, 2, 4]
room_list.append(room)
room = ["You are in the theater. There is a large screen and a projector attached to the ceiling. There is also a shelf filled with movie dvds.", None, 3, None, 5]
room_list.append(room)
room = ["You are in the room with your indoor pool. There is a big pool and a shelf with plenty of towels on it.", None, None, 5, None]
room_list.append(room)

current_room = 0
done = False
TV_remote = random.randrange(7)
if TV_remote == 1:
   bathroom = random.randrange(4)
elif TV_remote == 3:
   kitchen = random.randrange(5)
time = 0

print("You just got home from work.")
print("Your favorite movie starts at 7:30, the time right now is 6:00")
print("Go watch some TV.")
print("Use NESW to move, Q to quit and I to interact with the room you are in.")
print()
print()
print()
print()
print()

while done == False:
   print()
   print(room_list[current_room][0])
   direction = input("Which direction do you want to go? (NESW)")
   if direction.lower() == "n" or direction.lower == "north":
       next_room = room_list[current_room][1]
       if next_room == None:
           print("You can't go that way!")
       else:
           current_room = next_room
   if direction.lower() == "e" or direction.lower == "east":
       next_room = room_list[current_room][2]
       if next_room == None:
           print("You can't go that way!")
       else:
           current_room = next_room
   if direction.lower() == "s" or direction.lower == "south":
       next_room = room_list[current_room][3]
       if next_room == None:
           print("You can't go that way!")
       else:
           current_room = next_room
   if direction.lower() == "w" or direction.lower == "west":
       next_room = room_list[current_room][4]
       if next_room == None:
           print("You can't go that way!")
       else:
           current_room = next_room
   if direction.lower() == "q" or direction.lower == "quit":
       print("You quit.")
       done = True
   if direction.lower() == "i" or direction.lower == "interact":
       if current_room == 0:
           interact = input("Do you look in the bushes? (Y or N)")
           if interact.lower() == "y" or interact.lower() == "yes":
               if TV_remote == 0:
                   print("You found the remote in the bushes!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing in the bushes.")
       if current_room == 1:
           interact = input("Where do you want to look (toilet, bathtub, sink, or mirror)")
           if interact.lower() == "t" or interact.lower == "toilet":
               if bathroom == 0:
                   print("You found the remote behind the toilet!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing behind the toilet.")
           if interact.lower() == "b" or interact.lower == "bathtub":
               if bathroom == 1:
                   print("You found the remote in the bathtub!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing in the bathtub.")
           if interact.lower() == "s" or interact.lower == "sink":
               if bathroom == 2:
                   print("You found the remote by the sink!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing by the sink.")
           if interact.lower() == "mirror" or interact.lower == "m":
               print("You don't see the remote, only a very sad man.")
       if current_room == 2:
           interact = input("Do you want to look around the living room? (Y or N)")
           if interact.lower() == "y" or interact.lower() == "yes":
               if TV_remote == 2:
                   print("You find the TV remote on the coffee table!")
               else:
                   print("You don't find the TV remote, must be somewhere else in the house.")
           else:
               print("You just stand there.")
       if current_room == 3:
           interact = input("Where do you want to look (cabinets, oven, fridge, stove, or microwave)")
           if interact.lower() == "c" or interact.lower == "cabinets":
               if kitchen == 0:
                   print("You found the remote inside a cabinet!!")
                   done = True
                   Remote = True
               else:
                   print("Ther  e was nothing in the cabinets.")
           if interact.lower() == "o" or interact.lower == "oven":
               if kitchen == 1:
                   print("You found the remote in the oven!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing in the oven.")
           if interact.lower() == "f" or interact.lower == "fridge":
               if kitchen == 2:
                   print("You found the remote in the fridge!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing in the fridge.")
           if interact.lower() == "s" or interact.lower == "stove":
               if kitchen == 3:
                   print("You found the remote by the stove!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing by the stove.")
           if interact.lower() == "m" or interact.lower == "microwave":
               if kitchen == 4:
                   print("You found the remote in the microwave!")
                   done = True
                   Remote = True
               else:
                   print("There was nothing in the microwave.")
       if current_room == 4:
           interact = input("Do you look around the master bedroom? (Y or N)")
           if interact.lower() == "y" or interact.lower() == "yes":
               if TV_remote == 4:
                   print("You found it on a nightstand!")
                   done = True
                   Remote = True
               else:
                   print("You can not find the remote in your bedroom.")
           else:
               print("You do not look for anything.")
       if current_room == 5:
           interact = input("Do you look around the guest room? (Y or N)")
           if interact.lower() == "y" or interact.lower() == "yes":
               if TV_remote == 5:
                   print("You found it on a nightstand!")
                   done = True
                   Remote = True
               else:
                   print("You can not find the remote in the guest room.")
           else:
               print("You do not look for anything.")
       if current_room == 6:
           interact = input("Do you look around the theater? (Y or N)")
           if interact.lower() == "y" or interact.lower() == "yes":
               if TV_remote == 6:
                   print("You found it behind the movie dvds!")
                   done = True
                   Remote = True
               else:
                   print("You can not find the remote in your theater room.")
           else:
               print("You do not look for anything.")
       if current_room == 7:
           interact = input("Do you look around the indoor pool? (Y or N)")
           if interact.lower() == "y" or interact.lower() == "yes":
               if TV_remote == 7:
                   print("You found it behind the towel rack")
                   done = True
                   Remote = True
               else:
                   print("You can not find the remote in your indoor pool.")
           else:
               print("You do not look for anything.")
   if time >= 90:
       done = True
   time +=1
if Remote == True:
   print("Good job! You got to watch TV tonight.")
else:
   print("You lost! You don't get to watch TV tonight.")

