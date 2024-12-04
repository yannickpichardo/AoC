def get_x_mas(puzzle_grid):
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    patterns = ["MAS", "SAM"]
    count = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if puzzle_grid[i][j] == "A":
                # Diagonal from top-left to bottom-right
                diag1 = (
                    puzzle_grid[i - 1][j - 1]
                    + puzzle_grid[i][j]
                    + puzzle_grid[i + 1][j + 1]
                )
                # Diagonal from top-right to bottom-left
                diag2 = (
                    puzzle_grid[i - 1][j + 1]
                    + puzzle_grid[i][j]
                    + puzzle_grid[i + 1][j - 1]
                )

                # Check if both diagonals form 'MAS' or 'SAM'
                if diag1 in patterns and diag2 in patterns:
                    count += 1
    return count


if __name__ == "__main__":
    puzzle_str = open("day04input.txt").read()
    puzzle_grid = [list(line.strip()) for line in puzzle_str.strip().split("\n")]
    count = get_x_mas(puzzle_grid)
    print(f"The X-MAS pattern occurs {count} times in the grid.")
