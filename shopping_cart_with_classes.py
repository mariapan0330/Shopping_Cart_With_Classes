import os

class Cart():
    
    cart = {}
    # EXAMPLE cart = {"item_name": [quantity, price]}
    
    def add(self):
        os.system("cls")

        print("\n================================ ADD ================================ ")

        while True:
            item = input("What would you like to add to your cart? ").lower().strip()
            if item == 'done':
                self.show(True)
                break
            else:        
                print(f"\tYou've selected {item.upper()}.")

            while True:
                quant = input(f"\nHow many would you like to add? ")
                if quant == 'done':
                    self.show(True)
                    break
                
                if quant.isdigit() == False:
                    print("\t!!! Invalid Input. Please enter a whole number. !!!")
                    continue
                else:
                    break

            try:
                price = self.cart[item][1]
            except:
                print(f"\tYou've added {item.upper()} x {quant}.")
                while True:
                    price = input(f"\nWhat is the price of one {item}? $")

                    if price == 'done':
                        self.show(True)
                        break
                    
                    try:
                        price = "{:.2f}".format(float(price))
                    except:
                        print("\t!!! Invalid Input. Please enter a number. !!!")
                        continue
                    else:
                        break
            
            if price == 'done':
                break

            print(f"\tYou've added {item.upper()} x {quant} at ${price} each.")
            if item in self.cart: 
                quant = int(self.cart[item][0]) + int(quant)
                print(f"\tThere are now {item.upper()} x {quant} in your cart.")

            self.cart[item] = [quant, price]
            main(self)
            break
    
    def remove(self):
        os.system("cls")
        print("\n============================== REMOVE =============================== ")
        while True:
            if len(self.cart) == 0:
                print("Cart is empty. Nothing to remove.")
                main(self)
                break

            item = input("\nWhat item would you like to remove? \n(Enter an item or type ALL to remove all items from your cart): ").lower().strip()
            if item == 'done':
                self.show(True)
                break

            if item == 'all':
                while True:
                    really_clear = input("\nAre you sure you want to remove all items from your cart? This action cannot be undone. YES/NO: ").lower().strip()
                    if really_clear == 'yes':
                        self.cart.clear()
                        print("\tYou have removed all items from your cart.")
                        break
                    elif really_clear == 'no':
                        break
                    else:
                        print("\t!!! Invalid Input. !!!")
                        continue
            try:
                if really_clear == 'yes':
                    main(self)
                    break
                elif really_clear == 'no':
                    really_clear = ''
                    continue
                else:
                    pass
            except:
                pass

            if item in self.cart:
                if self.cart[item][0] == 1:
                    print(f"\t{item.upper()} removed.")

                quant = input(f"\nHow many {item.upper()} would you like to remove?" +
                    f"\n(Enter a whole number or type ALL to remove all {item.upper()} from your cart): ").lower().strip()
                if quant.isdigit() == False and quant != 'all':
                    print(f"\t!!! Invalid Input. Please enter a whole number or type ALL to remove all {item.upper()}. !!!")
                    continue
                elif quant == 'all':
                    quant = int(self.cart[item][0])
                    print(f"\tRemoving all {quant} {item.upper()} from your cart.")
                else:
                    print(f"\t{item.upper()} x {quant} has been removed from your cart.")
                
                quant = int(self.cart[item][0]) - int(quant)
                if int(quant) <= 0:
                    del self.cart[item]
                    quant = 0
                else:
                    self.cart[item][0] = quant
                print(f"\tThere are now {item.upper()} x {quant} in your cart.")
                main(self)
                break
            else:
                print("\tThat item is not in your cart.")
                main(self)
                break

    def done(self):
        while True:
            really_done = input("\nAre you sure you are done? You will not be able to modify your cart. YES/NO: ").lower().strip()

            if really_done == 'yes':
                os.system("cls")
                print('\n\n*********************************************************************')
                print("Thanks for using Shopping Cart! Here's a review of what's in your cart:", end='')
                self.show(True)
                break
            elif really_done == 'no':
                break
            else:
                print("\t!!! Invalid Input. !!!")
                continue

    def show(self, done=False):
        os.system("cls")
        print("\n============================= YOUR CART =============================")

        if self.cart:
            print(f"You have {len(self.cart)} items in your cart.")
            total = 0
            print(f"\tProduct\t\tQty\t\tUnit\t\tPrice")
            print('---------------------------------------------------------------------')
            for item, val in self.cart.items():
                f_item = item
                if len(f_item) > 6:
                    f_item = (item + '\n\t' + '-->')
                price = '{:.2f}'.format(float(val[0])*float(val[1]))
                print(f"\t{f_item.upper()}\t\t{val[0]}\t\t${val[1]}\t\t${price}")
                total += float(price)
            print("---------------------------------------------------------------------")
            print(f"Your total is ${'{:.2f}'.format(total)}")

        else:
            print("There are no items in your cart.")

        if done == False:
            main(self)
        else:
            print("---------------------------------------------------------------------")



def start(cart):
    """ Starts the shopping cart program. 
    Follow printed instructions or type help(command_name) for help. """
    os.system("cls")
    print("\n=========================== SHOPPING CART =========================== ")

    print("Welcome to the Shopping Cart.")
    print("Enter a command to get started: \n\tADD = Add item(s). \n\tREMOVE = Remove item(s)." + 
        "\n\tSHOW = Show the items in your cart." +
        "\n\tDONE = Type DONE at any time to exit the program and see a summary of your cart.")
    main(cart)


def main(cart):
    while True:
        print("---------------------------------------------------------------------")
        inp = input("What would you like to do? (ADD / REMOVE / SHOW / DONE): ").lower().strip()
        if inp not in {'add', 'remove', 'show', 'done'}:
            print("Invalid Input.")
            continue
        
        if inp == 'done':
            cart.done()
            break
        
        if inp == 'add':
            cart.add()
            break
        
        if inp == 'show':
            cart.show()
            break
        
        if inp == 'remove':
            cart.remove()
            break



my_cart = Cart()
start(my_cart)