'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"



'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
while True:
    num = int(input("Hello! Please enter a number for what month you would like to see (1-12): "))
    if num<1 or num >12:
        break
    end=num*3
    print(months[end-3:end])
print("Goodbye!")

