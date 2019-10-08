class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # Define neighbor array
        neighbors = [(-1,-1), (-1,0), (-1,1), (0,-1), (0, 1), (1,-1), (1,0), (1, 1)]

        # Basically going to iterate through the row and the length index, and check that the current index of the matrix + neighbor is within the matrix boundary, then perform the necessary live neighbor calculation.

        # get length and width of the board
        cols = len(board[0])
        rows = len(board)

        # Can't use copy_board = board[:][:]
        copy_board = [[board[row][col] for col in range(cols)] for row in range(rows)]

        for row in range(rows):
            for col in range(cols):

                # For each neighbor, count the number of neighbors
                live_neighbors = 0

                for neighbor in neighbors:
                    r = neighbor[0] + row
                    c = neighbor[1] + col

                    if (r >= 0 and r < rows) and (c >= 0 and c < cols) and (copy_board[r][c] == 1):
                        live_neighbors += 1

                if (live_neighbors < 2 or live_neighbors > 3) and copy_board[row][col] == 1:
                    board[row][col] = 0
                if live_neighbors == 3 and copy_board[row][col] == 0:
                    board[row][col] = 1

        return board
