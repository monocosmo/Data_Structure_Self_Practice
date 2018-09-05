# Implement BSTree

class BSTree(object):
  def __init__(self, elem = None):
    self.elem = elem
    self.lchild = None
    self.rchild = None

  def dict_form(self):
    dict_set = {
      "element": self.elem,
      "left": self.lchild,
      "right": self.rchild,
    }
    return dict_set

  def __str__(self):
    return(str(self.elem))

  # Node insertion (recursive)
  def insertR(self, elem):
    if self.elem is None:
      self.elem = elem
    elif self.elem == elem:
      self.elem == elem
    elif self.elem > elem:
      if self.lchild is None:
        self.lchild = BSTree(elem)
      else:
        self.lchild.insertR(elem)
    elif self.elem < elem:
      if self.rchild is None:
        self.rchild = BSTree(elem)
      else:
        self.rchild.insertR(elem)

  # pre-order (recursive)
  def preOrderR(self ,root):
    if root is None:
      return
    else:
      print(root.elem, end=",")
      self.preOrderR(root.lchild)
      self.preOrderR(root.rchild)

  # pre-order (non-recursive)
  def preOrder(self, root):
    if root is None:
      return
    helpStack = []
    node = root
    while node or helpStack:
      while node:
        # print "root"
        print(node.elem, end=",")
        # from root, check lchild first
        helpStack.append(node)
        node = node.lchild
      # this while loop ends when the current node has no lchild
      node = helpStack.pop()
      # start to check rchild
      node = node.rchild

  # in-order (recursive)
  def inOrderR(self ,root):
    if root is None:
      return
    else:
      self.inOrderR(root.lchild)
      print(root.elem, end=",")
      self.inOrderR(root.rchild)

  # in-order (non-recursive)
  def inOrder(self, root):
    if root is None:
      return
    helpStack = []
    node = root
    while node or helpStack:
      while node:
        # from root, check lchild first
        helpStack.append(node)
        node = node.lchild
      # this while loop ends when the current node has no lchild
      node = helpStack.pop()
      # print the current "root"
      print(node.elem, end=",")
      # start to check rchild
      node = node.rchild

  # post-order (recursive)
  def postOrderR(self ,root):
    if root is None:
      return
    else:
      self.postOrderR(root.lchild)
      self.postOrderR(root.rchild)
      print(root.elem, end=",")

  # post-order (non-recursive)
  def postOrder(self, root):
    if root is None:
      return
    helpStack1 = []
    helpStack2 = []
    node = root
    helpStack1.append(node)
    while helpStack1:
      # from next circle, rchild will be pop out first 
      node = helpStack1.pop()
      # Be aware!!! Here is NOT if...elif...
      # Must check both lchild and rchild of each "root"
      if node.lchild:
        helpStack1.append(node.lchild)
      if node.rchild:
        helpStack1.append(node.rchild)
      # "root" will be inserted into Stack2 first
      helpStack2.append(node)
    while helpStack2:
      print(helpStack2.pop().elem, end=",")

  # level-order
  def levelOrder(self, root):
    if root is None:
      return
    helpQueue = []
    node = root
    helpQueue.append(node)
    while helpQueue:
      node = helpQueue.pop(0)
      print(node.elem, end=",")
      if node.lchild:
        helpQueue.append(node.lchild)
      if node.rchild:
        helpQueue.append(node.rchild)

  # traverse
  def traverse(self, root):
    result = []
    self.traverseHelp(root, result)
    return result

  # traverse help function
  def traverseHelp(self, root, result):
    if root is None:
      return
    else:
      result.append(root.elem)
      self.traverseHelp(root.lchild, result)
      self.traverseHelp(root.rchild, result)

  # dived & conquer
  def dAndC(self, root):
    result = []
    if root is None:
      return result
    else:
      # divide
      left = self.dAndC(root.lchild)
      right = self.dAndC(root.rchild)

      # conquer
      result.append(root.elem)
      result = result + left + right
      return result

  # max depth (traverse)
  def maxDepthT(self, root):
    global depth
    depth = 0
    self.maxDepthTHelper(root, 1)
    return depth

  def maxDepthTHelper(self, root, currentDepth):
    global depth
    if root is None:
      return
    elif currentDepth > depth:
      depth = currentDepth
    self.maxDepthTHelper(root.lchild, currentDepth + 1)
    self.maxDepthTHelper(root.rchild, currentDepth + 1)

  # max depth (divide and conquer)
  def maxDepthDC(self, root):
    if root is None:
      # Note: return 0 when reaches the leaf
      return 0
    else:
      left = self.maxDepthDC(root.lchild)
      right = self.maxDepthDC(root.rchild)
      return max(left, right) + 1

tree_test = BSTree()
tree_test.insertR(8)
tree_test.insertR(3)
tree_test.insertR(10)
tree_test.insertR(1)
tree_test.insertR(6)
tree_test.insertR(4)
tree_test.insertR(7)
tree_test.insertR(14)
tree_test.insertR(13)
print("pre-order (recursive):")
tree_test.preOrderR(tree_test)
print()
print("pre-order (non-recursive):")
tree_test.preOrder(tree_test)
print()
print("in-order (recursive):")
tree_test.inOrderR(tree_test)
print()
print("in-order (non-recursive):")
tree_test.inOrder(tree_test)
print()
print("post-order (recursive):")
tree_test.postOrderR(tree_test)
print()
print("post-order (non-recursive):")
tree_test.postOrder(tree_test)
print()
print("level-order:")
tree_test.levelOrder(tree_test)
print()
print("traverse:")
print(tree_test.traverse(tree_test))
print("divide and conquer:")
print(tree_test.dAndC(tree_test))
print("max depth (traverse)")
print(tree_test.maxDepthT(tree_test))
print("max depth (divide and conquer)")
print(tree_test.maxDepthDC(tree_test))