def cesar_cipher(w):
    
    cesar = "abcdefghijklmnopqrstuvwxyzabc"
    cesar2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZABC"
    x = 0
    
    result = ""
    
    
    while x <= len(w) - 1:
        
        y = 0
        
        for y in range(len(cesar)):
        
            if w[x] == cesar[y]:
            
                result =  result + cesar[y + 3] 
                break
            
            elif w[x] == cesar2[y]:
            
                result = result + cesar2[y + 3]
                break

            elif w[x] == " ":
            
                result = result + " "
                break
                

        x += 1
        
    print(result)

word = input()
cesar_cipher(word)