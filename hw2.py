# hw2.py


"""
   **1a. def drawCircle(canvas, x0, y0, x1, y1):
    width = x1 - x0
    canvas.create_oval(50, 100, 250, 200, fill=fill, width=4)
     1b. Anchor=SW means put the text on the southwest side
     1c. According to de Morgans law (not(f(x) or not(g(y)))==not(f(x) and g(y))
     1d
     def f(x):
    a = -x
    b = 0
    for a in xrange(x)
        b += g(a)
        a += 3
    return b**
    2.def f(x,y):
    m = 0
    for z in xrange(2,x,y):
        if (x%z == m): if the reminder is zero 
            print "A",
            m += 1, will print "A" ,1: it will print 0+1=1
        elif (y + z > x):
            print "B",
        print (z if (z%3 == 2) else "C"),10%3==1, it will print "C"
    print
f(12, 4)

def g():
    for x in xrange(-1,5,2):
       print x, ":", it will print:-1,1,3,5
       for y in xrange(x, -x, -2):
           print y,it will print: x,x-2,x-4,x-6.....-x+4,-x+2,-x
       print
g()
3
def f(x, y):
        assert((type(x) == int) and (type(y) == int))
        if ((x <= 50) or (y > 25)): z = , so x>50 and y<25 lets say x=70 and y=20
        elif (x%10 + y%10 > 0): z = 42 70%10+20%10=0 
        elif (x == y + 40): z = 10 70!=20+40
        else: z = 5 
        return (z == 2**5/3) therefore, x=70 and y=20 will return true
** def g(z):
    total = 0
    while (z > 0): lets say z=10, the cycle should repeat 5 times to give total =1+2+3+4+5
        for y in range(0,z,2): it will give 0,2,4,6,8,10
            total += 1 it will be 1
        z -= 2  z become 8, the cycle will repeat because z>0, everything now starts from 8
    return ((z == 0) and (total == 1+2+3+4+5)) z=10    **
**4.
def isPerfect(x):
factor=0
  for factor in xrange(1, abs(x)):
    if (x % factor == 0) and (abs(x)= factor+factor):#sum of all factors or abs(x)==sum(factor)
      return True
  return False**
"""

######################################################################
# Place your non-graphics solutions here!
######################################################################

def makeBoard(moves):
    s=0
    while (moves > 0):
        moves=moves-1
        s+=8*(10**moves)
    return s

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
    

def getLeftmostDigit(n):
    return n/(10**(digitCount(n)-1))

def clearLeftmostDigit(n):
    return replaceKthDigit(n,digitCount(n)-1,0)

def makeMove(board,k,d):
    k=digitCount(board)-k
    if (k>=digitCount(board) or k<0):
        return "offboard!"
    elif (d!=1 and d!=2):
        return "move must be 1 or 2!"
    elif (kthDigit(board,k)!=8):
        return "occupied!"
    else:
        return replaceKthDigit(board,k,d)

def isWin(board):
    for k in xrange(digitCount(board)):
        if(kthDigit(board,k)==2 and kthDigit(board,k+1)==1 and kthDigit(board,k+2)==1):
             return True
      
    return False

def isFull(board):
    for k in xrange(digitCount(board)):
        if(kthDigit(board,k)==8):
             return False
      
    return True

#def play112(game):
    #if digitCount(game)==1:
        #return makeBoard(game)
#for k in xrange(1,digitCount(clearLeftmostDigit(game)),2)
    #elif kthdigit(clearleftmostDigit(game),k)!=1 and kthdigit(clearleftmostDigit(game),k)!=2:
        #return makeBoard(game): 
        
 #for k in xrange(0,digitCount((clearLeftmostDigit(game)),2)
                #for b in xrange(1,digitCount((clearLeftmostDigit(game)),2)
                                #if kthDigit(clearLeftmostDigit(makeBoard(getLeftmostdigit(game))
  #if isFull(makeBoard(getLeftmostdigit(game)) is Flase
            
               
######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

######################################################################
# Place your graphics solutions here (BELOW the ignore_rest line!)
######################################################################

from Tkinter import *
import math

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def drawCircle(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        fill = "blue"
    else:
        fill = rgbString(147, 197, 114) # pistachio!
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=4)

def drawCircleGradient(canvas, x0, y0, x1, y1):
    width = x1 - x0
    if (width > 200):
        fill = rgbString(0,255,0)
    else:
        fill = rgbString(0,255,0) # pistachio!
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=4)
    
def drawLinePattern(canvas, left, top, right, bottom):
    width = x1 - x0
    if (width > 200):
        fill = "black"
    else:
        fill = "black"
    canvas.create_line(left+50, top, right, bottom, fill=fill, width=4)


def drawCrazyCubes(canvas, x0, y0, x1, y1):
    pass
            
def drawHexagonsBonus(canvas, x0, y0, x1, y1):
    pass

######################################################################
# Drivers: do not modify this code
######################################################################

def onButton(canvas, drawFn):
    canvas.data.drawFn = drawFn
    redrawAll(canvas)
    
def redrawAll(canvas):
    canvas.delete(ALL)
    canvas.create_rectangle(0,0,canvas.data.width,canvas.data.height,fill="cyan")
    drawFn = canvas.data.drawFn
    if (drawFn):
        canvas.create_rectangle(50, 50, 450, 450, width=4)
        drawFn(canvas, 50, 50, 450, 450)
        canvas.create_rectangle(500, 150, 700, 350, width=4)
        drawFn(canvas, 500, 150, 700, 350)
        canvas.create_text(canvas.data.width/2,20, text=drawFn.__name__, fill="black", font="Arial 24 bold")

