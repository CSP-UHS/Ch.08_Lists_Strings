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
    userInput=int(input("Pick a month number (1-12): "))
    if userInput<1 or userInput>12:
        break
    end=userInput*3
    start=end-3
    print(months[start:end])
print("Goodbye")
