from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # открыть браузер с UI
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://zakupki.rosatom.ru/lk")
    print("➡️ Войди вручную, затем закрой окно.")

    input("⏳ Нажми Enter после ручного входа...")  # дождаться ручного входа

    context.storage_state(path="auth_state.json")  # сохранить cookies + localStorage
    browser.close()