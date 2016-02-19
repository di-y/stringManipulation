# hw3.py
# Dina Yerlan + dyerlan + section K

"""
Place your manually-graded materials here
1.a
First, using top-down design will make the code look more understandable
thus easier to debug
Second, top-down design allows programmer to concentrate on the big pictue of the problem
instead of being distracted by small parts of a big problem

1.b
It makes the code less understandable and hard to change. For example, if programmer wants to
change the code he/she will need to change all numbers. It can cause problems because
numbers usually dont stay same.

1.c
Excessive use of autograder is discouraged because it may lead to hardcoding and
students may become dependant on autograder.

1.d
c.upper().isupper()            (ord('A') <= ord(c) <= ord('a')+25)

(c in string.ascii_letters)    ('A' <= c <= 'Z')
(ord('A') <= ord(c) <= ord('a')+25) is similar to ('A' <= c <= 'Z')
c can be any char whose ord is between(65,122) for example ord("P")==80

2.
def f(s):
    for x in xrange(1,4): x takes values of 1,2,3
        spec = "%%0.%df" % x specifies the decimal to print
        print spec % float(s)ptints float 
        modificated float numbers 12.5,12.46,12.456
f("12.45645")

 
def g(s):
    result = ""
    for i in xrange(len(s)): i is inthe range of the lengh of strins s
        for j in xrange(i): j is in the range of i
            if (s[j] > s[i]): if the index of j is greater
                result += s[j] + s[i] it will create a new string that is the sum of j and i strings
    return result 
print g("aebdc")
eb
ebed
ebedec
ebedecdc
result "ebedecdc"
3.
def h(s, t):
    assert((len(t) == 2) and ("0" not in t) and (t[1] > t[0])) t should be "ab" or "12" or anything with two places
    count = 0 set the initial value of count as zero
    for r in s.split(","): s splitted with comma
        assert(r == t)  r should be equal to t
        count += 1 then add 1 to the previous count
    return (count == int(t[0]) + int(t[1])) return when count is equal to first number of t and second digit of t
For example s="12,12,12" and t="12" could return true

4.
import math
def largestNumber(text):
text= "I saw 3 dogs, 17 cats, and 14 cows!"
[int(text) for text in text.split() if text.isdigit()]
return max(int[text])

"""

######################################################################
# Place your solutions and test functions here!
######################################################################
def isPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = int(round(n**0.5))
    for factor in xrange(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def digitCount(n):
    n=abs(n)
    if n==0:
        return 1
    k=0
    s=0
    while (n>0):
        k=k+1
        n=n/10
    return k

def kthDigit(n, k):
    return (abs(n)/(10**k))%10

def replaceKthDigit(n, k, d):
    s=0
    for b in xrange (digitCount(n)):
        if b==k:
            continue 
        s= s+kthDigit(n,b)*10**b
    s=s+d*10**k
    return s

def isNearlyPalindromic(x):
  errorSum=0
  if (x < 2):
    return False
  for k in xrange(digitCount(x)):
    if kthDigit(x,k)!=kthDigit(x,digitCount(x)-k-1): 
      errorSum+=1
  if errorSum==2:
   return True
  else:
    return False

def nthNearlyPalindromicPrime (n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isPrime(guess)==True and isNearlyPalindromic(guess)==True:
            found += 1
    return guess

def testNthNearlyPalindromicPrime ():
    print "Testing nthNearlyPalindromicPrime()...",
    assert(nthNearlyPalindromicPrime(0) == 13)
    assert(nthNearlyPalindromicPrime (1) == 17)
    assert(nthNearlyPalindromicPrime (2) == 19)
    assert(nthNearlyPalindromicPrime (3) == 23)
    print "Passed!"

def isCarolPrime(k):
     return isPrime((2**k-1)**2-2)==True

def nthCarolPrime(n):
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if isCarolPrime(guess)==True:
            found += 1
    return (2**guess-1)**2-2

def testNthCarolPrime():
    print "Testing nthCarolPrime()...",
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime (1) == 47)
    assert(nthCarolPrime (2) == 223)
    assert(nthCarolPrime (3) == 3967)
    assert(nthCarolPrime (4) == 16127)
    print "Passed!"
    
def isKaprekarNumber(n):
    n=abs(n)
    if (n**2)/10**(digitCount(n**2)-(digitCount(n**2)/2))+(n**2)%10**(digitCount(n**2)-(digitCount(n**2)/2))==n:
     return True
    else:
     return False
    

def nearestKaprekarNumber(n):
    if type(n)!=int:
      round(n/1.0)
    uppercount=n
    lowercount=n
    if n==0:
        return 1
    if isKaprekarNumber(n)==True or n==1:
        return abs(n)
    while (isKaprekarNumber(n)!=n):
        lowercount-=1
        uppercount+=1
        if isKaprekarNumber(lowercount)==True and isKaprekarNumber(uppercount)==False:
                return lowercount
        if isKaprekarNumber(uppercount)==True and isKaprekarNumber(lowercount)==False:
                return uppercount
        if isKaprekarNumber(uppercount)==True and isKaprekarNumber(lowercount)==True:
            if (n-lowercount)<=(uppercount-n):
                return lowercount
            else:
                return uppercount
            
def testNearestKaprekarNumber():
    print "Testing nearestKaprekarNumber()...",
    assert(nearestKaprekarNumber(49) == 45)
    assert(nearestKaprekarNumber (51) == 55)
    assert(nearestKaprekarNumber (50) == 45)
    assert(nearestKaprekarNumber (100) == 99)
    assert(nearestKaprekarNumber (101) == 99)
    assert(nearestKaprekarNumber (13641234) == 13641364 )
    assert(nearestKaprekarNumber (1) == 1 )
    print "Passed!"

def patternedMessage(message, pattern):
    messagedPattern=0
    message1 = message.replace(" ","")
    result=""""""
    for i in xrange(len(pattern)):
        if (pattern[i] == "*"):
            result += message1[messagedPattern%len(message1)]
            messagedPattern += 1
        if (pattern[i] == " "):
            result +=" "
        if (pattern[i] == "'\n'"):
            result += "'\n'"
    return result
        
        
def testPatternedMessage():
    print "Testing patternedMessage()...",
    assert(patternedMessage("GoSteelers", "**********")== "GoSteelers")
    assert(patternedMessage("GoSteelers", "***********************")== "GoSteelersGoSteelersGoS")
    assert(patternedMessage("GoSteelers", "*******")== "GoSteel")
    assert(patternedMessage("GoSteelers", "**********")== "GoSteelers")
    assert(patternedMessage("Go Steel ers", "* *********")== "G oSteelers")
    print "Passed!"

def encrypt(plaintext, password):
    plaintext==plaintext.isdigit()
    
    return 

def testEncrypt():
    print "Testing encrypt()...",
    assert(False) # replace with your own tests!
    print "Passed!"

def decrypt(ciphertext, password):
    return 42

def testDecrypt():
    print "Testing decrypt()...",
    assert(False) # replace with your own tests!
    print "Passed!"

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def testAll():
    testNthNearlyPalindromicPrime()
    testNthCarolPrime()
    testNearestKaprekarNumber()
    testPatternedMessage()
    testEncrypt()
    testDecrypt()

def main():
    testAll()

if __name__ == "__main__":
    main()
