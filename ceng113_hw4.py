class Menu:
    def __init__(self,category,product,portion, price):
        self.__category = category
        self.__product = product
        self.__portion = portion
        self.__price = price
    
    def set_category(self, category):
        self.__category = category
    
    def set_product(self, product):
        self.___product = product
        
    def set_portion(self, portion):
        self.__portion = portion
    
    def set_price(self, price):
        self.__price = price
        
    def get_category(self):
        return self.__category
    
    def get_product(self):
        return self.__product
    
    def get_portion(self):
        return self.__portion
    
    def get_price(self):
        return self.__price
 

def make_list():
    #Reads the menu information from menu.txt file and make a list
    menu_items= []
    outfile=open("menu.txt","r")
    line=outfile.readline()
    line=outfile.readline()
    while line != "":
        line=line.strip("\n")
        word_list= line.split("; ")
        food = Menu(word_list[0],word_list[1],word_list[2],word_list[3])
        menu_items.append(food)
        line = outfile.readline()
    outfile.close()
    
    return menu_items

def get_categories(menu_items):
    #Returns a list of unique categories from the menu
    categories = []
    for item in menu_items:
        if item.get_category() not in categories:
            categories.append(item.get_category())
    return categories

def get_products(category, menu_items):
    #Returns a list of unique products in a given category
    products = []
    for item in menu_items:
        if item.get_category() == category:
            if item.get_product() not in products:
                products.append(item.get_product())
    return products
    
def get_product_portions(name, menu_items):
    #Returns a list of portions available for a given product
    portions = []
    for item in menu_items:
        if item.get_product() == name:
            portions.append(item.get_portion())
    return portions

def get_product_price(name, portion, menu_items):
    #Returns the price of a given product and portion
    
    for item in menu_items:
        if item.get_product() == name and item.get_portion() == portion:
            return item.get_price()
    

def main():
    
    try:
    
        menu_items=make_list()
        categories=get_categories(menu_items)
        
        choice=1
        order = []
        while choice==1:
            # Print the categories and make user select one
            print("Product Categories")
            count=0
            for i, category in enumerate(categories):
                print(f"{i+1}. {category}")
                count+=1
            
            category_choice = int(input("Please select product category: "))
            #Check for input validation
            while category_choice < 1 or category_choice > count:
                print("Please select a valid category")
                category_choice = int(input("Please select product category: "))
            
            selected_category = categories[category_choice - 1]
            products= get_products(selected_category, menu_items)
            
            print("----------------------------")
            
            # Print the products in the selected category and make user select one
            print(f"Products in {selected_category}")
            count=0
            for i, product in enumerate(products):
                print(f"{i+1}. {product}")
                count+=1
            
            product_choice = int(input("Please select product name: "))
            #Check for input validation
            while product_choice < 1 or product_choice > count:
                print("Please select a valid product")
                product_choice = int(input("Please select product name: "))
            
            selected_product = products[product_choice - 1]
            portions = get_product_portions(selected_product, menu_items)
            
            print("---------------------------")
            
            # Print the portions available for the selected product and make user select one
            print(f"{selected_product} Portions")
            count=0
            for i, portion in enumerate(portions):
                print(f"{i+1}. {portion}")
                count+=1
            portion_choice = int(input("Please select product portion: " ))
            #Check for input validation
            while portion_choice < 1 or portion_choice > count:
                print("Please select a valid portion")
                portion_choice = int(input("Please select product portion: "))
                
            selected_portion = portions[portion_choice - 1]
            selected_price = get_product_price(selected_product, selected_portion, menu_items)
            
            order.append((selected_product, selected_portion, selected_price))                    
            
            print("---------------------------")
            
            # Makes user add more products or checkout
            choice=int(input("1. Add New\n2. Checkout\nPlease select an operation: ")) 
            
            print("----------------------------")
        
        while choice != 2:
            print("Please select a valid operation!")
            choice=int(input("1. Add New\n2. Checkout\nPlease select an operation: "))
         
        #Calculate the total price
        total_price=0
        for item in order:
            product, portion, price = item
            price=price.lstrip("$")
            total_price += float(price)
            #Print the selections of user and the prices of them 
            price= "$" + str(price)
            print("{0:35} {1:15} {2:10}".format(product,portion,price))
            
            print("----------------------------")
        
        #Print the total price
        total_price= "$" + str(format(total_price, ".2f"))
        print("{0:35} {1:15} {2:10}".format("Total:"," ",total_price))

    except:
        print("An error occured, please make valid selections from the beginning!")
        main()
        
        
main()
