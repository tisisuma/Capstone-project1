from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from Data import data
from Locators import locators

from selenium.webdriver.support import expected_conditions as EC


class Test_OrangeHRM:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        # self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        yield
        # self.driver.close()

    def test_get_title(self, booting_function):
        self.driver.get(data.Web_Data().url)
        assert self.driver.current_url == data.Web_Data.url
        print("SUCCESS : Web Title Verified")

    def test_login(self, booting_function):
        global element
        self.driver.get(data.Web_Data().url)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().username_locator).send_keys(
            data.Web_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().password_locator).send_keys(
            data.Web_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().submit_button_locator).click()
        self.driver.implicitly_wait(3)

        assert self.driver.current_url == data.Web_Data().dashboardurl
        print("SUCCESS : Logged in with Username {a} & Password {b}".format(a=data.Web_Data().username,
                                                                            b=data.Web_Data.password))

        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().pim_locator).click()
        print("PIM selected")

    #Click on  Edit icon on userinfo




        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().edit_locator).click()
        self.driver.implicitly_wait(5)



    #To clear existing firstname

        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().firstname_locator).clear()
        self.driver.implicitly_wait(3)

    # Add new firstname


        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().firstname_locator).send_keys(
            data.Web_Data().name)
        self.driver.implicitly_wait(5)

    #Scrolldown the page to click on the save button
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().scroll_locator)
        self.driver.execute_script("window.scrollTo(0,1000)")

    #Click on save buton to save the edit information
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().savebtn_locator).click()




