from collections import Counter
from operator import attrgetter


class MyNode:

    def __init__(self, weight=0, left=None, right=None, data='root'):
        self.weight = weight
        self.left = left
        self.right = right
        self.data = data

    def __repr__(self):
        return f'Tree Node Weight: {self.weight}, Data: {self.data}'


def get_weight(nodes):
    weights = [node.weight for node in nodes]
    return weights


def build_tree(_string):
    freq = Counter(_string).most_common()
    tree = [MyNode(weight=i[1], left=MyNode(data=i[0])) for i in freq]
    tree.sort(key=attrgetter('weight'))

    while len(tree) > 2:
        tree[:2][0].data = '0'
        tree[:2][1].data = '1'
        node = MyNode(weight=sum(get_weight(tree[:2])), left=tree[:2][0], right=tree[:2][1])
        tree = tree[2:]
        tree.append(node)
        tree.sort(key=attrgetter('weight'))

    assert len(tree) == 2
    tree[0].data = '0'
    tree[1].data = '1'
    tree = MyNode(weight=sum(get_weight(tree)), left=tree[0], right=tree[1])
    return tree


def find_leaves(root):
    if root is None:
        return []
    if root.left is None and root.right is None:
        return [root.data]
    return [root.data + '->' + leaf for leaf in find_leaves(root.right) + find_leaves(root.left)]


def encoding_table(paths):
    table = {}
    for path in paths:
        table[path[-1:]] = path[4:][:-1].replace('->', '')
    return table


def encode(_string):
    table = encoding_table(find_leaves(build_tree(_string)))
    for letter in _string:
        if letter in table.keys():
            _string = _string.replace(letter, table[letter])
    return _string


user_input = input('String to encode: ')
encoded_string = encode(user_input)
print(f'\n{user_input} : {encoded_string}\nEncoding table:\n{encoding_table(find_leaves(build_tree(user_input)))}')
