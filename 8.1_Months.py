'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-12.
From the user input number, slice the string below in your program to print the three month abbreviation.
Keep repeating this until the user enters a non 1-12 number to quit.
Once the user quits, print "Goodbye!"
'''

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

while 1:
	month = int(input("Please enter a number between 1-12: "))
	if month < 1 or month > 12:
		print("ありがとございます。さよなら。(Thanks Much! Goodbye!)")
	else:
		pos = (month - 1) * 3
		monthabbr = months[pos:pos+3]
		print("The month abbreviation is: \'", monthabbr, "\'")
