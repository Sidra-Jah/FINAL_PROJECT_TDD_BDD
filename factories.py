# factories.py

import random

# Function to generate fake product data
def generate_fake_product():
    # Sample product names
    product_names = ["Widget", "Gadget", "Thingamajig", "Doodad", "Contraption"]
    product_price = round(random.uniform(5.00, 100.00), 2)  # Random price between 5.00 and 100.00
    product_name = random.choice(product_names)  # Select a random product name
    
    # Return product data as a dictionary
    return {
        "name": product_name,
        "price": product_price
    }

# Function to print fake product details
def print_fake_product():
    product = generate_fake_product()
    print("Product Name:", product["name"])
    print("Product Price: $", product["price"])

# Run the function to display a fake product
if __name__ == "__main__":
    print_fake_product()
