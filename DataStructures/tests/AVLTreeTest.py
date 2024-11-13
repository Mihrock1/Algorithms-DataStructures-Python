import unittest

from DataStructures.AVLTree import AVLTree


class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl = AVLTree()

    def test_initialization(self):
        self.assertTrue(self.avl.is_empty())
        self.assertEqual(self.avl.get_size(), 0)

        avl_with_root = AVLTree(10)
        self.assertFalse(avl_with_root.is_empty())
        self.assertEqual(avl_with_root.get_size(), 1)

    def test_insert_and_balance(self):
        # Insert values to trigger right rotation
        self.avl.insert(30)
        self.avl.insert(20)
        self.avl.insert(10)  # Right rotation should happen here

        # Check if tree rebalanced correctly
        self.assertEqual(self.avl.root.val, 20)
        self.assertEqual(self.avl.root.left.val, 10)
        self.assertEqual(self.avl.root.right.val, 30)

        # Insert values to trigger left rotation
        self.avl.insert(40)
        self.avl.insert(50)  # Left rotation should happen here

        # Check if tree rebalanced correctly
        self.assertEqual(self.avl.root.val, 20)
        self.assertEqual(self.avl.root.right.val, 40)
        self.assertEqual(self.avl.root.right.left.val, 30)
        self.assertEqual(self.avl.root.right.right.val, 50)

        # Insert values to trigger left-right rotation
        self.avl.insert(25)  # Left-Right rotation should happen here

        # Check if tree rebalanced correctly
        self.assertEqual(self.avl.root.val, 30)
        self.assertEqual(self.avl.root.left.val, 20)
        self.assertEqual(self.avl.root.left.left.val, 10)
        self.assertEqual(self.avl.root.left.right.val, 25)
        self.assertEqual(self.avl.root.right.val, 40)
        self.assertEqual(self.avl.root.right.right.val, 50)

    def test_delete_and_balance(self):
        # Set up a balanced tree
        values = [10, 20, 30, 40, 50, 25]
        for v in values:
            self.avl.insert(v)

        # Delete node with no children
        self.avl.delete(25)
        self.assertFalse(self.avl.exists(25))

        # Delete node with one child
        self.avl.delete(50)
        self.assertFalse(self.avl.exists(50))

        # Delete node with two children (root)
        self.avl.delete(30)
        self.assertFalse(self.avl.exists(30))

        # Check balance and structure after deletions
        self.assertEqual(self.avl.root.val, 40)
        self.assertEqual(self.avl.root.left.val, 20)
        self.assertEqual(self.avl.root.left.left.val, 10)

    def test_rotations(self):
        # Check right rotation
        self.avl.insert(30)
        self.avl.insert(20)
        self.avl.insert(10)  # Causes right rotation
        self.assertEqual(self.avl.root.val, 20)
        self.assertEqual(self.avl.root.left.val, 10)
        self.assertEqual(self.avl.root.right.val, 30)

        # Reset tree and check left rotation
        self.avl = AVLTree()
        self.avl.insert(10)
        self.avl.insert(20)
        self.avl.insert(30)  # Causes left rotation
        self.assertEqual(self.avl.root.val, 20)
        self.assertEqual(self.avl.root.left.val, 10)
        self.assertEqual(self.avl.root.right.val, 30)

    def test_balancing_factors_and_heights(self):
        values = [10, 20, 30, 40, 50, 25]
        for v in values:
            self.avl.insert(v)

        # Verify height and balance factors for nodes
        self.assertEqual(self.avl.root.height, 3)
        self.assertEqual(self.avl.root.balance_factor, 0)
        self.assertEqual(self.avl.root.left.height, 2)
        self.assertEqual(self.avl.root.right.height, 2)

    def test_insert_invalid_value(self):
        with self.assertRaises(ValueError):
            self.avl.insert("string")  # Non-numeric value

    def test_exists_invalid_value(self):
        with self.assertRaises(ValueError):
            self.avl.exists("string")  # Non-numeric value

    def test_delete_nonexistent_value(self):
        with self.assertRaises(ValueError):
            self.avl.delete(10)  # Value not in tree


if __name__ == "__main__":
    unittest.main()