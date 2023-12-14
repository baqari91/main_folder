import practice
import unittest

class TestPractice(unittest.TestCase):
    def test_add(self):
        self.assertEqual(practice.add(5, 10), 15)
        self.assertEqual(practice.add(-1, 1), 1)
        self.assertEqual(practice.add(-1, -1), -2)









# if __name__ == "__main__":
#     unittest.main()