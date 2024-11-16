import unittest
from datetime import datetime

class TestStockVisualizerInputs(unittest.TestCase):
    def test_stock_symbol(self):
        # Valid cases
        self.assertTrue(self.is_valid_symbol('AAPL'))
        self.assertTrue(self.is_valid_symbol('IBM'))
        self.assertTrue(self.is_valid_symbol('GOOGL'))
        
        # Invalid cases
        self.assertFalse(self.is_valid_symbol('aapl'))  # lowercase
        self.assertFalse(self.is_valid_symbol('AAPL123'))  # contains numbers
        self.assertFalse(self.is_valid_symbol(''))  # empty
        self.assertFalse(self.is_valid_symbol('TOOLONG'))  # > 7 characters
        self.assertFalse(self.is_valid_symbol('A@PL'))  # special characters

    def test_chart_type(self):
        # Valid cases
        self.assertTrue(self.is_valid_chart_type('1'))
        self.assertTrue(self.is_valid_chart_type('2'))
        
        # Invalid cases
        self.assertFalse(self.is_valid_chart_type('0'))
        self.assertFalse(self.is_valid_chart_type('3'))
        self.assertFalse(self.is_valid_chart_type('a'))
        self.assertFalse(self.is_valid_chart_type(''))

    def test_time_series(self):
        # Valid cases
        self.assertTrue(self.is_valid_time_series('1'))
        self.assertTrue(self.is_valid_time_series('2'))
        self.assertTrue(self.is_valid_time_series('3'))
        self.assertTrue(self.is_valid_time_series('4'))
        
        # Invalid cases
        self.assertFalse(self.is_valid_time_series('0'))
        self.assertFalse(self.is_valid_time_series('5'))
        self.assertFalse(self.is_valid_time_series('a'))
        self.assertFalse(self.is_valid_time_series(''))

    def test_date_format(self):
        # Valid cases
        self.assertTrue(self.is_valid_date('2024-11-15'))
        self.assertTrue(self.is_valid_date('2023-01-01'))
        self.assertTrue(self.is_valid_date('2020-12-31'))
        
        # Invalid cases
        self.assertFalse(self.is_valid_date('2024/11/15'))  # wrong separator
        self.assertFalse(self.is_valid_date('15-11-2024'))  # wrong format
        self.assertFalse(self.is_valid_date('2024-13-01'))  # invalid month
        self.assertFalse(self.is_valid_date('2024-11-32'))  # invalid day
        self.assertFalse(self.is_valid_date(''))  # empty

    def test_date_range(self):
        # Valid cases
        self.assertTrue(self.is_valid_date_range('2023-01-01', '2024-01-01'))
        self.assertTrue(self.is_valid_date_range('2024-01-01', '2024-11-15'))
        
        # Invalid cases
        self.assertFalse(self.is_valid_date_range('2024-01-01', '2023-01-01'))  # end before start
        self.assertFalse(self.is_valid_date_range('2024-01-01', '2025-01-01'))  # future date

    # Helper methods for validation
    def is_valid_symbol(self, symbol):
        # Check if symbol exists and is within length limits
        if not symbol or len(symbol) >= 7 or len(symbol) < 1:  # Changed > to >=
            return False
        # Check if it's all uppercase letters
        return symbol.isalpha() and symbol.isupper()

    def is_valid_chart_type(self, chart_type):
        return chart_type in ['1', '2']

    def is_valid_time_series(self, time_series):
        return time_series in ['1', '2', '3', '4']

    def is_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def is_valid_date_range(self, start_date, end_date):
        if not self.is_valid_date(start_date) or not self.is_valid_date(end_date):
            return False
        
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        current = datetime.now()
        
        return start <= end and end <= current

if __name__ == '__main__':
    unittest.main()