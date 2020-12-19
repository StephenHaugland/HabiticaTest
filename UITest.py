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
    time.sleep(5)

    


    # # save a screenshot to verify successful login
    # driver.save_screenshot("login.png")

#### Step 3: Begin UI Integration tests ####

    # Locate the text field to add new dailies
    # DailyTextField = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > textarea")

    # ## Test 01_AddFirstDaily 
    # DailyTextField.send_keys("Floss")
    # DailyTextField.send_keys(Keys.RETURN)
    
    # ## Test 02_AddSecondDaily
    # DailyTextField.clear()
    # DailyTextField.send_keys("Read")
    # DailyTextField.send_keys(Keys.RETURN)
    
    # ## Test 03_AddThirdDaily
    # DailyTextField.send_keys("Make Bed")
    # DailyTextField.send_keys(Keys.RETURN)
    # time.sleep(1)

    # ## Test 04_CheckFirstDaily
    # FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    # FirstCheckBox.click()
    # time.sleep(1)

    # ## Test 05_CheckSecondtDaily
    # SecondCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(2) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    # SecondCheckBox.click()
    # time.sleep(1)

    # ## Test 06_CheckThirdDaily
    # ThirdCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(3) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    # ThirdCheckBox.click()
    # time.sleep(1)

    # ## Test 05_UncheckFirstDaily
    # FirstUncheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-disabled-daily-todo-control-bg > div")
    # FirstUncheckBox.click()
    # time.sleep(1)

    # # Test 06_CheckAndUncheckFirstDailyOnce
    # # FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    # FirstCheckBox.click()
    # time.sleep(1)
    # FirstUncheckBox.click()
    
    # ## Test 07_CheckAndUncheckFirstDailyTenTimes
    # for x in range(10):
    # #     FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-neutral-control-bg > div")
    #     FirstCheckBox.click()
    #     # time.sleep(.2)
    # #     FirstCheckBox = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.left-control.d-flex.justify-content-center.task-disabled-daily-todo-control-bg > div")
    #     FirstCheckBox.click()


    # ## Test 08_DeleteFirstDaily
    # FirstDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    # FirstDailyOptions.click()
    # FirstDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    # FirstDailyDelete.click()
    # a = Alert(driver)
    # a.accept()
    
    # ## Test 09_DeleteSecondDaily
    # SecondDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(2) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    # SecondDailyOptions.click()
    # SecondDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(2) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    # SecondDailyDelete.click()
    # a = Alert(driver)
    # a.accept()

    # ## Test 10_DeleteThirdDaily
    # ThirdDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    # ThirdDailyOptions.click()
    # ThirdDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    # ThirdDailyDelete.click()
    # a = Alert(driver)
    # a.accept()
    
    # time.sleep(1)
    
    # ## Test 11_AddAndDelete100Dailies
    
    # for x in range(100):
    #     DailyTextField.clear()
    #     DailyTextField.send_keys(x)
    #     DailyTextField.send_keys(Keys.RETURN)

    # time.sleep(1)
   

    # for x in range(100):
    #     time.sleep(.1)
    #     FirstDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    #     FirstDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4)")
    #     FirstDailyOptions.click()
    #     FirstDailyDelete.click()
    #     a = Alert(driver)
    #     a.accept()
        
    time.sleep(1)
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


### Exploratory Tests - Tags

    # ## Test xx_AddSingleTag
    # # Create Task
    # DailyTextField = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > textarea")
    # DailyTextField.send_keys("Read")
    # DailyTextField.send_keys(Keys.RETURN)
    # # Inspect Options
    # FirstDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    # FirstDailyOptions.click()
    # FirstDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4)")
    # FirstDailyEdit.click()
    # time.sleep(1)
    # FirstDailyTags = driver.find_element_by_css_selector("#__BVID__469__BV_toggle_")
    # FirstDailyTags.click()
    # time.sleep(1)
    # FirstDailySaveOptions = driver.find_element_by_css_selector("#task-modal___BV_modal_header_ > div > div.d-flex.align-items-center.mb-3 > div > button.btn.btn-secondary.d-flex.align-items-center.justify-content-center")
    # FirstDailySaveOptions.click()
    # #Cleanup 
    # FirstDailyOptions = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.habitica-menu-dropdown-toggle")
    # FirstDailyOptions.click()
    # FirstDailyDelete = driver.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.daily > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content > div.task-clickable-area.task-clickable-area-user > div.d-flex.justify-content-between > div > div.dropdown-menu > div > div:nth-child(4) > span > span.text")
    # FirstDailyDelete.click()
    # a = Alert(driver)
    # a.accept()


