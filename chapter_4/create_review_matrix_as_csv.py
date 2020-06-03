import pandas as pd
import numpy as np


def main():
    # Read in.
    df = pd.read_csv("movie_ratings_data_set.csv")

    # Convert to pivot table.
    ratings_df = pd.pivot_table(df, index='user_id', columns='movie_id', aggfunc=np.mean)

    # Create a .csv file of the data.
    ratings_df.to_csv("review_matrix.csv", na_rep="")


if __name__ == "__main__":
    main()
