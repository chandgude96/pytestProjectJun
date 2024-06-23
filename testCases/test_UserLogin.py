import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Login:


    def test_url(self):
        driver = webdriver.Chrome()
        driver.get("https://automation.credence.in/")

        if driver.title == "CredKart":
            print("You are at credence")
            assert True
        else:
            print("failed to url")
            assert False


    def test_Userlogin(self):

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://automation.credence.in/login")

        driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Rohit344@credence.in")

        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("rohit@123")

        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        try:
            driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")

            print("Login Pass")
            assert True

        except:
            print("Login fail")
            assert False






