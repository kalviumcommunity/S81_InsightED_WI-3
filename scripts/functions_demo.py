# scripts/functions_demo.py

# 1. Defining a function with parameters
def greet_user(name, role):
    """Prints a personalized greeting."""
    print(f"Hello, {name}! Welcome to your role as a {role}.")

def calculate_discount(price, discount_percentage):
    """Calculates and prints the discounted price."""
    discount_amount = price * (discount_percentage / 100)
    final_price = price - discount_amount
    print(f"Original Price: ${price:.2f}")
    print(f"Discount: {discount_percentage}%")
    print(f"Final Price after discount: ${final_price:.2f}\n")

def main():
    print("--- Python Functions Demo ---\n")
    
    # 2. Calling functions and passing arguments
    print("Calling greet_user function...")
    greet_user("Alice", "Data Analyst")
    
    print("\nCalling calculate_discount function directly...")
    calculate_discount(150.0, 15)
    
    print("Calling calculate_discount function with different arguments...")
    calculate_discount(300.5, 20)
    
    print("--- Demo Completed ---")

# Best practice: separating definition from execution
if __name__ == "__main__":
    main()
