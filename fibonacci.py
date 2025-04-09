def fib():
    try:
        number = int(input("Enter a number for the fibonacci sequence: "))
        if number <= 1:
            print ("You entered an invalid number")
    except ValueError:
        print("You entered words instead of a number. Please run the code again.")
    else:
        start = 0
        first_num = 0
        second_num = 1
        end = number
        while start != end:
            print (first_num, end= " ")
            result = first_num + second_num
            second_num = first_num
            first_num = result
            start += 1

fib()
