import unittest
from my_list import MyList


class Tests(unittest.TestCase):

    def test_get_size(self):
        list = MyList(1, 2, 3, 4, 5)
        self.assertEqual(list.get_size(), 5)

    def test_clear(self):
        list = MyList(1, 2, 3, 4, 5)
        list.clear()
        self.assertEqual(list.get_size(), 0)

    def test_add_items(self):
        list = MyList(1, 2, 3, 4, 5)
        list.add(6, 7, 8, 9, 10)
        self.assertEqual(list.get_size(), 10)

    def test_has_item(self):
        list = MyList(1, 2, 3, 4, 5)
        self.assertTrue(list.has(2), True)
        self.assertFalse(list.has(20), False)

    def test_get(self):
        list = MyList(1, 2, 3, 4, 5)
        self.assertEqual(list.get(2), 3)
        self.assertIs(list.get(20), None)

    def test_get_index(self):
        list = MyList(1, 2, 3, 4, 5)
        self.assertEqual(list.get_index_of(3), 2)
        self.assertEqual(list.get_index_of(20), -1)

    def test_remove_item(self):
        list = MyList(1, 2, 3, 4, 5)
        self.assertEqual(list.remove(3), 4)
        self.assertEqual(list.get_size(), 4)
        self.assertIs(list.remove(20), None)


if __name__ == "__main__":
    unittest.main()
