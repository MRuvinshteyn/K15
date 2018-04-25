#Michael Ruvinshteyn
#SoftDev2 pd07
#K15 Do You Even List?
#2018 - 04 - 25

UC_letters = "QWERTYUIOPASDFGHJKLZXCVBNM" #uppercase letters
LC_letters = UC_letters.lower() #lowercase letters
nums = [str(x) for x in range(10)] #digits 0 through 9 -- put as strings to allow for easily searching for numbers in strings
specials = ".?!&#,;:-_*" #special characters

#returns whether inputted password meets minimal requirements:
#   at least one uppercase letter
#   at least one lowercase letter
#   at least one number
def minPass(p):
    return 1 in [1 if x in UC_letters else 0 for x in p] \
        and 1 in [1 if x in LC_letters else 0 for x in p] \
        and 1 in [1 if x in nums else 0 for x in p]

print "minPass(\"myNoobPass1234\"): " + str(minPass("myNoobPass1234"))
print "minPass(\"myNoobPass\"): " + str(minPass("myNoobPass"))
print ""

#returns password strength on a scale of 1 to 10 (integer) using the following criteria:
#   50% mix of upper- and lowercase letters
#   30% numbers
#   20% special characters
def passStrength(p):
    ret = 0.
    
    #judge composition of letters
    try:
        uppers = sum([1 if x in UC_letters else 0 for x in p])
        lowers = sum([1 if x in LC_letters else 0 for x in p])
        ret += 5. / (max(uppers,lowers) / min(uppers,lowers))
    except:
        print "no mix of upper and lowercase"
        
    #judge composition of numbers
    try:
        num = sum([1 if x in nums else 0 for x in p])
        ret += 3. / (num / (float(len(p)) * .3))
    except:
        print "no numbers"
        
    #judge composition of special characters
    try:
        spec = sum([1 if x in specials else 0 for x in p])
        ret += 2. / (spec / (float(len(p)) * .2))
    except:
        print "no special characters"
        
    return int(round(ret))

print "passStrength(\"myNoobPass1234\"): "
print passStrength("myNoobPass1234")
print ""
print "passStrength(\"aAbBcCdDeE543210;;;;\"): "
print passStrength("aAbBcCdDeE543210;;;;") #ideal password according to algo