# You have a shopping list and need to buy everything.
# Rules: If the store doesn't have an item, skip it
# Once all available items are bought, print "shopping done!"
# Hint: use "not in"


store_list = ["Rice", "Beans", "Spices", "Banana", "Mango", "Candies"]
buyers_list = ["Rice", "Beans", "Spices", "Plantain", "Banana", "Mango", "Cookies", "Candies"]

for item in buyers_list:
    if item not in store_list:
        print(f"Looking for {item}..., {item}is out of stock")
        continue
    print(f"Looking for {item}....., {item} found")

print("Shopping done!")









