
import pytest
from selenium import webdriver



@pytest.mark.usefixtures("get_browser")
class BaseTest:
    pass

class Test_google(BaseTest):

    def test_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title == "Google"