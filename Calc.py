operatorOptions = ["*","/","+","-"]

ops = "+"
digit1 = float()
digit2 = float()

while ops in operatorOptions and ops != "stop":

    digit1 = float(input("1st digit: "))

    digit2 = float(input("2nd digit: "))

    ops = input("operator (* / + - ): or type stop to quit. ")
    if ops == "*":
        total = digit1 * digit2
        print(round(total, 4))

    elif ops == "/":
        total = digit1 / digit2
        print(round(total, 4))

    elif ops == "-":
        total = digit1 - digit2
        print(round(total, 4))

    elif ops == "+":
        total = digit1 + digit2
        print(round(total, 4))


    else:
        print(f"{ops} is not a valid operator")

