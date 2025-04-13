from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth_state.json")
    page = context.new_page()

    page.goto("https://zakupki.rosatom.ru/lk")

    input("⏳ Нажми Enter после ручного входа...")  # дождаться ручного входа

    print("✅ Уже залогинен. Заголовок страницы:", page.title())
    browser.close()