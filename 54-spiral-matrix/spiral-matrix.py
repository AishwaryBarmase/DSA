class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:

        n = len(matrix)
        m = len(matrix[0])

        total = n * m
        elements = []
        counter = 0      
        
        colstart = 0
        rowstart = 0
        rowend = n - 1
        colend = m -1

        while counter < total:
            # First Row: colstart --> colend
            for i in range(colstart, colend+1):
                elements.append(matrix[rowstart][i])
                counter += 1
            rowstart += 1

            if counter == total:
                break

            #Last Column, rowstart --> rowend
            for i in range(rowstart, rowend+1):
                elements.append(matrix[i][colend])
                counter += 1
            colend -= 1

            if counter == total:
                break

            
            #Last Row, colend --> colstart
            for i in range(colend, colstart -1, -1):
                elements.append(matrix[rowend][i])
                counter += 1
            rowend -= 1
            
            if counter == total:
                break
            
            #First Column, rowend --> rowstart
            for i in range(rowend, rowstart -1, -1):
                elements.append(matrix[i][colstart])
                counter += 1

            colstart += 1

            if counter == total:
                break

            


        return elements