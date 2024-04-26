from customer import *
import FruitManager

def display_menu():
    print("\n-----WELCOME TO FRUIT MARKET-----")
    print("\n1) Manager")
    print("\n2) Customer")
    print("\n3) Exit")
    role = int(input("\nSelect Your Role : "))
    return role
    
role = display_menu()

while role!=3:
    if role == 1:
        FruitManager.displayMenu()
        choice = int(input("\nEnter Your Choice : "))
    
        if choice == 1:
            FruitManager.addFruitStock()
            ask = input("Do You Want To Perform More Operation? (Press Y For Yes And N For No) : ")
            if ask.lower() == 'y':
                FruitManager.displayMenu()        
            elif ask.lower == 'n':
                role = display_menu()
            else:
                print("\nPlease Enter Valid Choice...!!")
                FruitManager.displayMenu()
    
        elif choice == 2:
            FruitManager.ViewFruitStock()
            ask = input("Do You Want To Perform More Operation? (Press Y For Yes And N For No) : ")
            if ask.lower() == 'y':
                FruitManager.displayMenu()                
            elif ask.lower == 'n':
                role = display_menu()
            else:
                print("\nPlease Enter Valid Choice...!!")
                FruitManager.displayMenu()                
    
        elif choice == 3:
            FruitManager.updateFruitStock()
            ask = input("Do You Want To Perform More Operation? (Press Y For Yes And N For No) : ")
            if ask.lower() == 'y':
                FruitManager.displayMenu()                
            elif ask.lower == 'n':
                role = display_menu()
            else:
                print("\nPlease Enter Valid Choice...!!")
                FruitManager.displayMenu()                
    
        else:
            print("\nPlease Enter Valid Choice...!!")
            FruitManager.displayMenu()            

    elif role == 2:
        Customer.customer_menu()
        role = display_menu()  
    
    else:
        print("\nPlease Select Valid Role...!!")
        role = display_menu()

print("\nExit")