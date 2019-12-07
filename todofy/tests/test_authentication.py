import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def user_successful_login(driver):
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//input[@value='Log In']")
    name.send_keys("123@abc.com")
    password.send_keys("123123")
    submit.click()

def user_unsuccessful_login(driver):
    driver.get("http://127.0.0.1:8000/accounts/login")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//input[@value='Log In']")
    name.send_keys("122@abb.com")
    password.send_keys("111111")
    submit.click()

def user_login_syntax_error(driver):
    driver.get("http://127.0.0.1:8000/accounts/login/")
    name = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_xpath("//input[@value='Log In']")
    name.send_keys("123gmail.com")
    password.send_keys("111111")
    submit.click()