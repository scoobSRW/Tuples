orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Scotty", "AirPods", 3),
    ("Robert", "Beats", 15),
]

def display_orders(orders):
    for customer_name, product, quantity in orders:
        print(f"{customer_name} ordered {quantity} {product}(s).")

# Call the function to display the orders
display_orders(orders)
