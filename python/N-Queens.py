def solve_n_queens(n):
    board = [["."] * n for _ in range(n)]
    res = []

    def is_valid(r, c):
        for i in range(r):
            if board[i][c] == "Q":
                return False
        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if board[i][j] == "Q":
                return False
        for i, j in zip(range(r - 1, -1, -1), range(c + 1, n)):
            if board[i][j] == "Q":
                return False
        return True

    def backtrack(r=0):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if is_valid(r, c):
                board[r][c] = "Q"
                backtrack(r + 1)
                board[r][c] = "."

    backtrack()
    return res

# Example
solutions = solve_n_queens(4)
for sol in solutions:
    for row in sol:
        print(row)
    print()
