while True:
    try:
        a = int(input("enter first num : "))
        b = int (input("enter second num : "))
        c = (input("enter your opedrator:"))

        if c == "+":
            print(a+b)

        elif c == "-" :
            print(a-b)

        elif c == "*":
            print(a*b)

        elif c == "/" :
            print(a/b)

        else :
            print("invalid")

    except:
        print("Please try again")