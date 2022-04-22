import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager



""" The conftest.py file name should be conftest only, otherwise python doesnt understand the file, eg - config.py there is no "test" keywords is involved in it. """


@pytest.fixture(params=["chrome"],scope="class")
def get_browser(request):

    if request.param == "chrome":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    request.cls.driver = driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()