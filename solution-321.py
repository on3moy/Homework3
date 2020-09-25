"""
Exercise 3.21 (Calculate Change Using Fewest Number of Coins)
Write a script that inputs a purchase price of a dollar or less for an item. Assume the purchaser pays with a dollar bill.
Assume the purchaser  pays with a dollar bill. Detemrine the amount of change the cashier should give back to the purchaser.
Display the change using the fewest number of pennies, nickels, dimes and quarters. For example, if the purhcaser is due 73 cents in change,
the script would output:
Your change is:
2 quarters
2 dimes
3 pennies
"""

# Assign Variables
customer_pay = 1
quarters = .25
dimes = .1
nickels = .5
pennies = .01

# Ensure user inputs a decimal form 0-1
while True:
    purchase_price = input('What is the purchase price?: (Must be greater than $0 and less than $1)')
    if not purchase_price.isalpha():
        if float(purchase_price) > 0 and float(purchase_price)<=1:
            purchase_price = float(purchase_price)
            break

# Assign Variables
customer_pay = 1
quarters = .25
dimes = .10
nickels = .05
pennies = .01
names = ['Quarters', 'Dimes', 'Nickels', 'Pennies']

# Ensure user inputs a decimal form 0-1
while True:
    purchase_price = input('What is the purchase price?: (Must be greater than $0 and less than $1)')
    if not purchase_price.isalpha():
        if float(purchase_price) > 0 and float(purchase_price)<=1:
            purchase_price = float(purchase_price)
            break

# Calculations (1 - input for change)
quarter = int((1-purchase_price) // quarters)
dime = int((1-purchase_price) % quarters // dimes)
nickel = int((1-purchase_price) % quarters % dimes // nickels)
penny = int(round((1-purchase_price) % quarters % dimes % nickels / pennies))
result = [quarter, dime, nickel, penny]

# Print results
print(f'You have entered: ${purchase_price:.2f}\nYour change is ${1-purchase_price:.2f}')
loc = 0
for calc in result:
    if calc != 0:
        print(calc, names[loc])
    loc += 1