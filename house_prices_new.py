print("Welcome to House Prices")

name = input("What is your name?: ")
# get house prices
price = int(input('What is the house price (£)?: '))

# get user input and convert booleans
income = input("Do you have a high income? (yes/no): ").lower()
credit = input("Do you have good credit? (yes/no): ").lower()

has_good_credit = income == 'yes'
has_high_income = credit == 'yes'

# determine down payment

if has_good_credit and has_high_income:
    down_payment = 0.10 * price
    print("Eligible for loan")
    
else:
    down_payment = 0.20 * price
print(f"Higher down payment required: £{down_payment}")


# display result
print(f"{name}, your down payment is: {down_payment:,.2f}")

print('hello changes')