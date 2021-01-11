encrypeted_text="Lxwp{j}~uj}rxw|*)bx~)l{jltnm)}qn)lxmn7)]qn)ox{ln)r|)\][XWP)r}q)x~*"

decrypt=""
shift=0

for shift in range(-20,21,1):
    for c in encrypeted_text:
        d = ord(c)
        d += shift
        nc = chr(d)
        decrypt+=nc
    print()
    print(shift)
    print(decrypt)