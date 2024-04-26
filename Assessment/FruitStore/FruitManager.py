def addFruitStock():    #create function
    print("\n-----ADD FRUIT STOCK-----")
    fruit_name = input("\nEnter Fruit Name : ")     #get fruit name from user
    qty = int(input("\nEnter qty (in kg) : "))      #get fruit qty from user
    price = int(input("\nEnter Price : "))      #get fruit price from user
    f1 = open('stock.txt','a')      #open file in append mode
    f1.write(f"'{fruit_name}': {{'qty': '{qty}', 'price': {price}}}\n")    #write data in the file
    print("\nStock Added Successfully...!")     #display message

def ViewFruitStock():
    print("\n-----View All Stock-----")
    f1 = open('stock.txt','r')  #open file in read mode
    print(f1.read())    #display data

def updateFruitStock():
    print("\n-----Update Fruit Stock-----")
    fruit_name = input("\nEnter Fruit Name To Update : ")   #get fruit name from user
    found = False
    f1 = open('stock.txt','r')  #open file in read mode
    lines = f1.readlines()      #read file
    updated_lines = []  #initialize list
        
    for line in lines:
        if fruit_name in line:
            found = True
            new_qty = int(input("\nEnter New qty (in kg) : "))  #get updated fruit qty from user
            new_price = int(input("\nEnter New Price : "))  #get updated fruit price from user
            parts = line.split(':')     #split :
            updated_line = f"{parts[0]}: {{'qty': '{new_qty}', 'price': {new_price}}}\n"    #update value
            updated_lines.append(updated_line)  #store updated value in list
            print("\nStock Updated Successfully...!")   #display message
        else:       #condition = false
           updated_lines.append(line)   #value not updates  #store as it is value
    
    if not found:
        print("\nFruit Not Found In Stock....!!")
    else:
        fwr = open('stock.txt', 'w')    #open file in write mode
        fwr.writelines(updated_line)    #value are updated