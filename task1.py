#initialising the constant value for a pizza.
pizza_price = 12

#Taking input from the user.
def take_input():
    ''' calculate how much to charge a customer for their given order.'''
    
    while True:
        try:
            orders = int(input("Enter how many pizzas ordered? "))
            if orders > 0:
                break
            elif orders == 0:
                print("Cannot be zero!")
            else:
                print("Cannot be negative!!!")
        except:
            print("Enter a valid number!")
        
    delivery = input("Is delivery required? ")
    tuesday = input("Is it tuesday? ")
    app = input("Did the customer use the app? ")
    return orders, delivery, tuesday, app


#Calculating total order from a customer.
def calculate_total_orders(orders):
    
    total = orders * 12
    return total
    
#Calculating if the customer needs delivery.
def calculate_num(delivery, orders, total):
    if int(orders) >= 5:
        total = total
    elif int(orders) <5 and (delivery.lower() == "yes" or delivery.lower() == "y"):
        total = total + 2.5
    elif (delivery.lower() == "no" or delivery.lower() == "n"):
        total = total
    else:
        print("Invalid delivery!!!" )
    return total

#Calculating discount on tuesdays.
def tues_day(tuesday, total):
    if tuesday.lower() == "n" or tuesday.lower() == "no":
        total = total 
    elif tuesday.lower() == "y" or tuesday.lower() == "yes":
        total = total - (50/100) * total
    else:
        print("Invalid order!!!" )
    return total
    
#Calculating discount for using the app.
def bpp(app, total):
    if app.lower() == "yes" or app.lower() == "y":
        total = total - (25/100) * total
    elif app.lower() == "no" or app.lower() == "n":
        total = total
    else:
        print("Invalid!!!" )
    return total

#Getting input from the user.
orders, delivery, tuesday, app = take_input()

#Calculating total price based on input.
price =  calculate_total_orders(orders)
price_1 = calculate_num(delivery, orders, price)
price_2 = tues_day(tuesday, price_1)
price_3 = bpp(app, price_2)

#Printing final price after all calculations.
print(price_3)
