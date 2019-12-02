import pytest
from django.urls import reverse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from todofy.apps.todo.models import Todo


@pytest.fixture
def archived_todo():
    todo = Todo(content='Buy groceries!', archived=True)
    todo.save()

    return todo


def test_view_todo_history_populated(driver, live_server, archived_todo):
    driver.get(live_server.url + reverse('todo_history'))

    (WebDriverWait(driver, 3)
     .until(EC.presence_of_element_located((By.ID, "todo"))))
