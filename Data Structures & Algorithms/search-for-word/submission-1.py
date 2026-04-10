class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        def isValid(i,j):
            return i >= 0 and i < n and j >=0 and j < m

        def dfs(i,j,k,vis):
            print(i,j,k)
            if k == len(word):
                return True

            vis[(i,j)] = True
            res = False 
            for u,v in [[0,1],[0,-1],[-1,0],[1,0]]:
                l = i + u
                r = j + v
                # print(l,r,isValid(l,r),((l,r) not in vis), board[l][r] == word[k])
                if isValid(l,r) and ((l,r) not in vis) and board[l][r] == word[k]:
                    res = res or dfs(l,r,k+1,vis)
                    print(board[l][r])
                    if (l,r) in vis:
                        del vis[(l,r)]

            return res
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i,j,1,{}):
                    return True

        return False

                
                
            


        