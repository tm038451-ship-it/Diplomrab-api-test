import os
import sys
import requests

# Настройка путей для импорта config.py
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root_dir)

from config import GITHUB_API_URL  # noqa: E402


def test_get_root_endpoints() -> None:
    """TC-API-01: Успешное получение каталога запросов (Позитивный)"""
    response = requests.get(GITHUB_API_URL)
    assert response.status_code == 200
    data = response.json()
    assert "repository_url" in data


def test_get_public_repo_info() -> None:
    """TC-API-02: Получение информации о публичном репозитории (Позитивный)"""
    response = requests.get(f"{GITHUB_API_URL}/repos/psf/requests")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "requests"
    assert data["private"] is False


def test_get_repo_issues() -> None:
    """TC-API-03: Получ списка issues публичного репозитория (Позитивный)"""
    response = requests.get(f"{GITHUB_API_URL}/repos/psf/requests/issues")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_profile_with_invalid_token() -> None:
    """TC-API-04: Отправка запроса с невалидным токеном (Негативный)"""
    bad_headers = {"Authorization": "token ghp_INVALID_TOKEN_12345"}
    response = requests.get(f"{GITHUB_API_URL}/user", headers=bad_headers)
    assert response.status_code == 401
    assert response.json()["message"] == "Bad credentials"


def test_get_non_existent_repo() -> None:
    """TC-API-05: Запрос несуществующего репозитория (Негативный)"""
    url = f"{GITHUB_API_URL}/repos/invalid-user-12345/non-existent-repo"
    response = requests.get(url)
    assert response.status_code == 404
