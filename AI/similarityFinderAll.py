import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import Config


class SimilarityFinderAll:
    def __init__(self):
        self.df = None
        self.given_title = None
        self.vectorizer_title = None
        self.tfidf_matrix_title = None
        self.similarities = None

    def load_dataframe(self, df):
        self.df = df

    def set_given_title(self, title):
        if self.df is None:
            raise ValueError("Please load a DataFrame using the 'load_dataframe' method first.")

        self.given_title = title
        self._update_similarity()

    def _update_similarity(self):

        self.df['Combined_Text'] = self.df['Repro Steps'].astype(str) + '\n' + self.df['Symptom'].astype(str) + '\n' + \
                                   self.df['Issue Root Cause'].astype(str) + '\n' + self.df['QA Remark'].astype(str)

        # Optionally, you can also remove any leading/trailing whitespaces
        self.df['Combined_Text'] = df['Combined_Text'].str.strip()

        # Fill NaN values in 'Title' column with an empty string
        self.df['Combined_Text'] = self.df['Combined_Text'].fillna("")

        # Concatenate the given title with the existing titles in the DataFrame
        all_titles = self.df['Combined_Text'].append(pd.Series([self.given_title]), ignore_index=True)

        # Create a TF-IDF vectorizer for Title
        self.vectorizer_title = TfidfVectorizer()
        self.tfidf_matrix_title = self.vectorizer_title.fit_transform(all_titles)

        # Calculate the cosine similarity between the given title and all other titles
        self.similarities = cosine_similarity(self.tfidf_matrix_title[-1], self.tfidf_matrix_title[:-1])

    def get_most_similar_rows(self, num_rows=100):
        if self.similarities is None:
            raise ValueError("Please set the 'given_title' first.")

        # Get the indices of the top N most similar rows
        most_similar_indices = self.similarities.argsort()[0, ::-1][:num_rows]

        # Retrieve the most similar N rows from the original DataFrame
        most_similar_rows = self.df.iloc[most_similar_indices]

        return most_similar_rows


# # ------------------------------------------------ UNIT TEST----------------------------------------------------
#
# df = pd.read_csv(Config.CLEANED_CSV_PATH)
# # Sample usage:
# # Create an instance of the SimilarityFinderBasic class
# similarity_finder = SimilarityFinderAll()
#
# # Load the DataFrame
# similarity_finder.load_dataframe(df)
#
# # Set the given title using the set_given_title method
# similarity_finder.set_given_title("cannot enter month baishak as data entry")
#
# # Get the most similar rows
# most_similar_rows = similarity_finder.get_most_similar_rows()
#
# # Display the most similar rows as a DataFrame
# print(most_similar_rows)
