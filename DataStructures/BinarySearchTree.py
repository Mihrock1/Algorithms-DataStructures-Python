from shutil import Error
from typing import Union

class BinarySearchTree:
    class _Node:
        def __init__(self, val: Union[int, float]):
            if not isinstance(val, (int, float)):
                raise TypeError("Value must be a number")
            self.val = val
            self.left = None
            self.right = None

    def __init__(self, val: Union[None, int, float] = None):
        if val is not None:
            self.root = self._Node(val)
            self.size = 1
        else:
            self.root = None
            self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def get_min_val(self) -> Union[int, float]:
        if self.size == 0:
            raise Error("Tree is empty!")

        min_val = self._get_min_val_rec(self.root)
        return min_val.val

    def _get_min_val_rec(self, node: _Node) -> _Node:
        if node.left is not None:
            return self._get_min_val_rec(node.left)
        else:
            return node

    def get_max_val(self) -> Union[int, float]:
        if self.size == 0:
            raise Error("Tree is empty!")

        max_val = self._get_max_val_rec(self.root)
        return max_val.val

    def _get_max_val_rec(self, node: _Node) -> _Node:
        if node.right is not None:
            return self._get_max_val_rec(node.right)
        else:
            return node

    def traverse_in_order(self):
        if self.size == 0:
            raise Error("Tree is empty!")

        self._traverse_in_order_rec(self.root)

    def _traverse_in_order_rec(self, node: _Node):
        if node is not None:
            self._traverse_in_order_rec(node.left)
            print(str(node.val) + " ", end="")
            self._traverse_in_order_rec(node.right)

    def exists(self, val: Union[int, float]) -> bool:
        if not isinstance(val, (int, float)):
            raise ValueError("Can only accept a number as argument")

        node = self._find(self.root, val)
        return node is not None

    def _find(self, node: _Node, val) -> Union[_Node, None]:
        if node is None:
            return None

        if val < node.val:
            return self._find(node.left, val)
        elif val > node.val:
            return self._find(node.right, val)
        else:
            return node

    def insert(self, val: Union[int, float]) -> bool:
        if not isinstance(val, (int, float)):
            raise ValueError("Can only accept a number as argument")

        if self.is_empty():
            self.root = self._Node(val)
            self.size = 1
            return True

        self.root = self._insert_rec(self.root, val)
        self.size += 1
        return True

    def _insert_rec(self, node: _Node, val) -> Union[None, _Node]:
        # in case node doesn't exist, create it
        if node is None:
            return self._Node(val)

        if val < node.val:
            node.left = self._insert_rec(node.left, val)
        elif val > node.val:
            node.right = self._insert_rec(node.right, val)
        else:
            # in case node already exists
            return None

        return node

    def delete(self, val: Union[int, float]) -> bool:
        if not isinstance(val, (int, float)):
            raise ValueError("Can only accept a number as argument")

        self._delete_rec(self.root, val)
        self.size -= 1
        return True

    def _delete_rec(self, node: _Node, val) -> Union[None, _Node]:
        if node is None:
            raise ValueError("Value doesn't exist in tree")

        if val < node.val:
            node.left = self._delete_rec(node.left, val)
        elif val > node.val:
            node.right = self._delete_rec(node.right, val)
        else:
            # correct node is found
            # check for 3 scenarios based on number of children of node to be deleted:-
            if node.left is None and node.right is None:
                # no children
                return None
            elif node.left is not None and node.right is None:
                # only left child exists
                return node.left
            elif node.left is None and node.right is not None:
                # only right child exists
                return node.right
            else:
                # both children exist
                # get min node in right subtree
                min_left_node = self._get_min_val_rec(node.right)
                # copy data from min node in right subtree to node
                node.val = min_left_node.val
                # delete min node in right subtree
                return node

        return node




