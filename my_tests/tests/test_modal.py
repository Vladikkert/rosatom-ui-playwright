from pages.main_page import MainPage

#def test_navigation_to_tkp(page):
#    page.goto("https://zakupki.rosatom.ru/lk")
#    main = MainPage(page)
#    main.go_to_tkp()
#    assert "ТКП" in page.content()


def test_multi(page):
    page.goto("https://zakupki.rosatom.ru/lk")
    main = MainPage(page)
    main.go_to_itogi()
    main.close_modal()
    main.go_to_44fz()
    main.go_to_complaints()
    main.go_to_subscriptions()
    main.go_to_tkp()
    assert "ТКП" in page.content()






# def test_modal_can_be_closed(page):
#     page.goto("https://zakupki.rosatom.ru/lk")
#     main = MainPage(page)
#     main.go_to_itogi()
#     main.close_modal()
#     assert not page.is_visible("button.af-dialog__headerbtn")
#
# def test_navigation_to_44fz(page):
#     page.goto("https://zakupki.rosatom.ru/lk")
#     main = MainPage(page)
#     main.go_to_44fz()
#     assert "44-ФЗ" in page.content()
#
# def test_navigation_to_complaints(page):
#     page.goto("https://zakupki.rosatom.ru/lk")
#     main = MainPage(page)
#     main.go_to_complaints()
#     assert "Жалобы на закупку" in page.content()
#
# def test_navigation_to_subscriptions(page):
#     page.goto("https://zakupki.rosatom.ru/lk")
#     main = MainPage(page)
#     main.go_to_subscriptions()
#     assert "Подписки" in page.content()
#
# def test_navigation_to_tkp(page):
#     page.goto("https://zakupki.rosatom.ru/lk")
#     main = MainPage(page)
#     main.go_to_tkp()
#     assert "ТКП" in page.content()