#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    root = { }
    tree_index = 0
    tree[tree_index] = root
    for pattern in patterns:
      current_node = root
      for index, letter in enumerate(pattern):
        if letter in current_node:
          current_node = tree[current_node[letter]]
        else:
          tree_index += 1
          tree[tree_index] = {}
          current_node[letter] = tree_index
          current_node = tree[tree_index]
    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
