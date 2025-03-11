import json

from AI.similarityFinderAdvanced import SimilarityFinderAdvanced
from AI.similarityFinderTitle import SimilarityFinderTitle
from Filter.dataFrameFilter import DataFrameFilter
import pandas as pd
import numpy as np

import Config


class Runner:
    def __init__(self):
        self.df = None
        self.embeddings = None
        self.givenText = None
        self.mode = 'Advanced'
        self.numberOfResults = 100
        self.work_item_type_filter = None
        self.status_filter = None
        self.project_code_filter = None
        self.test_by_filter = None
        self.assigned_to_filter = None
        self.source_category_filter = None
        self.created_date_greater_than_filter = None
        self.created_date_lesser_than_filter = None

    def runSimilarityFinderTitle(self):
        # -------- Filter
        thisFilter = DataFrameFilter()

        thisFilter.WORK_ITEM_TYPE_FILTER = self.work_item_type_filter
        thisFilter.STATUS_FILTER = self.status_filter
        thisFilter.PROJECT_CODE_FILTER = self.project_code_filter
        thisFilter.TEST_BY_FILTER = self.test_by_filter
        thisFilter.ASSIGNED_TO_FILTER = self.assigned_to_filter
        thisFilter.SOURCE_CATEGORY_FILTER = self.source_category_filter
        thisFilter.CREATED_DATE_GREATER_FILTER = self.created_date_greater_than_filter
        thisFilter.CREATED_DATE_LESSER_FILTER = self.created_date_lesser_than_filter

        thisFilter.load_dataframe(self.df)
        filteredDataframe = thisFilter.filter_dataframe()

        # -------- Finder
        finder = SimilarityFinderTitle()
        finder.load_dataframe(filteredDataframe)

        finder.set_given_title(self.givenText)

        return finder.get_most_similar_rows(self.numberOfResults)

    def runSimilarityFinderAdvanced(self):
        # ------------- finder --------------
        finder = SimilarityFinderAdvanced()

        finder.loadDataframe(self.df)
        finder.setEmbeddings(self.embeddings)
        finder.setGivenText(self.givenText)

        ascendingDataframe = finder.getSimilarity()

        # ------ Filter ------

        thisFilter = DataFrameFilter()

        thisFilter.WORK_ITEM_TYPE_FILTER = self.work_item_type_filter
        thisFilter.STATUS_FILTER = self.status_filter
        thisFilter.PROJECT_CODE_FILTER = self.project_code_filter
        thisFilter.TEST_BY_FILTER = self.test_by_filter
        thisFilter.ASSIGNED_TO_FILTER = self.assigned_to_filter
        thisFilter.SOURCE_CATEGORY_FILTER = self.source_category_filter
        thisFilter.CREATED_DATE_GREATER_FILTER = self.created_date_greater_than_filter
        thisFilter.CREATED_DATE_LESSER_FILTER = self.created_date_lesser_than_filter

        thisFilter.load_dataframe(ascendingDataframe)
        filteredDataframe = thisFilter.filter_dataframe()

        filteredDataframe = filteredDataframe.head(self.numberOfResults).copy()

        return filteredDataframe

    @staticmethod
    def dataframeToJson(df):
        json_string = df.to_json(orient='records')
        json_object = json.loads(json_string)
        return json_object

    def run(self):

        if self.mode != 'Title':
            df = self.runSimilarityFinderAdvanced()
            return Runner.dataframeToJson(df)
        else:
            df = self.runSimilarityFinderTitle()
            return Runner.dataframeToJson(df)

# # ---------------------------- Unit Test -------------------------------------------------------------
#
# runner = Runner()
#
# runner.df = pd.read_csv(Config.CLEANED_CSV_PATH)
# runner.embeddings = np.load(Config.TRAINED_MODEL_PATH)
# runner.givenText = 'Cannot enter data entry'
# runner.numberOfResults = 100
# json_data = runner.run()
# print(json.dumps(json_data, indent=4))
