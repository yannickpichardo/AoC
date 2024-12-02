import numpy as np


def count_safe():
    pass


def get_safety_level(x: np.ndarray):
    x_diff = np.diff(x)
    # Check if increasing/decreasing
    if not (np.all(x_diff > 0) or np.all(x_diff < 0)):
        return False
    if np.any(np.abs(x_diff) >= 4):
        # Check if distance is bigger than 4
        return False
    return True


if __name__ == "__main__":
    file_path = r"day02input.txt"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            # Split line into numbers and convert to float
            data.append(np.array([float(value) for value in line.split()]))
    safety_levels = [get_safety_level(row) for row in data]
    print(sum(safety_levels))
