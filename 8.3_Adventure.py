'''
ADVENTURE PROGRAM
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''

import random

room_list=[]

room=["Front Porch",2,None,None,None] #room 0
room_list.append(room)

room=["Music Room",4,2,None,None,] #room 1
room_list.append(room)

room=["Lobby",5,3,0,1,] #room 2
room_list.append(room)

room=["Game Room",None,None,None,2] #room 3
room_list.append(room)

room=["Soccer Field",None,6,1,None] #room 4
room_list.append(room)

room=["Kitchen",6,None,2,None] #room 5
room_list.append(room)

room=["Locker Room",None,7,5,4] #room 6
room_list.append(room)

room=["Basketball Court",None,None,None,6] #room 7
room_list.append(room)

current_room = 0

print("Welcome to The House of Riddles! Here your Adventure starts at the Door. Please "
      "take off your shoes, carry your shoes, or place them in bags as this is a no shoe house. ")
print("When entering each room you will be given a description and there will be interaction to"
      " find in each room! Find all interactions to win!")



#start program
interaction = 0
done= False
while not done:
    print()
    print(room_list[current_room][0])
    drct = input("Which way? N.E.S.W or Q to quit")

    if drct.lower() == "n":
        next_room = room_list[current_room][1]
        if next_room==None:
            print("You cant go that way!")
        else:
            current_room= next_room

    elif drct.lower() == "e":
        next_room = room_list[current_room][2]
        if next_room==None:
            print("You cant go that way!")
        else:
            current_room= next_room

    elif drct.lower() == "s":
        next_room = room_list[current_room][3]
        if next_room==None:
            print("You cant go that way!")
        else:
            current_room= next_room

    elif drct.lower() == "w":
        next_room = room_list[current_room][4]
        if next_room==None:
            print("You cant go that way!")
        else:
            current_room= next_room

    elif drct.lower() == "q":
        print("Thanks for playing! You found", interaction, "interactions out of 10!")
        break
    else:
        print("Invalid Input")


#interaction in music room

    if current_room == 1:
        print("You have entered the Music Room! Here there are trumpets, saxophones, guitars,"
              " and even a harp! You're ")
        intrument = input("welcome to play any of these instruments. Pick an instrument or press (c) to continue "
                          "on your journey!")
        if intrument.lower() == "trumpet":
            interaction+=1
            print()
            print("You started playing the instrumental to Cheerleader by OMI, interesting choice...")
        if intrument.lower() == "saxophone":
            interaction+=1
            print()
            print("You started playing Careless Whisperer by George Michael, good choice.")
        if intrument.lower()== "guitar":
            interaction+=1
            print()
            print("You started playing All of Me by John Legend, way to set the mood...")
        if intrument.lower()== "harp":
            interaction+=1
            print()
            print("You don't know any harp songs, so you just decided to run your fingers through the strings to make a"
                  " sound")
        if intrument.lower()=="c":
            print()

#done music room

#Start of lobby room
    if current_room == 2:
        print("The lobby is always the first place you see when entering a hotel. It has to be the cleanest "
              "and looking the most comfortably to get customers. Riddle me this, They might mark the start of")
        desk = input("church, or signal days end at schools, you might have one by my desk, so I know when someone" 
                     " calls. What am I? (Press c to continue)")
        if desk.lower() == "bell":
            interaction += 1
            print()
            print("Good Job! You solved my riddle! Not all rooms will be this easy or even have riddles, "
                  "but you got a "
                  "good start. Now go explore!")

#end lobby
#Start of game room
    if current_room == 3:
        game = input("When entering the game room you see a boxing arcade machine and a flappy bird arcade machine. "
                     "What Game would you like to play? Boxing or Flappy Bird?(Press c to continue)")
#Boxing
        if game.lower() == "boxing":
            an = input("Answer this question to continue. Whats a fighters favorite dog?")
            if an.lower() == "boxer":
                interaction+=1
                print("Correct! You hit the bag and got a score of",random.randint(600,999),"!")
            else:
                print("Wrong! Check out other rooms and come back later to try again!")
#Flappy
        if game.lower() == "flappy bird":
            an2 = input("Before you can play the game riddle me this. What Bird is very rude?")
            if an2.lower() == "mocking bird":
                interaction+=1
                print("Correct! Machine is out order. It's been banned.")
            else:
                print("Wrong! Not the game for you, come back later loser. ")
#end flappy
        if game.lower() == "c":
            print()
#End game room
#Start soccer field
    if current_room == 4:
        print("Did you know that futbol, or soccer is the most popular sport in the world? ")
        print("It's also one of the hardest with only 0.00047% of players going pro. How about you try ")
        soccer = input( "shooting a penalty kick on a pro level keeper versus a computer. Ready? (Yes or No)")
        print()
        if soccer.lower() == "yes":
            an4 = input("Answer this simple question to move on. Messi or Ronaldo?")
            if an4.lower()=="messi":
                print()
                interaction+=1
                print("Correct!")
#Big soccer game
            computer_score=0
            player_score=0
            while not done:
                player = input("Do you want to shoot Left side, Down the Middle, or the Right side?(Press 4 to continue)")
                print()
                if player.lower() == "middle":
                    print("You shoot the ball down the middle!")
                if player.lower() == "left":
                    print("You shoot the ball left side!")
                if player.lower() == "right":
                    print("You shot the ball Right side!")

                print()
                # print("Lets see what the computer picked!")
                num = random.randint(1, 3)
                if num == 1:
                    print("The Keeper went left!!")
                if num == 2:
                    print("The Keeper stayed in the middle!")
                if num == 3:
                    print("The Keeper went right!")

                # print("Lets See who won!")
                print()
                # tie
                if num == 1 and player.lower() == "left":
                    computer_score+=1
                    print("The Keeper saved it!")
                if num == 2 and player.lower() == "middle":
                    computer_score+=1
                    print("The Keeper saved it!")
                if num == 3 and player.lower() == "right":
                    computer_score+=1
                    print("The Keeper saved it!")
                # end tie
                # 1 player goal
                if num == 1 and player.lower() == "middle":
                    player_score+=1
                    print("You scored down the middle!")
                if num == 1 and player.lower() == "right":
                    player_score+=1
                    print("You scored on the right side!")
                # end
                # 2 player goal
                if num == 2 and player.lower() == "left":
                    player_score+=1
                    print("You scored on the left side!")
                if num == 2 and player.lower() == "right":
                    player_score+=1
                    print("You scored on the right side!")
                # end
                # 3 player goal
                if num == 3 and player.lower() == "left":
                    player_score+=1
                    print("You scored on the left side!")
                if num == 3 and player.lower() == "middle":
                    player_score+=1
                    print("You scored down the middle!")
                # end
                if player.lower() == "4":
                    print("The keeper saved your shoots", computer_score, "time(s)")
                    print("You scored on the keeper", player_score, "time(s)")
                    break
        else:
            print("Maybe next time! Continue on your adventure!")
            print()
# end big soccer game
#start kitchen
    if current_room == 5:
        print("The kitchen is a place for delicious food and the best chef's in the world. The chef asks if you want ")
        print("to help him make a pizza for dinner. You don't know a thing about cooking but want to make a ")
        kitchen = input("good first impression. Do you want to help? (yes or no) ")
        print()
        if kitchen.lower() == "yes":
            kitchen2 = input("Chef tells you to preheat the oven. What temperature you setting it to? (Fahrenheit)")
            if kitchen2.lower() == "425f":
                print("The Chef is impressed and tests you even more with a riddle.")
                print()
                kitchen3 = input("What washes up on beaches?")

                if kitchen3.lower() == "microwaves":
                    interaction+=1
                    print("The chef is amazed and lets you choice a topping!")
                    kitchen4 = input("What topping are you adding to your pizza?")
                    if kitchen4.lower() == "cheese":
                        print("Plain, nice. You took a bite and wanted another slice! Good Job from the chef!")
                    elif kitchen4:
                        print("Interesting Choice.")

        if kitchen.lower() == "no":
            print("Get out of my kitchen! says the chef.")

#end kitchen
#Start locker room
    if current_room == 6:
        print("Coaches hype players up in the locker rooms, or players cry after losing a game. Riddle me this.")
        locker = input("What is an insect's favorite sport?")
        if locker.lower() == "cricket":
            print()
            interaction+=1
            print("Correct! Nothing else to do here. Move along!")
        else:
            print()
            print("Wrong come back later.")
#end locker room.
#start basketball
    basket3 = 0
    basket_free = 0
    if current_room == 7:
        print("On the basketball court ey? How about you try shooting some three's.")
        basketball = input("Trust me its harder than it looks.(Yes or no)")
        if basketball.lower() == "yes":
            print()
            print("Solve this riddle to continue.")
            print()
            basketball2 = input("What is a good restaurant for a basketball team?")
        # else:
        #     print("Not a basketball player I guess. Cya!")
            if basketball2.lower() == "dunkin donuts":
                interaction+=1
                print("Correct! Lets play a mini game!")
                while not done:
                    basketplayer = input("Do you want to shoot on the free throw line, or shoot a three?(4 to continue)")
                    if basketplayer == "three":
                        shoot = random.randint(0,100)
                        if shoot <=75:
                            print()
                            print("You shot a three and... AIIRR BALL")
                        if shoot >= 75:
                            basket3+=1
                            print()
                            print("You shot a three and... Swish!")
                    if basketplayer == "free throw":
                        shoot2 = random.randint(0,100)
                        if shoot2 <= 75:
                            basket_free += 1
                            print()
                            print("You Shot a free throw and.. Swish!")
                        if shoot2 >= 75:
                            print()
                            print("You shot a free throw and... AIIRR BALL")
                    if basketplayer == "4":
                        print()
                        print("You made",basket_free,"free throw(s)!")
                        print("You made",basket3,"three pointers!")
                        break
    if interaction == 10:
        print()
        print("You won!")
        quit()






















