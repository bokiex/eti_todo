import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def test_successful_login(driver):
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    name.send_keys("johndoe")
    password.send_keys("123123123d")
    submit.click()

    breadcrumb = driver.find_element_by_xpath("//li[@class='breadcrumb-item active']")
        
    assert breadcrumb.text == "Todo"

def test_todo_create_and_autoarchive(driver):
    driver.get("http://127.0.0.1:8000/todo/")
    content = driver.find_element_by_name("content")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    content.send_keys("ETI CA2")
    submit.click()

    item = driver.find_element_by_xpath("//li[@class='list-group-item']")

    assert item.text.startswith("ETI CA2")

def test_logout(driver):
    driver.get("http://127.0.0.1:8000/todo/")

    logout = driver.find_element_by_link_text("Log out")
    logout.click()

    driver.get("http://127.0.0.1:8000/accounts/login/")
        
    assert "Sign In" in driver.title

def test_successful_login2(driver):
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    name.send_keys("bob")
    password.send_keys("bobber123")
    submit.click()

    breadcrumb = driver.find_element_by_xpath("//li[@class='breadcrumb-item active']")
        
    assert breadcrumb.text == "Todo"

def test_todo_filter_check(driver):
    driver.get("http://127.0.0.1:8000/todo/")

    emptylist = driver.find_element_by_xpath("//li[@class='list-group-item disabled']")

    assert emptylist.text.startswith("No todo")