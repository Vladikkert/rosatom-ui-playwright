class MainPage:
    def __init__(self, page):
        self.page = page

    def go_to_itogi(self):
        self.page.get_by_text("Планирование и закупки по ЕОСЗ").click()
        self.page.wait_for_selector("text=Итоги")
        self.page.get_by_text("Итоги").click()

    def close_modal(self):
        self.page.wait_for_selector("button.af-dialog__headerbtn")
        self.page.locator("button.af-dialog__headerbtn").click()
        self.page.wait_for_selector("button.af-dialog__headerbtn", state="detached")

    def go_to_44fz(self):
        self.page.get_by_text("Планирование по 44-ФЗ").click()
        self.page.wait_for_selector("text=Параметры поиска")
        self.page.get_by_text("Параметры поиска").click()
        self.page.wait_for_selector("text=Заказчик")
        self.page.locator("div.af-select__selection", has_text="Заказчик").click()
        self.page.get_by_text("Госкорпорация \"Росатом\"").click()
        self.page.get_by_text("Применить").click()

    def go_to_complaints(self):
        self.page.get_by_text("Жалобы на закупку").click()
        self.page.wait_for_selector("text=Создать жалобу")
        self.page.get_by_text("Создать жалобу").click()
        self.page.wait_for_selector("text=Отмена")
        self.page.get_by_text("Отмена").click()

    def go_to_subscriptions(self):
        self.page.get_by_text("Подписки").click()
        self.page.wait_for_selector("text=Добавить")
        self.page.get_by_text("Добавить").click()
        self.page.wait_for_selector("text=Сохранить")
        self.page.locator("label:has-text('Планирование по ЕОСЗ')").click()
        self.page.locator("label:has-text('Планирование по 44-ФЗ')").click()
        self.page.locator("label:has-text('Закупки по ЕОСЗ')").click()

    def go_to_tkp(self):
        self.page.locator("a.menu__link:has(span:has-text('ТКП'))").click()