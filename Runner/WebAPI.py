from typing import List

from pydantic import BaseModel


class SearchFilters(BaseModel):
    workItemTypeFilter: List[str]
    statusFilter: List[str]
    projectCodeFilter: List[str]
    testByFilter: List[str]
    assignedToFilter: List[str]
    sourceCategoryFilter: List[str]
    createdDateGreaterThanFilter: str
    createdDateLesserThanFilter: str


class InputData(BaseModel):
    mode: str
    numberOfResults: int
    givenText: str
    searchFilters: SearchFilters
