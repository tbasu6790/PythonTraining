'''
SCENARIO : You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
Q1. Product Search System (Static Polymorphism)
Problem Statement:
Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
Requirements:
Use default arguments and/or *args, **kwargs to simulate method overloading.
Allow the following types of searches: 
-Only by name
-Name and category
-Name, category, and price range
 
Q2. Cart System with Quantity Variations (Static Polymorphism)
Problem Statement:
Design a class Cart that can add multiple products with variable quantities using *args or **kwargs. 
Requirements:
Add multiple products at once with name and quantity
Simulate static polymorphism using variable arguments 

Q3. Discount Application (Static Polymorphism) 
Problem Statement:
Create a class Discount that allows applying different types of discounts: 
Flat discount 
Percentage discount 
Buy One Get One
Use static polymorphism to overload the method using default parameters or *args
 
Q4. Payment System (Dynamic Polymorphism) 
Problem Statement:
Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
Requirements:
Override pay() method in each class to simulate different payment methods
'''

# Q1. Product Search System
# ================================
class ProductSearch:
    def __init__(self, products):
        self.products = products  # products is a list of dicts

    def search(self, name=None, category=None, price_range=None):
        results = self.products

        if name:
            results = [p for p in results if p["name"].lower() == name.lower()]
        if category:
            results = [p for p in results if p["category"].lower() == category.lower()]
        if price_range:
            low, high = price_range
            results = [p for p in results if low <= p["price"] <= high]

        return results


# Q2. Cart System
# ================================
class Cart:
    def __init__(self):
        self.items = {}  # {product_name: quantity}

    def add_items(self, *args, **kwargs):
        """
        *args → list of tuples (name, qty)
        **kwargs → key=product name, value=qty
        """
        for item in args:
            name, qty = item
            self.items[name] = self.items.get(name, 0) + qty

        for name, qty in kwargs.items():
            self.items[name] = self.items.get(name, 0) + qty

    def show_cart(self):
        print("=== Cart Items ===")
        for name, qty in self.items.items():
            print(f"{name}: {qty}")


# Q3. Discount Application
# ================================
class Discount:
    def apply(self, price, *args, discount_type="flat"):
        if discount_type == "flat":
            discount = args[0] if args else 0
            return max(0, price - discount)

        elif discount_type == "percentage":
            percent = args[0] if args else 0
            return price - (price * percent / 100)

        elif discount_type == "bogo":
            qty = args[0] if args else 1
            # For Buy 1 Get 1, effectively half the price for even qty
            return (qty // 2 + qty % 2) * price

        else:
            return price

# Q4. Payment System (Dynamic Polymorphism)
# ================================
class Payment:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must override pay()")


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class CODPayment(Payment):
    def pay(self, amount):
        print(f"Cash of ₹{amount} will be collected on delivery.")

# Example Usage
# ================================
if __name__ == "__main__":
    # Q1 Product Search
    products = [
        {"name": "Laptop", "category": "Electronics", "price": 55000},
        {"name": "Phone", "category": "Electronics", "price": 20000},
        {"name": "Shirt", "category": "Fashion", "price": 1500},
        {"name": "Shoes", "category": "Fashion", "price": 3000},
    ]
    ps = ProductSearch(products)
    print("\nQ1 Search Results:")
    print(ps.search(name="Laptop"))
    print(ps.search(name="Shirt", category="Fashion"))
    print(ps.search(category="Electronics", price_range=(10000, 30000)))

    # Q2 Cart
    print("\nQ2 Cart Example:")
    cart = Cart()
    cart.add_items(("Laptop", 1), ("Shirt", 2), Phone=1, Shoes=3)
    cart.show_cart()

    # Q3 Discount
    print("\nQ3 Discount Example:")
    d = Discount()
    print("Flat discount:", d.apply(1000, 200, discount_type="flat"))
    print("Percentage discount:", d.apply(2000, 10, discount_type="percentage"))
    print("BOGO (buy 1 get 1, qty=3):", d.apply(500, 3, discount_type="bogo"))

    # Q4 Payment
    print("\nQ4 Payment Example:")
    payments = [CreditCardPayment(), UPIPayment(), CODPayment()]
    for method in payments:
        method.pay(1500)
