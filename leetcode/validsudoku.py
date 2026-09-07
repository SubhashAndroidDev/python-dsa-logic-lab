class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                if num == ".":
                    continue

                box_index = (row // 3) * 3 + (col // 3)

                if num in rows[row] or \
                   num in cols[col] or \
                   num in boxes[box_index]:
                    return False

                rows[row].add(num)
                cols[col].add(num)
                boxes[box_index].add(num)

        return True


board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

solution = Solution()

result = solution.isValidSudoku(board)

print(result)