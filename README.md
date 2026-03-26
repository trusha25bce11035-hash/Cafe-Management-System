# Cafe-Management-System-

##Overview -
The Smart Cafe Management System is a thoughtfully designed Python-based application that brings together practical business needs and modern software development practices. At its core, it allows café administrators to easily manage their menu through complete CRUD operations—making it simple to add new items, update prices, organize categories, or remove outdated products whenever needed.                                                                                                           
What makes the system stand out is its intelligent recommendation feature. Instead of just listing items, it observes customer preferences and popular trends to suggest what a customer might enjoy next. This creates a more personalized experience and naturally encourages higher sales without feeling forced.                                   
The system also includes built-in business insights. Through simulated sales data and simple ASCII dashboards, it gives a clear picture of revenue patterns and performance trends, helping owners understand how their café is doing at a glance—even without complex tools.            
From order placement to final billing, the application manages the entire workflow smoothly. It ensures proper input validation, keeps track of inventory, and generates receipts, making daily operations organized and reliable.                                                                                                                     
Behind the scenes, the project follows clean coding practices and structured design. It uses patterns like the Repository Pattern to manage data efficiently and the Strategy Pattern to keep recommendation logic flexible. The code is modular, well-organized, and includes error handling, logging, and type hints—making it feel closer to a real-world production system than just a basic project.                                                                                                                  
Additionally, the system categorizes customers into groups such as VIP, Regular, Occasional, and New based on their behavior. This adds a layer of business intelligence that can help in understanding and serving customers better.
Overall, this project is not just about managing a café—it showcases how software can solve real problems in a practical, efficient, and user-friendly way, while also reflecting strong development fundamentals.


# **Smart Cafe Management System - Complete Design Documentation**

## **Problem Statement**
Traditional cafe management systems suffer from manual operations, lack of customer personalization, inefficient inventory management, and absence of data-driven insights. This leads to:
- **Operational Inefficiency**: Manual order processing causing errors and delays
- **Poor Customer Experience**: No personalized recommendations or loyalty recognition
- **Inventory Challenges**: Stockouts or overstocking due to poor tracking
- **Business Blindness**: Lack of analytics for sales trends and customer behavior
- **Scalability Limitations**: Difficulty in expanding operations or menu offerings

## **Objectives**
- **Automate Operations**: Streamline order processing and inventory management
- **Enhance Customer Experience**: Provide personalized recommendations and loyalty recognition
- **Enable Data-Driven Decisions**: Implement analytics for sales and customer insights
- **Ensure Scalability**: Design modular architecture for future expansions
- **Improve Efficiency**: Reduce manual errors and optimize resource utilization

## **Functional Requirements**
1. **Menu Management**
   - Add, view, update, delete menu items
   - Categorize items (beverage/food) with pricing
   - Track real-time stock levels

2. **Order Processing**
   - Customer order intake with validation
   - Automatic bill generation
   - Inventory deduction and stock updates

3. **Customer Management**
   - Customer preference tracking
   - Classification system (VIP/Regular/Occasional/New)
   - Order history maintenance

4. **Recommendation System**
   - Personalized item suggestions
   - Multiple recommendation strategies
   - Real-time preference analysis

5. **Analytics & Reporting**
   - Sales revenue tracking
   - Customer distribution reports
   - Sales simulation and forecasting

6. **Administrative Functions**
   - Comprehensive business dashboard
   - System monitoring and logging
   - Performance visualization

## **Non-functional Requirements**
- **Performance**: Process orders within 2-3 seconds, handle 50+ concurrent operations
- **Reliability**: 99% uptime, data consistency, automatic error recovery
- **Usability**: Intuitive interface, minimal training required
- **Maintainability**: Modular code, comprehensive documentation
- **Scalability**: Support menu expansion and multiple locations
- **Security**: Input validation, data integrity, audit logging

## **System Architecture Diagram**
```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Console UI  │  │ Menu        │  │ Bill Generator      │  │
│  │ Controller  │  │ Displayer   │  │ & Formatter         │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                               │
┌─────────────────────────────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Order       │  │ Recommendation │  │ Analytics        │  │
│  │ Processor   │  │ Engine        │  │ Engine            │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Customer    │  │ Inventory   │  │ CRUD Operations     │  │
│  │ Classifier  │  │ Manager     │  │ Handler             │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                               │
┌─────────────────────────────────────────────────────────────┐
│                    DATA ACCESS LAYER                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Repository  │  │ In-Memory   │  │ Logging &           │  │
│  │ Pattern     │  │ Storage     │  │ Monitoring          │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## **Process Flow / Workflow Diagram**

### **Order Processing Workflow**
```
┌─────────────┐    ┌───────────────┐    ┌─────────────────┐
│   Start     │───►│ Enter Customer│───►│ Display Menu    │
│   Order     │    │ Name          │    │ & Get Selection │
└─────────────┘    └───────────────┘    └─────────────────┘
                                                     │
