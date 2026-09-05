#sets {}
#intresection is between the two sets (&)this symbol is use dfor the intersection o f two sets 
#union the whole sets of two sets (|)this is the pie or union we called

coffee_essentials = {"coffee powder","sugar","milk"}
extra_essentials = {"water","chocalte syrup","sugar"}

all_spices = coffee_essentials | extra_essentials
print(f"all_spices: {all_spices}")

common_spices = coffee_essentials & extra_essentials
print(f"common_spices : {common_spices}")

# removing the common spices from the coffee_essentials set
difference_spices = coffee_essentials - extra_essentials
print(f"difference_spices : {difference_spices}")

#membership test 
print(f"is 'milk' in extra_essentials? : { 'milk' in coffee_essentials}")
#frozenset is immutable set we can not add or remove the elements from the frozen set


essential_spices = frozenset(["coffee powder","sugar","milk"])
print(f"essential_spices : {essential_spices}")

essential_spices.add("ice")
print(f"essential_spices : {essential_spices}")

