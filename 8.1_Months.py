'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''

Months = "JanFebMarAprMayJunJulAugSepOctNovDec"

while True:
    UserInput=int(input("Pick a month number (1-12):"))
    if UserInput<1 or UserInput>12:
        break
    End=UserInput*3
    Start=End-3
    print(Months[Start:End])

print("Goodbye.")