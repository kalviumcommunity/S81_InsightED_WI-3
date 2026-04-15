# scripts/collections_demo.py

def main():
    print("--- Python Collections Demo ---\n")

    # 1. Lists (Ordered, Mutable)
    print("1. Lists (Mutable):")
    data_columns = ["age", "income", "credit_score"]
    print(f"Original List: {data_columns}")
    
    # Access element using index
    print(f"Second column is: {data_columns[1]}")
    
    # Modify list: add and update elements
    data_columns.append("loan_amount") # Add
    data_columns[0] = "customer_age" # Modify
    print(f"Modified List: {data_columns}\n")

    # 2. Tuples (Ordered, Immutable)
    print("2. Tuples (Immutable):")
    database_config = ("localhost", 5432, "admin_user")
    print(f"Original Tuple: {database_config}")
    
    # Access element using index
    print(f"Port number is: {database_config[1]}")
    
    # Demonstrate immutability
    try:
        print("Attempting to modify the tuple...")
        database_config[0] = "127.0.0.1"
    except TypeError as e:
        print(f"Error caught! Tuples cannot be modified: {e}\n")

    # 3. Dictionaries (Key-Value, Mutable)
    print("3. Dictionaries (Key-Value):")
    model_metrics = {
        "accuracy": 0.85,
        "precision": 0.81,
        "recall": 0.89
    }
    print(f"Original Dictionary: {model_metrics}")
    
    # Access value using key
    print(f"Model Accuracy: {model_metrics['accuracy']}")
    
    # Modify dictionary: update and add key-value pairs
    model_metrics["accuracy"] = 0.87 # Modify
    model_metrics["f1_score"] = 0.84 # Add new key
    print(f"Modified Dictionary: {model_metrics}\n")

    print("- Demo Completed -")

if __name__ == "__main__":
    main()
