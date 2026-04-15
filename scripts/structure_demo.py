"""
This script demonstrates how to properly structure Python code for readability and reuse.
It follows the standard structure:
1. Imports (if any)
2. Reusable Functions
3. Execution Logic (main)
"""

# ---------------------------------------------------------
# 1. Imports (None strictly required, but usually placed here)
# ---------------------------------------------------------
import math

# ---------------------------------------------------------
# 2. Reusable Functions (Logic separated from execution)
# ---------------------------------------------------------
def process_user_data(raw_data):
    """
    Cleans and processes raw user data.
    By putting this in a function, we avoid repeating this block.
    """
    cleaned_data = raw_data.strip().lower()
    return cleaned_data

def calculate_bmi(weight_kg, height_m):
    """
    Calculates Body Mass Index (BMI).
    """
    if height_m <= 0:
        return 0
    return weight_kg / math.pow(height_m, 2)

def display_user_stats(name, bmi):
    """
    Prints the user statistics uniformly. 
    """
    print(f"User: {name.capitalize()} | BMI: {bmi:.2f}")

# ---------------------------------------------------------
# 3. Main Execution Function
# ---------------------------------------------------------
def main():
    print("--- Code Structure Demo ---\n")
    
    # Setup data
    user_1_raw = "  ALICE  "
    user_2_raw = "  BoB "
    
    # Process data using the reusable function instead of duplicating .strip().lower()
    user_1_clean = process_user_data(user_1_raw)
    user_2_clean = process_user_data(user_2_raw)
    
    # Calculate metrics
    bmi_alice = calculate_bmi(68.0, 1.65)
    bmi_bob = calculate_bmi(85.0, 1.80)
    
    # Output using reusable display function
    display_user_stats(user_1_clean, bmi_alice)
    display_user_stats(user_2_clean, bmi_bob)
    
    print("\n--- Demo Completed ---")

# ---------------------------------------------------------
# 4. Standard Python Entry Point
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
