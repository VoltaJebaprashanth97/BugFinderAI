import pandas as pd
import numpy as np

import Config


def loadDataframe():
    df = pd.read_csv(Config.CLEANED_CSV_PATH)
    return df


def loadEmbeddings():
    embeddings = np.load(Config.TRAINED_MODEL_PATH)
    return embeddings
