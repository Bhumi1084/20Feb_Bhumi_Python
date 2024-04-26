from customer import * 
import FruitManager

def display_menu():     #create function
    print("\n-----WELCOME TO FRUIT MARKET-----")
    print("\n1) Manager")
    print("\n2) Customer")
    print("\n3) Exit")
    role = int(input("\nSelect Your Role : "))      #get value from user
    return role     #return value
    
role = display_menu()   #call function

def displayMenu():      #create function for add,view and update stock
    print("\n-----Fruit Market Manager-----")
    print("\n1) Add Fruit Stock")
    print("\n2) View Fruit Stock")
    print("\n3) Update Fruit Stock")
    choice = int(input("\nEnter Your Choice : "))   #get value from user
    return choice   #return choice value 

while role!=3:  
    if role == 1:   #check condition role equal to 1    #condition = true        
        choice = displayMenu()      #call function 
    
        if choice == 1:     #choice equal to 1  #condition = true
            FruitManager.addFruitStock()    #call function
            ask = input("Do You Want To Perform More Operation? (Press Y For Yes And N For No) : ")     #get value from user
            if ask.lower() == 'y':      #condition = true            
                choice = displayMenu()  #call function 
            elif ask.lower() == 'n':    #condition = false
                role = display_menu()   #call function
            else:
                print("\nPlease Enter Valid Choice...!!")     #display message           
                choice = displayMenu()      #call function
    
        elif choice == 2:            #choice equal to 2     #condition = true
            FruitManager.ViewFruitStock()   #call function
            ask = input("Do You Want To Perform More Operation? (Press Y For Yes And N For No) : ")
            if ask.lower() == 'y':
                choice = displayMenu()
            elif ask.lower() == 'n':
                role = display_menu()
            else:
                print("\nPlease Enter Valid Choice...!!")
                choice = displayMenu()
    
        elif choice == 3:
            FruitManager.updateFruitStock()
            ask = input("Do You Want To Perform More Operation? (Press Y For Yes And N For No) : ")
            if ask.lower() == 'y':                
                choice = displayMenu()
            elif ask.lower() == 'n':
                role = display_menu()
            else:
                print("\nPlease Enter Valid Choice...!!")                
                choice = displayMenu()
    
        else:   #condition are false
            print("\nPlease Enter Valid Choice...!!")   #display message           
            choice = displayMenu()      #call function

    elif role == 2:
        Customer.customer_menu()
        role = display_menu()  
    
    else:
        print("\nPlease Select Valid Role...!!")
        role = display_menu()

print("\nExit")     #display message