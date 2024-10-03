from shutil import Error
from typing import Union

class BinarySearchTree:
    class __Node:
        def __init__(self, key: Union[int, float]):
            if not isinstance(key, (int, float)):
                raise TypeError("Value must be a number")
            self.key = key
            self.parent = None
            self.left = None
            self.right = None

    def __init__(self, key: Union[None, int, float] = None):
        if key is not None:
            self.root = self.__Node(key)
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, key: Union[int, float]) -> bool:
        if not isinstance(key, (int, float)):
            raise Error("Value must be a number")

        if self.size == 0:
            self.root = self.__Node(key)
            self.size = 1
            return True
        else:
            node = self.__insert_rec(self.root, key)
            if node is None:
                return False

            self.size += 1
            return True

    def __insert_rec(self, node: __Node, key: Union[int, float]) -> Union[__Node, None]:
        if key < node.key:
            if node.left is None:
                node.left = self.__Node(key)
                node.left.parent = node
                return node.left
            else:
                self.__insert_rec(node.left, key)
        elif key == node.key:
            return None
        else:
            if node.right is None:
                node.right = self.__Node(key)
                node.right.parent = node
                return node.right
            else:
                self.__insert_rec(node.right, key)

    def get_min_val(self) -> Union[int, float]:
        if self.size == 0:
            raise Error("Tree is empty!")

        min_val = self.__get_min_val_rec(self.root)
        return min_val.key

    def __get_min_val_rec(self, node: __Node) -> __Node:
        if node.left is not None:
            return self.__get_min_val_rec(node.left)
        else:
            return node

    def get_max_val(self) -> Union[int, float]:
        if self.size == 0:
            raise Error("Tree is empty!")

        max_val = self.__get_max_val_rec(self.root)
        return max_val.key

    def __get_max_val_rec(self, node: __Node) -> __Node:
        if node.right is not None:
            return self.__get_max_val_rec(node.right)
        else:
            return node

    def traverse_in_order(self):
        if self.size == 0:
            raise Error("Tree is empty!")

        self.__traverse_in_order(self.root)

    def __traverse_in_order(self, node: __Node):
        if node is not None:
            self.__traverse_in_order(node.left)
            print(str(node.key) + " ", end="")
            self.__traverse_in_order(node.right)

    def search(self, key: Union[int, float]) -> bool:
        if self.size == 0:
            raise Error("Tree is empty!")

        node = self.__search_rec(self.root, key)
        return node is not None

    def __search_rec(self, node: __Node, key: Union[int, float]) -> Union[__Node, None]:
        if key < node.key:
            if node.left is None:
                return None
            else:
                return self.__search_rec(node.left, key)
        elif key == node.key:
            return node
        else:
            if node.right is None:
                return None
            else:
                return self.__search_rec(node.right, key)

    def delete(self, key: Union[int, float]) -> bool:
        if self.size == 0:
            raise Error("Tree is empty!")

        node = self.__search_rec(self.root, key)
        if node is None:
            return False
        parent = node.parent

        if node.left is None and node.right is None:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

        elif node.left is None and node.right is not None:
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right

        elif node.left is not None and node.right is None:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left

        else:
            right_subtree_min_node = self.__get_min_val_rec(node.right)
            node.key = right_subtree_min_node.key

            right_subtree_min_node.key = None
            if right_subtree_min_node.parent.left == right_subtree_min_node:
                right_subtree_min_node.parent.left = None
            else:
                right_subtree_min_node.parent.right = None

        self.size -= 1
        if self.size == 0:
            self.root = None
        return True




