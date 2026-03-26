"""
Smart Cafe Management System - Compact Version
Maintains all core features: CRUD, ML, Simulation, Analytics
"""

import datetime
import random
import logging
from collections import defaultdict
from typing import List, Dict, Tuple

# Configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Data Storage
MENU_ITEMS = {
    1: {"name": "Coffee", "price": 50, "category": "beverage", "stock": 100},
    2: {"name": "Tea", "price": 30, "category": "beverage", "stock": 80},
    3: {"name": "Pastry", "price": 200, "category": "food", "stock": 50}
}
ORDERS_DB = []
CUSTOMER_PREFERENCES = {}

class Repository:
    """Data access layer"""
    @staticmethod
    def save_order(order_data: Dict) -> bool:
        ORDERS_DB.append(order_data)
        logging.info(f"Order saved: {order_data['customer_name']}")
        return True
    
    @staticmethod
    def get_daily_revenue() -> int:
        return sum(order["total_amount"] for order in ORDERS_DB)

class Recommender:
    """ML recommendation strategies"""
    @staticmethod
    def get_recommendation(customer_name: str) -> str:
        # Preference-based
        if customer_name in CUSTOMER_PREFERENCES:
            category = CUSTOMER_PREFERENCES[customer_name]["preferred_category"]
            items = [item for item in MENU_ITEMS.values() if item["category"] == category and item["stock"] > 0]
            if items: 
                recommended = random.choice(items)
                return f"Based on your preferences, try our {recommended['name']}!"
        
        # Popular items - FIXED: Handle case where no orders exist
        if ORDERS_DB:
            popular = defaultdict(int)
            for order in ORDERS_DB:
                for item in order["items"]:
                    popular[item[0]] += item[1]  # item[0] is the item name
            
            if popular: 
                recommended_item = max(popular.items(), key=lambda x: x[1])[0]
                return f"Popular choice: {recommended_item}!"
        
        # Random fallback - FIXED: Handle case where no items available
        available = [item for item in MENU_ITEMS.values() if item["stock"] > 0]
        if available:
            recommended = random.choice(available)
            return f"We recommend: {recommended['name']}!"
        
        return "No recommendations available right now."

def classify_customer(total_spent: int, orders: int) -> str:
    """Customer classification"""
    if total_spent > 1000 and orders > 5: 
        return "VIP Customer"
    elif total_spent > 500: 
        return "Regular Customer"
    elif total_spent > 100: 
        return "Occasional Customer"
    return "New Customer"

# CRUD Operations
def create_item():
    """Create new menu item"""
    try:
        name = input("Item name: ").strip()
        if not name:
            print("Error: Item name cannot be empty!")
            return
            
        price = int(input("Price: "))
        if price <= 0:
            print("Error: Price must be positive!")
            return
            
        category = input("Category (beverage/food): ").strip().lower()
        if category not in ["beverage", "food"]:
            print("Error: Category must be 'beverage' or 'food'!")
            return
            
        stock = int(input("Stock: "))
        if stock < 0:
            print("Error: Stock cannot be negative!")
            return
        
        new_id = max(MENU_ITEMS.keys()) + 1
        MENU_ITEMS[new_id] = {"name": name, "price": price, "category": category, "stock": stock}
        print(f"Added {name}!")
        
    except ValueError:
        print("Error: Please enter valid numbers for price and stock!")

def read_menu(admin=False):
    """Display menu"""
    if admin:
        print("\n--- MENU INVENTORY ---")
        print(f"{'ID':<3} {'Name':<10} {'Price':<6} {'Stock':<6} {'Category':<10}")
        print("-" * 40)
        for id, item in MENU_ITEMS.items():
            print(f"{id:<3} {item['name']:<10} Rs{item['price']:<4} {item['stock']:<6} {item['category']:<10}")
    else:
        print("\n--- MENU ---")
        available_items = [item for item in MENU_ITEMS.values() if item["stock"] > 0]
        if not available_items:
            print("Sorry, all items are currently out of stock!")
            return
            
        for id, item in MENU_ITEMS.items():
            if item["stock"] > 0:
                print(f"{id}. {item['name']:<10} - Rs {item['price']}")

