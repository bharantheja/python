ingredients = ["maggi","masala","water","ketchup"]
ingredients.append("vegetables")
print(f"ingredients are : {ingredients}")
ingredients.remove("ketchup")
print(f"ingredients are : {ingredients}")

spices_options = ["Salt", "Cardamom","garam masala"]
maggie_sauces = ["chilli sauce","soyy sauce"]

maggie_sauces.extend(spices_options)
print(f"maggie items are : {maggie_sauces}")

maggie_sauces.insert(4,"lemon")
print(f"maggie :{maggie_sauces}")

last_added = maggie_sauces.pop()
print(f"{last_added}")
print(f"maggie :{maggie_sauces}")

maggie_sauces.reverse()
print(f"maggie :{maggie_sauces}")

maggie_sauces.sort()
print(f"maggie :{maggie_sauces}")

spicy_level = [1,2,3,4,5,]
print(f"maximum spicy level is : {max(spicy_level)}")
print(f"minimum spicy level is : {min(spicy_level)}")

#operator overloading doing the more than one task by uusing the operators we can easily concat the two or more operands/.
maggie_mix = ["water","soya sauce"]
extra_flavor = ["chilli sauce","vinegar"]

full_liquid_mix = maggie_mix + extra_flavor
print(f"liqiud mix : {full_liquid_mix}")

strong_brew = ["coffee","water"] * 3
print(f"strong brew : {strong_brew}")

ingredients.concat("jam","butter")
ingeredits.dupli
