import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#
# class Base():
#
#     @pytest.fixture(params=["chrome", "firefox"], scope="function")
#     def get_browser(request):
#         if request.param == "chrome":
#             driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         request.cls.driver = driver
#         driver.implicitly_wait(10)
#         yield driver
#         driver.close()


class BaseTest():

    @pytest.fixture(scope="class")
    def get_browser(request):
        if request.param == "chrome":
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        request.cls.driver = driver
        driver.implicitly_wait(10)
        yield driver
        driver.close()



# @pytest.fixture
# def input_value():
#    input = 39
#    return input

