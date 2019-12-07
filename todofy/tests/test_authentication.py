import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def test_user_successful_login(driver):
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    name.send_keys("johndoe")
    password.send_keys("123123123d")
    submit.click()

    breadcrumb = driver.find_element_by_xpath("//li[@class='breadcrumb-item active']")
        
    assert breadcrumb.text == "Todo"


def test_user_unsuccessful_login(driver):
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//button[@type='submit']")
    name.send_keys("bobber")
    password.send_keys("123123")
    submit.click()

    assert "Sign In" in driver.title
