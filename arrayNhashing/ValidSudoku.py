from collections import defaultdict

class Sudoku:
    # Class Sudoku
    # This class helps in encapsulating the properties and methods of a sudoku board

    def __init__(self,matrix):
        # Constructor
        # Input
        #   matrix  (matrix)    This is a 9x9 matrix that contains numbers (1-9) or . (signify empty cells).
        # Attributes
        #   self.sudoku         (matrix)    Store the sudoku board layout
        #   self.chunkCounter   (int)       Check which chunks have been counted
        #   self.chunkIndices   (matrix)    Stores the starting row and starting column of each and every 3x3 chunk present in the sudoku board    
        self.sudoku= matrix
        self.chunkCounter=0
        self.chunkIndices=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]


    def getNextChunk(self):
        # Method
        # Returns the next 3x3 chunk of the Sudoku Board
        # Input
        #   None
        # Output
        #   (matrix)    3x3 chunk of the sudoku board
        
        # Check if all chunks have been returned 
        if self.chunkCounter>=9:
            # If yes then return a False flag saying that there are no more chunks to be checked
            return False,0
        
        # Get the respective starting chunk indices (starting row and starting column).
        chunkIndex = self.chunkIndices[self.chunkCounter]
        
        # Increment the chunk counter
        self.chunkCounter+=1
        
        # Extract out the chunk from the sudoku board
        chunk=[]
        for i in range(3):
            q=[]
            for j in range(3):
                q.append(self.sudoku[chunkIndex[0]+i][chunkIndex[1]+j])
            chunk.append(q)
        
        # Return a True flag and the chunk with it
        return True, chunk


    def checkChunk(self,chunk):
        # Method
        # Checks if the given chunk is valid or not
        # Input
        # chunk     (matrix)    3x3 matrix that contains the chunk information
        # Output
        # (bool)    Returns True if the chunk is valid, False otherwise
        
        # Initialize our hashmap
        dct=defaultdict(int)
        
        # Check each element in the chunk
        for i in range(3):
            for j in range(3):
                
                # If the chunk cell is not empty
                if chunk[i][j]!='.':
                    
                    # If the number in the cell has occurred before
                    if dct[chunk[i][j]]==1:
                        # Return an invalid chunk
                        return False
                    else:
                        # Add to Hashmap as a visited cell
                        dct[chunk[i][j]]=1
        
        # Since we found no duplicate elements we'll return it as a Valid Chunk
        return True

    def checkRow(self,row):
        # Method
        # Checks the validity of a given row
        # Input
        #   row     (list)  List of numbers and . signifying the elements in the row
        # Output
        #   (bool)  Returns True if the row is valid, False otherwise
        
        # Initialize our hashmap
        dct=defaultdict(int)
        
        # Iterate through each element in the row
        for i in range(9):
            if row[i]!='.':
                
                # If the elemnent was found before 
                if dct[row[i]]==1:
                    # Return that the Row is not Valid
                    return False
                # Add the element to the visited hashmap
                dct[row[i]]=1
        # If no duplicates found then return the row as valid
        return True
    
    def checkColumn(self,col):
        # Method
        # Checks the validity of a given column
        # Input
        #   col     (list)  List of numbers and . signifying the elements in the Column
        # Output
        #   (bool)  Returns True if the column is valid, False otherwise
        
        # Initialize our hashmap        
        dct=defaultdict(int)
        
        # Iterate through each element in the column
        for i in range(9):
            if col[i]!='.':
                
                # If the element was found before 
                if dct[col[i]]==1:
                    # Return that the column is not valid
                    return False
                # add the element to the visited hash map
                dct[col[i]]=1
        # If no duplicates found then return the column as valid
        return True
    
    def checkValidity(self):
        # Method 
        # This method checks the validity of the sudoku board by performing 3 tasks
        #   1) Check every chunk
        #   2) Check every row
        #   3) Check every column
        # Input
        #   None
        # Output
        #   (bool)  True if the sudoku board is valid, false otherwise
        
        # Check Each Chunk
        while(True):
            
            # Get the next chunk 
            ret,chunk = self.getNextChunk()
            
            # If checked all chunks then break
            if ret==False:
                break
            
            # Check if the chunk is invalid
            if not self.checkChunk(chunk):
                # Repeated Element in chunk
                return False
        
        # Check Each Row
        for i in range(9):
            
            # Get the next row
            row = self.sudoku[i]
            
            # Check the row
            ret = self.checkRow(row)
            
            # Check if the row is invalid
            if ret==False:
                # Repeated element in row
                return False
            
        # Check Each Column
        for i in range(9):
            
            # Get next column
            q=[]
            for j in range(9):
                q.append(self.sudoku[j][i])
                
            # Check the column
            ret=self.checkColumn(q)
            
            # Check if the column is invalid
            if ret==False:
                # Repeated Elemet in Column
                return False        
        
        # If no violation was found hence the sudoku board must be valid
        return True

class Solution:
    def isValidSudoku(self, board):
        # Function
        # Returns whether the sudoku is valid or not. Meaning there are no repeated numbers in a chunk, along the row and along the columns
        # Input:
        #   board   (matrix)    a 9X9 sudoku board with numbers (1-9) and . at different positions (. signifies empty cell)
        # Output:
        #   (bool)  Returns True if the sudoku board is valid; False otherwise
        
        # Instantiate the Sudoku class with the given board
        sudoku = Sudoku(board)
        
        # Return the method where it checks if the Sudoku board is valid
        return sudoku.checkValidity()