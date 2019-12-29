# import pytest
# from django.urls import reverse
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait


# def test_view_navbar_index(driver, live_server):
#     driver.get(live_server.url + reverse('todo_index'))

#     # nav = driver.find_element_by_class_name('navbar-nav')
#     item = driver.find_element_by_id('index')

#     item.click()

#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.url_matches(live_server.url + reverse('todo_index')))


# def test_view_navbar_history(driver, live_server):
#     driver.get(live_server.url + reverse('todo_index'))

#     # nav = driver.find_element_by_class_name('navbar-nav')
#     item = driver.find_element_by_id('history')

#     item.click()

#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.url_matches(live_server.url + reverse('todo_history')))
