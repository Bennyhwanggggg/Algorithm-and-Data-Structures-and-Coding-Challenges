'''
Python version: 3.6
Author: Benny Hwang

BST implementation
'''
class BST:
  def __init__(self, value=None, node_type=None):

    self.value = value;
    # use node type to check if intersections are from the same source
    self.node_type = node_type # store the source that made the end point
    if self.value is not None:
      self.left_node = BST()
      self.right_node = BST()
    else:
      self.left_node = None
      self.right_node = None


  def insert(self, value, node_type):

    if self.value is None:
      self.value = value
      self.node_type = node_type
      self.left_node = BST()
      self.right_node = BST()
      return
    if self.value > value:
      return self.left_node.insert(value, node_type)
    return self.right_node.insert(value, node_type)


  def delete(self, value):
    return self._delete(value, self, '')


  def _delete(self, value, parent, link):

    if self.value is None:
      return False
    if self.value > value:
      return self.left_node._delete(value, self, 'L')
    if self.value < value:
      return self.right_node._delete(value, self, 'R')

    # First two work for no child or one child
    if self.left_node.value is None: # one child case
      new_tree = self.right_node
    elif self.right_node.value is None: # one child case 
      new_tree = self.left_node
    elif self.left_node.right_node.value is None:
      # Get max on left tree. A node is max if it has no right node
      new_tree = self.left_node
      new_tree.right_node = self.right_node
    else:
      # Get max on left tree
      node_1 = self.left_node
      node_2 = node_1.right_node
      while node_2.right_node.value is not None:
        node_1 = node_2
        node_2 = node_2.right_node
      new_tree = node_2 # make the max node the new root
      new_tree.right_node = self.right_node # set the original right node to right
      node_1.right_node = node_2.left_node # link the node that is moved left node
      new_tree.left_node = self.left_node # relink the left node in original

    # copy values
    if link == '':
      self.value = new_tree.value
      self.node_type = new_tree.node_type
      self.left_node = new_tree.left_node
      self.right_node = new_tree.right_node
    elif link == 'L':
      parent.left_node = new_tree
    else:
      parent.right_node = new_tree
    return True


  def search_in_range(self, left, right, node_type):
    result = []
    if self.value is None:
      return []
    # only return results where value is within the range and node types are different
    elif left < self.value and self.value < right and self.node_type != node_type:
      result.append(self.value)
      result.extend(self.left_node.search_in_range(left, right, node_type))
      result.extend(self.right_node.search_in_range(left, right, node_type))
    elif right <= self.value:
      result.extend(self.left_node.search_in_range(left, right, node_type))
    elif self.value <= left:
      result.extend(self.right_node.search_in_range(left, right, node_type))
    return result


  # prints the binary tree with root node on the left and children on the right
  def print_binary_tree(self):
    if self.value is None:
      return
    self._print_binary_tree(0, self.height())


  def _print_binary_tree(self, n, height):
    if n > height:
      return
    if self.value is None:
      print('\n' * (2 ** (height - n + 1) - 1), end = '')
    else:
      self.left_node._print_binary_tree(n + 1, height)
      print('      ' * n, self.value, ' ', self.node_type, sep = '')
      self.right_node._print_binary_tree(n + 1, height)


  def height(self):
    if self.value is None:
      return 0
    return max(self.left_node._height(), self.right_node._height())


  def _height(self):
    if self.value is None:
      return 0
    return max(self.left_node._height(), self.right_node._height()) + 1


if __name__ == "__main__":
  # for testing pupose only
  test_tree = BST(8)
  test_tree.insert(11)
  test_tree.insert(5)
  test_tree.insert(1)
  test_tree.insert(3)
  test_tree.insert(9)
  test_tree.insert(7)
  test_tree.insert(11)
  test_tree.delete(5)
  test_tree.insert(10)
  test_tree.delete(9)
  test_tree.print_binary_tree()
  print(test_tree.search_in_range(1, 6))
  # compare result against https://people.ok.ubc.ca/ylucet/DS/BST.html

