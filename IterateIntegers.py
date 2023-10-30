for numbers in range (1,51):
    if numbers %3== 0 and numbers %5 == 0:
        print(f"{numbers} is divisble by both 3 and 5!")
    elif numbers %3 == 0:
        print(f"{numbers} is divisble by 3")
    elif numbers %5 == 0:
        print(f"{numbers} Is divisble by 5")
    else:
        print (numbers)