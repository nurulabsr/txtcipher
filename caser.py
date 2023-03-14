def caesercyper_fun(inputTxt, step):
    cyper = []
    output = []
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for datum in inputTxt:
        if datum in uppercase:
        
         indexx = uppercase.index(datum);
         print(f"Index", indexx)
        cy = (indexx + step)%26
        print(f"cy:", cy)
        cyper.append(cy)
        print(cyper);
        newLatter = uppercase[cy]
        output.append(newLatter)
        print(output)
        # elif latter in lowercase:
            
    
    # print("Test the fun")
    
caesercyper_fun("ABC", 2)
   
    
    
    
    
# print("Test the py script")