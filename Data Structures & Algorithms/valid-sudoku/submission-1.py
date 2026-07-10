class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h_line = [[] for _ in range(9)]
        
        for i in range(9):
            h_line = [r[i] for r in board if r[i]!="."]
            if len(set(h_line))!=len(h_line):
                return False
            b_line = [x for x in board[i] if x!="."]
            if len(set(b_line))!=len(b_line):
                return False
            
        for i in range(3):
            for j in range(3):
                tmp=[]
                for k in range(3):
                    tmp+=board[(i*3)+k][j*3:(j+1)*3]
                if len(set(tmp)) != len([x for x in tmp if x!="."])+1:
                    return False

        
        return True
