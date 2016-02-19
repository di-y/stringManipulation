# hw1.py
# Dina Yerlan + dyerlan + section K

######################################################################
# Place your non-autograded solutions below here!
######################################################################
#
# 1a.Lets say A=1010
#          and B=1001
# De Morgans Law says that A and B == not ((not A) or (not B))
# A and B will be 1000, notA=0101 not B=0110
# notA or notB==0111
# not(notA or notB)==1000
# 1000==1000. proved
# 1b. For example, 5 and True, the "5" here is actually a truthy value
# and if we put expression. So, x is any expression that will be true if it was truthy and actually
# false in the case it was falsy expression
# 1c. The floating point number for which x%1==0 should be integer.For example, 5.0%1=0.0==0
# 1d. One example of such expression could be "+", we can use plus to calculate numbers or
#we can use it for operations such as hello+ word and it will show helloworld.
#another example could be "==" sign which could be used to find the sum or just a result of opertions
#of numbers and "=="can also be used to equate not numbers like true==false
#####################
#2.
#def f(x): return (x**2)/(x%7)
#def g(x): return x-1 
#def h(x, y): return (f(g(x)) % g(f(y)))
#print h(9, 13)
#g(9)=8, f(8)=64
#f(y)=28 g(28)=27
#h(9.13)=10
#####################
#def f(x, y):
    #print "f",      # don't miss this print statement!
    #return (x > y)  it will return (1.0)
#def g(x, y):
    #print "g",      # ditto
    #return (x > 2*y)  it will return (-1,-2)
#def h(x, y):
    #print "h",      # ditto
    #return x*y       it will return 0,0,2 and 6
 
#print f(1, 0) and g(-1,-2) and f(3,4) and g(5,6)
#print h(-1, 0) or h(0, 1) or h(1, 2) or h(2, 3)
#####################
#3.
#def f(x,y):
    #return ((type(x) == type(y) == int) and
            #(100 > x > y > 0) and
            #(x/10 + x%10 + y/10 + y%10 < 5) and
            #(x % 10 == y % 10) and
            #(x == y * 3))
 #lets assume that y=10, than x would be 30
 #30/10+0+10/10+0=4<5
 #x%10=y%10=0, x=30 y=10 satisfies all requirements
############################################
# Reasoning Over Code  (continued).  
#def g(x, y):
    #return x - x/y*y  # hint: what is this doing in general?

#def h(x, y):
    #return ((type(x) == type(y) == int) and
            #(40 > x > 30) and (13 > y > 10) and  # hint: notice unusual bounds here
            #(g(x, y) == 5))
#we are given that x-(x/y)*y equals to 5, this means x cannot be the multiplier of y
#because it that case the result will be zero.
#therefore we can cross out options 33,36
#as it can be seen from the bounds, x/y will give 3
#therefore we can plug in 38 and 38-3*11=5
#the answer is x=38, y=11
############################################
#4. import math
#def quad(a,b,c):
    #return max((-b + math.sqrt(b**2 - 4*a*c)) / (2 * a),(-b - math.sqrt(b**2 - 4*a*c)) / (2 * a)) or 0
#print(quad(1,5,3))
############################################
#Bonus/Optional  [1 pt each]

#a.       If x and y are integers where ((x%y == y%x) and (x != y)) is True, what must be true about x and y?
#one of the values must be 1, so 1mod2=0 and 2mod1=0
#b.  What will this print?
#def r(x, y): return (x*y == 0)*1 or x+r(r(x/3,y/4),x/5)
#print r(5,3)
#this will not return anything, the function r is not defined
############################################

#def f1(x, y):
    #assert(type(x) == type(y) == int)
    #z = 10+x*y
    # note: almostEqual is as defined in the class notes
    #return (100>x>y>0) and (x-y<10) and almostEqual(z%(z-5),z**0.5)
# logically z is larger than 100 for any values, this means z%(z-5) always gives 5,
# then our goal is to find the number that is close to the square of 5==25,
# so x*y must be close to 15, as x-y<10 than the only value could be x=1 y=10
#which is 5=square root 21, it is not very precise but close.
#def f2(x):
    #return ((type(x) != type(int(x))) and
            #((x % 1)**2 == int(x % 1)) and
            #(100 > x**2 > 8*x > 0))
#for example lets take 10.000001 (10.000001%1)**2 is nearly 0
#and (10.000001)**2> 10.000001*8. Therefore, the 10.000001 will work
#def f3(x, y):
    #return (100>x>y>0) and (x+y == 10) and (y/x == x/y - 1)
#we mightconsider(9,1), (8,2)(7,3)....
#y/x is always 0, so we should find the values that will make x/y ==1,
#this value is (6,4) 4/6=6/4-1.proved.
#def f4(x, y):
    #return ((100>x>y>0) and (x+x**y == 100))
# the simplest way is to plug in y=1, so x should be 50,
# 50+50**1==10. Answer:x=50,y=1.

#def f5(x, y):
    #return ((100>x>y>0) and
            #(x+y == 16) and
            #(round(float(x/y)) != round(float(x)/y)))
#for example, it could be (13.6,12.4) ,float(x) will round 13.6 to 14 and the result on
#each side will turn out different
#we consider only (15,1), (14,2) and so on.
#def f6(x):
    #assert ((type(x) == int) and
            #(1000 > x > 0))
    #y = x%10*100 + x/10%10*10 + x/100
    #return ((x == y) and
            #(int(x**0.5) == 11) and
            #(x / 125) > (x / 135))
