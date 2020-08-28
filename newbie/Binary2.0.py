def binary(n):
    result = ""
    
    while n > 0:

        if (n % 2) == 0 :
            result = "0" + result 
            n = n // 2

        else:
            result =  "1" + result 
            n = n // 2

    print(result)



number = int(input())
binary(number)