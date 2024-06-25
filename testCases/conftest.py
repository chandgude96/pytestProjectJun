import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

## add argument
def pytest_addoption(parser):
    parser.addoption("--browser")

#pass value
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#passing actual value
@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print("Launching edge browser")
    else:
        print("headlessmode")
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)

    driver.maximize_window()
    driver.get("https://automation.credence.in/")

    return driver

def pytest_metadata(metadata):
    metadata["Batch"] = "Ct15"
    metadata["Class"] = "Credence"
    metadata.pop("Platform", None)

@pytest.fixture(params=[
    ("Credencetest@test.com","Credence@123"),
    ("Credencetest@test.com451","Credence@123"),
    ("Credencetest@test.com", "Credence@12331"),
    ("Credencetest@test12334.com1", "Credence@125531")
])

def getDataforLogin(request):
    return request.param
