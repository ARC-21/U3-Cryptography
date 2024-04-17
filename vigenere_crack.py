alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751, .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]
eng_freq_squared = []
for freq in eng_freq:
    eng_freq_squared.append(freq * freq)
engIoC = sum(eng_freq_squared)

def i_of_c(text):
    ioc = 0
    for letter in alpha:
        ioc += (text.count(letter)/len(text) * (text.count(letter)-1)/(len(text)-1))
    return ioc

def friedman_test(text):
    ioc = i_of_c(text)
    return len(text)*(engIoC-(1/26))/(ioc*(len(text)-1)+engIoC-len(text)*(1/26))

def gcd_of_list(int_list):
    gcd = 1
    is_div = True
    for i in range(2,min(int_list)+1):
        #print("i is " + str(i))
        for num in int_list:
            #print("num is " + str(num))
            if num % i != 0:
                #print("failed i is " + str(i))
                is_div = False
                break
        if is_div:
            gcd = i
            #print("successful i is " + str(i))
        is_div = True
    return gcd

def find_plausible_gcd(int_list, minimum, gcd):
    #print(int_list)
    if gcd > 1:
        return gcd
    else:
        if minimum == 1:
            minimum += 1
        #print("now it's " + str(int_list))
        new, repeats = get_repeats(int_list)
        for i in range(len(new)):
            if repeats[i] < minimum:
                int_list = remove_all_occurrences(int_list, new[i])
        #print("now again it's " + str(int_list))
        return find_plausible_gcd(int_list, minimum+1, gcd_of_list(int_list))

def get_repeats(int_list):
    new = []
    repeats = []
    for n in int_list:
        if n not in new:
            #print(str(n) + " is not a repeat")
            new.append(n)
            repeats.append(1)
        else:
            #print(str(n) + " is a repeat")
            repeats[new.index(n)] += 1
    return new, repeats
        
def remove_all_occurrences(int_list, num):
    while num in int_list:
        int_list.remove(num)
    return int_list

def kasiski_test(text):
    tgs = []
    distances = []
    for i in range(0,len(text)-2):
        #print("text[i-3:i] is " + text[i-3:i])
        if text[i:i+3] in tgs:
            #print("                                       match")
            #pos = text.index(text[i:i+3])
            #distances.append(text.index(text[i:i+3],pos + 1) - pos)
            pos = text.index(text[i:i + 3], i)
            previous_pos = text.index(text[i:i + 3])
            distances.append(pos - previous_pos)

            #print("match is " + str(text[i:i+3]))
            #print("pos is " + str(pos))
            #print("2nd pos is " + str(text.index(text[i:i+3],pos + 1)))
            #print("distance is " + str(text.index(text[i:i+3], pos+1) - pos))
        else:
            #print("not match")- - - -
            tgs.append(text[i:i+3])
    #print("distances are " + str(distances))
    return find_plausible_gcd(distances,1,gcd_of_list(distances))

def make_cosets(text, n):
    cosets = [""]*n
    for i in range(n):
        cosets[i] += text[i:len(text):n]
    return cosets

def find_total_difference(l1,l2):
    differences = []
    for i in range(26):
        differences.append(abs(l1[i]-l2[i]))
        #print("difference is " + str(differences[i]))
    return sum(differences)

def find_likely_letter(coset):
    coset_freqs = []
    differences = []
    for i in range(26):
        coset_freqs.append(coset.count(alpha[i])/len(coset))
    for i in range(26):
        differences.append(find_total_difference(coset_freqs, eng_freq))
        coset_freqs.append(coset_freqs[0])
        del coset_freqs[0]
        #print("len is " + str(len(coset_freqs)))
    #print("min is " + str(min(differences)))
    return alpha[differences.index(min(differences))]
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

def crack(text):
    user_len = ""
    while 2 > 1:
        print("Friedman Test Result: " + str(friedman_test(text)))
        print("Kasiski Test Result: " + str(kasiski_test(text)))
        user_len = input("Enter the keyword length you'd like to try (enter 'quit' to forfeit): ")
        if user_len == "quit":
            break
        user_len = int(user_len)
        cosets = make_cosets(text, user_len)
        print("Likely letters:")
        for coset in cosets:
            print("    -" + find_likely_letter(coset))
        kw = input("Enter the keyword you'd like to try: ")
        print("Result: " + vigenere_decode(text, kw))
        print("______________________________________")

