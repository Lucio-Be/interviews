def reverse(w):
    large = len(w)
    reverse = ""
    
    for x in (range(large)):
        
        reverse = reverse + w[large - 1]
        large -= 1 
    
    print(reverse)


word = input()
reverse(word)