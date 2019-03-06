'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-13.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
while True:
    user_input = int(input("Enter a month number! \n\r"))
    if user_input > 0 and user_input < 13:
        print(months[user_input*3-3:user_input*3])
    elif user_input == 13:
        print("Goodbye!")
        break