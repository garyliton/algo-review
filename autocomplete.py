class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        self.end = False

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
                node.end = False
                node = node.children[char]

        node.is_word = True
        node.word = word
        node.end = True

    def search(self, s):
        node = self.root

        for char in s:
            if char in node.children:
                node = node.children[char]
            else:
                return []

        return self.traverse(node)

    def traverse(self, node):
        res = []

        if node.is_word:
            res.append(node.word)
        for char in node.children:
            temp_node = node.children[char]
            while temp_node.end != True:
                if temp_node.is_word:
                    res.append(temp_node.word)
                temp_node = temp_node.children[list(temp_node.children.keys())[0]]
            res.append(temp_node.word)
        return res

def autocomplete(prefix, words):
    trie = Trie()

    for word in words:
        trie.insert(word)

    return trie.search(prefix)

print(autocomplete("de", ["dog", "deer", "deal"]))
print(autocomplete("ca", ["cat", "car", "cer"]))



