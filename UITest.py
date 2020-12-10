############################################
## Stephen Haugland
## Software Quality Assurance
## Habitica UI Tests
############################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




def main():

#### Step 1: Open Habitica's website ####
    websiteURL = "https://habitica.com/login"
    driver = webdriver.Chrome()
    driver.get(websiteURL)
    # TODO: change hard coded sleep to a reactive wait
    time.sleep(5)
    assert "Habitica" in driver.title

#### Step 2: Login to Habitica with username and password ####

    # find username and password fields on login page
    usernameField = driver.find_element_by_id("usernameInput")
    passwordField = driver.find_element_by_id("passwordInput")

    # clear both fields
    usernameField.clear()
    passwordField.clear()

    # enter username and password into fields
    usernameField.send_keys("YOUR_USERNAME_HERE")
    passwordField.send_keys("YOUR_PASSWORD_HERE")    

    # find and click login button
    loginButton = driver.find_element_by_css_selector("[type=submit]")
    loginButton.click()

    # save a screenshot to verify successful login
    driver.save_screenshot("test1.png")

#### Step 3: Begin UI tests ####

    ## Test 01_AddFirstDaily

    ## Test 02_AddSecondDaily

    ## Test 03_AddThirdDaily

    ## Test 04_CheckFirstDaily

    ## Test 05_UncheckFirstDaily

    ## Test 06_CheckAndUncheckFirstDailyOnce

    ## Test 07_CheckAndUncheckFirstDailyTenTimes

    ## Test 08_DeleteFirstDaily

    ## Test 09_DeleteSecondDaily

    ## Test 10_DeleteLastDaily

    ## Fuzz testing for text search box ##
    # naughty strings
    # queries





    driver.close()


if __name__ == '__main__':
    main()
