# scripts/basic_analysis.py

def main():
    # 1. Define variables and sample data
    print("--- Starting Basic Data Analysis ---")
    
    # A simple dataset represented as a list of dictionaries
    sales_data = [
        {"month": "January", "sales": 1500},
        {"month": "February", "sales": 1800},
        {"month": "March", "sales": 1200},
        {"month": "April", "sales": 2100},
        {"month": "May", "sales": 1750}
    ]
    
    print(f"Loaded {len(sales_data)} records for analysis.\n")
    
    # 2. Simple calculations
    total_sales = 0
    highest_sale = 0
    best_month = ""
    
    for record in sales_data:
        amount = record["sales"]
        month = record["month"]
        
        # Calculate total
        total_sales += amount
        
        # Find maximum sale
        if amount > highest_sale:
            highest_sale = amount
            best_month = month
            
    # Calculate average
    average_sales = total_sales / len(sales_data)
    
    # 3. Print outputs
    print("--- Analysis Results ---")
    print(f"Total Sales: ${total_sales}")
    print(f"Average Sales: ${average_sales:.2f}")
    print(f"Best Month: {best_month} with ${highest_sale} in sales")
    
    print("--- Analysis Complete ---")

if __name__ == "__main__":
    main()
