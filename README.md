## Rosatom UI Test Framework

Автоматизированная система UI-тестирования для личного кабинета [zakupki.rosatom.ru](https://zakupki.rosatom.ru), построенная на базе **Playwright** и **Pytest**.


## Цель

Повысить стабильность и предсказуемость релизов, автоматически проверяя ключевые пользовательские сценарии в интерфейсе: навигация, фильтрация, работа с модальными окнами и взаимодействие с интеграциями.


## Структура проекта

project/ ├── conftest.py 
Настройка фикстур и браузера ├── pages/ │ └── main_page.py 
Page Object для главной страницы ├── tests/ │ └── test_modal.py 
Набор тестов ├── utils/ │ └── logger.py 
Заготовка под логирование ├── pytest.ini 


## Установка

1. Клонируйте репозиторий:
git clone https://github.com/your-username/rosatom-ui-playwright.git
cd rosatom-ui-playwright

2. Установите зависимости:
pip install playwright pytest
playwright install


## Сохраните состояние авторизации вручную

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://zakupki.rosatom.ru/lk")
    input("Войдите вручную и нажмите Enter...")
    context.storage_state(path="auth_state.json")
    browser.close()


## Что тестируется

-Навигация по боковому меню: ТКП, Жалобы, Подписки, Планирование
-Работа с модальными окнами
-Валидация элементов: чекбоксы, селекты, кнопки
-Проверка доступности и содержимого элементов на страницах

## Пример теста

def test_navigation_to_tkp(page):
    page.goto("https://zakupki.rosatom.ru/lk")
    main = MainPage(page)
    main.go_to_tkp()
    assert "ТКП" in page.content()

## Планы на развитие

 -Интеграция Allure Reports
 -Поддержка CI (GitHub Actions)
 -Расширение покрытия по сценариям взаимодействия с SAP и другими системами
 -Скриншоты при ошибках
 -Кастомное логирование действий

## Автор
📒 ФИО: Иккерт Владислав
📬 Email: vl4d.ikkert@gmail.com
💬 Telegram: @Vladislav_Ikkert
💼 GitHub: https://github.com/Vladikkert