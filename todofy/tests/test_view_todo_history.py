import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from todofy.apps.todo.models import Todo


@pytest.fixture
def login_page(driver, live_server, admin_user):
    driver.get(live_server.url + "/accounts/login")

    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")

    name.send_keys("admin")
    password.send_keys("password")

    submit.click()
    


@pytest.fixture
def archived_todo(admin_user):
    todo = Todo(content='Buy groceries!', user=admin_user, archived=True)
    todo.save()

    return todo


def test_view_todo_history_populated(driver, live_server, archived_todo, login_page):
    driver.get(live_server.url + reverse('todo_history'))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "todo"))))
