from src.client import get


def test_get_todo_1():
    r = get("/todos/1")
    assert r.status_code == 200

    data = r.json()
    assert data["id"] == 1
    assert "title" in data
    assert "completed" in data


def test_get_user_1():
    r = get("/users/1")
    assert r.status_code == 200

    data = r.json()
    assert "name" in data
    assert "email" in data


def test_get_posts_by_userid():
    r = get("/posts", params={"userId": 1})
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["userId"] == 1


def test_negative_todo_does_not_exist():
    r = get("/todos/999999")
    assert r.status_code == 200

    data = r.json()
    assert data == {}
