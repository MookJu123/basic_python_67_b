"""
#
# Part : python string fromating
# 
"""
price = 60
txt = f"price is {price} bath."
price(txt)
txt = f"price is {price:.2f} bath."
print(txt)

price = 50
tax = 0.25
txt = f"price is {price + (price*tax)} bath."
print(txt)

price = 10000
txt = f"price is {price:,} bath."
print(txt)
