import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GoogleSearchPage:
    # Locator Attributes listed here...
    SEARCH_FIELD = (By.CLASS_NAME, 'gLFyf gsfi')
    SEARCH_BUTTON = (By.CLASS_NAME, 'gNO89b')
    FEELING_LUCKY = (By.ID, 'gbqfbb')


    # initializer because all page objects need a reference to the webdriver instance.

    def __init__(self, browser):
        self.browser = browser

    # Interaction methods are below, these allow us to use baked in "actions" for a specific page object.

    def load(self):
        self.browser.get(self.config_url)

    def standard_search(self, search_term):
        # Define and find the search_field element.
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        # Type in the search term using send_keys().
        search_field.send_keys(search_term)
       
       # Define and find the search button.
        search_button = self.browser.find_element(*self.SEARCH_BUTTON)
        # Click the search button.
        search_button.click()

    def feeling_lucky_search(self, search_term):
        # Define and find the search_field element.
        search_field = self.browser.find_element(*self.SEARCH_FIELD)
        # Type in the search term using send_keys().
        search_field.send_keys(search_term)

        # Define and find the feeling lucky search button.
        search_button = self.browser.find_element(*self.FEELING_LUCKY)
        # Click the Feeling Lucky search button.
        search_button.click()

    def verify_url(self, expected_url):
        # Get the actual URL currently open in the browser
        actual_url = self.browser.current_url

        # Assert (check) that the actual url matches the expected url
        assert(actual_url == expected_url)
