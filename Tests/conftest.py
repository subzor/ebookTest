import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from ..Config.config import TestData

@pytest.fixture(params=["chrome"], scope="class") # change params=["chrome"] to firefox to use geckodriver
def init_driver(request):
    """Initialize friver"""
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument("--width=1300")
        options.add_argument("--height=1000")
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH, options=options)
    if request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument("--width=1300")
        options.add_argument("--height=1000")
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLE_PATH, options=options)
    
    request.cls.driver = web_driver
    yield
    web_driver.close()
