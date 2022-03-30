from pages.google import GoogleSearchPage


def test_google_search(browser, config_url):

    google_search_page = GoogleSearchPage(browser, config_url)
    google_search_page.load()
    google_search_page.standard_search("Selenium Documentation")






