
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



def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
