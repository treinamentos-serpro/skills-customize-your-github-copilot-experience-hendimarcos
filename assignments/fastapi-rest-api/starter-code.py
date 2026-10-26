from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Study Activities API")


class StudyItemCreate(BaseModel):
    title: str
    subject: str
    completed: bool = False


class StudyItem(StudyItemCreate):
    id: int


items = [
    StudyItem(id=1, title="Review Python functions", subject="Computer Science")
]


@app.get("/health")
def health_check():
    # TODO: Return a JSON response that confirms the API is running.
    pass


@app.get("/items", response_model=list[StudyItem])
def list_items():
    # TODO: Return all study activities.
    pass


@app.get("/items/{item_id}", response_model=StudyItem)
def get_item(item_id: int):
    # TODO: Find the activity by ID or raise an HTTP 404 error.
    pass


@app.post(
    "/items",
    response_model=StudyItem,
    status_code=status.HTTP_201_CREATED,
)
def create_item(item: StudyItemCreate):
    # TODO: Assign an ID, save the new activity, and return it.
    pass


@app.put("/items/{item_id}", response_model=StudyItem)
def update_item(item_id: int, item: StudyItemCreate):
    # TODO: Update the matching activity or raise an HTTP 404 error.
    pass


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    # TODO: Delete the matching activity or raise an HTTP 404 error.
    pass
