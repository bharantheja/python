#dictionary
#it coverts the number into the word  
students = dict(study="10th",strength="40",name="rohan")
print(f"students : {students}")

curry_recipe = {}
curry_recipe["base"] = "sambar"
curry_recipe["liquid"] = "water"

print(f"curry_recipe : {curry_recipe ['base']}")
print(f"curry_recipe : {curry_recipe}")

del curry_recipe["liquid"]
print(f"curry_recipe : {curry_recipe}")
#membership operator {in}
print(f"is the corrinder present? {'corrinder' in curry_recipe}")

chai_order = {"type": "Ginger Chai", "size": "Medium","sugar": 1}

# print(f"Order details (keys): {chai_order.keys()}")
# print(f"Order details (values): {chai_order.values()}")
# print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"removed last item :{last_item}")

extra_spices = {"ginger": "sliced", "cardamom": "crushed"}
curry_recipe.update(extra_spices)
print(f"curry_recipe : {curry_recipe}")

customer_ticket = chai_order["size"]
print(f"customer_ticket : {customer_ticket}")

customer_ticket = chai_order.get("note","no note ")
print(f"customer_ticket : {customer_ticket}")

customer_ticket = chai_order.get("size","no note ")
print(f"customer_ticket : {customer_ticket}")








# Step 1: Create a customer dictionary with name, age, and city
customer = {
    "name": "John Doe",
    "age": 32,
    "city": "New York"
}

# Step 2: Add email and phone

# Step 3: Print customer's name and city

# Step 4: Check if "email" exists

# Step 5: Delete the "age" field

# Step 6: Print all keys, values, and items

# Step 7: Remove and print the last inserted item

# Step 8: Use .get() to access "membership"

# Step 9: Update dictionary with "address"

# Step 10: Print final dictionary

customer =  dict(name="john doe",age="32",city="newyork")
print(f"customer details : {customer}")

customer["email"] = "john.doe@example.com"
customer["phone"] = "123-456-7890"
print(f"updated dictionary : {customer}")
