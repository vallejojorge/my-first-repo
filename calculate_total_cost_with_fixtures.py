def calculate_total_cost(items, tax_rate, discount):
    subtotal = sum(items)
    total = subtotal * (1 + tax_rate) - discount
    return total
import pytest

# Fixture to provide test cases
@pytest.fixture
def test_data():
    return [
        ([], 0.1, 0, 0),  # No items
        ([10, 20, 30], 0.1, 5, 60),  # With items
        ([100], 0.2, 10, 90),  # Single item with tax and discount
        ([50, 50], 0.05, 10, 90)  # Items with discount
    ]

def test_calculate_total_cost(test_data):
    for items, tax_rate, discount, expected in test_data:
        # Add your print here to visualize inputs and outputs
        print(f"items={items}, tax_rate={tax_rate}, discount={discount}, expected={expected}, result={result}")
        assert calculate_total_cost(items, tax_rate, discount) == expected
        # pytest -s -v test_calculate_total_with_fixtures.py