example = "UZRZEGNJENVLISEXRHLYPYEGTESBJHJCSBPTGDYFXXBHEEIFTCCHVRKPNHWXPCTUQTGDJHTBIPRFEMJCNHVTCFSAIIJENREGSALHXHWZWRZXGTTVWGDHTEYXISAGQTCJPRSIAPTUMGZALHXHHSOHPWCZLBRZTCBRGHCDIQIKTOAAEFTOPYEGTENRAIALNRXLPCEPYKGPNGPRQPIAKWXDCBZXGPDNRWXEIFZXGJLVOXAJTUEMBLNLQHGPWVPEQPIAXATYENVYJEUEI"
crack(example)
c1 = "RVCQWMYFULRIKPFMQEMTJJOCLHYVHNFONGOGUFCRWHEPYAOOQSQCBYCRGMFYRSMRQUQSMYBXGKULHCRHIZSMSTZGQCCBNJMFMBARVURHBGGQFCFCHBGBAUCLIGQGHBMINPSFWWHECHPOHBCGAVULQYRCJPCXSQYECIBRCQHLGPORWILGQGHBQAUJZVGHMMTNCLNGHNPIFWBYCRMRCVCEOGHYJCHEWHMHBCFYYFFGSLRSMRGGWDFYWHRSRRKUQHIMGBMFNYBXGHGYRYZCNFTLGSXKOHYBXIOMGGEGTLCOEMINYBXEWPCHYPFCZZYYBMUSLQ"
c2 = "EFMREXHTGRQQVDODIPQSIVVNURSUVVNGNXRRIOIBEPOZNISWDRIOEOWVVYAVVIDFJFTYQDPFRKQMQCCFQBQXNRTKYRRHRCQWTXVZNIZVRDCEODSHZVCWDEENVCQWTXVVRRBSJTRMUZVRIIAOWMQIZNXYPYGJAEDMYKKIGCWXEYAUKRDNPSKCHHXVLQZMQILNFOVVVRNFSRJIVNGBEWKEGCVKRTZTJWWYGIIHSGDVZOPYJUGHUKBIPGETUYJDNXOTSXKOJIPMPXFZNIDLHKICQBVHEKNGCWDPURGCSXTTEUMSQULMRDMRPRNFSQSNVMGXXDVZOPMSPOFNNIVHHVRTOHWQRSEYHLPXOHKPJQIIVRQVKEAVKVJGKPTYKUCDMKXKOCEGWKKHUFUTMIFQUEKCAUKKTGXMQQEEQBQRTVPTYKUCDMKXKOCEGWKKHUKHGZYURFSGYJSTFGTKQPKEGKCXRHZNFKWHSLEPMIRHZNUDVXEKIQXWWJRTYSPOCLTQWEWGGETPSUOZNIKWSGTIHSGWCJKQBWRNMIPQEJKMEPZVRDCEODLHRIOEOWVQWPTYKUCDMKXKWJLSQPXHPIESEMUGJEZZIUVZSGSRPCEYFSJIGIEPDWXDAEEDWLPTLWNMQIBNQGPHFXEQPXKGRPRVMFCKIQXHRORIPCTHEZANSDHFRLIYVLVYMUKRGHFROKPOQXIEBIOCKEFDEVMJIPMPXFVTGCXLPXDGLYJIZNIKRGORIPDELPZNIDLHUFUTMIFQUEKWTOGDEPDEWKFNQPXKGSUKVHVAJTGWEQFDAPKKHOVNVYJGGIIXOHDTKIHKGWUJUEREVORCJSRHEFDGYJFQDPWDIURIOIBEPUKHGCIPKXHVLIFQESKNIUGUPCBXRHKHGZVRIIAOWMQIGRQMIVUSUVYJWGETJOXHTDSQPXZCIEFOZHNFPOORWKJUUOHIQITJSWOCIGGBTUQTEUCALVYTJOXHTDPTYKUCDMKXKLOGLGWIQVRTKYRRTTOFSRJTVSGBZHFWOTDLHCTTWKPZTZTKXKRHJOWBGHEFDGCSIVNATOIQIZNGOVLPXCQWFLPVSGXKLPVETSRJVVCJXMTWVSYSXKUFFVGEUGUEXOPRRDEPDTUCTTKMIV"
c3 = "OPKLNPCAVGYQRPKSAJUMYIUGVJHETIRRYWRHEEXQVBYEGSEIZVJSSMKEXWRSHVVHKWYXRVKSJTGVTIWSMQTHBSIHDAVPNCYEYJKIAXRGFMJXBXYIRIRPVXUIKQIXRHJMHXRCNRVRJZSSHWWEXMSSEIKLVVGQRXIIRQJIGLVJVKKSSEDEIWLEOSLXAWXXLJZZZEOXUEYIVDEFYETOHWAWGETLZITHEYXKZLRCUEEHNWSISIRXPZKWJMEWOWTQNHVJJZZLRWKEDZYMGARWIWAWRXICDVMXUICMABKZRRRXOPKFRWKSABOQRWZXRIYWRPUSHEUVXMEKVVJEGTIINMTXGLVIGMIXEMTGPZXIAXNENKAXBJWHPZORTHRCGQMLGLFYMAOXJEJTVZZSSXYIZKURBQPHMQBIVRGVZXGVNXZSINUVUEKIRMKOGLVJGIZANWJIQMTJYMXLOAATNRUADVYXBRNLJEGWGLZVOGTMAIRRYPGHNZRVDKUWRYCGZZGFBZVLDAXMTLKEISRIJIEXNTUAYCIINBORTWVZZZGPGMDINWTXUINETWTINGYPVVJMAKFTKWYMGIKLZTOJGWYEABZLRTFWOMXAVXYXCMKRBVDSPALEPIXEUMJJESDXCMCEYPZXRIYSAIFJOPUWRTZGOCXIFAYMXPGVRWFGJVZVVZVHOPGXGLVITMYJBPCSRGUYNFFYOENIACFYHWBIOMXFMWZLRVZWRIZGUMEKTWAXUITEKBOSAFVRZIZLVXIEI"
crack(c1)
crack(c2)
crack(c3)

