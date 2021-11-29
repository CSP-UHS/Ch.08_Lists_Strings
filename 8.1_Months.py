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
    num = int(input("What month? To quit break range of 1-12 "))
    end = num * 3
    start = end - 3
    if num >= 1 and num <= 12:
        print(months[start,end])
    else:
        done = True