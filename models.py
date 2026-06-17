"""
ByteBites Data Models

Four core classes for the restaurant ordering system:
1. Customer - Manages customer information and purchase history
2. Item - Represents menu items with price, category, and popularity rating
3. Transaction - Records a customer's purchase with multiple items and timestamp
4. Menu - Manages available items and provides filtering and search functionality
"""

from datetime import datetime


class Item:
    """Represents a single food item with properties and popularity tracking."""

    def __init__(self, item_id: str, name: str, price: float, category: str):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = 0.0

    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    def get_category(self) -> str:
        return self.category

    def get_rating(self) -> float:
        return self.popularity_rating

    def set_popularity(self, rating: float) -> None:
        self.popularity_rating = rating


class Customer:
    """Represents an app user with persistent identity and transaction history."""

    def __init__(self, customer_id: str, name: str):
        self.customer_id = customer_id
        self.name = name
        self.purchase_history = []

    def get_name(self) -> str:
        return self.name

    def get_id(self) -> str:
        return self.customer_id

    def add_purchase(self, transaction: "Transaction") -> None:
        self.purchase_history.append(transaction)

    def get_purchase_history(self) -> list:
        return self.purchase_history

    def get_total_spent(self) -> float:
        total = 0.0
        for transaction in self.purchase_history:
            total += transaction.calculate_total()
        return total


class Transaction:
    """Groups selected items for a single purchase and calculates total cost."""

    def __init__(self, transaction_id: str, customer: Customer):
        self.transaction_id = transaction_id
        self.customer = customer
        self.items_ordered = []
        self.timestamp = datetime.now()

    def add_item(self, item: Item) -> None:
        self.items_ordered.append(item)

    def remove_item(self, item: Item) -> None:
        self.items_ordered.remove(item)

    def get_items(self) -> list:
        return self.items_ordered

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items_ordered:
            total += item.get_price()
        return total

    def get_item_count(self) -> int:
        return len(self.items_ordered)

    def get_customer(self) -> Customer:
        return self.customer


class Menu:
    """Manages the collection of all items and provides filtering/search capabilities."""

    def __init__(self):
        self.items = []
        self.categories = set()

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        self.categories.add(item.get_category())

    def remove_item(self, item_id: str) -> None:
        self.items = [item for item in self.items if item.item_id != item_id]
        self.categories = set(item.get_category() for item in self.items)

    def get_all_items(self) -> list:
        return self.items

    def filter_by_category(self, category: str) -> list:
        return [item for item in self.items if item.get_category() == category]

    def get_categories(self) -> list:
        return list(self.categories)

    def get_item_by_id(self, item_id: str) -> Item | None:
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def get_popular_items(self) -> list:
        return sorted(self.items, key=lambda item: item.get_rating(), reverse=True)
