import pandas as pd
import Config


class DataFrameFilter:
    def __init__(self):
        self.df = None
        self.WORK_ITEM_TYPE_FILTER = None
        self.STATUS_FILTER = None
        self.PROJECT_CODE_FILTER = None
        self.TEST_BY_FILTER = None
        self.ASSIGNED_TO_FILTER = None
        self.SOURCE_CATEGORY_FILTER = None
        self.CREATED_DATE_GREATER_FILTER = None  # Greater than
        self.CREATED_DATE_LESSER_FILTER = None  # Less than

    def load_dataframe(self, this_dataframe):
        self.df = this_dataframe

    def filter_dataframe(self):

        if self.WORK_ITEM_TYPE_FILTER is not None and bool(self.WORK_ITEM_TYPE_FILTER):
            self.df = self.df.loc[self.df['Work Item Type'].isin(self.WORK_ITEM_TYPE_FILTER)]

        if self.STATUS_FILTER is not None and bool(self.STATUS_FILTER):
            self.df = self.df.loc[self.df['State'].isin(self.STATUS_FILTER)]

        if self.PROJECT_CODE_FILTER is not None and bool(self.PROJECT_CODE_FILTER):
            self.df = self.df.loc[self.df['Project Code'].isin(self.PROJECT_CODE_FILTER)]

        if self.TEST_BY_FILTER is not None and bool(self.TEST_BY_FILTER):
            self.df = self.df.loc[self.df['Test By'].isin(self.TEST_BY_FILTER)]

        if self.ASSIGNED_TO_FILTER is not None and bool(self.ASSIGNED_TO_FILTER):
            self.df = self.df.loc[self.df['Assigned To'].isin(self.ASSIGNED_TO_FILTER)]

        if self.SOURCE_CATEGORY_FILTER is not None and bool(self.SOURCE_CATEGORY_FILTER):
            self.df = self.df.loc[self.df['Source Category'].isin(self.SOURCE_CATEGORY_FILTER)]

        if self.CREATED_DATE_GREATER_FILTER is not None and bool(self.CREATED_DATE_GREATER_FILTER):
            self.df = self.df.loc[self.df['Created Date'] >= self.CREATED_DATE_GREATER_FILTER]

        if self.CREATED_DATE_LESSER_FILTER is not None and bool(self.CREATED_DATE_LESSER_FILTER):
            self.df = self.df.loc[self.df['Created Date'] <= self.CREATED_DATE_LESSER_FILTER]


        return self.df


# # ---------------------------------- UNIT TEST ---------------------------
#
#
# df = pd.read_csv(Config.CLEANED_CSV_PATH)
#
# df_filter = DataFrameFilter()
#
# df_filter.load_dataframe(df)
#
# df2 = df_filter.filter_dataframe()
#
# # Display the resulting DataFrame df2
# print(df2)
