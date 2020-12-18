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
    driver = webdriver.Chrome("S:/Documents/Dev/chromedriver.exe")
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

    # # save a screenshot to verify successful login
    # driver.save_screenshot("test1.png")

#### Step 3: Begin UI tests ####

    ## Test 01_AddFirstDaily
    # verify that there are no dailies currently being tracked 
    DailyTextField = driver.find_element_by_css_selector('[placeholder="Add a Daily"]')
    DailyTextField.send_keys("floss")
    # save a screenshot to verify task successfully added
    driver.save_screenshot("test1.png")

    ## Test 02_AddSecondDaily
    DailyTextField.clear()
    DailyTextField.send_keys("Read")
    # save a screenshot to verify task successfully added
    driver.save_screenshot("test2.png")

    ## Test 03_AddThirdDaily
    DailyTextField.clear()
    DailyTextField.send_keys("Make Bed")
    driver.save_screenshot("test3.png")
    ## Test 04_CheckFirstDaily
    FirstCheckBox = driver.find_element_by_css_selector('[class="task-control daily-todo-control task-better-control-inner-daily-todo"]')
    FirstCheckBox.click()
    driver.save_screenshot("test4.png")
    ## Test 05_UncheckFirstDaily
    FirstCheckBox.click()
    driver.save_screenshot("test5.png")
    ## Test 06_CheckAndUncheckFirstDailyOnce
    FirstCheckBox.click()
    FirstCheckBox.click()
    driver.save_screenshot("test6.png")
    ## Test 07_CheckAndUncheckFirstDailyTenTimes
    for x in range(10):
        FirstCheckBox.click()
        FirstCheckBox.click()
    driver.save_screenshot("test7.png")
    ## Test 08_DeleteFirstDaily
    FirstDeleteButton = driver.find_element_by_css_selector('[class="habitica-menu-dropdown-toggle"]')
    FirstDeleteButton.click()
    driver.save_screenshot("test8.png")
    ## Test 09_DeleteSecondDaily
    SecondDeleteButton = driver.find_element_by_css_selector('[class="habitica-menu-dropdown-toggle"]')
    SecondDeleteButton.click()
    driver.save_screenshot("test9.png")
    ## Test 10_DeleteLastDaily
    ThirdDeleteButton = driver.find_element_by_css_selector('[class="habitica-menu-dropdown-toggle"]')
    ThirdDeleteButton.click()
    driver.save_screenshot("test10.png")

#### Fuzz testing for user input fields ####

    # naughty strings
    # TODO: implement function to take in different naughty strings
    # TODO: verify there are no errors differently than taking screenshots

    ## Test 10_NaughtyString1
    DailyTextField.clear()
    DailyTextField.send_keys("undefined")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")
    
    ## Test 11_NaughtyString2
    DailyTextField.clear()
    DailyTextField.send_keys("undef")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 12_NaughtyString3
    DailyTextField.clear()
    DailyTextField.send_keys("null")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 13_NaughtyString4
    DailyTextField.clear()
    DailyTextField.send_keys("NULL")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 14_NaughtyString5
    DailyTextField.clear()
    DailyTextField.send_keys("(null)")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 15_NaughtyString6
    DailyTextField.clear()
    DailyTextField.send_keys("true")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 16_NaughtyString7
    DailyTextField.clear()
    DailyTextField.send_keys("false")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 17_NaughtyString8
    DailyTextField.clear()
    DailyTextField.send_keys("True")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 18_NaughtyString9
    DailyTextField.clear()
    DailyTextField.send_keys("False")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 18_NaughtyString9
    DailyTextField.clear()
    DailyTextField.send_keys("TRUE")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 19_NaughtyString10
    DailyTextField.clear()
    DailyTextField.send_keys("FALSE")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    ## Test 20_NaughtyString10
    DailyTextField.clear()
    DailyTextField.send_keys("hasOwnProperty")
    # save a screenshot to verify no errors
    driver.save_screenshot("test1.png")

    driver.close()


if __name__ == '__main__':
    main()
