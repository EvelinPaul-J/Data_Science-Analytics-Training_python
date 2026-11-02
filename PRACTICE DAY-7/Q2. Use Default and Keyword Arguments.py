'''Q2. Use Default and Keyword Arguments
Example Input: prices = [100, 50]
calculate_bill(prices, tax_rate=0.10, discount=0.20)
Example Output: Subtotal: 150.00
Discount: 30.00
Tax: 12.00
Final total: 132.00'''
prices = [100,50]
def calculate_bill(prices, tax_rate=0.10, discount=0.20):
    subtotal = sum(prices)
    discount_amt = subtotal * discount
    final_amt = subtotal - discount_amt
    tax = final_amt * tax_rate
    total = final_amt + tax
    print("Subtotal : ",subtotal)
    print("Discount : ",discount_amt)
    print("Tax : ",tax)
    print("Final total : ",total)
calculate_bill(prices,tax_rate=0.10,discount=0.20)