┌─────────────┐    ┌───────────────┐    ┌─────────────────┐
│ Generate    │◄──│ Update        │◄───│ Validate Stock  │
│ Bill &      │   │ Inventory     │    │ & Quantity      │
│ Recommendations │               │    │                 │
└─────────────┘    └───────────────┘    └─────────────────┘
```

### **Admin Management Workflow**
```
┌─────────────┐    ┌───────────────┐    ┌─────────────────┐
│ Admin       │───►│ Select CRUD   │───►│ Validate Input  │
│ Login       │    │ Operation     │    │ & Business Rules│
└─────────────┘    └───────────────┘    └─────────────────┘
                                                     │
┌─────────────┐    ┌───────────────┐    ┌─────────────────┐
│ Confirm     │◄───│ Execute       │◄───│ Process Data    │
│ Operation   │    │ Operation     │    │ Changes         │
└─────────────┘    └───────────────┘    └─────────────────┘
```

## **UML Diagrams**

### **Use Case Diagram**
```
┌─────────────────────────────────────────────────────────────┐
│                        Actors                               │
├─────────────────────────────────────────────────────────────┤
│  • Customer                   • Admin                       │
│  • System                     • Cafe Staff                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                        Use Cases                            │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │ Place Order     │  │ View Menu       │  │ Get Bill    │  │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │ Receive Rec     │  │ Manage Menu     │  │ View Analytics│ │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │ Run Simulation  │  │ Classify Customers│ │ Track Inventory││
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### **Class Diagram / Component Diagram**
```python
class CafeManagementSystem:
    - menu_items: Dict
    - orders_db: List
    - customer_preferences: Dict
    
    + main()
    + take_order()
    + show_analytics()

class Repository:
    + save_order(order_data: Dict) -> bool
    + get_customer_orders(customer_name: str) -> List
    + get_daily_revenue() -> int

class Recommender:
    + get_recommendation(customer_name: str) -> str
    + collaborative_filtering_strategy() -> str
    + preference_based_strategy() -> str
    + random_strategy() -> str

class OrderProcessor:
    - validate_quantity_input(qty: str, max: int) -> Tuple[bool, int, str]
    - calculate_total(items: List) -> int
    - update_inventory(items: List) -> None

class CustomerClassifier:
    + classify_customer(total_spent: int, order_count: int) -> str
```

### **Sequence Diagram**
```
Customer          System          OrderProcessor   Recommender
  │                  │                  │               │
  │  place_order()   │                  │               │
  │─────────────────>│                  │               │
  │                  │ display_menu()   │               │
  │<─────────────────│                  │               │
  │                  │                  │               │
  │ select_items()   │                  │               │
  │─────────────────>│                  │               │
  │                  │ validate_stock() │               │
  │                  │─────────────────>│               │
  │                  │                  │               │
  │                  │ get_recommendation()             │
  │                  │─────────────────────────────────>│
  │                  │                  │               │
  │                  │ generate_bill()  │               │
  │<─────────────────│                  │               │
```

## **Database/Storage Design**

### **ER Diagram**
```
Entities:
┌─────────────────┐         ┌─────────────────┐
│   MENU_ITEMS    │         │     ORDERS      │
├─────────────────┤         ├─────────────────┤
│ item_id (PK)    │┼┐       │ order_id (PK)   │
│ name            │ │      ┌│ customer_name   │
│ price           │ │      ││ order_date      │
│ category        │ │      ││ total_amount    │
│ stock           │ │      ││ customer_type   │
└─────────────────┘ │      │└─────────────────┘
                    │      │
┌─────────────────┐ │      │ ┌─────────────────┐
│ ORDER_ITEMS     │┼┘      └▶│     ITEM        │
├─────────────────┤          ├─────────────────┤
│ order_id (FK)   │          │ item_name (FK)  │
│ item_name       │          │ quantity        │
│ quantity        │          │ item_price      │
│ item_price      │          │ item_total      │
│ item_total      │          └─────────────────┘
└─────────────────┘

┌─────────────────┐
│ CUSTOMER_PREFS  │
├─────────────────┤
│ customer_name(PK)│
│ preferred_category│
│ total_spent      │
│ order_count      │
│ last_order_date  │
└─────────────────┘
```

### **Schema Design**
```python
# In-memory Database Schema
MENU_ITEMS = {
    item_id: {
        "name": str,
        "price": int,
        "category": str,  # "beverage" or "food"
        "stock": int
    }
}

ORDERS_DB = [
    {
        "customer_name": str,
        "order_date": str,
        "items": List[Tuple[str, int, int, int]],  # (name, qty, price, total)
        "total_amount": int,
        "customer_type": str
    }
]

CUSTOMER_PREFERENCES = {
    customer_name: {
        "preferred_category": str,
        "total_spent": int,
        "order_count": int,
        "last_order": str
    }
}
```

