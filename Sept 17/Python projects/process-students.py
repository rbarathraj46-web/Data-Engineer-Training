import json

with open("students.json", "r") as file:
    students = json.load(file)
print("All Students:")
for s in students:
    print(" ", s["name"])

print("\nMarks summary:")
for s in students:
    total = sum(s["marks"].values())
    avg = total / len(s["marks"])
    print(f"   {s['name']} -> Total:{total}, Average:{avg:.2f}")