def update_item():
    """Update menu item"""
    try:
        id = int(input("Item ID to update: "))
        if id not in MENU_ITEMS:
            print("Error: Item not found!")
            return
        
        print(f"Current: {MENU_ITEMS[id]}")
        field = input("Field to update (name/price/category/stock): ").strip()
        if field not in ["name", "price", "category", "stock"]:
            print("Error: Invalid field!")
            return
        
        value = input("New value: ").strip()
        
        # Validate based on field type
        if field in ["price", "stock"]:
            value = int(value)
            if value < 0:
                print("Error: Value cannot be negative!")
                return
        elif field == "category":
            if value not in ["beverage", "food"]:
                print("Error: Category must be 'beverage' or 'food'!")
                return
        elif field == "name":
            if not value:
                print("Error: Name cannot be empty!")
                return
        
        MENU_ITEMS[id][field] = value
        print("Item updated!")
        
    except ValueError:
        print("Error: Please enter valid input!")

def delete_item():
    """Delete menu item"""
    try:
        id = int(input("Item ID to delete: "))
        if id in MENU_ITEMS:
            name = MENU_ITEMS[id]["name"]
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ").lower()
            if confirm == 'y':
                del MENU_ITEMS[id]
                print(f"Deleted {name}!")
            else:
                print("Deletion cancelled.")
        else:
            print("Error: Item not found!")
    except ValueError:
        print("Error: Please enter a valid ID!")

def admin_menu():
    """Admin CRUD interface"""
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Add Item")
        print("2. View All Items") 
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Back to Main Menu")
        
        choice = input("Choice: ").strip()
        
        if choice == "1": 
            create_item()
        elif choice == "2": 
            read_menu(admin=True)
        elif choice == "3": 
            update_item()
        elif choice == "4": 
            delete_item()
        elif choice == "5": 
            break
        else: 
            print("Error: Invalid choice!")

# Order Processing
def take_order():
    """Process customer order"""
    items = []
    total = 0
    
    name = input("Customer name: ").strip()
    if not name:
        name = "Guest"
        print("Note: Using 'Guest' as customer name")

    while True:
        read_menu()  # Show customer menu
        if not any(item["stock"] > 0 for item in MENU_ITEMS.values()):
            print("No items available for order!")
            break
            
        print("4. Finish Order")
        print("5. Get Recommendation")
        choice = input("Please select (1-5): ").strip()
        
        if choice == "4": 
            break
        elif choice == "5": 
            recommendation = Recommender.get_recommendation(name)
            print(f"{recommendation}")
            continue
        
        try:
            item_id = int(choice)
            if item_id not in MENU_ITEMS:
                print("Error: Please select a valid menu item!")
                continue
            
            item = MENU_ITEMS[item_id]
            if item["stock"] <= 0:
                print(f"Sorry, {item['name']} is out of stock!")
                continue
            
            qty_input = input(f"Enter quantity for {item['name']}: ").strip()
            if not qty_input.isdigit():
                print("Error: Please enter a valid number!")
                continue
                
            qty = int(qty_input)
            if qty <= 0:
                print("Error: Quantity must be positive!")
                continue
            if qty > item["stock"]:
                print(f"Error: Only {item['stock']} items available!")
                continue
            
            # Calculate and add to order
            item_total = item["price"] * qty
            items.append([item["name"], qty, item["price"], item_total])
            total += item_total
            item["stock"] -= qty  # Update inventory
            print(f"Added {qty} x {item['name']} - Rs {item_total}")
            
        except ValueError:
            print("Error: Please enter valid input!")
    
    return name, items, total

