UC_letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
LC_letters = UC_letters.lower()
nums = [str(x) for x in range(10)]
specials = ".?!&#,;:-_*"

def minPass(p):
    return 1 in [1 if x in UC_letters else 0 for x in p] \
        and 1 in [1 if x in LC_letters else 0 for x in p] \
        and 1 in [1 if x in nums else 0 for x in p]

print minPass("myNoobPass1234")