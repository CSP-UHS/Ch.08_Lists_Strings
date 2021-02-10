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
done=False
while not done:
    themonth=float(input("Enter month number 1-13"))
    if themonth==13:
        done=True
        break
    start=themonth*3-3
    end=themonth*3
    print(months[int(start):int(end)])


