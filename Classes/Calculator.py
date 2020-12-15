from Classes import ComplexNumbers as cn

while True:
    print("Complex calculator")
    print("Enter first real part and then complex part")

    fr = int(input())
    fi = int(input())

    print("Enter an operation: +, -, *, /, mag, conj")

    option = input()

    operation = None
    first = cn.CN(fr, fi)

    if(not (option == "mag" or option == "conj")):
        print("Enter second real part and the complex part")

        sr = int(input())
        si = int(input())

        second = cn.CN(sr, si)

        if(option == "+"):
            operation = first + second
        elif (option == "-"):
            operation = first - second
        elif (option == "*"):
            operation = first*second
        elif (option == "/"):
            operation = first/second
        print("Value of operation: " + operation.show())

    elif(option == "mag"):
        operation = first.mag()
        print("Value of operation: " + operation)
    elif(option == "conj"):
        operation = first.conjugate()
        print("Value of operation: " + operation.show())
    else:
        print("Wrong value of operation. Try Again")