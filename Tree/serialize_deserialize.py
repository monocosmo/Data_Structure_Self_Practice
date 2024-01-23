from collections import deque

class TreeNode(object):
  def __init__(self, val = None):
    self.val = val
    self.left = None
    self.right = None

class Solution(object):
  def serialize(self, root):
    seq = []
    q = deque([root])
    
    while q:
      node = q.popleft()
      if not node:
        seq.append('#')
      else:
        seq.append(str(node.val))
        q.append(node.left)
        q.append(node.right)

    # tailing redudant '#'
    while len(seq) > 1 and seq[-1] == '#':
      seq.pop()

    return ','.join(seq)

  def deserialize(self, input_str):
    seq = input_str.split(',')
    if len(seq) <= 0:
      return None
    if seq[0] == '#':
      return None

    root = TreeNode(int(seq[0]))
    q = deque([root])
    idx = 1

    while q:
      node = q.popleft()
      # add left child
      if idx < len(seq) and seq[idx] != '#':
        left = TreeNode(int(seq[idx]))
        node.left = left
        q.append(left)
      idx += 1
      # add right child
      if idx < len(seq) and seq[idx] != '#':
        right = TreeNode(int(seq[idx]))
        node.right = right
        q.append(right)
      idx += 1

    return root

if __name__ == '__main__':
  test_input = '1,2,3,#,#,4,5'
  s = Solution()
  tree = s.deserialize(test_input)
  test_output = s.serialize(tree)
  print(test_output)

      