## **ML-Related Components**

### **Dataset Description**
```python
# Synthetic Dataset Generated from Customer Interactions
Data Features:
- Customer order history (items, quantities, frequencies)
- Temporal patterns (order timing, frequency)
- Spending behavior (total amounts, average order value)
- Preference patterns (category preferences, item affinities)

Dataset Size: Dynamic, grows with system usage
Data Types: Categorical (items, categories), Numerical (prices, quantities)
Data Source: Real-time customer interactions and order processing
```

### **Model Selection Rationale**
```python
# Recommendation System Models
1. Collaborative Filtering (Popular Items)
   - Rationale: Leverages collective customer behavior
   - Use Case: New customers or when personal data is limited
   - Advantage: No cold-start problem for popular items

2. Preference-Based Filtering
   - Rationale: Personalized recommendations based on individual history
   - Use Case: Returning customers with order history
   - Advantage: Highly personalized suggestions

3. Random Strategy (Fallback)
   - Rationale: Ensures recommendations when other methods fail
   - Use Case: System initialization or data scarcity
   - Advantage: Always provides some recommendation

# Customer Classification Model
Rule-Based Classification:
- VIP: total_spent > 1000 AND order_count > 5
- Regular: total_spent > 500
- Occasional: total_spent > 100
- New: Default classification

Rationale: Simple, interpretable, business-aligned rules
```

### **Evaluation Methodology**
```python
# Recommendation System Evaluation
Metrics:
1. Recommendation Relevance
   - Measure: Percentage of recommended items actually ordered
   - Method: Track if recommended items appear in subsequent orders

2. Customer Engagement
   - Measure: Order frequency after recommendations
   - Method: Compare pre and post-recommendation order patterns

3. Business Impact
   - Measure: Average order value increase
   - Method: Compare AOV with and without recommendations

# Classification System Evaluation
Metrics:
1. Classification Accuracy
   - Measure: Alignment with business definitions
   - Method: Manual review of customer categorization

2. Business Value
   - Measure: VIP customer retention rates
   - Method: Track repeat business from classified segments

# Testing Approach
A/B Testing: Compare recommendation strategies
Cross-Validation: Use historical data to validate models
Business Metrics: Revenue impact, customer satisfaction
```

## **Implementation Architecture**
```
TECHNOLOGY STACK:
• Language: Python 3.8+
• Storage: In-memory dictionaries (prototype)
• Patterns: Repository, Strategy, Modular
• Libraries: Standard Python (datetime, logging, collections)

DATA FLOW:
1. User Input → Validation → Processing → Storage → Output
2. Real-time: Order → Stock Update → Recommendation → Bill
3. Batch: Analytics → Reporting → Business Insights

SCALABILITY PATH:
Current: In-memory → Future: SQL Database → Cloud: Microservices
```

## Features
1- Complete CRUD operations for menu management
2- ML-powered recommendation system with multiple strategies
3- Customer classification (VIP/Regular/Occasional/New)
4- Sales simulation with visual analytics
5- Real-time inventory tracking and stock management
6- Comprehensive order processing with validation
7- Business intelligence dashboard
8- Error handling and logging system
9- ASCII-based data visualization

 ## Technologies/Tools Used
1- Python 3.8+ - Core programming language
2- Standard Libraries: datetime, logging, random, collections
3- Design Patterns: Repository Pattern, Strategy Pattern
4- Type Hints - For code clarity and maintenance
5- Data Structures: Dictionaries, Lists, DefaultDict
6- ASCII Visualization - For sales and stock dashboards

##  Steps to Install & Run the Project
1. Ensure Python 3.8+ is installed on your system
2. Download the code and save as `cafe_system.py`
3. Open terminal/command prompt in the project directory
4. Run the application: `python cafe_system.py`
5. No external dependencies required - uses only Python standard library
6. Automatic log file `cafe_system.log` will be created for monitoring

 ## Instructions for Testing
1- Test CRUD Operations: Use Admin Menu (Option 5) to add, view, update, delete menu items
2- Test Order Processing: Place orders with different quantities and customer names
3- Test Recommendations: Order as multiple customers to build preference history
4- Test Stock Management: Order items to deplete stock and verify out-of-stock messages
5- Test Analytics:Place several orders then check analytics dashboard (Option 2)
6- Test Error Handling: Enter invalid inputs, negative quantities, non-existent menu items
7- Test Simulation: Run sales simulation (Option 3) to view revenue projections
8- Verify Logging: Check `cafe_system.log` file for system activity records



