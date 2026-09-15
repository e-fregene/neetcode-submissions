class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r=0,len(matrix)-1
        while r>l:
            for x in range(r-l): #=last array
                top,bottom=l,r


                #save topleft, rotate bottom left into it
                topleft= matrix[top][l+x]
                matrix[top][l+x]= matrix[bottom-x][l]

                #then move bototm right into moved position(bottom left)
                matrix[bottom-x][l] = matrix[bottom][r-x]

                #move topright into bottom right
                matrix[bottom][r-x] = matrix[top+x][r]

                #moved saved topleft into topright
                matrix[top+x][r]= topleft
            l+=1
            r-=1
        