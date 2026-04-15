# scripts/loops_demo.py

def main():
    print("--- Python Loops Demo ---\n")

    # 1. for loop iterating over a sequence
    print("1. For loop over a list:")
    data_points = [10, 25, 5, 80, 15]
    for value in data_points:
        print(f"Processing data point: {value}")

    # 2. Control flow with 'continue' and 'break' inside a for loop
    print("\n2. For loop with 'continue' and 'break':")
    for value in data_points:
        if value < 10:
            print(f"Skipping small data point: {value}")
            continue  # Skips the rest of the loop for this iteration
        
        if value > 50:
            print(f"Aborting loops - encountered unusually large data point: {value}")
            break     # Exits the loop entirely
        
        print(f"Acceptable value logged: {value}")

    # 3. while loop with clear termination condition
    print("\n3. While loop with precise termination:")
    retry_count = 0
    max_retries = 3
    
    while retry_count < max_retries:
        print(f"Attempting data fetch... (Attempt {retry_count + 1} of {max_retries})")
        # Simulating work by incrementing immediately
        retry_count += 1
        
        if retry_count == 2:
            print("Fetch successful on attempt 2.")
            break
            
    print("\n--- Demo Completed ---")

if __name__ == "__main__":
    main()
