def decimal(number):
    
    length = len(number)
    y = len(number) - 1
    result = 0
    
    for x in range(int(length)):
        
        
        if number[y] == "1":
            
            result = result + 2**x
           
        y -= 1
        
    return result    



def binary(n):
    result = []
    resultado_inverso = []
    number = n
    x = 0
    
    #Gives the binary number
    while n > 0 :

        if (n % 2) == 0 :
            result.append(0)
            n = n // 2

        else:
            result.append(1)
            n = n // 2
    
    #Reverse the list
    x = len(result) - 1
    for y in range(len(result)):
        
        numero = result[x]
        resultado_inverso.append(numero)
        x -= 1
        
    print(resultado_inverso)





nOne = input()
nTwo = input()

suma = decimal(nOne) + decimal(nTwo)

print("La suma es: ")
binary(suma)
