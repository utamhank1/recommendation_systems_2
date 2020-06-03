import pandas as pd
import numpy as np
import matrix_factorization_utilities


def main():
    # Load the data.
    raw_dataset_df = pd.read_csv("movie_ratings_data_set.csv")

    # Load movie titles.
    movies_df = pd.read_csv("movies.csv")

    # Convert running list of users into a matrix.
    ratings_df = pd.pivot_table(raw_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)

    # Apply matrix factorization to get main features.
    U, M = matrix_factorization_utilities.low_rank_matrix_factorization(ratings_df.values, num_features=15,
                                                                        regularization_amount=.1)

    # Find all predicted ratings by multiplying U and M matrices.
    predicted_ratings = np.matmul(U, M)

    print("Enter a user_id between 1 and 100 to get a recommendation:")
    user_id_to_search = int(input())

    print(f"Movies previously reviewed by user_id {user_id_to_search}")

    reviewed_movies_df = raw_dataset_df[raw_dataset_df['user_id'] == user_id_to_search]
    reviewed_movies_df = reviewed_movies_df.merge(movies_df, on='movie_id')

    print(reviewed_movies_df[['title', 'genre', 'value']])

    input("Press enter to continue.")

    print("Movies we will recommend:")

    user_ratings = predicted_ratings[user_id_to_search - 1]
    movies_df['rating'] = user_ratings

    already_reviewed = reviewed_movies_df['movie_id']
    recommended_df = movies_df[movies_df.index.isin(already_reviewed) == False]
    recommended_df = recommended_df.sort_values(by=['rating'], ascending=False)

    print(recommended_df[['title', 'genre', 'rating']].head(5))


if __name__ == "__main__":
    main()
