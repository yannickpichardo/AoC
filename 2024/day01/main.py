import numpy as np


def get_distance_sum(x: np.ndarray, y: np.ndarray):
    distance = np.abs(x - y)
    return np.sum(distance)


def get_similarity_score(x: np.ndarray, y: np.ndarray):
    # Create set of occurrences of y
    unique_counts = np.unique(y, return_counts=True)
    y_counts = dict(zip(*unique_counts))
    score = sum(value * y_counts.get(value, 0) for value in x)
    return score


if __name__ == "__main__":
    txt_path = r"day01input.txt"
    col1, col2 = np.loadtxt(txt_path, unpack=True)
    ordered_col1 = np.sort(col1)
    ordered_col2 = np.sort(col2)
    distance_sum = get_distance_sum(x=ordered_col1, y=ordered_col2)
    print(distance_sum)
    sim_score = get_similarity_score(ordered_col1, ordered_col2)
    print(sim_score)
