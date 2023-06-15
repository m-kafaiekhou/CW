

class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Order:
    def __init__(self, order_number, customer, product, quantity):
        self.order_number = order_number
        self.customer = customer
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def remove_item(self, product):
        for item in self.items:
            if item[0] == product:
                self.items.remove(item)

    def update_quantity(self, product, quantity):
        for item in self.items:
            if item[0] == product:
                item[1] = quantity

    def view_cart(self):
        for item in self.items:
            print(f"{item[0].name}: {item[1]}")

    def checkout(self, customer):
        order_number = "?"
        for item in self.items:
            order = Order(order_number, customer, item[0], item[1])
            customer.add_to_order_history(order)
        self.items = []


class Customer(ShoppingCart):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)

p = Product("car", "ahmad", 100, 10)
c = Customer("ali", "tehran")
c.add_item(p, )




