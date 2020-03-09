print("Please input a positive integer:")
firstnum = int(input())
while firstnum != 1:
    if firstnum % 2 == 0:
        firstnum = firstnum / 2
        print(firstnum)
    else:
        firstnum = (firstnum * 3) + 1
        print(firstnum)