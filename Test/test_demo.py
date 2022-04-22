
import pytest
from selenium import webdriver



# @pytest.mark.usefixtures("get_browser")
# class BaseTest:
#     pass
#
# class Test_google(BaseTest):
#
#     def test_chrome(self):
#         self.driver.get("http://www.google.com")
#         assert self.driver.title == "Google"
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("get_browser")
class BaseTest:
    pass

class Test_google(BaseTest):
    @pytest.mark.parametrize(
                "username,password",
                [
                    ("admin@gamil.com","admin@123"),
                    ("naveen@gmail.com","balaji@123")
                ]
    )
    def test_chrome(self,username,password):
        self.driver.get("https://www.instagram.com/?hl=en")
        self.driver.find_element(by=By.XPATH,value="//input[@name='username']").send_keys(username)
        self.driver.find_element(by=By.XPATH, value="//input[@name='password']").send_keys(password)