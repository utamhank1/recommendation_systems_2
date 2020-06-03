import pandas as pd
import numpy as np
import os
import webbrowser


def main():
    # Read in.
    df = pd.read_csv("movie_ratings_data_set.csv")

    # Convert running list to pivot table.
    ratings_df = pd.pivot_table(df, index='user_id', columns='movie_id', aggfunc=np.mean)

    # Create webpage.
    html = ratings_df.to_html()

    # Save html to temporary file.
    with open("review_matrix.html", "w") as f:
        f.write(html)

    # Open webpage.
    full_filename = os.path.abspath("review_matrix.html")
    webbrowser.open(f"file://{full_filename}")


if __name__ == "__main__":
    main()
