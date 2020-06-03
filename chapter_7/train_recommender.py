import pickle
import pandas as pd
import numpy as np
import matrix_factorization_utilities


def main():
    # Load data.
    raw_dataset_df = pd.read_csv("movie_ratings_data_set.csv")

    # Convert running list to a matrix.
    ratings_df = pd.pivot_table(raw_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)

    # Apply matrix factorization.
    U, M = matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.values,
                                                                        num_features=15,
                                                                        regularization_amount=.1)

    # Find all predicted ratings by multiplying U and M.
    predicted_ratings = np.matmul(U, M)

    # Save features and predicted ratings to file for later use.
    pickle.dump(U, open("user_features.dat", "wb"))
    pickle.dump(M, open("product_features.dat", "wb"))
    pickle.dump(predicted_ratings, open("predicted_ratings.dat", "wb"))


if __name__ == "__main__":
    main()