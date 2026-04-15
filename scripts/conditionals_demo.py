# scripts/conditionals_demo.py

def main():
    print("--- Python Conditionals Demo ---\n")

    # Sample Data
    temperature = 25
    weather = "sunny"
    is_weekend = True

    # 1. Basic if statement
    print("1. Basic if statement:")
    if temperature > 20:
        print("It's a warm day.")
    
    # 2. if-else for Decision Branching
    print("\n2. if-else statement:")
    if weather == "rainy":
        print("Remember to bring an umbrella.")
    else:
        print("No umbrella needed today.")

    # 3. Handling Multiple Conditions with elif
    print("\n3. if-elif-else statement:")
    user_age = 20
    if user_age < 13:
        print("User category: Child")
    elif user_age < 20:
        print("User category: Teenager")
    elif user_age < 65:
        print("User category: Adult")
    else:
        print("User category: Senior")

    # 4. Using Logical Operators (and, or, not)
    print("\n4. Logical Operators (and, or, not):")
    
    # 'and' operator
    if temperature > 20 and weather == "sunny":
        print("Perfect weather for a beach trip!")
        
    # 'or' operator
    if weather == "rainy" or weather == "snowy":
        print("You'll probably want to stay indoors.")
    else:
        print("Great day to be outside!")
        
    # 'not' operator combined with 'and'
    if is_weekend and not (weather == "rainy"):
        print("It's the weekend and it's not raining, let's go hiking!")

    print("\n--- Demo Completed ---")

if __name__ == "__main__":
    main()
