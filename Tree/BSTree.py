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

  # Node indertion (recursive)
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

  # in-order (recursive)
  def inOrderR(self ,root):
    if root is None:
      return
    else:
      self.inOrderR(root.lchild)
      print(root.elem, end=",")
      self.inOrderR(root.rchild)

  # post-order (recursive)
  def postOrderR(self ,root):
    if root is None:
      return
    else:
      self.postOrderR(root.lchild)
      self.postOrderR(root.rchild)
      print(root.elem, end=",")

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
print("in-order (recursive):")
tree_test.inOrderR(tree_test)
print()
print("post-order (recursive):")
tree_test.postOrderR(tree_test)
print()