def graphicsMain():
    root = Tk()
    canvas = Canvas(root, width=750, height=500)
    class Struct: pass
    canvas.data = Struct()
    canvas.data.width = 750
    canvas.data.height = 500
    buttonFrame = Frame(root)
    canvas.data.drawFns = [drawCircle, drawCircleGradient, drawLinePattern, drawCrazyCubes, drawHexagonsBonus]
    canvas.data.drawFn = canvas.data.drawFns[0]
    for i in xrange(len(canvas.data.drawFns)):
        drawFn = canvas.data.drawFns[i]
        b = Button(buttonFrame, text=drawFn.__name__, command=lambda drawFn=drawFn:onButton(canvas, drawFn))
        b.grid(row=0,column=i)
    canvas.pack()
    buttonFrame.pack()
    redrawAll(canvas)
    root.mainloop()

######################################################################
# Tests
######################################################################

def testMakeBoard():
    print "Testing makeBoard()...",
    assert(makeBoard(1) == 8)
    assert(makeBoard(2) == 88)
    assert(makeBoard(3) == 888)
    print "Passed!"

def testDigitCount():
    print "Testing digitCount()...",
    assert(digitCount(0) == 1)
    assert(digitCount(5) == digitCount(-5) == 1)
    assert(digitCount(42) == digitCount(-42) == 2)
    assert(digitCount(121) == digitCount(-121) == 3)
    print "Passed!"

def testKthDigit():
    print "Testing kthDigit()...",
    assert(kthDigit(789, 0) == kthDigit(-789, 0) == 9)
    assert(kthDigit(789, 1) == kthDigit(-789, 1) == 8)
    assert(kthDigit(789, 2) == kthDigit(-789, 2) == 7)
    assert(kthDigit(789, 3) == kthDigit(-789, 3) == 0)
    assert(kthDigit(789, 4) == kthDigit(-789, 4) == 0)
    print "Passed!"

def testReplaceKthDigit():
    print "Testing replaceKthDigit()...",
    assert(replaceKthDigit(789, 0, 6) == 786)
    assert(replaceKthDigit(789, 1, 6) == 769)
    assert(replaceKthDigit(789, 2, 6) == 689)
    assert(replaceKthDigit(789, 3, 6) == 6789)
    assert(replaceKthDigit(789, 4, 6) == 60789)
    print "Passed!"

def testGetLeftmostDigit():
    print "Testing getLeftmostDigit()...",
    assert(getLeftmostDigit(7089) == 7)
    assert(getLeftmostDigit(89) == 8)
    assert(getLeftmostDigit(9) == 9)
    assert(getLeftmostDigit(0) == 0)
    print "Passed!"

def testClearLeftmostDigit():
    print "Testing clearLeftmostDigit()...",
    assert(clearLeftmostDigit(60789) == 789)
    assert(clearLeftmostDigit(789) == 89)
    assert(clearLeftmostDigit(89) == 9)
    assert(clearLeftmostDigit(9) == 0)
    assert(clearLeftmostDigit(0) == 0)
    print "Passed!"

def testMakeMove():
    print "Testing makeMove()...",
    assert(makeMove(8, 1, 1) == 1)
    assert(makeMove(888888, 1, 1) == 188888)
    assert(makeMove(888888, 2, 1) == 818888)
    assert(makeMove(888888, 5, 2) == 888828)
    assert(makeMove(888888, 6, 2) == 888882)
    assert(makeMove(888888, 6, 3) == "move must be 1 or 2!")
    assert(makeMove(888888, 7, 1) == "offboard!")
    assert(makeMove(888881, 6, 1) == "occupied!")
    print "Passed!"

def testIsWin():
    print "Testing isWin()...",
    assert(isWin(888888) == False)
    assert(isWin(112888) == True)
    assert(isWin(811288) == True)
    assert(isWin(888112) == True)
    assert(isWin(211222) == True)
    assert(isWin(212212) == False)
    print "Passed!"

def testIsFull():
    print "Testing isFull()...",
    assert(isFull(888888) == False)
    assert(isFull(121888) == False)
    assert(isFull(812188) == False)
    assert(isFull(888121) == False)
    assert(isFull(212122) == True)
    assert(isFull(212212) == True)
    print "Passed!"

def testPlay112():
    print "Testing play112()...",
    assert(play112( 5 ) == "88888: Unfinished!")
    assert(play112( 521 ) == "81888: Unfinished!")
    assert(play112( 52112 ) == "21888: Unfinished!")
    assert(play112( 5211231 ) == "21188: Unfinished!")
    assert(play112( 521123142 ) == "21128: Player 2 wins!")
    assert(play112( 521123151 ) == "21181: Unfinished!")
    assert(play112( 52112315142 ) == "21121: Player 1 wins!")
    assert(play112( 523 ) == "88888: Player 1: move must be 1 or 2!")
    assert(play112( 51223 ) == "28888: Player 2: move must be 1 or 2!")
    assert(play112( 51211 ) == "28888: Player 2: occupied!")
    assert(play112( 5122221 ) == "22888: Player 1: occupied!")
    assert(play112( 51261 ) == "28888: Player 2: offboard!")
    assert(play112( 51122324152 ) == "12212: Tie!")
    print "Passed!"

def testAll():
    testMakeBoard()
    testDigitCount()
    testKthDigit()
    testReplaceKthDigit()
    testGetLeftmostDigit()
    testClearLeftmostDigit()
    testMakeMove()
    testIsWin()
    testIsFull()
    testPlay112()

######################################################################
# Main: you may modify this to run just the parts you want to test
######################################################################

def main():
    graphicsMain()
    testAll()

if __name__ == "__main__":
    main()
