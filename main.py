from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Initiator import Initiator
from Runner.Runner import Runner
from Runner.WebAPI import *
from SendFilters.getUniqueFilterValues import GetUniqueFilterValues

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set this to the appropriate origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATAFRAME = Initiator.loadDataframe()
EMBEDDINGS = Initiator.loadEmbeddings()


@app.get("/")
def root():
    return "BUG FINDER AI IS RUNNING"


@app.get("/get_filters")
def root_with_param():
    filters = GetUniqueFilterValues()
    return filters.getUniqueFilterValues(DATAFRAME)


@app.get("/{given_text}")
def root_with_param(given_text: str):
    runner = Runner()
    runner.df = DATAFRAME
    runner.embeddings = EMBEDDINGS
    runner.givenText = given_text

    return runner.run()


@app.post("/process_data")
async def process_data(data: InputData):
    runner = Runner()
    runner.df = DATAFRAME
    runner.embeddings = EMBEDDINGS

    # Access the input data using the data variable
    runner.mode = data.mode
    runner.numberOfResults = data.numberOfResults
    runner.givenText = data.givenText
    search_filters = data.searchFilters

    # Access specific filters
    runner.work_item_type_filter = search_filters.workItemTypeFilter
    runner.status_filter = search_filters.statusFilter
    runner.project_code_filter = search_filters.projectCodeFilter
    runner.test_by_filter = search_filters.testByFilter
    runner.assigned_to_filter = search_filters.assignedToFilter
    runner.source_category_filter = search_filters.sourceCategoryFilter
    runner.created_date_greater_than_filter = search_filters.createdDateGreaterThanFilter
    runner.created_date_lesser_than_filter = search_filters.createdDateLesserThanFilter

    # Run the processing logic
    return runner.run()
