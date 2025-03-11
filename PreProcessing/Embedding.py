import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np
import Config


def embed_Model():
    # Read the DataFrame from the CSV file

    csv_path = Config.CLEANED_CSV_PATH
    model_path = Config.TRAINED_MODEL_PATH

    df = pd.read_csv(csv_path)

    # Combine text columns into a single column
    df['Combined_Text'] = df['Title'].astype(str) + df['Repro Steps'].astype(str) + '\n' + df['Symptom'].astype(str) + '\n' + df['Issue Root Cause'].astype(str) + '\n' + df['QA Remark'].astype(str)

    # Remove leading/trailing whitespaces
    df['Combined_Text'] = df['Combined_Text'].str.strip()

    # Load a pre-trained BERT-based model
    model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

    # Encode the DataFrame once and store the embeddings
    df_embeddings = model.encode(df['Combined_Text'].tolist())

    # Save the embeddings to the specified path
    np.save(model_path, df_embeddings)


# # ----------------------------------------------- UNIT TEST ----------------------
embed_Model()
