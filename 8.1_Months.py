'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
month_list= "JanFebMarAprMayJunJulAugSepOctNovDec"
for i in range(30):
    user_input = int(input("Enter a number between 1 and 12"))
    if user_input==1:
        print(month_list[0:3])
    elif user_input==2:
        print(month_list[3:6])
    elif user_input==3:
        print(month_list[6:9])
    elif user_input==4:
        print(month_list[9:12])
    elif user_input==5:
        print(month_list[12:15])
    elif user_input==6:
        print(month_list[15:18])
    elif user_input==7:
        print(month_list[18:21])
    elif user_input==8:
        print(month_list[21:24])
    elif user_input==9:
        print(month_list[24:27])
    elif user_input==10:
        print(month_list[27:30])
    elif user_input==11:
        print(month_list[30:33])
    elif user_input==12:
        print(month_list[33:36])
    else:
        print("Goodbye")
        break
