import pytest


@pytest.fixture(scope='module')
def driver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    options.headless = True

    chrome = webdriver.Chrome(options=options)

    yield chrome

    chrome.close()
