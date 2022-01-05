'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
done=True
month_list= "JanFebMarAprMayJunJulAugSepOctNovDec"
while done==True:
    user_input = int(input("Enter a number between 1 and 12"))
    end_point = user_input*3
    start_point = end_point-3
    print(month_list[start_point:end_point])
    if user_input>12:
        print("goodbye")
        done=False