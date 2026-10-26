import pytest
from fastapi import FastAPI, HTTPException, status
from fastapi.testclient import TestClient
from pydantic import BaseModel

app = FastAPI(title="Study Activities API")


class StudyItemCreate(BaseModel):
    title: str
    subject: str
    completed: bool = False


class StudyItem(StudyItemCreate):
    id: int


INITIAL_ITEMS = [
    StudyItem(id=1, title="Review Python functions", subject="Computer Science")
]
items = list(INITIAL_ITEMS)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items", response_model=list[StudyItem])
def list_items():
    return items


@app.get("/items/{item_id}", response_model=StudyItem)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.post(
    "/items",
    response_model=StudyItem,
    status_code=status.HTTP_201_CREATED,
)
def create_item(item: StudyItemCreate):
    next_id = max((existing.id for existing in items), default=0) + 1
    created_item = StudyItem(id=next_id, **item.dict())
    items.append(created_item)
    return created_item


@app.put("/items/{item_id}", response_model=StudyItem)
def update_item(item_id: int, item: StudyItemCreate):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            updated_item = StudyItem(id=item_id, **item.dict())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")


@pytest.fixture

def client():
    items.clear()
    items.extend(INITIAL_ITEMS)
    return TestClient(app)


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_items_returns_seed_data(client):
    # TODO: Assert the status and the initial activity returned by GET /items.
    pytest.fail("Complete this test.")


def test_get_item_returns_404_for_unknown_id(client):
    # TODO: Request an unknown ID and assert that the status is 404.
    pytest.fail("Complete this test.")


def test_create_item_returns_created_item(client):
    # TODO: Send a valid POST request and assert its status and response data.
    pytest.fail("Complete this test.")


def test_create_item_rejects_invalid_data(client):
    # TODO: Send a POST request without the required title and assert status 422.
    pytest.fail("Complete this test.")


def test_update_item_returns_updated_item(client):
    # TODO: Update item 1 and assert its status and updated response data.
    pytest.fail("Complete this test.")


def test_delete_item_removes_item(client):
    # TODO: Delete item 1, assert status 204, then assert GET /items/1 returns 404.
    pytest.fail("Complete this test.")
