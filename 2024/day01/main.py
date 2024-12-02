import numpy as np


def get_distance_sum(x: np.ndarray, y: np.ndarray) -> int:
    # Sort arrays
    x = np.sort(x)
    y = np.sort(y)
    distance = np.abs(x - y)
    return int(np.sum(distance))


def get_similarity_score(x: np.ndarray, y: np.ndarray) -> int:
    # Create set of occurrences of y
    unique_counts = np.unique(y, return_counts=True)
    # Create dictionary for easy indexing
    y_counts = dict(zip(*unique_counts))
    score = int(sum(value * y_counts.get(value, 0) for value in x))
    return score


if __name__ == "__main__":
    txt_path = r"day01input.txt"
    col1, col2 = np.loadtxt(txt_path, unpack=True)
    distance_sum = get_distance_sum(x=col1, y=col2)
    print(distance_sum)
    sim_score = get_similarity_score(x=col1, y=col2)
    print(sim_score)