def generate_bill(name: str, items: List, total: int):
    """Generate customer bill"""
    if not items:
        print("No items in order!")
        return
        
    print("\n" + "="*50)
    print("                 CAFE BILL RECEIPT")
    print("="*50)
    print(f"Customer: {name}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 50)
    print(f"{'Item':<12} {'Qty':<4} {'Price':<8} {'Total':<10}")
    print("-" * 50)
    
    for item in items:
        print(f"{item[0]:<12} {item[1]:<4} Rs{item[2]:<6} Rs{item[3]:<8}")
    
    print("-" * 50)
    print(f"{'GRAND TOTAL':<12} {'':<4} {'':<8} Rs{total:<8}")
    print("=" * 50)
    
    # Customer classification
    order_count = len([o for o in ORDERS_DB if o["customer_name"] == name]) + 1
    customer_type = classify_customer(total, order_count)
    print(f"\nCustomer Status: {customer_type}")

def save_order(name: str, items: List, total: int):
    """Save order with analytics"""
    if not items:
        return
        
    order_data = {
        "customer_name": name,
        "order_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": items,
        "total_amount": total,
        "customer_type": classify_customer(total, 1)
    }
    
    Repository.save_order(order_data)
    
    # Update customer preferences for future recommendations
    if items:
        first_item_name = items[0][0]  # Get name of first ordered item
        # Find the category of the first ordered item
        for item in MENU_ITEMS.values():
            if item["name"] == first_item_name:
                preferred_category = item["category"]
                break
        else:
            preferred_category = "beverage"  # Default fallback
            
        CUSTOMER_PREFERENCES[name] = {
            "preferred_category": preferred_category,
            "last_order": datetime.datetime.now().strftime("%Y-%m-%d"),
            "total_spent": total,
            "order_count": len([o for o in ORDERS_DB if o["customer_name"] == name]) + 1
        }

# Simulation & Analytics
def simulate_sales():
    """Sales simulation with visualization"""
    print("\n--- 7-DAY SALES SIMULATION ---")
    sales = []
    
    for day in range(7):
        base_sales = random.randint(2000, 5000)
        weekend_boost = 1.3 if day >= 5 else 1.0  # Weekend boost
        daily_total = int(base_sales * weekend_boost)
        sales.append(daily_total)
        
        print(f"Day {day+1}: Rs {daily_total}")
    
    print(f"\nAnalytics:")
    print(f"   Average: Rs {sum(sales)/7:.0f}")
    print(f"   Best: Rs {max(sales)}")
    print(f"   Worst: Rs {min(sales)}")
    print(f"   Total: Rs {sum(sales)}")

def show_analytics():
    """Business analytics"""
    revenue = Repository.get_daily_revenue()
    print(f"\n--- BUSINESS ANALYTICS ---")
    print(f"Total Orders: {len(ORDERS_DB)}")
    print(f"Total Revenue: Rs {revenue}")
    print(f"Unique Customers: {len(CUSTOMER_PREFERENCES)}")
    
    if ORDERS_DB:
        avg_order = revenue / len(ORDERS_DB)
        print(f"Average Order Value: Rs {avg_order:.2f}")

# Main Application
def main():
    """Main controller"""
    print("=" * 50)
    print("       SMART CAFE MANAGEMENT SYSTEM")
    print("=" * 50)
    
    while True:
        print("\nMAIN MENU")
        print("1. Take New Order")
        print("2. View Analytics") 
        print("3. Sales Simulation")
        print("4. Get Recommendations")
        print("5. Admin Menu")
        print("6. Exit System")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            name, items, total = take_order()
            if items:
                generate_bill(name, items, total)
                save_order(name, items, total)
                recommendation = Recommender.get_recommendation(name)
                print(f"\n{recommendation}")
                print("Thank you for your order!")
            else:
                print("No order placed.")
                
        elif choice == "2": 
            show_analytics()
        elif choice == "3": 
            simulate_sales()
        elif choice == "4": 
            name = input("Enter customer name: ").strip()
            if name:
                recommendation = Recommender.get_recommendation(name)
                print(f"\nRecommendation for {name}:")
                print(recommendation)
            else:
                print("Error: Please enter a customer name!")
        elif choice == "5": 
            admin_menu()
        elif choice == "6": 
            print("\n" + "=" * 50)
            print("          CAFE SYSTEM CLOSED")
            print("=" * 50)
            revenue = Repository.get_daily_revenue()
            print(f"Final Report: {len(ORDERS_DB)} orders, Rs {revenue} revenue")
            print("Thank you!")
            break
        else: 
            print("Error: Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSystem interrupted by user")
    except Exception as e:
        print(f"\nSystem error: {e}")
        print("Please restart the application.")
