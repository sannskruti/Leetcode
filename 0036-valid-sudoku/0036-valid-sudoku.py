class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        m = len(board)
        n = len(board[0])

        # 1. Check each ROW for duplicates
        for i in range(m):
            nums = set()

            for j in range(n):
                num = board[i][j]

                if num == '.':
                    continue

                if num in nums:
                    return False

                nums.add(num)

        # 2. Check each COLUMN for duplicates
        for i in range(n):
            nums = set()

            for j in range(m):
                num = board[j][i]  # Fixed indexing

                if num == '.':
                    continue

                if num in nums:
                    return False

                nums.add(num)

        # 3. Check each 3x3 SUB-BOX for duplicates
        for row in range(0, m, 3):
            for col in range(0, n, 3):

                nums = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        num = board[i][j]

                        if num == '.':
                            continue

                        if num in nums:
                            return False

                        nums.add(num)

        return True