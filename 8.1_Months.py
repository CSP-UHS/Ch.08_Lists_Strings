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
    num = int(input("Chose a month 1-12 or 13 to quit: "))
    end = num * 3
    start = end - 3
    if num == 13:
        done = True
    else:
        print("Your month was ", months[start:end])