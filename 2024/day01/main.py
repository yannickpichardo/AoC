import numpy as np


def get_distance_sum(x: np.ndarray, y: np.ndarray):
    distance = np.abs(x - y)
    return np.sum(distance)


if __name__ == "__main__":
    txt_path = r"day01input.txt"
    col1, col2 = np.loadtxt(txt_path, unpack=True)
    ordered_col1 = np.sort(col1)
    ordered_col2 = np.sort(col2)
    distance_sum = get_distance_sum(x=ordered_col1, y=ordered_col2)
    print(distance_sum)
