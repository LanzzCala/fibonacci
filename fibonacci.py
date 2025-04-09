def fib():
    try:
        number = int(input("Enter a number for the fibonacci sequence: "))
        if number == 0:
            print(number)
        elif number <= 1:
            print (number)
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
    except ValueError:
        print(f"You entered text instead of a number. Please run the code again.")


fib()
