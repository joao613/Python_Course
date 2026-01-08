# Exercise 2 | Shoppin Cart Program

item = input("What item would you like to buy: ")
price = float(input("What is the price of the item: "))
quantity = int(input("How many would you like to buy: "))

total = price * quantity

print(f"You have bought {quantity} {item}/s")
print(f"The total is : {total}€")