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

    # Swap rows and columns of product features.
    M = np.transpose(M)

    # Choose a singular movie to find similar movies to. In this case, movie number 5.
    movie_id = 5

    # Get the selected movie's name and genre.
    movie_info = movies_df.loc[5]

    print("We are finding movies similar to this movie")
    print(f"Movie title: {movie_info.title}")
    print(f"Genre: {movie_info.genre}")

    # Get movie features.
    current_movie_features = M[movie_id - 1]

    print("The attributes for this movie are:")
    print(current_movie_features)

    ######################################## Logic for finding similar movies ##########################################

    # Subtract current movie features from every other movie's features.
    difference = M - current_movie_features

    # Take the abval of the difference.
    ab_difference = np.abs(difference)

    # Each movie has 15 features, Sum those 15 features to get a total "difference score" for each.
    total_diff = np.sum(ab_difference, axis=1)

    # Create new column in movie list with each movie's difference score.
    movies_df['difference_score'] = total_diff

    # Sort movie list by difference score from least to most different.
    sorted_movie_list = movies_df.sort_values('difference_score')

    # Print the 5 most similar movies to the selected movie.
    print("The 5 most similar movies are:")
    print(sorted_movie_list[['title', 'difference_score']][0:5])


if __name__ == "__main__":
    main()
