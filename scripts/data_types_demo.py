# scripts/data_types_demo.py

def main():
    print("--- Python Numeric and String Data Types Demo ---\n")

    # 1. Integer and floating-point variables
    items_sold = 150 # Integer
    price_per_item = 19.99 # Float
    
    print("1. Numeric Data Types:")
    print(f"Items sold (int): {items_sold}, Type: {type(items_sold)}")
    print(f"Price per item (float): ${price_per_item}, Type: {type(price_per_item)}")

    # Arithmetic operations on numeric types
    total_revenue = items_sold * price_per_item
    print(f"Total Revenue (items_sold * price_per_item) = ${total_revenue:.2f}\n")

    # 2. String variables with meaningful values
    product_name = "Wireless Headphones"
    store_location = "New York Branch"

    print("2. String Data Types:")
    # String concatenation
    delivery_note = product_name + " shipping from " + store_location
    print("Concatenation output:", delivery_note)

    # String formatting
    summary = f"Store: {store_location} | Product: {product_name} | Revenue: ${total_revenue:.2f}"
    print("Formatting output:", summary, "\n")

    # 3. Type mismatch and Conversion
    print("3. Type Mismatch and Conversion:")
    
    # Simulating data being read as strings (common when reading from CSV or input)
    string_quantity = "50"
    string_price = "25.50"

    print(f"Original string values: quantity='{string_quantity}', price='{string_price}'")

    try:
        # Example showing an error or incorrect behavior (Type Mismatch)
        # Attempting arithmetic with strings will throw an error or do string repetition/concatenation
        bad_total = string_quantity + string_price 
        print(f"Unexpected behavior if treated as strings (concatenation instead of addition): {string_quantity} + {string_price} = {bad_total}")
    except Exception as e:
        print("Error:", e)

    # Correcting the issue with explicit conversion
    actual_quantity = int(string_quantity)
    actual_price = float(string_price)
    correct_total = actual_quantity * actual_price

    print(f"Correct arithmetic after conversion (int * float): {actual_quantity} * {actual_price} = {correct_total}")

if __name__ == "__main__":
    main()
