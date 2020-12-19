############################################
## Stephen Haugland
## Software Quality Assurance
## Habitica UI Tests
############################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

import time
import json




def main():

#### Step 1: Open Habitica's website ####
    websiteURL = "https://habitica.com/login"
    driver = webdriver.Chrome("S:/Documents/Dev/chromedriver.exe")
    driver.get(websiteURL)
    # TODO: change hard coded sleep to a reactive wait
    time.sleep(2)
    assert "Habitica" in driver.title

    # timeout = 5
    # try:
    #     element_present = EC.presence_of_element_located((By.ID, 'main'))
    #     WebDriverWait(driver, timeout).until(element_present)
    # except TimeoutException:
    #     print("Timed out waiting for page to load")
    # finally:
    #     print("Page loaded")

#### Step 2: Login to Habitica with username and password ####

    # find username and password fields on login page
    usernameField = driver.find_element_by_id("usernameInput")
    passwordField = driver.find_element_by_id("passwordInput")

    # clear both fields
    usernameField.clear()
    passwordField.clear()

    # get username and pass from credential.json
    f = open('credentials.json',)
    credentials = json.load(f)
    username = credentials["username"]
    password = credentials["password"]

    # enter username and password into fields
    usernameField.send_keys(username)
    passwordField.send_keys(password)    

    # find and click login button
    loginButton = driver.find_element_by_css_selector("[type=submit]")
    loginButton.click()

    # TODO: change hard coded sleep to a reactive wait
    # wait.until
    time.sleep(4)

    


    # # save a screenshot to verify successful login
    # driver.save_screenshot("login.png")

#### Step 3: Begin UI Integration tests ####

    # Locate the text field to add new dailies
    DailyTextField = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > textarea")

    ## Test 01_AddFirstDaily 
    DailyTextField.send_keys("Floss")
    DailyTextField.send_keys(Keys.RETURN)
    
    ## Test 02_AddSecondDaily
    DailyTextField.clear()
    DailyTextField.send_keys("Read")
    DailyTextField.send_keys(Keys.RETURN)
    
    ## Test 03_AddThirdDaily
    DailyTextField.send_keys("Make Bed")
    DailyTextField.send_keys(Keys.RETURN)
    
    ## Test 04_CheckFirstDaily
    time.sleep(1)
    FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    FirstCheckBox.click()
    time.sleep(1)

    ## Test 05_UncheckFirstDaily
    FirstUncheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-disabled-daily-todo-control-bg > div")
    FirstUncheckBox.click()
    time.sleep(1)

    # Test 06_CheckAndUncheckFirstDailyOnce
    # FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    FirstCheckBox.click()
    time.sleep(1)
    FirstUncheckBox.click()
    
    ## Test 07_CheckAndUncheckFirstDailyTenTimes
    for x in range(10):
    #     FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
        FirstCheckBox.click()
        time.sleep(1)
    #     FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-disabled-daily-todo-control-bg > div")
        FirstCheckBox.click()


    ## Test 08_DeleteFirstDaily
    FirstDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    FirstDailyOptions.click()
    FirstDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    FirstDailyDelete.click()
    a = Alert(driver)
    a.accept()
    
    ## Test 09_DeleteSecondDaily
    SecondDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(2) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    SecondDailyOptions.click()
    SecondDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(2) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    SecondDailyDelete.click()
    a = Alert(driver)
    a.accept()

    ## Test 10_DeleteThirdDaily
    ThirdDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    ThirdDailyOptions.click()
    ThirdDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    ThirdDailyDelete.click()
    a = Alert(driver)
    a.accept()
    
    time.sleep(2)

#### Fuzz testing for user input fields ####

#     # naughty strings
#     # TODO: implement function to take in different naughty strings
#     # TODO: verify there are no errors differently than taking screenshots

#     ## Test 10_NaughtyString1
#     DailyTextField.clear()
#     DailyTextField.send_keys("undefined")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")
    
#     ## Test 11_NaughtyString2
#     DailyTextField.clear()
#     DailyTextField.send_keys("undef")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 12_NaughtyString3
#     DailyTextField.clear()
#     DailyTextField.send_keys("null")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 13_NaughtyString4
#     DailyTextField.clear()
#     DailyTextField.send_keys("NULL")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 14_NaughtyString5
#     DailyTextField.clear()
#     DailyTextField.send_keys("(null)")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 15_NaughtyString6
#     DailyTextField.clear()
#     DailyTextField.send_keys("true")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 16_NaughtyString7
#     DailyTextField.clear()
#     DailyTextField.send_keys("false")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 17_NaughtyString8
#     DailyTextField.clear()
#     DailyTextField.send_keys("True")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 18_NaughtyString9
#     DailyTextField.clear()
#     DailyTextField.send_keys("False")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 18_NaughtyString9
#     DailyTextField.clear()
#     DailyTextField.send_keys("TRUE")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 19_NaughtyString10
#     DailyTextField.clear()
#     DailyTextField.send_keys("FALSE")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

#     ## Test 20_NaughtyString10
#     DailyTextField.clear()
#     DailyTextField.send_keys("hasOwnProperty")
#     # save a screenshot to verify no errors
#     driver.save_screenshot("test1.png")

    driver.close()


if __name__ == '__main__':
    main()
