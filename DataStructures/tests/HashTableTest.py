import unittest
from abc import ABC, abstractmethod

from DataStructures.HashTable import _OpenAddressingHashTable, HashTable


class BaseHashTableTest(ABC, unittest.TestCase):
    @abstractmethod
    def create_hash_table(self, *args, **kwargs) -> HashTable:
        """Create and return a hash table instance."""
        pass

    def test_insert_and_find(self):
        hash_table = self.create_hash_table()

        # Test inserting values and finding them
        self.assertTrue(hash_table.insert(1))
        self.assertTrue(hash_table.insert(2))
        self.assertTrue(hash_table.insert(3))

        # Verify that `find` returns an index with the correct value
        idx1 = hash_table.find(1)
        idx2 = hash_table.find(2)
        idx3 = hash_table.find(3)

        self.assertNotEqual(idx1, -1)
        self.assertEqual(hash_table.table[idx1], 1)

        self.assertNotEqual(idx2, -1)
        self.assertEqual(hash_table.table[idx2], 2)

        self.assertNotEqual(idx3, -1)
        self.assertEqual(hash_table.table[idx3], 3)

        # Test finding a non-existing value
        self.assertEqual(hash_table.find(4), -1)

    def test_delete(self):
        hash_table = self.create_hash_table()

        # Insert and delete a value
        hash_table.insert(5)
        self.assertEqual(hash_table.delete(5), 5)

        # Try finding a deleted value
        self.assertEqual(hash_table.find(5), -1)

        # Deleting a non-existing value should raise an exception
        with self.assertRaises(ValueError):
            hash_table.delete(6)

    def test_reinsertion_after_deletion(self):
        hash_table = self.create_hash_table()

        # Insert, delete, and re-insert a value
        hash_table.insert(7)
        hash_table.delete(7)
        self.assertEqual(hash_table.find(7), -1)  # Should not find it after deletion

        # Insert again and ensure it is added
        self.assertTrue(hash_table.insert(7))
        self.assertNotEqual(hash_table.find(7), -1)

    def test_resize(self):
        hash_table = self.create_hash_table(init_capacity=3, load_factor=0.5)

        # Insert values to trigger a resize
        hash_table.insert(1)
        hash_table.insert(2)

        # Capacity should have grown
        self.assertGreaterEqual(hash_table.capacity, 3 * 2)
        self.assertNotEqual(hash_table.find(1), -1)
        self.assertNotEqual(hash_table.find(2), -1)


class TestOpenAddressingHashTable(BaseHashTableTest):
    def create_hash_table(self, *args, **kwargs) -> HashTable:
        return _OpenAddressingHashTable(*args, **kwargs)