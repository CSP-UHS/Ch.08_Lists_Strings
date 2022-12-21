"""
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the
three-month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
"""
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
done = False
while not done:
    yourMonth = int(input("Enter a month using numbers 1 - 12."))
    if 0 < yourMonth < 13:
        print(months[yourMonth*3-3:yourMonth*3])
    else:
        break
print()
print("Thanks for playing. Goodbye!")
