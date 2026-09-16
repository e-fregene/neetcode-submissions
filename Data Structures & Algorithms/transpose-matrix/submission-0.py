class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        #cols # in array
        #rows is amount of arrays

        row,col= len(matrix), len(matrix[0])

        res=[]
        for c in range(col):
            new_row=[] #number of cols become number of rows
            for r in range(row):
                new_row.append(matrix[r][c])

            res.append(new_row)

        return res