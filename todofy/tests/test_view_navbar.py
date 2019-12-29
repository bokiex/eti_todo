import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def login_page(driver, live_server, admin_user):
    driver.get(live_server.url + "/accounts/login")

    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")

    name.send_keys("admin")
    password.send_keys("password")

    submit.click()


def test_view_navbar_index(driver, live_server, login_page):
    driver.get(live_server.url + reverse('todo_index'))

    # nav = driver.find_element_by_class_name('navbar-nav')
    item = driver.find_element_by_id('index')

    item.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_matches(live_server.url + reverse('todo_index')))


def test_view_navbar_history(driver, live_server, login_page):
    driver.get(live_server.url + reverse('todo_index'))

    # nav = driver.find_element_by_class_name('navbar-nav')
    item = driver.find_element_by_id('history')

    item.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.url_matches(live_server.url + reverse('todo_history')))
