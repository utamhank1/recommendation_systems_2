def main():
    ratings = [5,
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
               ]

    for i, value in enumerate(ratings):
        print(f"Updating rating: {i}")
        ratings[i] = value*2


if __name__ == "__main__":
    main()