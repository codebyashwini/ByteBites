# ByteBites UML Class Diagram

## ASCII UML Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                        BYTEBITES SYSTEM                                         │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────┐         ┌────────────────────────────────┐
│           CUSTOMER             │         │           ITEM                 │
├────────────────────────────────┤         ├────────────────────────────────┤
│ Attributes:                    │         │ Attributes:                    │
│  - customer_id: str            │         │  - item_id: str                │
│  - name: str                   │         │  - name: str                   │
│  - purchase_history: List      │         │  - price: float                │
│                                │         │  - category: str               │
│ Methods:                       │         │  - popularity_rating: float    │
│  + __init__(id, name)          │         │                                │
│  + get_name() -> str           │         │ Methods:                       │
│  + get_id() -> str             │         │  + __init__(id, name,         │
│  + add_purchase(tx) -> None    │         │            price, category)    │
│  + get_purchase_history()      │         │  + get_name() -> str           │
│    -> List[Transaction]        │         │  + get_price() -> float        │
│  + get_total_spent() -> float  │         │  + get_category() -> str       │
│                                │         │  + get_rating() -> float       │
│                                │         │  + set_popularity(rating)      │
│                                │         │    -> None                     │
└────────────────────────────────┘         └────────────────────────────────┘
           △                                           △
           │ *                                         │ 1..*
           │ purchases                                 │ contains
           │                                           │
           └──────────────────────────────────┬────────┘
                                              │
                                    ┌─────────┴──────────┐
                                    │                    │
                                    │                    │
                      ┌─────────────┴─────────────┐      │
                      │                           │      │
        ┌─────────────────────────────────┐       │      │
        │          TRANSACTION            │       │      │
        ├─────────────────────────────────┤       │      │
        │ Attributes:                     │       │      │
        │  - transaction_id: str          │       │      │
        │  - customer: Customer           │       │      │
        │  - items_ordered: List[Item]    │◄──────┼──────┘
        │  - timestamp: datetime          │       │
        │                                 │       │
        │ Methods:                        │       │
        │  + __init__(id, customer)       │       │
        │    -> None                      │       │
        │  + add_item(item) -> None       │───────┘
        │  + remove_item(item) -> None    │
        │  + get_items() -> List[Item]    │
        │  + calculate_total()            │
        │    -> float                     │
        │  + get_item_count()             │
        │    -> int                       │
        │  + get_customer()               │
        │    -> Customer                  │
        └─────────────────────────────────┘
                      △
                      │ 1
                      │ creates
                      │
        ┌─────────────────────────────────┐
        │           MENU                  │
        ├─────────────────────────────────┤
        │ Attributes:                     │
        │  - items: List[Item]            │
        │  - categories: Set[str]         │
        │                                 │
        │ Methods:                        │
        │  + __init__()                   │
        │    -> None                      │
        │  + add_item(item) -> None       │
        │  + remove_item(item_id)         │
        │    -> None                      │
        │  + get_all_items()              │
        │    -> List[Item]                │
        │  + filter_by_category(category) │
        │    -> List[Item]                │
        │  + get_categories()             │
        │    -> List[str]                 │
        │  + get_item_by_id(item_id)      │
        │    -> Item | None               │
        │  + get_popular_items()          │
        │    -> List[Item]                │
        └─────────────────────────────────┘
