import math

def zad1():
    enter = input("enter 3 numbers(separate with ,)")
    nums = enter.split(",")
    suma = 0
    mult = 1
    mid = 0
    diff = abs(int(nums[0])-int(nums[1]))
    for n in nums:
        mult*=int(n)
        suma+=int(n)
    mid = suma/len(nums)
    print("sum:", suma, "\nmultiplication:", mult, "\nmid:", mid, "\ndifference module:", diff )


def zad2():
    enter = int(input("enter number"))
    if enter %2 == 0:
        print('PARNOE')
    else:
        print('NEPARNOE')


def zad3():
    x = float(input("enter x "))
    y = float(input("enter y "))
    a = 0
    b = 0

    formula = (x-a)**2 + (y-b)**2
    if formula <= 1:
        print("YES")
    else:
        print("NO")

    dist = math.sqrt((x - a)**2 + (y - b)**2)
    print(dist)

def zad4():
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


def zad5():
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    lst = [a,b]
    if a!=b:
        print(max(lst), "більше, ніж", min(lst), "на", abs(a-b))


def zad6():
    inp = input("enter string ")
    if inp == inp[::-1]:
        print(True)
    else:
        print(False)


def zad7():
    num = int(input("enter n: "))
    i=0
    j=0
    for i in range(1, num+1):
         for j in range(1, num+1):
             print(f"{i} * {j} = {i * j}")
         print("\n")

zad7()
