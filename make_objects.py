from shopping_system import *


george = Customer("George")
laptop = Product("Laptop", 2000, 6)
mouse = Product("Mouse", 60, 10)
charger = Product("Charger", 14.99, 4)

store = Store()
store.add_product(laptop)
store.add_product(mouse)
store.add_product(charger)
