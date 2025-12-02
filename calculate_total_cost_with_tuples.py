def calculate_total_cost(items, tax_rate, discount):
    subtotal = sum(items)
    total = subtotal * (1 + tax_rate) - discount
    
    return total

import pytest

# Test cases as a list of tuples
test_cases = [
    ([], 0.1, 0, 0),  # No items
    ([10, 20, 30], 0.1, 5, 60),  # With items
    ([100], 0.2, 10, 90),  # Single item with tax and discount
    ([50, 50], 0.05, 10, 90)  # Items with discount
]

@pytest.mark.parametrize("items, tax_rate, discount, expected", test_cases)
def test_calculate_total_cost(items, tax_rate, discount, expected):
    result = calculate_total_cost(items, tax_rate, discount)
    print(f"items={items}, tax_rate={tax_rate}, discount={discount}, expected={expected}, result={result}")
    assert result == expected
