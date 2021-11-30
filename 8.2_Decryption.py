'''
DECRYPTION PROGRAM
------------------
An encryption program was used to generate the following secret code. The encryption program converted each character 
of the string into its ASCII decimal number, applied a +/-20 algorithm to it and then converted it back to
characters. Your task is to write a Decryption program to decipher the following secret code. Don't waste time changing 
your program 40 times. Use a FOR loop from -20 to +20 to generate all the possibilities in one run of your program.

Secret Message: Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*
'''

sm = "Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"

for i in range(-20, 20):
    check = len(sm)
    et = ""
    for c in sm:
        x = ord(c)
        x += i
        l = chr(x)
        et = et + l
    for ch in et:
        if ord(ch) == 32 or ord(ch) == 33 or ord(ch) == 46 or 65 <= ord(ch) <= 90 or 97 <= ord(ch) <= 122:
            check -= 1
    if check == 0:
        break
print(et)
