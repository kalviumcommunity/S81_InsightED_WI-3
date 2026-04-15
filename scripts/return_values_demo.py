# scripts/return_values_demo.py

def calculate_monthly_revenue(sales, price_per_unit):
    """
    Accepts the number of sales and unit price, 
    and returns the total revenue.
    """
    total_revenue = sales * price_per_unit
    return total_revenue

def apply_tax(revenue, tax_rate):
    """
    Accepts total revenue and tax rate, 
    returns the actual net profit after deducting tax.
    """
    tax_amount = revenue * (tax_rate / 100)
    net_profit = revenue - tax_amount
    return net_profit

def main():
    print("--- Python Function Returns Demo ---\n")
    
    # 1. Calling function and passing arguments
    units_sold = 1500
    price = 25.50
    
    # Storing returned value in a variable
    gross_revenue = calculate_monthly_revenue(units_sold, price)
    print(f"Gross Revenue (calculated): ${gross_revenue:.2f}")
    
    # 2. Reusing the returned value meaningfully
    # Passing the returned gross_revenue variable into another function
    tax_rate = 15.0 # 15% tax
    net_profit = apply_tax(gross_revenue, tax_rate)
    print(f"Tax Rate: {tax_rate}%")
    print(f"Net Profit (after tax): ${net_profit:.2f}")

    print("\n--- Demo Completed ---")

if __name__ == "__main__":
    main()
