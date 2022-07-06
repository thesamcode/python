
def integerList():
    for i in range(0, 151):
        print(i)

integerList()

def multipleFive():
    for i in range(5, 5001):
        if i%5 == 0:
            print(i)

multipleFive()

def dojoWay():
    for i in range(1, 101):
        if i%10 == 0:
            print('Coding Dojo')
        elif i%5 == 0:
            print('Coding')
        else:
            print(i)

dojoWay()
    

def hugeNum():
    sum1=0
    for i in range(0, 500001):
        if i%2 != 0:
            sum1 = i + sum1
    print(sum1)

hugeNum()

def countDown():
    for i in range(2018, 0, -4):
        print(i)

countDown()

def flexCount(lowNum, highNum, mult):
    for i in range(lowNum, highNum+1):
        if i%mult == 0:
            print(i)

flexCount(2,9,3)