### Reward Tests

    # ## Test XX_RewardZero
    # rewardTest(driver, 0, "zero")
    # time.sleep(1)
    
    # ## Test XX_RewardOne
    # rewardTest(driver, 1, "one")
    # time.sleep(1)

    # ## Stops here because negative is invalid
    # ## Test XX_RewardSmallNegative
    # rewardTest(driver,"-0.000000001","small negative")
    # time.sleep(1)

    # ## Test XX_RewardSmallPositive
    # rewardTest(driver,"0.000000001","small positive")
    # time.sleep(1)

    # ## Test XX_RewardNegativeOne
    # rewardTest(driver,-1,"negative one")
    # time.sleep(1)
    
    # ## Test XX_RewardInfinity
    # rewardTest(driver,"Infinity","Infinity")
    # time.sleep(1)


    # ## Test XX_RewardAlphabet - See what characters are accepted
    # rewardTest(driver,"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","Infinity")
    # time.sleep(5)

    # ## Test XX_RewardLargePositive
    # rewardTest(driver,9999999999,"Large Positive")
    # time.sleep(1)

    # ## Test XX_RewardLargeNegative
    # rewardTest(driver,-9999999999,"Large Negative")
    # time.sleep(1)

    # ## Test XX_RewardCurrentGoldPlusALittle
    # currentGoldElement = driver.find_element_by_css_selector("#menu_collapse > div.currency-tray.form-inline > div.item-with-icon.gold > span")
    # currentGold = currentGoldElement.get_attribute('innerHTML')
    # cost = float(currentGold) + .01
    # rewardTest(driver,str(cost),"Current gold plus a little")

    # ## Test XX_RewardCurrentGoldMinusALittle
    # currentGoldElement = driver.find_element_by_css_selector("#menu_collapse > div.currency-tray.form-inline > div.item-with-icon.gold > span")
    # currentGold = currentGoldElement.get_attribute('innerHTML')
    # cost = float(currentGold) - .01
    # rewardTest(driver,str(cost),"Current gold minus a little")

    # ## Test XX_RewardCurrentGold
    # currentGoldElement = driver.find_element_by_css_selector("#menu_collapse > div.currency-tray.form-inline > div.item-with-icon.gold > span")
    # currentGold = currentGoldElement.get_attribute('innerHTML')
    # cost = float(currentGold)
    # rewardTest(driver,str(cost),"Current gold")


    time.sleep(5)


    driver.close()


def rewardTest(driv, cost, name):
    # Create reward
    RewardTextField = driv.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.reward > div.tasks-list > textarea")
    RewardTextField.send_keys(name)
    RewardTextField.send_keys(Keys.RETURN)

    # Set cost
    FirstRewardOptions = driv.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.reward > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content.no-right-border.reward-content")
    FirstRewardOptions.click()
    FirstRewardCostInput = driv.find_element_by_css_selector("#task-modal___BV_modal_body_ > div > form > div:nth-child(1) > div > div > input")
    FirstRewardCostInput.clear()
    FirstRewardCostInput.send_keys(cost)
    FirstRewardSave = driv.find_element_by_css_selector("#task-modal___BV_modal_header_ > div > div.d-flex.align-items-center.mb-3 > div > button.btn.btn-secondary.d-flex.align-items-center.justify-content-center")
    FirstRewardSave.click()
    FirstRewardRedeem = driv.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.reward > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.right-control.d-flex.align-items-center.justify-content-center.reward-control.task-reward-control-bg")
    FirstRewardRedeem.click()
    time.sleep(2)

    # Cleanup
    FirstRewardOptions = driv.find_element_by_css_selector("#app > div.container-fluid > div.sticky > div > div > div.row.tasks-columns > div.tasks-column.col-lg-3.col-md-6.reward > div.tasks-list > div.sortable-tasks > div:nth-child(1) > div > div > div.task-content.no-right-border.reward-content > div.task-clickable-area.task-clickable-area-user")
    FirstRewardOptions.click()
    FirstRewardDelete = driv.find_element_by_css_selector("#task-modal___BV_modal_body_ > div > form > div.d-flex.justify-content-center.mt-4.mb-4 > button")
    FirstRewardDelete.click()
    a = Alert(driv)
    a.accept()


if __name__ == '__main__':
    main()

