class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, idx, visited):
            if idx == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if (r, c) in visited or board[r][c] != word[idx]:
                return False

            visited.add((r, c))
            found = (
                dfs(r + 1, c, idx + 1, visited)
                or dfs(r - 1, c, idx + 1, visited)
                or dfs(r, c + 1, idx + 1, visited)
                or dfs(r, c - 1, idx + 1, visited)
            )
            visited.remove((r, c)) 
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0, set()):
                    return True
        return False
