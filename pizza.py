# Name: Omwira Nkere
# Prog Purpose: This program finds the cost and the size of a pizza
# pizza cost:[Small:9.99, medium:12.99, large: 14.99, extra_large: 17.99]
# Sales tax rate: 5.5%     

import datetime

#define pizza size, price and tax rate
if small: pizza_price(9.99)
if pizza_size == medium: pizza_price (12.99)
if pizza_size == large: pizza_price (14.99)
if pizza_size == extra_large: pizza_price(17.99)
sales_tax_rate = 5.5

#define global variables
size = 1 # S means Small, M means medium, L means large & X means extra_large
pizza_size = 0 
pizza_cost = 0
numpizza = 0


############## define program functions ######################
def main():
        get_user_data()
        perform_calculations()
        display_results()

def get_user_data():
        global pizza_size, numpizza
        pizza_size = int(input("Enter S for small; enter M for medium; enter L for large; enter X for extra_large:"))
        numpizza = int(input("Number of pizza for:"))

def perform_calculations():
        global pizza_cost, sales_tax
        pizza_cost = numpizza * pizza_price
        sales_tax = pizza_cost * sales_tax_rate
        total = Pizza_cost + sales_tax
        
def display_results():
    print('\n-----------------------------------------')
    print('*************** PALERMO PIZZA **************')
    print('\n****THE BEST PLACE FOR THE BEST PIZZA*****')
    print('--------------------------------------------')
    print('pizza         $ ' + format(pizza_cost,'10,.2f'))
    print('Sales Tax     $ ' + str(sales_tax))
    print('Total         $ ' + str(total))
    print('---------------------------------------')
    print(str(datetime.datetime.now()))
    print("NOTE: PVCC Fee Rates: https://www.pvcc.edu/tuition-and-fees")


##########  call on main program to execute ###########
main()
