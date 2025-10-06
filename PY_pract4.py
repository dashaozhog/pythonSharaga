import random

def task1():
    array = []
    sum = 0
    dob = 1
    for i in range(1, 11):
        array.append(i)
        sum+=i
        dob*=i
        print(i)
    print(sum)
    print(dob)
def task2():
    enter = input("fill in array(space separation)")
    ent_list = enter.split(" ")
    array = [[],[],[]]
    for i in range(0,3):
        sum = 0
        while len(array[i])<3:
            array[i].append(int(ent_list[0]))
            sum+=int(ent_list[0])
            ent_list.pop(0)
        print(f"row {i+1} sum =", sum)
    print(array)

def task3():
    num = int(input("enter array length: "))
    array = []
    for i in range(0,num):
        array.append(random.randint(1,100))
    print(array)
    print(f"Max: {max(array)}\nMin: {min(array)}")
def task4():
    enter = input("fill in the array(separate with space): ")
    enter_list = enter.split(" ")
    array = [[[0,0],[0,0]],[[0,0],[0,0]]]
    i = 0
    suma = 0
    ind = 0
    while i<=1:
        j = 0
        while j <=1 :
            k = 0
            while k <=1:
                array[i][j][k] = int(enter_list[0])
                suma+=int(enter_list[0])
                if int(enter_list[0]) >10:
                    print(f"element {enter_list[0]}[{ind}] is more than 10")
                enter_list.pop(0)
                k+=1
                ind+=1
            j+=1
        i+=1
    print(array)
def task5():
    ent1 = input("enter array 1(separate with space)")
    ent2 = input("enter array 2(separate with space)")
    array1 = ent1.split(" ")
    array2 = ent2.split(" ")
    common = []
    for i in array1:
        if i in array2:
            common.append(i)
            print(i)

task5()


