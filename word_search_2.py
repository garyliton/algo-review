class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                node.children[char] = Node()
                node = node.children[char]

        node.is_word = True
        node.word = word

    def search(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.is_word


class Solution:
    def findWords(self, board, words):
        trie = Trie()
        hash_set = set()

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char in trie.root.children:
                    self.dfs(board, i, j, hash_set, trie.root)

        return list(hash_set)

    def dfs(self, board, i, j, hash_set, node):
        if node.is_word:
            node.is_word = False
            hash_set.add(node.word)
            return

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] not in node.children:
            return

        temp = board[i][j]
        board[i][j] = "#"

        self.dfs(board, i + 1, j, hash_set, node.children[temp])
        self.dfs(board, i - 1, j, hash_set, node.children[temp])
        self.dfs(board, i, j + 1, hash_set, node.children[temp])
        self.dfs(board, i, j - 1, hash_set, node.children[temp])

        board[i][j] = temp
        return


s = Solution()
board = [['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']]
words = ["oath", "pea", "eat", "rain"]
print(s.findWords(board, words))
