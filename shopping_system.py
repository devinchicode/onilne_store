class Product:
    def __init__(self, product_name: str, price: float, quantity: int):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.is_available = False

    def __str__(self):
        return f"{self.product_name}, price: {self.price}$, items available:{self.quantity}"

    def update_stock(self, quantity_amount: int):
        if self.quantity + quantity_amount < 0:
            return f"Sorry, you have just {self.quantity} items."

        self.quantity += quantity_amount


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.cart = {}

    def add_to_cart(self, product, quantity):
        if quantity <= 0:
            return f"You must add to cart number of items greater than 0."
        if not product.is_available:
            return "Sorry, this item isn't available right now."

        if product.quantity - quantity < 0:
            return f"The maximum quantity you can buy: {product.quantity}"

        else:
            if product not in self.cart:
                self.cart[product] = 0
            saved_quantity = quantity
            self.cart[product] += quantity
            product.update_stock(-quantity)
            return f"added to your cart:{saved_quantity} items of {product.product_name}"

    def remove_from_cart(self, product, quantity):
        if self.cart.get(product) == 0 or product not in self.cart:
            return "You don't have items of this product in your cart."

        elif quantity > self.cart.get(product):
            return f"You have {self.cart.get(product)} items of {product.product_name} in your cart."

        else:
            self.cart[product] -= quantity
            if self.cart[product] == 0:
                self.cart.pop(product)

            return f"{quantity} items of {product.product_name} has been removed."

    def show_cart(self):
        if not self.cart:
            return "Your cart is empty."
        
        for product in self.cart:
            print(f"{product.product_name}, {self.cart[product]} items, price per item: {product.price}$")

    def checkout(self):
        bill = 0
        for product in self.cart:
            if self.cart[product] == 0:
                continue
            bill += product.price * self.cart[product]
        self.cart.clear()
        return f"You need to pay: {bill}$"


class Store:
    def __init__(self):
        self.items_quantity = {}
        self.items_price = {}

    def add_product(self, product):
        if product:
            self.items_price[product] = product.price
            self.items_quantity[product] = product.quantity
            product.is_available = True
            return f"item {product} added successfully.\nquantity: {product.quantity}.\nprice:{product.price}."
        else:
            return False

    def remove_product(self, product):
        self.items_price.pop(product)
        self.items_quantity.pop(product)
        product.is_available = False
        return f"item {product} removed successfully."

    def show_products(self):
        for product in self.items_quantity:
            print(product)
