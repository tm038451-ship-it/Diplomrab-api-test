# Базовые URL для тестирования
SAUCEDEMO_URL = "https://saucedemo.com"
GITHUB_API_URL = "https://api.github.com"

# Авторизационные данные из системы
GITHUB_TOKEN = "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"

# Настройки заголовков для API-запросов
GITHUB_HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28"
}
