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
while done == False:
    i = int(input("Type the number correlating to a month"))
    months="JanFebMarAprMayJunJulAugSepOctNovDec"
    end=i*3
    start=end-3
    print(months[start:end])
    if i < 1 or i > 12:
        done =True


