# Implement Binary Tree

# Node
class Node(object):
  def __init__(self, elem = None, lchild = None, rchild = None):
    self.elem = elem
    self.lchild = lchild
    self.rchild = rchild

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

# node_test = Node("a")
# print(node_test.get_elem())
# print(node_test)
# print(node_test.dict_form())

# BiTree
class BiTree(object):
  def __init__(self, tree_node = None):
    self.root = tree_node

  # none-recursion-add-node
  def add_node(self, elem):
    # if left is empty, add to left, elif right is empty, add to right.
    # else go through left and right child nodes, until find empty node.
    node = Node(elem)

    if self.root is None:
      # if root is empty
      self.root = node
    else:
      node_queue = []
      node_queue.append(self.root)
      while len(node_queue) >= 0:
        tree_node = node_queue.pop(0)
        if tree_node.lchild is None:
          tree_node.lchild = node
          break
        elif tree_node.rchild is None:
          tree_node.rchild = node
          break
        else:
          node_queue.append(tree_node.lchild)
          node_queue.append(tree_node.rchild)

  # transfer list to tree
  def add_node_list(self, elem_list):
    for elem in elem_list:
      self.add_node(elem)

  


