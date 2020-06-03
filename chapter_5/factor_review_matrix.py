import pandas as pd
import numpy as np
import matrix_factorization_utilities


def main():
    # Load the data.
    raw_dataset_df = pd.read_csv("movie_ratings_data_set.csv")

    # Convert running list of users into a matrix.
    ratings_df = pd.pivot_table(raw_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)

    # Apply matrix factorization to get main features.
    U, M = matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.values, num_features=15,
                                                                        regularization_amount=.1)

    # Find all predicted ratings by multiplying U and M.
    predicted_ratings = np.matmul(U, M)

    # Save the ratings to a .csv file.
    predicted_ratings_df = pd.DataFrame(index=ratings_df.index,
                                        columns=ratings_df.columns,
                                        data=predicted_ratings)
    predicted_ratings_df.to_csv("predicted_ratings.csv")


if __name__ == "__main__":
    main()


