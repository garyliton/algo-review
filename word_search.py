class Solution:
    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.search(board, word, i, j, 0):
                    return True
        return False

    def search(self, board, word, i, j, count):
        if count == len(word):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[count]:
            return False

        temp = board[i][j]
        board[i][j] = ' '
        found = self.search(board, word, i + 1, j, count + 1) or \
                self.search(board, word, i - 1, j, count + 1) or \
                self.search(board, word, i, j + 1, count + 1) or \
                self.search(board, word, i, j - 1, count + 1)

        board[i][j] = temp
        return found


s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")