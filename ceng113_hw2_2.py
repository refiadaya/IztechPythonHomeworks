
def count_special_character(text_input,special_input):   
   
    text = list(text_input)
    special = list(special_input)

    counter = 0 
 
    for x in text : 
        if x in special : 
            counter +=1 
    return counter


text_input = input("Write your text: ")
special_input = input("Enter a special character: ")    
    
counter = count_special_character(text_input,special_input)

print("Number of special characters: ",counter) 
