def calculate_total_cost(items, tax_rate, discount): 
 subtotal = sum(items) 
 total = subtotal * (1 + tax_rate) - discount 
 return total 

import unittest

class TestCalculateTotalCost(unittest.TestCase):
    
    def test_no_items(self):
        # Logpoint here: result={result}
        self.assertEqual(calculate_total_cost([], 0.1, 0), 0)

    def test_with_items(self):
        self.assertEqual(calculate_total_cost([10, 20, 30], 0.1, 5), 60)  # (10 + 20 + 30) * 1.1 - 5
        self.assertEqual(calculate_total_cost([100], 0.2, 10), 90)  # (100) * 1.2 - 10

    def test_with_discount(self):
        # Logpoint here: result={result}
        self.assertEqual(calculate_total_cost([50, 50], 0.05, 10), 90)  # (50 + 50) * 1.05 - 10

if __name__ == '__main__':
    unittest.main()
# This is running a commint in my local mini-mac 11/30/2025
