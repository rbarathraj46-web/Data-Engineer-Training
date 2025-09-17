import json

with open("products.json", "r") as file:
    products = json.load(file)
print("Available Products:")
for p in products:
    print(f"  {p["name"]} ({p["category"]})")

print("\nInventory Values")
for p in products:
    total_value = p["price"] * p["stock"]
    print(f"{p["name"]} = ${total_value}")

out_of_stock = [p["name"] for p in products if p["stock"] == 0]
if out_of_stock:
    print(f"\nOut of Stock",",".join(out_of_stock))
else:
    print("\nAll products are in Stock.")