# calculate_discount.py      
#user input for price and discount percent
price=float(input("Enter the price: "))
discount_percent=float(input("Enter the discount percent: "))  

# Calculate the final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price
#calculate the final price after discount
final_price = calculate_discount(price, discount_percent)

if discount_percent >= 20: 
    print(f"The final price after discount is: {final_price}")
else:
    print(f"final price is the same as original price {price}.")


