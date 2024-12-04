def check_word(word, row, col, dir_row, dir_col, puzzle_grid):
    word_length = len(word)
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    for k in range(word_length):
        new_row = row + dir_row * k
        new_col = col + dir_col * k
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if puzzle_grid[new_row][new_col] != word[k]:
                return False
        else:
            return False
    return True


def check_word_in_puzzle(word, puzzle_grid):
    rows = len(puzzle_grid)
    cols = len(puzzle_grid[0])
    count = 0
    directions = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ]
    for i in range(rows):
        for j in range(cols):
            if puzzle_grid[i][j] == word[0]:
                for dir_row, dir_col in directions:
                    if check_word(word, i, j, dir_row, dir_col, puzzle_grid):
                        count += 1
    return count


if __name__ == "__main__":
    word = "XMAS"
    puzzle_str_test = open("day04test.txt").read()
    puzzle_grid_test = [
        list(line.strip()) for line in puzzle_str_test.strip().split("\n")
    ]
    count_test = check_word_in_puzzle(word, puzzle_grid_test)
    assert count_test == 18

    puzzle_str = open("day04input.txt").read()
    puzzle_grid = [list(line.strip()) for line in puzzle_str.strip().split("\n")]
    count = check_word_in_puzzle(word, puzzle_grid)
    print(f"The word '{word}' occurs {count} times in the grid.")
