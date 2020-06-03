import pandas as pd
import os
import webbrowser


def main():
    # Read the dataset.
    data_table = pd.read_csv("movie_ratings_data_set.csv")

    # Create webpage to view the data.
    html = data_table[0:100].to_html()

    # Save html to temporary file.
    with open("data.html", "w") as f:
        f.write(html)

    # Open web page in web browser.
    full_filename = os.path.abspath("data.html")
    webbrowser.open(f"file://{full_filename}")


if __name__ == "__main__":
    main()
