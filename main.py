from make_objects import *


store.show_products()
print("----------------")
laptop.update_stock(-9)
# store.remove_product(laptop)
store.show_products()
print("----------------")
print(george.add_to_cart(laptop, 3))
print("----------------")
print(george.remove_from_cart(laptop,1))
print("----------------")
print(george.add_to_cart(laptop,2))
print("----------------")
print("----------------")
george.show_cart()
print("----------------")
print(george.checkout())
store.show_products()