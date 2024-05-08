def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def backtracking_n_queens(board, row, n, solutions):
    if row == n:
        solutions.append([row[:] for row in board])
        return
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            backtracking_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0

def branch_and_bound_n_queens(n):
    def is_promising(board, row, col, n):
        # Check if there is a queen in the same column
        for i in range(row):
            if board[i][col] == 1:
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 1:
                return False

        return True

    def backtrack(board, row, n, solutions, min_conflicts):
        if row == n:
            solutions.append([row[:] for row in board])
            return

        for col in range(n):
            if is_promising(board, row, col, n):
                board[row][col] = 1
                conflict_count = count_conflicts(board, row, col, n)
                if conflict_count < min_conflicts[row]:
                    min_conflicts[row] = conflict_count
                    backtrack(board, row + 1, n, solutions, min_conflicts)
                board[row][col] = 0

    def count_conflicts(board, row, col, n):
        conflicts = 0
        for i in range(n):
            if i != col and board[row][i] == 1:
                conflicts += 1
            if i != row and board[i][col] == 1:
                conflicts += 1
            if 0 <= row - i < n and 0 <= col - i < n and i != row and i != col and board[row - i][col - i] == 1:
                conflicts += 1
            if 0 <= row - i < n and 0 <= col + i < n and i != row and i != col and board[row - i][col + i] == 1:
                conflicts += 1
        return conflicts

    solutions = []
    min_conflicts = [float('inf')] * n
    board = [[0] * n for _ in range(n)]
    backtrack(board, 0, n, solutions, min_conflicts)
    return solutions

def print_solutions(solutions):
    for idx, sol in enumerate(solutions, 1):
        print(f"Solution {idx}:")
        for row in sol:
            print(" ".join(map(str, row)))
        print()

def get_input():
    n = int(input("Enter the number of queens: "))
    return n

# Backtracking
n = get_input()
backtracking_solutions = []
backtracking_n_queens([[0] * n for _ in range(n)], 0, n, backtracking_solutions)
print("Backtracking Solutions:")
print_solutions(backtracking_solutions)

# Branch and Bound
n = get_input()
branch_and_bound_solutions = branch_and_bound_n_queens(n)
print("Branch and Bound Solutions:")
print_solutions(branch_and_bound_solutions)
