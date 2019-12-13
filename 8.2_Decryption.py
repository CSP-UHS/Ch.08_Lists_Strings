'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''

secretMessage ='Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*'

for change in range(-20, 20):
    decryption = ""
    for i in range(len(secretMessage)):
        num = ord((secretMessage[i]))
        num += change
        decryption += chr(num)
    print(decryption)



# print()
# for item in secretMessage:
#     ad = ord(item)
#     asciiList.append(ad)
# while applied == 20:
#     for item in asciiList:
#         item += applied
#         od = chr(item)
#         decryption



