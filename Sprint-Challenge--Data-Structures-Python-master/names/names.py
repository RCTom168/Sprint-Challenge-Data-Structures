import time
from binary_search_tree import BSTNode
# (Hint: You might try importing a data structure you built during the week)
# Our Binary Search Tree data structure from earlier in the week should be very helpful

### binary_search_tree.py BSTNode Code ###
# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     # Return statements technically aren't needed
#     def insert(self, value):
#         if value >= self.value:
#             if self.right is None:
#                 self.right = BSTNode(value)
#                 return
#             else:
#                 self = self.right
#                 return self.insert(value)

#         elif value < self.value:
#             if self.left is None:
#                 self.left = BSTNode(value)
#                 return
#             else:
#                 self = self.left
#                 return self.insert(value)

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         if self.value == target:
#             return True

#         elif target > self.value:
#             if self.right is None:
#                 return False
#             else:
#                 self = self.right
#                 return self.contains(target)

#         else:    
#             if self.left is None:
#                 return False
#             else:
#                 self = self.left
#                 return self.contains(target)


### Names.py Code ###

print("\n Original Names.py Code:\n")

start_time = time.time()

# f = open('names_1.txt', 'r')
f = open(r'C:\Users\robtom\Desktop\Sprint-Challenge--Data-Structures-Python-master\names\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_2.txt', 'r')
f = open(r'C:\Users\robtom\Desktop\Sprint-Challenge--Data-Structures-Python-master\names\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds", '\n', "-"*85)


### Improved Names.py Code ###
print("\n Improved Names.py Code:\n")

start_time = time.time()

# f = open('names_1.txt', 'r')
f = open(r'C:\Users\robtom\Desktop\Sprint-Challenge--Data-Structures-Python-master\names\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_2.txt', 'r')
f = open(r'C:\Users\robtom\Desktop\Sprint-Challenge--Data-Structures-Python-master\names\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

bst = BSTNode('names')


for name in names_1:
    bst.insert(name)

for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds", '\n', "-"*85)


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

### Stretch Goal Names.py Code ###
print("\n Stretch Goal Names.py Code:\n")

start_time = time.time()

# f = open('names_1.txt', 'r')
f = open(r'C:\Users\robtom\Desktop\Sprint-Challenge--Data-Structures-Python-master\names\names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

# f = open('names_2.txt', 'r')
f = open(r'C:\Users\robtom\Desktop\Sprint-Challenge--Data-Structures-Python-master\names\names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

names = {}
for name in names_1 + names_2:
    if name in names:
        duplicates.append(name)
    else:
        names[name] = 1

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds", '\n', "-"*85)