def count_valleys(step_list):
    current_level = 0
    valleys = 0

    for step in step_list:
        if step == 'U':
            current_level += 1
            if current_level == 0:
                valleys += 1
        else:
            current_level -= 1

    return valleys

step_list = 'DDUUUDDDUUUU'
number_of_valleys = count_valleys(step_list)
print("Number of valleys:", number_of_valleys)
step_list = 'DUDDUUDDUU'
number_of_valleys = count_valleys(step_list)
print("Number of valleys:", number_of_valleys)


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SortedBinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self._insert_recursively(current_node.left, value)
            else:
                current_node.left = TreeNode(value)
        elif value > current_node.value:
            if current_node.right:
                self._insert_recursively(current_node.right, value)
            else:
                current_node.right = TreeNode(value)
        else:
            pass

    def inorder_traversal(self):
        result = []
        self._inorder_recursively(self.root, result)
        return result

    def _inorder_recursively(self, current_node, result):
        if current_node:
            self._inorder_recursively(current_node.left, result)
            result.append(current_node.value)
            self._inorder_recursively(current_node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursively(self.root, result)
        return result

    def _postorder_recursively(self, current_node, result):
        if current_node:
            self._postorder_recursively(current_node.left, result)
            self._postorder_recursively(current_node.right, result)
            result.append(current_node.value)

    def preorder_traversal(self):
        result = []
        self._preorder_recursively(self.root, result)
        return result

    def _preorder_recursively(self, current_node, result):
        if current_node:
            result.append(current_node.value)
            self._preorder_recursively(current_node.left, result)
            self._preorder_recursively(current_node.right, result)


sorted_binary_tree = SortedBinaryTree()
# sorted_binary_tree.insert(20)
# sorted_binary_tree.insert(22)
# sorted_binary_tree.insert(25)
# sorted_binary_tree.insert(21)
# sorted_binary_tree.insert(8)
# sorted_binary_tree.insert(4)
# sorted_binary_tree.insert(12)
# ------------------------------------------------------------------
# sorted_binary_tree.insert(15)
# sorted_binary_tree.insert(10)
# sorted_binary_tree.insert(22)
# sorted_binary_tree.insert(4)
# sorted_binary_tree.insert(12)
# sorted_binary_tree.insert(18)
# sorted_binary_tree.insert(24)
# ------------------------------------------------------------------
# sorted_binary_tree.insert(10)
# sorted_binary_tree.insert(5)
# sorted_binary_tree.insert(15)
# sorted_binary_tree.insert(3)
# sorted_binary_tree.insert(7)
# sorted_binary_tree.insert(12)
# sorted_binary_tree.insert(20)
# ------------------------------------------------------------------
sorted_binary_tree.insert(25)
sorted_binary_tree.insert(15)
sorted_binary_tree.insert(10)
sorted_binary_tree.insert(22)
sorted_binary_tree.insert(4)
sorted_binary_tree.insert(12)
sorted_binary_tree.insert(18)
sorted_binary_tree.insert(24)
sorted_binary_tree.insert(50)
sorted_binary_tree.insert(35)
sorted_binary_tree.insert(70)
sorted_binary_tree.insert(31)
sorted_binary_tree.insert(44)
sorted_binary_tree.insert(66)
sorted_binary_tree.insert(90)


print("Inorder Traversal:", sorted_binary_tree.inorder_traversal())
print("Postorder Traversal:", sorted_binary_tree.postorder_traversal())
print("Preorder Traversal:", sorted_binary_tree.preorder_traversal())