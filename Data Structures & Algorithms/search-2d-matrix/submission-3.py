class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])

        top,bottom = 0,r-1

        just_less_than_the_target = bottom

        while top <= bottom:
            m = top + (bottom-top)//2

            if matrix[m][0] <= target:
                top = m + 1
                just_less_than_the_target = m
            else:
                bottom = m - 1

        left, right = 0 , c - 1

        print(just_less_than_the_target)

        while left <= right:
            m = left + (right-left)//2

            if matrix[just_less_than_the_target][m] == target:
                return True

            if matrix[just_less_than_the_target][m] > target:
                right = m -1 
            else:
                left = m + 1

        return False


            

