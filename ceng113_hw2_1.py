
def userName():  
    name = input("Enter a username: ")
    letters= []
    letters.extend(name)
    
    while not letters[0] == "e" :
        name= input("Please use'e' at the beginning of the username: ")
        letters= []
        letters.extend(name)
    
    while len(name) < 6 or len(name) > 12 :
        name= input("Please enter username in the allowed lenght: ")
    
    while name.isalnum() == False :
        name= input("Please enter a username that does not contain any characters " \
              "other than alphanumeric characters: ") 
        
    print("Your username" , name , "is VALID")




def password():    
    password= input("Please enter a password: ")
    while len(password) < 8 :
        password= input("Please enter a password that has at least 8 characters: ")
    


userName()
password()
