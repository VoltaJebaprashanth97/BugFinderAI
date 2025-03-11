import pandas as pd
from sentence_transformers import SentenceTransformer, util
import numpy as np

import Config


class SimilarityFinderAdvanced:
    def __init__(self):
        self.embeddings = None
        self.givenText = None
        self.df = None

    def setEmbeddings(self, this_embedding):
        self.embeddings = this_embedding

    def setGivenText(self, given_text):
        self.givenText = given_text

    def loadDataframe(self, data_frame):
        self.df = data_frame

    def getSimilarity(self):
        model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

        given_text = self.givenText

        # Encode the given text
        given_text_embedding = model.encode([given_text])

        # Calculate cosine similarity with stored DataFrame embeddings
        cosine_similarities = util.pytorch_cos_sim(given_text_embedding, np.array(self.embeddings)).numpy().flatten()

        # Create a copy of the original DataFrame
        result_df = self.df.copy()

        # Add a new column 'Cosine_Similarity' to the DataFrame
        result_df['Cosine_Similarity'] = cosine_similarities

        # Sort by cosine similarity in descending order
        result_df = result_df.sort_values(by='Cosine_Similarity', ascending=False)

        return result_df


# # ------------------------------------------- UNIT TEST -------------------------------
# df = pd.read_csv(Config.CLEANED_CSV_PATH)
# embeddings = np.load(Config.TRAINED_MODEL_PATH)
#
# finder = SimilarityFinderAdvanced()
#
# finder.loadDataframe(df)
# finder.setEmbeddings(embeddings)
# finder.setGivenText("Cannot enter data entry for month baishak")
#
# print(finder.getSimilarity())
