import json

import pandas as pd
import Config


class GetUniqueFilterValues:
    def __init__(self):
        pass

    def getUniqueFilterValues(self, df):
        unique_values = {
            'Work Item Type': df['Work Item Type'].value_counts().index.tolist(),
            'State': df['State'].value_counts().index.tolist(),
            'Project Code': df['Project Code'].value_counts().index.tolist(),
            'Test By': df['Test By'].value_counts().index.tolist(),
            'Assigned To': df['Assigned To'].value_counts().index.tolist(),
            'Source Category': df['Source Category'].value_counts().index.tolist(),
        }

        # Convert to JSON
        unique_values_json = pd.Series(unique_values).to_json(orient='index')
        json_object = json.loads(unique_values_json)
        return json_object


# # ----------------------------------- UNIT TEST -------------------------------
#
# df = pd.read_csv(Config.CLEANED_CSV_PATH)
# filter = GetUniqueFilterValues()
# print(filter.getUniqueFilterValues(df))
