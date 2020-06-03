import numpy as np


def main():
    array = np.array([5,
                      2,
                      3,
                      3,
                      4,
                      5,
                      5,
                      1,
                      5,
                      1,
                      3,
                      4
                      ])

    ratings = array * 2
    print(ratings)


if __name__ == "__main__":
    main()