```

## Relationship Legend

- **→** : Association (uses/references)
- **◄** : Aggregation (contains, but items can exist independently)
- **△** : Inheritance direction (if applicable)
- **1, ***: Multiplicity (1 = one, * = many)

---

## Detailed Class Specifications

### 1. CUSTOMER Class

**Purpose**: Represents an app user with persistent identity and transaction history.

**Attributes**:
- `customer_id: str` - Unique identifier for the customer
- `name: str` - Customer's name
- `purchase_history: List[Transaction]` - Record of all past transactions

**Methods**:
- `__init__(customer_id, name)` - Constructor
- `get_name() -> str` - Returns customer name
- `get_id() -> str` - Returns customer ID
- `add_purchase(transaction: Transaction) -> None` - Adds a transaction to history
- `get_purchase_history() -> List[Transaction]` - Retrieves all transactions
- `get_total_spent() -> float` - Calculates sum of all transaction totals

**Rationale**: The spec mentions "tracking their names and their past purchase history so the system can verify they are real users." This requires storing both identity and transaction records.

---

### 2. ITEM Class

**Purpose**: Represents a single food item with its properties.

**Attributes**:
- `item_id: str` - Unique identifier for the item
- `name: str` - Item name (e.g., "Spicy Burger")
- `price: float` - Cost of the item
- `category: str` - Category classification (e.g., "Drinks", "Desserts")
- `popularity_rating: float` - Numeric rating/popularity score (0-5 or similar)

**Methods**:
- `__init__(item_id, name, price, category)` - Constructor
- `get_name() -> str` - Returns item name
- `get_price() -> float` - Returns price
- `get_category() -> str` - Returns category
- `get_rating() -> float` - Returns popularity rating
- `set_popularity(rating: float) -> None` - Updates the popularity rating

**Rationale**: The spec requires "name, price, category, and popularity rating for every item we sell." These attributes directly map to the class properties. Getters provide read access, and the setter allows updating popularity based on user engagement.

---

### 3. MENU Class

**Purpose**: Manages the collection of all items and provides filtering/search capabilities.

**Attributes**:
- `items: List[Item]` - Complete inventory of all food items
- `categories: Set[str]` - Derived set of unique categories (for efficient lookup)

**Methods**:
- `__init__()` - Constructor, initializes empty menu
- `add_item(item: Item) -> None` - Adds an item to the menu
- `remove_item(item_id: str) -> None` - Removes an item by ID
- `get_all_items() -> List[Item]` - Returns all items in the menu
- `filter_by_category(category: str) -> List[Item]` - Returns items matching a category
- `get_categories() -> List[str]` - Returns list of all available categories
- `get_item_by_id(item_id: str) -> Item | None` - Retrieves a specific item
- `get_popular_items() -> List[Item]` - Returns items sorted by popularity (bonus feature)

**Rationale**: The spec requires "a way to manage the full collection of items — a digital list that holds all items and lets us filter by category." The Menu class is the container that supports browsing (get_all_items), filtering (filter_by_category), and lookup (get_item_by_id). The categories set provides O(1) lookup for available categories.

---

### 4. TRANSACTION Class

**Purpose**: Groups selected items for a single purchase and calculates total cost.

**Attributes**:
- `transaction_id: str` - Unique identifier for the transaction
- `customer: Customer` - Reference to the customer making the purchase
- `items_ordered: List[Item]` - Items included in this transaction
- `timestamp: datetime` - When the transaction was created (audit trail)

**Methods**:
- `__init__(transaction_id, customer: Customer) -> None` - Constructor
- `add_item(item: Item) -> None` - Adds an item to the transaction
- `remove_item(item: Item) -> None` - Removes an item from the transaction
- `get_items() -> List[Item]` - Returns all items in the transaction
- `calculate_total() -> float` - Sums the prices of all items
- `get_item_count() -> int` - Returns number of items in transaction
- `get_customer() -> Customer` - Returns the associated customer

**Rationale**: The spec states "when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost." The Transaction class encapsulates a purchase event with items and provides cost calculation via `calculate_total()`.

---

## Key Relationships

### 1. Customer ↔ Transaction (1 to Many)
- **Multiplicity**: 1 Customer : * Transactions
- **Type**: Aggregation (Customer contains Transactions, but Transactions are managed separately)
- **Meaning**: A customer can have multiple purchases over time. Each transaction records one purchase session.
- **Implementation**: Customer stores purchase_history as a list; Transaction holds a reference to its customer.

### 2. Menu ↔ Item (1 to Many)
- **Multiplicity**: 1 Menu : * Items
- **Type**: Aggregation (Menu contains Items, but Items can be reused/shared)
- **Meaning**: The menu holds all available items. Items can be part of many transactions without duplication.
- **Implementation**: Menu maintains a list of all Item objects.

### 3. Transaction ↔ Item (1 to Many)
- **Multiplicity**: 1 Transaction : * Items
- **Type**: Aggregation (Transaction aggregates Items for a single purchase)
- **Meaning**: A transaction groups multiple item selections together for checkout.
- **Implementation**: Transaction maintains items_ordered as a list of Item references.

### 4. Transaction → Customer (1 to 1)
- **Multiplicity**: 1 Transaction : 1 Customer
- **Type**: Association (each transaction belongs to one customer)
- **Meaning**: When creating a transaction, it must be associated with a specific customer.
- **Implementation**: Transaction constructor takes a customer object as a parameter.

---

## Design Notes

### Why these relationships work:
1. **No circular dependencies**: Customer → Transaction → Item ← Menu forms a clean dependency graph
2. **Single responsibility**: Each class manages one concern (identity, item properties, inventory, purchase grouping)
3. **Reusability**: Items exist in the Menu independently and can be added to multiple Transactions
4. **Traceability**: Transactions link Customers to their purchases, enabling the "verify they are real users" requirement

### Methods not explicitly in the spec but included because:
1. **Getters/Setters**: Essential for encapsulation and data access in OOP
2. **Constructors**: Needed to instantiate objects with required initial state
3. **calculate_total()**: Directly implied by "compute the total cost"
4. **filter_by_category()**: Directly implied by "filter by category"
5. **get_item_by_id()**: Essential for looking up specific items when adding to transactions
6. **add_purchase() on Customer**: Necessary to build purchase history over time
7. **Timestamp on Transaction**: Good practice for audit trails (implied by "history")

### Assumptions made:
1. Items are immutable after creation (hence no setters except popularity)
2. Menu is a singleton-like shared resource (not owned by customers)
3. Transactions are immutable after creation (no setters for items list, only add/remove)
4. Popularity rating is the only mutable item property
5. IDs are strings (could be UUIDs or numeric strings)