# it might be assumed that x=121 but it does not satisfy the last part,
#so we might assume that x=131 
 ######################################################################
# Place your autograde solutions below here
######################################################################

def kthDigit(x, k):
    return (abs(x)/(10**k))%10

def numberOfPoolBalls(x):
    return x*(1+x)/2

def numberOfPoolBallRows(x):
    return ceiling(float((-1+(1+8*x)**0.5)/2.0))
def ceiling(n):
    return int(n) + (n % 1 > 0)

def isEvenPositiveInt(x):
    return type(x)==int and x>0 and x%2==0
    
def isPerfectCube(x):
    return x==0 or int(round(((abs(x)**(1.0/3.0))))**3)==abs(x)

def isTriangular(x):
    return type(x)==int and x>=0 and ((-1+(1+8*x)**0.5)/2.0)%1==0

def fabricYards(inches):
    return ceiling(inches/36+((inches%36)/36.0)) 
def ceiling(n):
    return int(n) + (n % 1 > 0)

def fabricExcess(inches):
     return ((36-(inches%36)+36))%36

def nearestBusStop(x):
    return (x+3)/8*8

def areCollinear(x1, y1, x2, y2, x3, y3):
    return (x2-x1)==(x3-x1)==(x3-x2)==0 or (x2-x1)!=0 and(x3-x1)!=0 and (x3-x2)!=0 and(y2-y1)/(x2-x1)==(y3-y1)/(x3-x1)and (y3-y1)/(x3-x1)==(y3-y2)/(x3-x2)
######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testKthDigit():
    print "Testing kthDigit()...",
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-789, 0) == 9)
    print "Passed!"

def testNumberOfPoolBalls():
    print "Testing numberOfPoolBalls()...",
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 1+2)
    assert(numberOfPoolBalls(3) == 1+2+3)
    assert(numberOfPoolBalls(10) == 55)
    print "Passed!"

def testNumberOfPoolBallRows():
    print "Testing numberOfPoolBallRows()...",
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(54) == 10)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print "Passed!"
 
def testIsEvenPositiveInt():
    print "Testing isEvenPositiveInt()...",
    assert(isEvenPositiveInt(2) == True)
    assert(isEvenPositiveInt(2040608) == True)
    assert(isEvenPositiveInt(21) == False)
    assert(isEvenPositiveInt(20406081) == False)
    assert(isEvenPositiveInt(0) == False)
    assert(isEvenPositiveInt(-2) == False)
    assert(isEvenPositiveInt(-2040608) == False)
    assert(isEvenPositiveInt("Go Steelers!") == False)
    assert(isEvenPositiveInt(1.23456) == False)
    assert(isEvenPositiveInt(True) == False)
    print "Passed!"
 
def testIsPerfectCube():
    print "Testing isPerfectCube()...",
    assert(isPerfectCube(0) == True)
    assert(isPerfectCube(1) == True)
    assert(isPerfectCube(-1) == True)
    assert(isPerfectCube(8) == True)
    assert(isPerfectCube(-8) == True)
    assert(isPerfectCube(27) == True)
    assert(isPerfectCube(-27) == True)
    assert(isPerfectCube(16) == False)
    assert(isPerfectCube(-16) == False)
    print "Passed!"
 
def testIsTriangular():
    print "Testing isTriangular()...",
    assert(isTriangular(0) == True)
    assert(isTriangular(1) == True)
    assert(isTriangular(2) == False)
    assert(isTriangular(3) == True)
    assert(isTriangular(4) == False)
    assert(isTriangular(5) == False)
    assert(isTriangular(6) == True)
    assert(isTriangular(54) == False)
    assert(isTriangular(55) == True)
    assert(isTriangular(56) == False)
    assert(isTriangular(-1) == False)
    print "Passed!"
 
def testFabricYards():
    print "Testing fabricYards... ",
    assert(fabricYards(0) == 0)
    assert(fabricYards(1) == 1)
    assert(fabricYards(35) == 1)
    assert(fabricYards(36) == 1)
    assert(fabricYards(37) == 2)
    assert(fabricYards(72) == 2)
    assert(fabricYards(73) == 3)
    assert(fabricYards(108) == 3)
    assert(fabricYards(109) == 4)
    print "Passed all tests!"
 
def testFabricExcess():
    print "Testing fabricExcess... ",
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    assert(fabricExcess(72) == 0)
    assert(fabricExcess(73) == 35)
    assert(fabricExcess(108) == 0)
    assert(fabricExcess(109) == 35)
    print "Passed all tests!"

def testNearestBusStop():
    print "Testing nearestBusStop()...",
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print "Passed all tests!"
 
def testAreCollinear():
    print "Testing areCollinear()...",
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    print "Passed all tests!"

def testAll():
    testKthDigit()
    testNumberOfPoolBalls()
    testNumberOfPoolBallRows()
    testIsEvenPositiveInt()
    testIsPerfectCube()
    testIsTriangular()
    testFabricYards()
    testFabricExcess()
    testNearestBusStop()
    testAreCollinear()

if __name__ == "__main__":
    testAll()
 
