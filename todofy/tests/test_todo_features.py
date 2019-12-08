import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def test_successful_login():
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    name.send_keys("johndoe")
    password.send_keys("123123123d")
    submit.click()

    breadcrumb = driver.find_element_by_xpath("//li[@class='breadcrumb-item active']")
        
    assert breadcrumb.text == "Todo"

def test_todo_create():
    driver.get("http://127.0.0.1:8000/todo/")
    content = driver.find_element_by_name("content")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    content.send_keys("ETI CA2")
    submit.click()

    item = driver.find_element_by_xpath("//li[@class='list-group-item']")

    assert item.text.startswith("ETI CA2")

def test_todo_deletion():
    driver.get("http://127.0.0.1:8000/todo/")
    delete = driver.find_element_by_xpath("//button[@type='submit'][@class='btn btn-sm btn-warning']")
    delete.click()

    assert len(delete) == 0

def test_todo_deletion_error():
    driver.get("http://127.0.0.1:8000/todo/")
    delete = driver.find_elements_by_xpath("//button[@class='btn btn-sm btn-warning']")

    assert len(delete) == 0
