import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def test_successful_signup(driver, live_server):
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    name = driver.find_element_by_name("username")
    password1 = driver.find_element_by_name("password1")
    password2 = driver.find_element_by_name("password2")
    signup = driver.find_element_by_xpath("//button[@type='submit']")

    name.send_keys("whysee")
    password1.send_keys("123123abc")
    password2.send_keys("123123abc")
    signup.click()
        
    driver.get("http://127.0.0.1:8000/accounts/login/#!")
    assert "Sign In" in driver.title

def test_unsuccessful_signup(driver):
    driver.get("http://127.0.0.1:8000/accounts/signup/")
    name = driver.find_element_by_name("username")
    password1 = driver.find_element_by_name("password1")
    password2 = driver.find_element_by_name("password2")
    signup = driver.find_element_by_xpath("//button[@type='submit']")

    name.send_keys("why")
    password1.send_keys("123")
    password2.send_keys("123")
    signup.click()
    
    error = driver.find_element_by_xpath("//div[@class='invalid-feedback']")

    assert error.text.startswith("This")