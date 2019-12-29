import pytest


@pytest.fixture(scope='module')
def driver():
    from selenium import webdriver

    options = webdriver.ChromeOptions()
    #options.headless = True

    chrome = webdriver.Chrome(options=options)

    chrome.set_window_size(1440, 900)

    yield chrome

    chrome.close()
