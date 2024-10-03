import unittest
from shutil import Error

from BinarySearchTree import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Initialize a Binary Search Tree before each test."""
        self.bst = BinarySearchTree()

    def test_insert(self):
        """Test insertion of elements into the BST."""
        self.assertTrue(self.bst.insert(10), "Insert should return True")
        self.assertTrue(self.bst.insert(5), "Insert should return True")
        self.assertTrue(self.bst.insert(20), "Insert should return True")
        self.assertFalse(self.bst.insert(10), "Insert should return False for duplicate")

    def test_search(self):
        """Test searching for elements in the BST."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.assertTrue(self.bst.search(10), "Search should find 10")
        self.assertTrue(self.bst.search(5), "Search should find 5")
        self.assertTrue(self.bst.search(20), "Search should find 20")
        self.assertFalse(self.bst.search(15), "Search should return False for missing value")

    def test_get_min_val(self):
        """Test finding the minimum value in the BST."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.bst.insert(2)
        self.assertEqual(self.bst.get_min_val(), 2, "Min value should be 2")

    def test_get_max_val(self):
        """Test finding the maximum value in the BST."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.bst.insert(25)
        self.assertEqual(self.bst.get_max_val(), 25, "Max value should be 25")

    def test_traverse_in_order(self):
        """Test inorder traversal."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.bst.insert(15)
        self.bst.insert(25)

        self.bst.traverse_in_order()

    def test_delete_leaf_node(self):
        """Test deleting a leaf node."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.assertTrue(self.bst.delete(5), "Should return True after deleting a leaf")
        self.assertFalse(self.bst.search(5), "Node 5 should no longer exist in the tree")

    def test_delete_node_with_one_child(self):
        """Test deleting a node with one child."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.bst.insert(25)  # Add one child to 20
        self.assertTrue(self.bst.delete(20), "Should return True after deleting a node with one child")
        self.assertFalse(self.bst.search(20), "Node 20 should no longer exist in the tree")

    def test_delete_node_with_two_children(self):
        """Test deleting a node with two children."""
        self.bst.insert(10)
        self.bst.insert(5)
        self.bst.insert(20)
        self.bst.insert(15)
        self.bst.insert(25)
        self.assertTrue(self.bst.delete(20), "Should return True after deleting a node with two children")
        self.assertFalse(self.bst.search(20), "Node 20 should no longer exist in the tree")

    def test_get_min_val_empty_tree(self):
        """Test get_min_val on an empty tree should raise an error."""
        with self.assertRaises(Error):
            self.bst.get_min_val()

    def test_get_max_val_empty_tree(self):
        """Test get_max_val on an empty tree should raise an error."""
        with self.assertRaises(Error):
            self.bst.get_max_val()

    def test_insert_invalid_type(self):
        """Test inserting a non-numeric type should raise an error."""
        with self.assertRaises(Error):
            self.bst.insert("string")

    def test_size_of_tree(self):
        """Test size of the tree after operations."""
        self.assertEqual(self.bst.get_size(), 0, "Initial size should be 0")
        self.bst.insert(10)
        self.assertEqual(self.bst.get_size(), 1, "Size should be 1 after one insertion")
        self.bst.insert(20)
        self.assertEqual(self.bst.get_size(), 2, "Size should be 2 after another insertion")

    def test_is_empty(self):
        """Test is_empty method."""
        self.assertTrue(self.bst.is_empty(), "Tree should be empty initially")
        self.bst.insert(10)
        self.assertFalse(self.bst.is_empty(), "Tree should not be empty after insertion")

if __name__ == "__main__":
    unittest.main()