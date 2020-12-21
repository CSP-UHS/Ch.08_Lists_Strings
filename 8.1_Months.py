'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
done = False
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
while not done:
    number=int(input("Please enter a number 1-13: "))
    if number == 13:
        done = True
        break
    start=number*3-3
    end=number*3
    print("You chose",months[start:end])
print("Goodbye!")
