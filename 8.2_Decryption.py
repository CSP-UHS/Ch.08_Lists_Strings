'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''
secretmsg = "Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"

for i in range(-20, 21, 1):
    check = len(secretmsg)
    decrypt=""
    for c in secretmsg:
        id = ord(c)
        id += i
        ch = chr(id)
        decrypt += ch
        if id == 32 or id == 33 or id == 46 or 65 <= id <=90 or 97 <= 122:
            check -= 1
        if check == 0:
            break
    print(i, " : ", decrypt)

# secret image is -9  :  Congratulations! You cracked the code. The force is STRONG with you!