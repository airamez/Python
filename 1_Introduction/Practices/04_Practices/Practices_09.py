"""
Read the purchase price and desired profit percentage(%) for a product and calculate the sale price.
    e.g.
    INPUT
      Purchase Price = 500.00
      Desired Profit (%) = 30
    OUTPUT
      Sale Price = 650.00
"""
purchase_price = float(input("Purchase Price: "))
desired_profit = float(input("Desired Profit (%): "))

profit = purchase_price * (desired_profit / 100)
sale_price = purchase_price + profit

print("Profit =", profit)
print("Sale price = ", sale_price)
