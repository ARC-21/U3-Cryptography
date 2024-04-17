def encode_letter(c,code_alpha):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if c not in alpha:
        #print("in encode, C IS " + str(c))
        if c not in alpha.lower():
            return c
        return code_alpha[alpha.index(c.upper())].lower()
    return code_alpha[alpha.index(c)]

def decode_letter(c, code_alpha):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if c not in code_alpha:
        #print("in decode, C IS " + str(c))
        if c not in code_alpha.lower():
            return c
        return alpha[code_alpha.index(c.upper())].lower()
    return alpha[code_alpha.index(c)]

def substitution_encode(word, code_alpha):
    encoded_word = ''
    for c in word:
        encoded_word += encode_letter(c,code_alpha)
    return encoded_word

def substitution_decode(word, code_alpha):
    decoded_word = ''
    for c in word:
        decoded_word += decode_letter(c,code_alpha)
    return decoded_word

#pt = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
#a2 = "GWCHBUFINAMKZTQELPSJYROVXD"
#enc = substitution_encode(pt, a2)
#dec = substitution_decode(enc, a2)
#print(enc, dec)
#print(substitution_encode(input("Word: "), input("Substitution Alphabet: ")))
#print(substitution_decode(input("Word: "), input("Substitution Alphabet: ")))
pt = "'Don't stop believin'!' - Journey, 1981"
a2 = "GWCHBUFINAMKZTQELPSJYROVXD"
enc = substitution_encode(pt, a2)
dec = substitution_decode(enc, a2)
print(enc)
print(dec)
