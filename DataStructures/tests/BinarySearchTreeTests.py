import unittest
from shutil import Error

from DataStructures.BinarySearchTree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = BinarySearchTree()

    def test_initialization(self):
        self.assertTrue(self.bst.is_empty())
        self.assertEqual(self.bst.get_size(), 0)

        bst_with_root = BinarySearchTree(10)
        self.assertFalse(bst_with_root.is_empty())
        self.assertEqual(bst_with_root.get_size(), 1)

    def test_insert(self):
        self.bst.insert(10)
        self.assertFalse(self.bst.is_empty())
        self.assertEqual(self.bst.get_size(), 1)

        # Insert additional values
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.get_size(), 3)

        # Duplicate insertion should return False
        self.assertFalse(self.bst.insert(10))

    def test_get_min_val(self):
        with self.assertRaises(Error):
            self.bst.get_min_val()  # Tree is empty

        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.get_min_val(), 5)

    def test_get_max_val(self):
        with self.assertRaises(Error):
            self.bst.get_max_val()  # Tree is empty

        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.assertEqual(self.bst.get_max_val(), 15)

    def test_exists(self):
        self.assertFalse(self.bst.exists(10))

        self.bst.insert(10)
        self.assertTrue(self.bst.exists(10))
        self.assertFalse(self.bst.exists(5))

        self.bst.insert(5)
        self.assertTrue(self.bst.exists(5))

    def test_delete_leaf(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)

        # Delete a leaf node
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertEqual(self.bst.get_size(), 2)

    def test_delete_node_with_one_child(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)  # Node with one child

        # Delete a node with one child
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertTrue(self.bst.exists(3))
        self.assertEqual(self.bst.get_size(), 3)

    def test_delete_node_with_two_children(self):
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(15)
        self.bst.insert(3)
        self.bst.insert(7)  # Node with two children

        # Delete a node with two children
        self.bst.delete(5)
        self.assertFalse(self.bst.exists(5))
        self.assertTrue(self.bst.exists(7))
        self.assertEqual(self.bst.get_size(), 4)

    def test_insert_invalid_value(self):
        with self.assertRaises(ValueError):
            self.bst.insert("string")  # Non-numeric value

    def test_exists_invalid_value(self):
        with self.assertRaises(ValueError):
            self.bst.exists("string")  # Non-numeric value

    def test_delete_nonexistent_value(self):
        with self.assertRaises(ValueError):
            self.bst.delete(10)  # Value not in tree


if __name__ == "__main__":
    unittest.main()