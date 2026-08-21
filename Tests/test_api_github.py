import uuid
import requests
from config import GITHUB_API_URL


def test_get_root_endpoints(api_session: requests.Session) -> None:
    """TC-API-01: Успешное получение каталога запросов (Позитивный)"""
    response: requests.Response = api_session.get(GITHUB_API_URL)
    assert response.status_code == 200
    data: dict = response.json()
    assert "current_user_url" in data
    assert "repository_url" in data


def test_get_user_profile(api_session: requests.Session) -> None:
    """TC-API-02: Получение персональных данных
    авторизованного пользователя (Позитивный)"""
    response: requests.Response = api_session.get(f"{GITHUB_API_URL}/user")
    assert response.status_code == 200
    data: dict = response.json()
    assert "login" in data
    assert "id" in data
    assert data["type"] == "User"


def test_create_public_repository(api_session: requests.Session) -> None:
    """TC-API-03: Создание нового публичного
    репозитория через API (Позитивный)"""
    # Генерируем уникальное имя, чтобы тест всегда был независим
    unique_name: str = f"coursework-api-test-{uuid.uuid4().hex[:6]}"
    payload: dict = {"name": unique_name, "private": False}

    response: requests.Response = api_session.post(
        f"{GITHUB_API_URL}/user/repos", json=payload
    )
    assert response.status_code == 201
    data: dict = response.json()
    assert data["name"] == unique_name
    assert data["private"] is False


def test_get_profile_with_invalid_token() -> None:
    """TC-API-04: Отправка запроса с
    невалидным секретным токеном  (Негативный)"""
    bad_headers: dict = {"Authorization": "token ghp_INVALID_TOKEN_12345"}
    response: requests.Response = requests.get(
        f"{GITHUB_API_URL}/user", headers=bad_headers
    )
    assert response.status_code == 401
    data: dict = response.json()
    assert data["message"] == "Bad credentials"


def test_create_repo_empty_name(api_session: requests.Session) -> None:
    """TC-API-05: Создание репозитория с уже занятым именем  (Негативный)"""
    payload: dict = {"name": ""}
    response: requests.Response = api_session.post(
        f"{GITHUB_API_URL}/user/repos", json=payload
    )
    assert response.status_code == 422
