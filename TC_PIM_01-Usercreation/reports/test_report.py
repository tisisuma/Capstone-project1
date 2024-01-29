from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
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
        self.driver.get(data.Web_Data().addempurl)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().add_locator).click()
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().empname_locator).send_keys(
            data.Web_Data().empname)
        self.driver.find_element(by=By.NAME, value=locators.Web_Locators().lastname_locator).send_keys(
            data.Web_Data.lastname)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.Saveemp_locator).click()
        self.driver.implicitly_wait(10)
        #Adding Nickname
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.nickname_locator).send_keys(data.Web_Data.nickname)
        #Adding otherid
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.otherid_locator).send_keys(data.Web_Data.otherid)
        #Adding driverlicense
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.license_locator).send_keys(data.Web_Data.driverlicense)
        #Adding license expiry date
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.licenseexp_locator).click()
        year_dropdown = Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.year_locator))
        year_dropdown.select_by_visible_text("2016")
        month_dropdown = Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.month_locator))
        month_dropdown.select_by_visible_text("May")
        date=Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.licenseexp_locator))
        date.select_by_visible_text("17")
        #Adding SSN number
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.ssn_locator).send_keys(data.Web_Data.ssn)
        #Adding SIN Number
        self.driver.find_element(by=By.XPATH,value=locators.Web_Locators.sinno_locator).send_keys(data.Web_Data.sin)
        #Adding Nationality
        nationality =Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.nationality_locatot))
        nationality.select_by_visible_text("Indian")
        #Adding Marital Status
        maritalstatus =Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.maritalstatus_locator))
        maritalstatus.select_by_visible_text("Married")
        # Scrolldown the page
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators().maritalstatus_locator)
        self.driver.execute_script("window.scrollTo(0,1000)")
        #Adding DOB
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.doblocator).click()
        dobyear =Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.dobyear_locator))
        dobyear.select_by_visible_text("1996")
        dobmonth = Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.dobmonth_locator))
        dobmonth.select_by_visible_text("May")
        dobdate=Select(self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.doblocator))
        dobdate.select_by_visible_text("17")
        #Adding Gender
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.gender_locator).click()
        #Adding Military Service
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.militaryservice_locator).send_keys(data.Web_Data.militaryservice)
        #Adding Checkmark
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.smoker_locator).click()
        #Saving all personal information
        self.driver.find_element(by=By.XPATH, value=locators.Web_Locators.save_info_locator).click()
        print("All details Added")






