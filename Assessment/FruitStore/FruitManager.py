def displayMenu():
    print("\n-----Fruit Market Manager-----")
    print("\n1) Add Fruit Stock")
    print("\n2) View Fruit Stock")
    print("\n3) Update Fruit Stock")

def addFruitStock():
    print("\n-----ADD FRUIT STOCK-----")
    fruit_name = input("\nEnter Fruit Name : ")
    qty = int(input("\nEnter qty (in kg) : "))
    price = int(input("\nEnter Price : "))
    f1 = open('stock.txt','a')
    f1.write(f"'{fruit_name}': {{'qty': '{qty}', 'price': {price}}}\n")
    print("\nStock Added Successfully...!")

def ViewFruitStock():
    print("\n-----View All Stock-----")
    f1 = open('stock.txt','r')
    print(f1.read())

def updateFruitStock():
    '''print("\n-----Update Fruit Stock-----")
    f1 = open('stock.txt','a')
    fruit_name = input("\nEnter Fruit Name To Update : ")
    if fruit_name in f1:
        new_qty = int(input("\nEnter New qty (in kg) : "))
        new_price = int(input("\nEnter New Price : "))
        [fruit_name]['qty'] = new_qty
        [fruit_name]['price'] = new_price
        print("\nStock Updated Successfully...!")
    else:
        print("\nFruit Not Found In Stock....!!")'''