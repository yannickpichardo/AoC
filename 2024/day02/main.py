import numpy as np
import time


def get_safety_level(x: np.ndarray):
    x_diff = np.diff(x)
    # Check if increasing/decreasing
    if not (np.all(x_diff > 0) or np.all(x_diff < 0)):
        return False
    if np.any(np.abs(x_diff) >= 4):
        # Check if distance is bigger than 4
        return False
    return True


def get_safety_level_dampened(x: np.ndarray):
    if get_safety_level(x):
        return True
    for i in range(len(x)):
        x_dampened = np.delete(x, i)
        if get_safety_level(x_dampened):
            return True
    return False


def get_safety_level_dampened_vectorized(x: np.ndarray):
    if get_safety_level(x):
        return True

    # Create an identity matrix for each row with all options:
    masks = np.eye(len(x), dtype=bool)
    # Create all the possible dampened dampened_arrays
    # This however will lead to an overestimation
    dampened_arrays = [x[~mask] for mask in masks]
    return any(get_safety_level(x_dampened) for x_dampened in dampened_arrays)


if __name__ == "__main__":
    file_path = r"day02input.txt"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            # Split line into numbers and convert to float
            data.append(np.array([float(value) for value in line.split()]))
    safety_levels = [get_safety_level(row) for row in data]
    print(sum(safety_levels))
    start_loop = time.time()
    safety_levels_dampened = [get_safety_level_dampened(row) for row in data]
    print(sum(safety_levels_dampened))
    print(f"Time: {time.time() - start_loop}")
    start_vect = time.time()
    safety_levels_dampened_vector = [
        get_safety_level_dampened_vectorized(row) for row in data
    ]
    print(sum(safety_levels_dampened_vector))
    print(f"Time Vect: {time.time() - start_vect}")
    # No Noticeable difference between times.
