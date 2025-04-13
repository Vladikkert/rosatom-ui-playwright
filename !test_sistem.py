from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(storage_state="auth_state.json")
    page = context.new_page()

    page.goto("https://zakupki.rosatom.ru/lk")

    # ⏳ Подожди, пока загрузится нужный элемент
    page.wait_for_selector("text=Планирование и закупки по ЕОСЗ")

    # 👇 Клик по элементу с нужным текстом
    page.get_by_text("Планирование и закупки по ЕОСЗ").click()

    print("✅ Кнопка нажата!")
    input("Нажми Enter для выхода...")

    browser.close()
