from product import add_product, delete_product, list_product, update_product

def menu():
    while True:
        print("\n===== Product Menu =====")
        print("1. Add Product")
        print("2. List all Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter choice(1-5) :")

        if choice == "1":
            name = input("Enter product name :")
            price = input("Enter product price :")
            stock = input("Enter product stock :")
            add_product(name,price,stock)

        elif choice == "2":
            list_product()

        elif choice == "3":
            pid = int(input("Enter product id to update : "))
            price = input("Enter new price : ")
            stock = input("Enter new stock : ")

            update_product(pid,
                           price=float(price) if price else None,
                           stock=int(stock) if stock else None)
            
        elif choice == "4":
            pid=int(input("Enter product id to delete : "))
            delete_product(pid)

        elif choice == "5":
            print("Exiting... The menu !!")
            break
        
        else:
            print("Wrong option selected !!")

if __name__ == "__main__": #it means run this file as the launcher file
    menu() #menu is called and we see the menu directly

#This is done because when we are importing other files the compiler will run them first but we want to run the main.py first.
#Hence, if __name__=="__main__" is required to execute it first, leaving all other files behind.

