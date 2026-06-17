"""
Unit tests for ByteBites data models.

Tests for:
- Item: food items with price, category, popularity
- Customer: user identity and purchase history
- Transaction: groups items and calculates totals
- Menu: manages item collection with filtering and search
"""

import pytest
from models import Item, Customer, Transaction, Menu


# ============================================================================
# FILTERING TESTS — Menu.filter_by_category()
# ============================================================================

def test_filter_returns_only_matching_items():
    """Filtering by category returns only items in that category."""
    menu = Menu()
    burger = Item("1", "Burger", 8.99, "sandwiches")
    fries = Item("2", "Fries", 3.99, "sides")
    hot_dog = Item("3", "Hot Dog", 7.99, "sandwiches")
    menu.add_item(burger)
    menu.add_item(fries)
    menu.add_item(hot_dog)

    result = menu.filter_by_category("sandwiches")

    assert burger in result
    assert hot_dog in result
    assert fries not in result


def test_filter_returns_empty_list_for_nonexistent_category():
    """Filtering for a category that doesn't exist returns empty list."""
    menu = Menu()
    coke = Item("1", "Coke", 2.99, "beverages")
    menu.add_item(coke)

    result = menu.filter_by_category("desserts")

    assert result == []
    assert len(result) == 0


def test_filter_on_empty_menu_returns_empty_list():
    """Filtering an empty menu returns empty list."""
    menu = Menu()

    result = menu.filter_by_category("sandwiches")

    assert result == []


# ============================================================================
# TRANSACTION TOTAL TESTS — Transaction.calculate_total()
# ============================================================================

def test_transaction_total_sums_multiple_item_prices():
    """Transaction total correctly sums prices of all items in order."""
    customer = Customer("c1", "Alice")
    transaction = Transaction("t1", customer)
    burger = Item("1", "Burger", 8.99, "sandwiches")
    fries = Item("2", "Fries", 3.99, "sides")
    drink = Item("3", "Coke", 2.50, "beverages")
    transaction.add_item(burger)
    transaction.add_item(fries)
    transaction.add_item(drink)

    total = transaction.calculate_total()

    assert total == pytest.approx(15.48)


def test_transaction_total_for_empty_transaction_is_zero():
    """Empty transaction with no items returns total of 0."""
    customer = Customer("c1", "Alice")
    transaction = Transaction("t1", customer)

    total = transaction.calculate_total()

    assert total == 0


def test_transaction_total_with_single_item():
    """Transaction with one item returns that item's price."""
    customer = Customer("c1", "Alice")
    transaction = Transaction("t1", customer)
    burger = Item("1", "Burger", 8.99, "sandwiches")
    transaction.add_item(burger)

    total = transaction.calculate_total()

    assert total == pytest.approx(8.99)


def test_transaction_total_with_duplicate_items():
    """Transaction total includes same item added multiple times."""
    customer = Customer("c1", "Alice")
    transaction = Transaction("t1", customer)
    burger = Item("1", "Burger", 8.99, "sandwiches")
    transaction.add_item(burger)
    transaction.add_item(burger)

    total = transaction.calculate_total()

    assert total == pytest.approx(17.98)


# ============================================================================
# CUSTOMER LIFETIME SPENDING TESTS — Customer.get_total_spent()
# ============================================================================

def test_customer_total_spent_sums_all_transaction_totals():
    """Customer lifetime spending sums totals from all purchases."""
    customer = Customer("c1", "Alice")

    transaction1 = Transaction("t1", customer)
    burger = Item("1", "Burger", 8.99, "sandwiches")
    fries = Item("2", "Fries", 3.99, "sides")
    transaction1.add_item(burger)
    transaction1.add_item(fries)
    customer.add_purchase(transaction1)

    transaction2 = Transaction("t2", customer)
    salad = Item("3", "Salad", 7.99, "salads")
    drink = Item("4", "Sprite", 2.51, "beverages")
    transaction2.add_item(salad)
    transaction2.add_item(drink)
    customer.add_purchase(transaction2)

    total_spent = customer.get_total_spent()

    assert total_spent == pytest.approx(23.48)


def test_customer_total_spent_with_no_purchase_history_is_zero():
    """Customer with no purchases returns total spent of 0."""
    customer = Customer("c1", "Alice")

    total_spent = customer.get_total_spent()

    assert total_spent == 0


def test_customer_total_spent_with_single_transaction():
    """Customer with one transaction returns that transaction total."""
    customer = Customer("c1", "Alice")
    transaction = Transaction("t1", customer)
    burger = Item("1", "Burger", 8.99, "sandwiches")
    transaction.add_item(burger)
    customer.add_purchase(transaction)

    total_spent = customer.get_total_spent()

    assert total_spent == pytest.approx(8.99)


# ============================================================================
# SORTING TESTS — Menu.get_popular_items()
# ============================================================================

def test_popular_items_returns_items_ranked_by_rating():
    """Popular items returns all items sorted highest to lowest popularity."""
    menu = Menu()
    burger = Item("1", "Burger", 8.99, "sandwiches")
    burger.set_popularity(4.8)
    fries = Item("2", "Fries", 3.99, "sides")
    fries.set_popularity(4.2)
    salad = Item("3", "Salad", 7.99, "salads")
    salad.set_popularity(4.5)
    menu.add_item(burger)
    menu.add_item(fries)
    menu.add_item(salad)

    result = menu.get_popular_items()

    assert result[0] == burger
    assert result[1] == salad
    assert result[2] == fries


def test_popular_items_on_empty_menu_returns_empty_list():
    """Getting popular items from empty menu returns empty list."""
    menu = Menu()

    result = menu.get_popular_items()

    assert result == []


def test_popular_items_with_equal_ratings_returns_all_items():
    """Items with equal popularity ratings are all included in result."""
    menu = Menu()
    burger = Item("1", "Burger", 8.99, "sandwiches")
    burger.set_popularity(4.5)
    fries = Item("2", "Fries", 3.99, "sides")
    fries.set_popularity(4.5)
    menu.add_item(burger)
    menu.add_item(fries)

    result = menu.get_popular_items()

    assert len(result) == 2
    assert burger in result
    assert fries in result
