import csv
import json
import statistics
from pathlib import Path

class Product:
    def __init__(self, product_id, name, category, price, stock):
        self.id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_stock(self, qty):
        if qty <= self.stock:
            self.stock -= qty
        else:
            raise ValueError(f"Not enough stock for {self.name}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []  # list of Order objects

    def add_order(self, order):
        self.orders.append(order)


class Order:
    def __init__(self, order_id, customer, items):
        # items = list of {"product": Product, "qty": int}
        self.order_id = order_id
        self.customer = customer
        self.items = items

    def get_total(self):
        return sum(item["product"].price * item["qty"] for item in self.items)


def load_products(filepath="products.csv"):
    products = {}
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products[int(row["id"])] = Product(
                int(row["id"]),
                row["name"],
                row["category"],
                float(row["price"]),
                int(row["stock"])
            )
    return products


def save_products(products, filepath="products.csv"):
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "category", "price", "stock"])
        writer.writeheader()
        for p in products.values():
            writer.writerow({
                "id": p.id, "name": p.name, "category": p.category,
                "price": p.price, "stock": p.stock
            })



def load_orders(filepath="orders.json", products=None):
    with open(filepath, "r") as f:
        data = json.load(f)

    orders = []
    for o in data:
        items = [{"product": products[i["product_id"]], "qty": i["qty"]} for i in o["items"]]
        customer = Customer(o["customer"])
        order = Order(o["order_id"], customer, items)
        customer.add_order(order)
        orders.append(order)
    return orders


def save_orders(orders, filepath="orders.json"):
    data = []
    for o in orders:
        items = [{"product_id": item["product"].id, "qty": item["qty"]} for item in o.items]
        data.append({
            "order_id": o.order_id,
            "customer": o.customer.name,
            "items": items
        })
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def generate_sales_report(orders):
    total_revenue = 0
    revenue_per_category = {}
    customer_spending = {}

    for o in orders:
        total = o.get_total()
        total_revenue += total

        for item in o.items:
            cat = item["product"].category
            revenue_per_category[cat] = revenue_per_category.get(cat, 0) + item["product"].price * item["qty"]

        customer_spending[o.customer.name] = customer_spending.get(o.customer.name, 0) + total

    top_customer = max(customer_spending, key=customer_spending.get)

    return {
        "total_revenue": total_revenue,
        "revenue_per_category": revenue_per_category,
        "top_customer": (top_customer, customer_spending[top_customer])
    }


def generate_inventory_report(products):
    low_stock = [p.name for p in products.values() if p.stock < 5]

    prices_by_cat = {}
    for p in products.values():
        prices_by_cat.setdefault(p.category, []).append(p.price)
    avg_price = {cat: statistics.mean(prices) for cat, prices in prices_by_cat.items()}

    return {
        "low_stock_products": low_stock,
        "avg_price_by_category": avg_price
    }

def menu():
    products = load_products()
    orders = load_orders(products=products)

    while True:
        print("\n--- E-Commerce Order Management ---")
        print("1. View Products")
        print("2. Place New Order")
        print("3. View All Orders")
        print("4. Generate Reports")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            for p in products.values():
                print(f"{p.id}. {p.name} ({p.category}) - Price: {p.price}, Stock: {p.stock}")

        elif choice == "2":
            order_id = max((o.order_id for o in orders), default=100) + 1
            customer_name = input("Enter customer name: ")
            items = []
            while True:
                pid = int(input("Enter product id (0 to finish): "))
                if pid == 0:
                    break
                qty = int(input("Enter quantity: "))
                if pid in products:
                    try:
                        products[pid].update_stock(qty)
                        items.append({"product": products[pid], "qty": qty})
                    except ValueError as e:
                        print(e)
                else:
                    print("Invalid product id")

            if items:
                customer = Customer(customer_name)
                new_order = Order(order_id, customer, items)
                customer.add_order(new_order)
                orders.append(new_order)
                save_products(products)
                save_orders(orders)
                print(f"Order {order_id} placed. Total: {new_order.get_total()}")

        elif choice == "3":
            for o in orders:
                print(f"Order {o.order_id} by {o.customer.name}, Total: {o.get_total()}")
                for item in o.items:
                    print(f"  - {item['product'].name} x {item['qty']}")

        elif choice == "4":
            print("\n--- Sales Report ---")
            sales = generate_sales_report(orders)
            print("Total Revenue:", sales["total_revenue"])
            print("Revenue per Category:", sales["revenue_per_category"])
            print("Top Customer:", sales["top_customer"])

            print("\n--- Inventory Report ---")
            inv = generate_inventory_report(products)
            print("Low Stock Products:", inv["low_stock_products"])
            print("Average Price by Category:", inv["avg_price_by_category"])

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    # Ensure files exist
    if not Path("products.csv").exists():
        with open("products.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "name", "category", "price", "stock"])
            writer.writeheader()

    if not Path("orders.json").exists():
        with open("orders.json", "w") as f:
            json.dump([], f)

    menu()