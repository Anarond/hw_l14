from pages.search_page import SearchPage

def test_search_product(browser_set):
    search_page = SearchPage()

    search_page.open()

    search_page.open_search()
    search_page.send_product_search("iPod Touch")
    search_page.click_search_button()
    search_page.check_search_result("iPod Touch")