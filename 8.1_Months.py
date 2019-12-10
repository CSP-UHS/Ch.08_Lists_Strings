'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-13.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
done = False
month = int(input("Please pick a month(1-12) or quit "))
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
while done == False:
    if month > 12 or month < 1:
        print("Goodbye!")
        done = True
        break
    end = month*3
    print(months[end-3:end])
    month = int(input("Please pick a month(1-12) or quit(13) "))

