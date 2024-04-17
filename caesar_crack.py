def decrypt_letter(letter, shift):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if letter not in alpha and letter not in alpha.lower():
        return letter
    index = alpha.index(letter.upper())
    new = index-shift
    if letter not in alpha:
        return alpha[new].lower()
    return alpha[new]

def decrypt(word,shift):
    string = ""
    for n in word:
        string += decrypt_letter(n,shift)
    return string

def caesar_crack(word):
    eta = [0] * 3
    shift = 1
    best = "."
    for i in range(1,26):
        test = decrypt(word,i)
        new = eta_count(test)
        if sum(new) > sum(eta):
            eta = new
            shift = i
            best = test
    return best

def eta_count(word):
    return [word.count("E") + word.count("e"),word.count("T")+word.count("t"),word.count("a")+word.count("A")]

enc1 = "iodj{brx_fdph_vdz_dqg_frqtxhuhg}"
print(caesar_crack(enc1))
enc2 = "'Pgpcjmzoj dszfwo wplcy ez aczrclx l nzxafepc, mpnlfdp te eplnspd jzf szh ez estyv' - Depgp Uzmd, qzcxpc NPZ lyo ncplezc zq Laawp"
print(caesar_crack(enc2))
enc3 = "'Max Bgmxkgxm? Px tkx ghm bgmxkxlmxw bg bm.' - Ubee Ztmxl, yhngwxk hy Fbvkhlhym, 1993"
print(caesar_crack(enc3))
enc4 = "Dszce lyo dhppe"
print(caesar_crack(enc4))
