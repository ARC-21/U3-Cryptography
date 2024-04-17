def swap(enc_text, first, second):
    new = ""
    #print(enc_text)
    #print(len(enc_text))
    for i in range(len(enc_text)):
        #print(i)
        if enc_text[i] == first:
            new += second
        elif enc_text[i] == first.lower():
            new += second.lower()
        elif enc_text[i] == second:
            new += first
        elif enc_text[i] == second.lower():
            new += first.lower()
        else:
            new += enc_text[i]
    return new

def letter_freqs(word):
    print("Letter frequencies:")
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in alpha:
        print(char + ": " + str(word.count(char)+word.count(char.lower())))
    print("Remember, the most common letters in English are usually ETAOINSHRDLU in that order.")
    print()

enc_text = "AAaaBBbbCCcc"
while enc_text != "quit":
    print("Current text: ", enc_text)
    user_text = input("Type a pair of letters to swap, for example AB would swap A and B, or type 'quit': ")
    if user_text == "quit":
        break
    enc_text = swap(enc_text, user_text[0], user_text[1])
    letter_freqs(enc_text)
