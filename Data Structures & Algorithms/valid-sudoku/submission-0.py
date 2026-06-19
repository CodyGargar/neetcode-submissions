class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = [row[c : c + 3] for row in board[r : r + 3]]
                if not self.check3x3(box):
                    print(box)
                    print("False by 3x3")
                    return False

        for i in range(9):
            if(not self.checkrow(board[i])):
                print("False by row")
                return False
            if(not self.checkrow([row[i] for row in board])):
                print("False by col")
                return False
        return True

    def check3x3(self, board: List[List[str]]):
        flat_list = [item for row in board for item in row]
        return self.checkrow(flat_list)
    def checkrow(self, board: List[str]):
        for x in range(len(board) - 1):
            for y in range(x + 1, len(board)):
                if(board[x] != "." and board[y] != "." and board[x] == board[y]):
                    return False
        return True