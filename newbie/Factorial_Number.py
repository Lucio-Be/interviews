def factorial_number(n):
    x = 0
    result = 1
    for x in range(n):
        result = result * n  
        n -= 1
    print ("Factorial Number:", result)

number = int(input())
factorial_number(number)