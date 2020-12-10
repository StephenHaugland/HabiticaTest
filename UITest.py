############################################
## Stephen Haugland
## Software Quality Assurance
## Habitica UI Tests
############################################


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




def main():
    # 
    websiteURL = "https://habitica.com/login"
    driver = webdriver.Chrome()
    driver.get(websiteURL)
    time.sleep(4)
    assert "Habitica" in driver.title

#### Step 1: Login to Habitica with username and password ####

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

#### Step 2: Begin UI tests ####

    ## Test that 

    ## Fuzz testing? Text search box, naughty strings, queries


    ## 



    driver.close()


if __name__ == '__main__':
    main()
