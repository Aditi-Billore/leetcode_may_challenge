def main():
    btree = [1,2,3,None,4]
    x = 2
    y = 3

    num1 = btree.index(x)
    num2 = btree.index(y)

    level1 = 0
    level2 = 0

    parent1 = (num1 -2)//2 if num1 %2 == 0 else (num1 - 1)//2
    parent2 = (num2 -2)//2 if num2 %2 == 0 else (num2 - 1)//2

    temp = num1
    while temp != 0:
        temp = (temp -2)//2 if temp %2 == 0 else (temp - 1)//2
        level1 += 1


    temp = num2
    while temp != 0:
        temp = (temp -2)//2 if temp %2 == 0 else (temp - 1)//2
        level2 += 1

    print(True) if (level1 == level2) and (parent1 != parent2) else print(False)



if __name__ == "__main__":
    main()
