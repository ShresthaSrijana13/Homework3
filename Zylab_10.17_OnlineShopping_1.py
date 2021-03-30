# Srijana Shrestha
# 1918305
class ItemToPurchase:  # creating a class itemToPurchase
    def __init__(self):  # constructor
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):  # defining function to print item cost
        print(self.item_name, self.item_quantity, '@', '$' + str(int(self.item_price)), '=',
              '$' + str(int(self.item_quantity) * int(self.item_price)))  # printing and calculation of cost


if __name__ == "__main__":
    item = ItemToPurchase()  # calling itemToPurchase function
    print('Item 1')  # printing  block
    print('Enter the item name:')  # printing block
    item.item_name = input()  # user input
    print('Enter the item price:')  # printing block
    item.item_price = float(input())  # user input
    print('Enter the item quantity:')  # printing block
    item.item_quantity = int(input())   # user input

    print()  # printing empty line

    item2 = ItemToPurchase()  # itemToPurchase function call
    print('Item 2')  # printing block
    print('Enter the item name:')  # printing block
    item2.item_name = input()  # user input
    print('Enter the item price:')  # printing block
    item2.item_price = float(input())  # user input
    print('Enter the item quantity:')  # printing block
    item2.item_quantity = int(input())  # user input

    print()  # printing empty line
    print('TOTAL COST')  # printing block
    item.print_item_cost()  # print_item_cost function call for item
    item2.print_item_cost() # print_item_cost function call for item2
    print()  # printing empty line
    print('Total:', '$' + str(int(item.item_price * item.item_quantity) + int(item2.item_price * item2.item_quantity)))
