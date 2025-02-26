#class Node:
 #   def __init__(self, val):
  #      self.val = val
   #     self.children = []

    #def add_child(self, node):
     #   self.children.append(node)


#def traverse_tree(node, result=None):
 #   if result is None:
  #      result = []
   # result.append(node.val)
    #for child in node.children:
     #   traverse_tree(child, result)
   # return result


#def process_data(data):
 #   if not isinstance(data, list) or len(data) == 0:
  #      return None
   # root = Node(data[0])
   # nodes = {data[0]: root}
   # for i in range(1, len(data), 2):
    #    parent_val = data[i]
     #   child_val = data[i + 1]
      #  if parent_val in nodes:
       #     parent_node = nodes[parent_val]
        #else:
         #   parent_node = Node(parent_val)
          #  nodes[parent_val] = parent_node
        #if child_val in nodes:
        #    child_node = nodes[child_val]
        #else:
         #   child_node = Node(child_val)
          #  nodes[child_val] = child_node
        #parent_node.add_child(child_node)
    #return traverse_tree(root)


#data = [1, 1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 3, 7]
#result = process_data(data)
#print(result)


# chatgpt link:
# https://chatgpt.com/c/67bebcac-afbc-8010-ab9e-1722f2d16a37

class TreeNode:
    """Represents a node in a tree with a value and a list of children."""

    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        """Adds a child node to the current node."""
        self.children.append(child_node)


def depth_first_traversal(node, traversal_result=None):
    """Performs a depth-first traversal of the tree starting from the given node."""
    if traversal_result is None:
        traversal_result = []

    traversal_result.append(node.value)

    for child in node.children:
        depth_first_traversal(child, traversal_result)

    return traversal_result


def build_tree_from_data(data_list):
    """Builds a tree from a given list of parent-child relationships and returns its traversal."""
    if not isinstance(data_list, list) or len(data_list) == 0:
        return None

    # Create root node
    root_value = data_list[0]
    node_map = {root_value: TreeNode(root_value)}

    # Process the parent-child relationships
    for i in range(1, len(data_list), 2):
        parent_value, child_value = data_list[i], data_list[i + 1]

        # Retrieve or create the parent node
        parent_node = node_map.get(parent_value, TreeNode(parent_value))
        node_map[parent_value] = parent_node

        # Retrieve or create the child node
        child_node = node_map.get(child_value, TreeNode(child_value))
        node_map[child_value] = child_node

        # Establish the parent-child relationship
        parent_node.add_child(child_node)

    return depth_first_traversal(node_map[root_value])


# Example data representing parent-child relationships
data = [1, 1, 2, 1, 3, 2, 4, 2, 5, 3, 6, 3, 7]
traversal_result = build_tree_from_data(data)
print(traversal_result)
