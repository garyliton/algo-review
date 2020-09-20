class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def display(root):
    while root is not None:
        print(str(root.val) + '->', end = '')
        root = root.next
    print('None')


def insert(root, val):
    # create node
    temp = Node(val)

    # first Node in linked list
    if root is None:
        root = temp
    else:
        cur_node = root
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = temp

    return root


def arr_to_lst(lst):
    root = None

    for num in lst:
        root = insert(root, num)

    return root


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    root = arr_to_lst(lst)
    display(root)
