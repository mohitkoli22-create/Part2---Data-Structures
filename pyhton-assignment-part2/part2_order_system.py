menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


#TASK1 - Explore the Menu

 # 1  Print the full menu grouped by category,

categories = set(item["category"] for item in menu.values())

# menu.values() → gives all item details (dictionary inside dictionary)
# item["category"] → extracts category like Starters, Mains
# set(...) → removes duplicates

for category in categories:
    print(category)

# loop through menu items 

for name, details in menu.items():
    
    if details["category"] == "Starters":
 # Check availablity       
        status = "Available" if details["available"] else "Not Available"
 # Print formatted output       
        print(f"{name:<15}  ₹{details['price']:.2f}.  [{status}]") 

# {name:<15} → left align text in 15 spaces
# :.2f → 2 decimal places

# 2 Using dictionary methods, compute and print:

 # a. Total number of items in the menu
 
total_items = len(menu)

  #len(menu) → counts number of keys

  # avalilable items in the menu
available_items = sum(1 for item in menu.values() if item["available"])

  # loop through all items
  # if available is - count1
  # sum() add them up

 # most expensive item in the menu

most_expensive_item = max(menu.items(), key=lambda x: x[1]["price"]) 

# menu.items() - gives (name, details) pairs
# key=lambda x: x[1]["price"] - sort by price
# max() finds highest price item

cheapest_item = min(menu.items(), key=lambda x: x[1]["price"])
# min() finds lowest price item
# select items priced < 150

print(f"Total items: {total_items}")
print(f"Available items: {available_items}")
print(f"Most expensive item: {most_expensive_item[0]} at ₹{most_expensive_item[1]['price']:.2f}")
print(f"Cheapest item: {cheapest_item[0]} at ₹{cheapest_item[1]['price']:.2f}")




# TASK2 - Cart Operations

cart = []


# Implement a function to add item and show quantity to cart.

def add_to_cart(item_name, quantity):

    if item_name not in menu:
        print(f"{item_name} is not on the menu.")
        return
    
    if not menu[item_name]["available"]:
        print(f"Invalid request, {item_name} is currently not available.")
        return
    
    # Check if item already exists in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return # to avoid duplicate entry 

    # If item not in cart, add it
    cart.append({"item": item_name, "quantity": quantity, "price": menu[item_name]["price"]})
    print(f"added {item_name} x{quantity}")


def remove_from_cart(item_name):
    # remove item from cart
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name} from cart.")
            return
    #to find item in cart and remove it
    print(f"{item_name} is not in the cart.")


def update_cart(item_name, quantity):
    # Update quantity
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] = quantity
            print(f"Updated {item_name} quantity to {quantity}.")
            return
    print(f"{item_name} is not in the cart.")


# Simulation 
if __name__ == "__main__":
    add_to_cart("Paneer Tikka", 2)
    print(cart)
    
    add_to_cart("Gulab Jamun", 1)
    print(cart)

    add_to_cart("Paneer Tikka", 1)
    print(cart)

    add_to_cart("Mystery Burger", 1) 
    print(cart)

    add_to_cart("Chicken Wings", 1)
    print(cart)

    remove_from_cart("Gulab Jamun")
    print(cart)


# Order Summary


print("\n====== Order Summary======:")

subtotal = 0

for item in cart:
    item_total_price = item["quantity"] * item["price"]
    subtotal += item_total_price
    print(f"{item['item']:<15} x{item['quantity']}   ₹{item_total_price:.2f}")

    gst = subtotal * 0.05
    total = subtotal + gst

    print("-----------------------------")
    print(f"Subtotal:   ₹{subtotal:.2f}")
    print(f"GST (5%):   ₹{gst:.2f}")
    print(f"Total:      ₹{total:.2f}")
    print("=============================")


# TASK3 - Inventory Tracker with Deep Copy
     
    import copy

     # Deep copy
    inventory_copy = copy.deepcopy(inventory)

    # create new copy so changes in original wont affect new copy

    # modify original inventory
    inventory["Paneer Tikka"]["stock"] = 5

    print("\nOriginal Inventory:", inventory["Paneer Tikka"])
    print("Inventory Copy:", inventory_copy["Paneer Tikka"])

    # Restore
    inventory = copy.deepcopy(inventory_copy)
    # reset original inventory to copy

    for item in cart:
        name = item["item"]
        qty = item["quantity"]
        
        stock = inventory[name]["stock"]
        
        if stock < qty:
            print(f"Warning: Only {stock} available for {name}")
            inventory[name]["stock"] = 0
            # prevent negative stock
        else:
            inventory[name]["stock"] -= qty


# Reorder Alerts
print("\nReorder Alerts:")

for name, data in inventory.items():
    if data["stock"] <= data["reorder_level"]:
        print(f"⚠ Reorder Alert: {name} — Only {data['stock']} left (level: {data['reorder_level']})")
# if stock is low - alert



# Task 4 — Sales Log Analysis (6 marks)

# Revenue per Day
daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total
    #add all order totals for the day
    print(date, "₹", total)

# Best Selling Day
best_day = max(daily_revenue, key=daily_revenue.get)
# To find day with highest revenue
print("\nBest Day:", best_day, "₹", daily_revenue[best_day])

# Most Ordered Item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
# If item not in count start from 0 then +1
print("\nMost Ordered Item:", most_ordered)

# Add New Day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]
# adds new order value


# Re-run revenue logic again.

# Enumerate Orders
print("\nAll Orders:\n")

count = 1
# number the orders

for date, orders in sales_log.items():
# gives list of orders for each date

    
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        count += 1
        # count - order number
        # date - order date
        # order_id - unique id for order
        # total - order total
        # items - list of items in order    