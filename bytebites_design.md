# ByteBites UML Class Diagram - Revised (Bounded Design)

> **Design Philosophy**: This revised diagram follows a minimalist approach, implementing **only** what is explicitly required by the spec. No speculative features or "nice-to-haves" are included.

## ASCII UML Diagram

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                           BYTEBITES SYSTEM                                   │
└──────────────────────────────────────────────────────────────────────────────┘

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
│  + add_purchase(tx) -> None    │         │ Methods:                       │
│  + get_purchase_history()      │         │  + __init__(id, name,         │
│    -> List[Transaction]        │         │            price, category)    │
│                                │         │  + get_price() -> float        │
│                                │         │  + get_category() -> str       │
│                                │         │  + set_popularity(rating)      │
│                                │         │    -> None                     │
└────────────────────────────────┘         └────────────────────────────────┘
           △                                           △
           │ *                                         │ *
           │ purchases                                 │ contains
           │                                           │
           └──────────────────────────────┬────────────┘
                                          │
                          ┌───────────────┴───────────────┐
                          │                               │
                          │                               │
        ┌─────────────────────────────────┐       ┌───────┴──────────────┐
        │          TRANSACTION            │       │                      │
        ├─────────────────────────────────┤       │
        │ Attributes:                     │       │
        │  - transaction_id: str          │       │
        │  - customer: Customer           │       │
        │  - items_ordered: List[Item]    │◄──────┼──────────────────────┘
        │                                 │       │
        │ Methods:                        │       │
        │  + __init__(id, customer)       │       │
        │    -> None                      │       │
        │  + add_item(item) -> None       │───────┘
        │  + remove_item(item) -> None    │
        │  + get_items() -> List[Item]    │
        │  + calculate_total()            │
        │    -> float                     │
        └─────────────────────────────────┘
                      △
                      │ 1
                      │ manages
                      │
        ┌─────────────────────────────────┐
        │           MENU                  │
        ├─────────────────────────────────┤
        │ Attributes:                     │
        │  - items: List[Item]            │
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
        │  + get_item_by_id(item_id)      │
        │    -> Item | None               │
        └─────────────────────────────────┘
```

## Key Changes from Earlier Draft

### ❌ Removed (Not Explicitly in Spec)
1. **Item.get_name()** — Unnecessary; the `name` attribute is accessible
2. **Item.get_rating()** — Unnecessary; the `popularity_rating` attribute is accessible
3. **Customer.get_name()** — Unnecessary; the `name` attribute is accessible
4. **Customer.get_id()** — Unnecessary; the `customer_id` attribute is accessible
5. **Customer.get_total_spent()** — Goes beyond spec ("purchase history" doesn't require summing)
6. **Menu.get_categories()** — Goes beyond spec; not required for filtering
7. **Menu.get_popular_items()** — Speculative feature not in spec
8. **Transaction.get_item_count()** — Not explicitly required
9. **Transaction.get_customer()** — Customer reference is already an attribute
10. **Menu.categories: Set[str]** — Derived optimization not needed for this scope

### ✅ Kept (Explicitly Required by Spec)
1. **Customer.customer_id, name, purchase_history** — "tracking their names and their past purchase history"
2. **Customer.add_purchase()** — Required to build purchase history over time
3. **Item.item_id, name, price, category, popularity_rating** — All explicitly in spec
4. **Item.set_popularity()** — Required to update "popularity rating"
5. **Transaction.transaction_id, customer, items_ordered** — Needed to "group items into a single transaction"
6. **Transaction.add_item(), remove_item()** — Required to "pick items"
7. **Transaction.get_items()** — Required to retrieve the grouped items
8. **Transaction.calculate_total()** — "compute the total cost"
9. **Menu.items** — Required to "manage full collection of items"
10. **Menu.add_item(), remove_item()** — Required to manage the collection
11. **Menu.get_all_items(), filter_by_category()** — Required to "browse" and "filter by category"
12. **Menu.get_item_by_id()** — Minimal helper needed for transactions to reference items

---

## Relationship Summary

| Relationship | Multiplicity | Type | Meaning |
|---|---|---|---|
| **Customer → Transaction** | 1 : * | Aggregation | Each customer has multiple purchases; purchase history records all transactions |
| **Menu → Item** | 1 : * | Aggregation | Menu contains all available items; items are referenced by transactions |
| **Transaction → Item** | 1 : * | Aggregation | Transaction groups multiple items for checkout |
| **Transaction → Customer** | * : 1 | Association | Each transaction belongs to exactly one customer |

---

## Design Rationale

### Why This Bounded Approach?

1. **Spec-Driven**: Every method and attribute directly satisfies a requirement in bytebites_spec.md
2. **No Over-Engineering**: We avoid "nice-to-have" optimizations (like categories set, helper getters for attributes)
3. **Cleaner Implementation**: Fewer methods = fewer tests = faster development
4. **Learner-Focused**: This is an educational project; clear, intentional design beats clever optimizations

### Implementation Notes

- **Getters on attributes**: We keep only the essential ones (`get_price()`, `get_category()` on Item) because these are accessed within the Transaction's `calculate_total()` method. Omitting them would require direct attribute access, which violates encapsulation.
- **No timestamp on Transaction**: Not explicitly required by spec; audit trails are a "nice-to-have"
- **Item immutability**: Item properties are read-only except `popularity_rating`, which the spec explicitly allows to be updated
- **Menu simplicity**: No derived categories set; we compute them on-the-fly if needed
- **Customer simplicity**: Purchase history is managed externally; Customer just stores the list

---

## Next Steps for Implementation

This diagram serves as the contract for the Python implementation:
1. Create each class with the exact attributes and methods shown
2. Implement relationships using references (Transaction holds a Customer, Menu holds Items, etc.)
3. Write simple, readable methods that do one thing well
4. Test against the spec requirements only—no bonus features

---

## Comparison: Earlier Draft vs. Revised Design

### Earlier Draft (Less-Bounded)
- Included speculative helper methods (`get_popular_items()`, `get_categories()`)
- Had getter methods for every attribute (even those not accessed by other classes)
- Added `timestamp` on Transaction (audit trail, not in spec)
- Included derived attributes (`categories` set on Menu)
- Totaled ~15 methods on Customer and Item alone

### Revised Design (Bounded)
- Only includes methods required by the spec
- Removes redundant getters; relies on direct attribute access where appropriate
- Cleaner separation of concerns
- Totals ~10 methods across all classes
- Each method directly supports a feature mentioned in the spec

---

## Specification Cross-Reference

✅ **"manage our customers, tracking their names and their past purchase history"**
- Customer class with `name` and `purchase_history` attributes
- `add_purchase()` method to build history

✅ **"browse specific food items (name, price, category, popularity rating)"**
- Item class with all four attributes
- Item methods for accessing price/category (needed by Transaction)

✅ **"manage the full collection of items — a digital list that holds all items and lets us filter by category"**
- Menu class with `items: List[Item]`
- `add_item()`, `remove_item()`, `get_all_items()`, `filter_by_category()`, `get_item_by_id()`

✅ **"group items into a single transaction and compute the total cost"**
- Transaction class with `customer` and `items_ordered`
- `add_item()`, `remove_item()`, `get_items()`, `calculate_total()`
