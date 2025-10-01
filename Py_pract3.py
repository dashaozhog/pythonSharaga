from random import randint

def zad1():
    n = int(input("input n: "))
    m = int(input("input m: "))
    sum = 0
    for i in range(n,m):
        sum+=i
        print(f"+{i} = {sum}")

def zad2():
    n = int(input("input n: "))
    fact = 1
    for i in range(1, n+1):
        fact*=i
        print(f"*{i} = {fact}")
    print(fact)

def zad3():
    n = int(input("enter n: "))
    chisla = [2,3,5,7]
    if n in chisla:
        return 'prostoe!'
    else:
        for i in chisla:
            if n%i == 0:
                return 'neprostoe..'
            else:
                continue
        return 'prostoe!'

def zad4():
    n = int(input("enter n: "))
    i = 0
    j = 0
    while i<n:
        i+=1
        while j<n:
            j+= 1
            print(f"{i}*{j}={i*j}")
        j = 0
        print()

def zad5():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    c = int(input("enter c: "))
    d = b**2-4*a*c
    if d>=0:
        x1 = (0-b - math.sqrt(d))/2*a
        x2 = (0-b + math.sqrt(d))/2*a
        print("Discriminant:", d, "\n x1=", x1, "     x2=", x2 )
    else:
        print("fuckoff")

def zad6():
    inp = input("enter string ")
    if inp == inp[::-1]:
        print(True)
    else:
        print(False)

def zad7():
    num = randint(1,100)
    guess = int(input("guess the number! "))
    while guess!=num:
        if guess>num:
            print("!SMALLER!")
        else:
            print("!BIGGER!")
        guess = int(input("guess the number! "))
    print("HELL YEEEAHHHH")

def zad8():
     enter = input("enter numbers(separate with space)")
     nums = enter.split(" ")
     print(f"minimal: {min(nums)}\nmaximal: {max(nums)}")


def zad9():
    n = int(input("enter n: "))
    fibon = [0,1]
    print(0)
    print(1)
    for i in range(1,n-1):
        fibon.append(fibon[i]+fibon[i-1])
        print(fibon[i+1])

zad9()
