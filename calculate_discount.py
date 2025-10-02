# calculate_discount.py     
# This program calculates the final price after applying a discount if the discount percent is 20% or more.
# It also validates user input for price and discount percent.


#1. float input function with error handling

def get_float(prompt: str) -> float:

# Prompt the user for a float input until a valid float is entered

    while True:
        raw = input(prompt)

        try:
            return float(raw)

        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    
# Get user input for price and discount percent
price = get_float("Enter the price: ")
discount_percent = get_float("Enter the discount percent: ")

# Validate inputs and print warnings if necessary
if price < 0:
    print("Warning: Price is negative.")
if discount_percent < 0 or discount_percent > 100:
    print("Warning: Discount percent is outside 0–100%.")


# Calculate the final price after discount
def calculate_discount(price: float, discount_percent: float) -> float:
       
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Calculate and format the final price to two decimal places
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20: 
    print(f"The final price after discount is: {final_price:.2f}")
else:
    print(f"The final price is the same as original price {price:.2f}.")


