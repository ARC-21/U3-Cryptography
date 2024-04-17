def vigenere_encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_word  = ""
    cipher = ""
    while len(key_word) < len(message):
        key_word += key
    for i in range(len(message)):
        new = alpha.index(message[i]) + alpha.index(key_word[i])
        if new > 25:
            new -= 26
        cipher += alpha[new]
    return cipher

def vigenere_decode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_word  = ""
    cipher = ""
    while len(key_word) < len(message):
        key_word += key
    for i in range(len(message)):
        new = alpha.index(message[i]) - alpha.index(key_word[i])
        if new < 0:
            new += 26
        cipher += alpha[new]
    return cipher

pt = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
key = "TEST"
ct = vigenere_encode(pt, key)
dt = vigenere_decode(ct, key)
print(ct, dt)

pt = "SPHINXOFBLACKQUARTZJUDGEMYVOW"
key = "KEYWORD"
ct = vigenere_encode(pt, key)
dt = vigenere_decode(ct, key)
print(ct, dt)

text = "IFNJVRZLLDXZUESLXNUIKHH"
key = "GRADER"
dt = vigenere_decode(text,key)
print(dt)
