import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_Credekart_Login_params:

    def test_CredeKart_Login_params_003(self,setup,getDataforLogin):
        self.driver = setup

        self.driver.maximize_window()

        self.driver.get("https://automation.credence.in/login")

        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(getDataforLogin[0])

        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(getDataforLogin[1])

        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        try:
            self.driver.find_element(By.XPATH, "//h2[normalize-space()='CredKart']")
            self.driver.save_screenshot(".\\Screenshots\\test_Userlogin.PNG")

            print("Login Pass")
            assert True

        except:
            print("Login fail")
            assert False
        self.driver.quit()


