def encrypt_letter(letter, shift):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter not in alpha and letter not in alpha.lower():
        return letter
    index = alpha.index(letter.upper())
    new = index + shift
    if new > 26:
        if letter in alpha.lower():
            return alpha[new-26].lower()
        return alpha[new-26]
    if letter in alpha.lower():
        return alpha[new].lower()
    return alpha[new]

def decrypt_letter(letter, shift):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter not in alpha and letter not in alpha.lower():
        return letter
    index = alpha.index(letter.upper())
    new = index-shift
    if letter not in alpha:
        return alpha[new].lower()
    return alpha[new]

def encrypt(word,shift):
    string = ""
    for n in word:
        string += encrypt_letter(n,shift)
    return string

def decrypt(word,shift):
    string = ""
    for n in word:
        string += decrypt_letter(n,shift)
    return string

pt = "'The greatest films of all time were never made' - Taylor Swift, 2020"
shift = 10
enc = encrypt(pt, shift)
dec = decrypt(enc, shift)
print(enc)
print(dec)

#print(decrypt_letter("R",10))
