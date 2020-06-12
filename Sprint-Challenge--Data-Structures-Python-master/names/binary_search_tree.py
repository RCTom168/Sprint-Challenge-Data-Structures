"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    # Return statements technically aren't needed
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
                return
            else:
                self = self.right
                return self.insert(value)

        elif value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
                return
            else:
                self = self.left
                return self.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        elif target > self.value:
            if self.right is None:
                return False
            else:
                self = self.right
                return self.contains(target)

        else:    
            if self.left is None:
                return False
            else:
                self = self.left
                return self.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # If the root value is the highest, just return the value
        if self.right is None:
            return self.value
        else:
            # Move along to the next subtree that has the higher value and repeat
            self = self.right
            return self.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Why is this the first line?
        # 
        fn(self.value)

        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    # Lowest number is always the furthest to the left
    def in_order_print(self, node):
        # Base Case
        if node is None:
            if node.left:
                node.in_order_print(node.left)
            
            print(node.value)

            if node.right:
                node.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    # Use a Queue
    def bft_print(self, node):
        stack = [node]

        while stack != []:
            look = stack[0]

            if look.right:
                stack.append(look.right)
            if look.left:
                tack.append(look.left)

            print(look.value)
            stack = stack[1:]

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = [node]

        while stack != []:
 
            look = stack[-1]
            print(look.value)
            stack = stack[0:-1]
            if look.right is not None:
                stack.append(look.right)
                
            if look.left is not None:
                stack.append(look.left)

    # Use a stack with the root node
    # 

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node:
            print(node.value),
            

            node.pre_order_dft(node.left)

            node.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            node.post_order_dft(node.left)
            node.post_order_dft(node.right)
            print(node.value)
