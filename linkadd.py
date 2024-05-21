import json

file_path = "create1.json"

# Read 
with open(file_path, "r") as json_file:
    data = json.load(json_file)

# Extract values 
name = data["name"]
age = data["age"]
city = data["city"]
email = data["email"]
is_employee = data["is_employee"]
purchase = data["purchase"]
languages = data["languages"]
address = data["address"]


# Print 
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Email:", email)
print("Is Student:", "Yes" if is_employee else "No")
print("Purhase:")

for products, amount in purchase.items():
    print(f"- {products}: {amount}")
    
print("Address:")
print(f"- Street: {address['street']}")
print(f"- City: {address['city']}")
print(f"- Zip Code: {address['zip_code']}")
