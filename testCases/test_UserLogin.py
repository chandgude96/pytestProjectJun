import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_Login:


    def test_url(self, setup):
        self.driver = setup

        self.driver.get("https://automation.credence.in/")
        self.driver.maximize_window()

        if self.driver.title == "CredKart":
            self.driver.save_screenshot("C:\\Users\\nikhi\\PycharmProjects\\pytestProjectJun\\Screenshots\\Title.PNG")
            print("You are at credence")
            assert True
        else:
            print("failed to url")
            assert False

    def test_Userlogin(self, setup):

        self.driver = setup

        self.driver.maximize_window()

        self.driver.get("https://automation.credence.in/login")

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys("Rohit344@credence.in")

        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys("rohit@123")

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            self.driver.save_screenshot(".\\Screenshots\\test_Userlogin11.PNG")

            print("Login Pass")
            assert True

        except:
            print("Login fail")
            assert False
        self.driver.quit()

#pytest -v -s -n=2 --html=Report/myreport.html --alluredir="C:\Users\nikhi\PycharmProjects\pytestProjectJun\AllureReports" --browser chrome

