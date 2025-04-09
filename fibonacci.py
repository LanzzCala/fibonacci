def fib(number):
    print (f"You entered {number}.")
    if number <= 1:
        return number
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

fib(10)