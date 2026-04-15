# scripts/pep8_readability_demo.py

def calculate_discounted_price(original_price, discount_percentage):
    """
    Calculates the final price of an item after applying a discount.
    """
    
    # We validate the discount percentage to ensure we don't accidentally
    # increase the price or yield a negative cost.
    if discount_percentage < 0 or discount_percentage > 100:
        return original_price
        
    discount_amount = original_price * (discount_percentage / 100)
    final_price = original_price - discount_amount
    
    return final_price

def main():
    print("--- PEP8 Readability and Naming Demo ---\n")
    
    # Bad Example (do not use):
    # p = 150
    # d = 20
    # fp = p - (p * (d / 100))
    # print(fp) # What do 'p', 'd', and 'fp' mean without context?
    
    # Good Example (using descriptive variable names and PEP 8 snake_case)
    laptop_retail_price = 1200.00
    holiday_discount_percentage = 15.0
    
    final_laptop_price = calculate_discounted_price(
        laptop_retail_price, 
        holiday_discount_percentage
    )
    
    print(f"Original Price: ${laptop_retail_price:.2f}")
    print(f"Discount Applied: {holiday_discount_percentage}%")
    print(f"Final Price: ${final_laptop_price:.2f}")
    
    print("\n--- Demo Completed ---")

if __name__ == "__main__":
    main()
