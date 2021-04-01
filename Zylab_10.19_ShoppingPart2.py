#  Srijana Shrestha
#  1918305
# creating class item to purchase
class ItemToPurchase:
    def __init__(self, item_name='none', item_price=0, item_quantity=0, item_description='none'):  # adding constructors
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):  # defining function for print_item_cost
        print(self.item_name, self.item_quantity, '@', '$' + str(int(self.item_price)), '=',
              '$' + str(int(self.item_quantity) * int(self.item_price)))

    def print_item_description(self):  # defining function for print item description
        print(self.item_name, ':', self.item_description)


class ShoppingCart:  # creating class shoppingCart

    def __init__(self, customer_name='none', current_date='January 1, 2016', cart_items=None):  # adding constructors
        if cart_items is None:
            cart_items = []
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = cart_items

    def add_item(self):  # defining function for add item

        item_name = input('Enter the item name:\n')
        item_description = input('Enter the item description:\n')
        item_price = int(input('Enter the item price:\n'))
        item_quantity = int(input('Enter the item quantity:\n'))
        self.cart_items.append(ItemToPurchase(item_name, item_price, item_quantity, item_description))

    def remove_item(self):  # defining function to remove item

        name_of_item = str(input('Enter name of item to remove:\n'))  # user input for item name
        s = 0
        for item in self.cart_items:  # for loop to iterate in cart.items
            if item.item_name == name_of_item:  # applying if condition to check item
                self.cart_items.pop(s)  # deleting items

                flag = True  # if flag is true then break
                break

            else:
                flag = False
            s = s + 1

        if not flag:
            print('Item not found in cart. Nothing removed.')  # print statement

    def modify_item(self):  # defining function to modify item

        name = str(input('Enter the item name:\n'))  # user input for the item name

        for item in self.cart_items:
            #  applying if condition to check input item in the cart or not
            if item.item_name == name:
                quantity = int(input('Enter the new quantity:\n'))

                item.item_quantity = quantity
                flag = True
                break

            else:
                flag = False

        if not flag:
            print('Item not found in cart. Nothing modified.')

    def get_num_items_in_cart(self):  # defining function to get num items in cart

        num_items = 0
        for item in self.cart_items:
            num_items = num_items + item.item_quantity  # addition
        return num_items  # returning num of items

    def get_cost_of_cart(self):  # defining get cost of cart function

        Total_cost = 0
        for item_in_cart in self.cart_items:
            sub_total = item_in_cart.item_price * item_in_cart.item_quantity  # calculating sub total
            Total_cost = Total_cost + sub_total  # calculating total cost
        return Total_cost  # returning value

    def print_total(self):  # defining print total function

        Total_cost = self.get_cost_of_cart()  # calling get cost of cart function for total

        if Total_cost == 0:  # checking condition either total cost is equal to 0
            print('SHOPPING CART IS EMPTY')  # printing statement
        else:
            self.output_cart()  # calling function output cart

    def print_descriptions(self):  # defining print descriptions function

        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date), end='\n')
        print('\nItem Descriptions')  # printing statement

        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))  # printing statement

    def output_cart(self):  # defining output cart function

        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items:', self.get_num_items_in_cart())
        print()  # printing empty line

        total_count = 0  # assigning total count as 0
        for item in self.cart_items:
            cost = (item.item_quantity * item.item_price)  # calculating cost
            print('{} {} @ ${} = ${}'.format(item.item_name, item.item_quantity, item.item_price, cost))
            total_count = total_count + cost  # calculating total count

        if len(self.cart_items) == 0:  # checking cart has any item
            print('SHOPPING CART IS EMPTY')  # printing statement
        print()  # printing empty line

        print('Total: ${}'.format(total_count))


def print_menu(ShoppingCart):
    # assigning menu
    menu = (
        '\nMENU\n''a - Add item to cart\n''r - Remove item from cart\n''c - Change item quantity\n'
        'i - Output items\' descriptions\n''o - Output shopping cart\n''q - Quit\n')

    option = ''
    while option.upper() != 'Q':  # if option is not equal
        print(menu)  # printing menu
        option = input('Choose an option:\n')  # user input for option

        #  checking condition for user option
        while (option != 'a' and option != 'o' and option != 'i' and option != 'r'
               and option != 'c' and option != 'q'):
            option = input('Choose an option:\n')

        #  if condition is a
        if option.lower() == 'a':
            print('ADD ITEM TO CART')
            ShoppingCart.add_item()  # call function add_item

        #  if condition is o
        if option.lower() == 'o':
            print('OUTPUT SHOPPING CART')
            ShoppingCart.output_cart()  # call function output_cart

        #  if condition is i
        if option.lower() == 'i':
            print('OUTPUT ITEMS\' DESCRIPTIONS')
            ShoppingCart.print_descriptions()  # call function print_description

        #  if condition is r
        if option.lower() == 'r':
            print('REMOVE ITEM FROM CART')
            ShoppingCart.remove_item()  # call function remove_item

        #  if condition is c
        if option.lower() == 'c':
            print('CHANGE ITEM QUANTITY')
            ShoppingCart.modify_item()  # call function modify_item


def main():  # declaring main function
    customer_name = str(input('Enter customer\'s name:\n'))  # user input for customer name
    current_date = str(input('Enter today\'s date:\n\n'))  # user input current date

    print('Customer name:', customer_name, end='\n')  # print statement
    print('Today\'s date:', current_date)  # print statement

    print_menu(ShoppingCart(customer_name, current_date))  # calling function


if __name__ == '__main__':
    main()  # function call
