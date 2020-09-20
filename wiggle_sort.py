class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def wiggleSort(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    less = True
    for i in range(len(nums) - 1):
        if less:
            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
        else:
            if nums[i] < nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
        less = not less

    return nums


def insert(root, val):
    temp = Node(val)

    if root is None:
        root = temp
    else:
        cur_node = root
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = temp

    return root


def lst_to_linked_list(lst):
    if len(lst) == 0:
        return None

    root = None
    for num in lst:
        root = insert(root, num)

    return root


def lst_to_linked_list_2(lst):
    root = Node(lst[0])
    temp = root
    for num in lst[1:]:
        temp.next = Node(num)
        temp = temp.next

    return root


def print_linked_list(head):
    node = head

    while node is not None:
        print(str(node.val) + "->", end="")
        node = node.next
    print("None")


print_linked_list(lst_to_linked_list_2(wiggleSort([3, 5, 2, 1, 6, 4])))
