'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

done = False
while not done:
    answer = int(input("Please enter a number 1-13: "))
    if answer == 13:
        done = True
        print("Bye")
        break
    start = answer*3-3
    end = answer*3
    print("The month is", months[start:end])
