import unittest

class TestSplitFunction(unittest.TestCase):
    def test_split_by_space(self):
        text = "Hello World !"  
        result = text.split()
        print(f"RESULT1: {result}")

    def test_split_by_comma(self):
        text = "apple,banana,orange"
        result = text.split(',')
        print(f"RESULT2: {result}")

    def test_split_by_empty_string(self):
        text = "test"
        with self.assertRaises(ValueError):
            text.split("")

    def test_split_with_limit(self):
        text = "one,two,three,four"
        result = text.split(',', 2)
        print(f"RESULT4: {result}")

    def test_split_on_empty_string(self):
        # Тест на разделение пустой строки
        text = ""
        result = text.split()
        print(f"RESULT5: {result}")

    def test_split_with_multiple_spaces(self):
        # Тест на строку с несколькими пробелами
        text = "  Hello   World  "
        result = text.split()
        print(f"RESULT6: {result}")

if __name__ == "__main__":
    unittest.main()
