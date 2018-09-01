# Implement BSTree

class BSTree(object):
  def __init__(self, elem = None):
    self.elem = elem
    self.lchild = None
    self.rchild = None

  def get_elem(self):
    return self.elem

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
def insert(tree, elem):
  if tree.elem is None:
    tree.elem = elem
  elif tree.elem == elem:
    tree.elem == elem
  elif tree.elem < elem:
    if tree.lchild is None:
      tree.lchild = BSTree(elem)
    else:
      insert(tree.lchild, elem)
  else:
    if tree.rchild is None:
      tree.rchild = BSTree(elem)
    else:
      insert(tree.rchild, elem)

tree_test = BSTree()
insert(tree_test ,8)
insert(tree_test ,10)
insert(tree_test ,3)
insert(tree_test ,1)
print(tree_test)