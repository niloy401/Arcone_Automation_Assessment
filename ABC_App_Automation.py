
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from typing import Dict, Any
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait

cap: Dict[str, Any] = {
    
    "platformName": "Android",
    "automationName": "UiAutomator2",
    "appPackage": "com.arcone.arcone",
    "deviceName": "Pixel 9 Pro",
}

## Variables for login credentials and URL ##
email_input = "azmin@excelbd.com"
password_input = "D!m77(2SJ,5j"

url = "http://localhost:4724"

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

### Custom Functions for Task-1 and Task-2 for automating purpose ###

# Function to select a date in the calendar
def select_calendar_date(date_number: int):
    
    date_xpath = f"//android.view.View[@text='{date_number}']"
    date_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, date_xpath)))
    date_element.click()
    
# Function to select any Year in the calendar    
def select_year(year: int):
    year_xpath = f"//android.widget.TextView[@resource-id='android:id/text1' and @text='{year}']"
    year_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, year_xpath)))
    year_element.click()    
    
  
# Function to click the previous month arrow in the calendar  
def click_prev_month(times: int = 1):
    for _ in range(times):
        Prev_month_arrow = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Previous month")))
        Prev_month_arrow.click()
        
        
# Function to click the next month arrow in the calendar  
def click_next_month(times: int = 1):
    for _ in range(times):
        Next_month_arrow = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Next month")))
        Next_month_arrow.click()
        
        
 # Function to select a status from the dropdown       
def select_status(status_filter: str):
    
    filter_xpath = f"//android.widget.ScrollView//android.widget.TextView[contains(@text, '{status_filter}')]"
    dropdown_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, filter_xpath)))
    dropdown_element.click()
    
 # Function to select a leave type from the dropdown
def select_leave_type(leave_type_filter: str):
    leave_type_xpath = f"//android.widget.TextView[@text='{leave_type_filter}']"
    dropdown_element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, leave_type_xpath)))
    dropdown_element.click()      
  
# Function to navigate back multiple times
def navigate_back(times: int = 1):
    for _ in range(times):
     driver.back()
     
  ###############################  
     
           ## Task 1: Attendance Report Search ##
           ## Objective: Automate searching attendance reports within the HR module. ##
     
# Using WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 20)

 ## Appication Login Process ##
 
# Locating the email and password fields and performing actions
email_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Enter Email']")))
assert email_field.is_displayed(), "Email field is not displayed"
email_field.send_keys(email_input)
# Validating the email input value
assert email_field.text == email_input, "Email input value mismatch"

# Locating the password field and performing actions
password_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Enter Password']")))
assert password_field.is_displayed(), "Password field is not displayed"
driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='']").click() # Clicking on the eye icon to show password
password_field.send_keys(password_input)
# Validating the password input value
assert password_field.text == password_input, "Password input value mismatch"

# Locating the login button and performing a click action
login_button = driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='Login']")
login_button.click()

# Granting the app permission for location access for one time
location_permission_modal = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Only this time']")))
location_permission_modal.click() # Performing a click action on the modal

# Validating the landing screen is displayed after login
landing_screen = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Self Overview']")))
assert landing_screen.is_displayed(), "Landing screen is not displayed"
# Navigating to the HR app icon
navigate_back()

# Locating the HR app icon and performing a click action
HR_app_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='HR']")))
# Validating the HR app icon is displayed
assert HR_app_icon.is_displayed(), "HR Icon is not displayed"
HR_app_icon.click()

# Locating the My Attendance app icon and performing a click action
My_Attendance_app_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='My Attendance']")))
# Validating the My Attendance app icon is displayed
assert My_Attendance_app_icon.is_displayed(), "My Attendance Icon is not displayed"
My_Attendance_app_icon.click()


## Click on the calendar icon to open the date picker and setting the date range ##

# Locating the calendar From field and performing a click action
calendar_from = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='From']"))).click()

 ## Navigating and choosing the desired month #
click_prev_month(2) # Navigating back two months

# Navigating and selecting the desired date 
select_calendar_date(8)

# Clicking the OK button to confirm the date selection
driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='OK']").click()

# Locating the calendar To field and performing a click action
calendar_to = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='To']"))).click()

## Navigating and choosing the desired month #
click_prev_month(1) # Navigating back one month

# Navigating and selecting the desired date
select_calendar_date(8)

# Clicking the OK button to confirm the date selection
driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='OK']").click()


# Locating the Status dropdown and performing a click action
driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='Status']").click()

# Filtering by 'On Leave' status
# Selecting the status option from the dropdown
select_status("On Leave")

#Validating the search results appear by checking if the employee name is displayed
assert wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Shaid Azmin']"))).is_displayed(),"Employee name is not displayed"

# Take a screenshot of the search results
driver.get_screenshot_as_file("ss1.png")

# Further validating the employee attendance details by status
serial = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='1.']"))).click()
attendance_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Attendance Details']")))
assert attendance_button.is_displayed(), "Employee attendance details is not displayed"

# Navigating multiple times
navigate_back(4)

## Closing the application ##

# Locating the app close button and validating if it is displayed
app_close_button = driver.find_element(by=AppiumBy.XPATH, value= "//*[@content-desc='OK']")
assert app_close_button.is_displayed(), "App close button is not displayed"

# Click the app close button 
app_close_button.click()

driver.terminate_app("com.arcone.arcone") # Terminate the app to remove it from background

##########

 ## Task 2: Check-IN & Leave Application Creation ##
 ## Objective: Automate key HR internal workflows—employee check-in and leave application submission. ##
 
  
  ## Precondition: App is logged in from Task-1 ##
  
# Restart the app from app package for Task-2
driver.activate_app("com.arcone.arcone")

# Validating the landing screen is displayed after login
landing_screen = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Self Overview']")))
assert landing_screen.is_displayed(), "Landing screen is not displayed"
navigate_back()

# Locating the HR app icon and performing a click action
HR_app_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='HR']")))
# Validating the HR app icon is displayed
assert HR_app_icon.is_displayed(), "HR Icon is not displayed"
HR_app_icon.click()

# Locating the Check-OUT app button and performing a click action
checkout_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@content-desc='Check-OUT']")))
assert checkout_button.is_displayed(), "Check-IN button is not displayed"
assert checkout_button.is_enabled(), "Check-IN button is not enabled"
checkout_button.click()

# Validating if the app permission modal is displayed
app_permission_modal = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Only this time']")))
assert app_permission_modal.is_displayed(), "App permission modal is not displayed"

# Validating if the camera permission is granted
permission_grant_button = wait.until(EC.presence_of_element_located
            ((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button"))).click()

# Clicking the camera SHUTTER button to take a ohoto
camera_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@content-desc='Shutter']")))
camera_button.click()

# Clicking the DONE button to confirm the photo and validating the button is enabled
Done_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Done')))
assert Done_button.is_enabled(), "Done button is not enabled"
Done_button.click()

# Selecting the log type as IN from the dropdown
Log_type_input = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Log Type']"))).click()
select_input = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='IN']"))).click()

# Tapping the checkin button in the employee check-in screen and validating the button exists
employee_checkin_button = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Check-IN")))
assert employee_checkin_button.is_displayed(), "Employee Check-IN button is not displayed"
assert employee_checkin_button.is_enabled(), "Employee Check-IN button is not enabled"
employee_checkin_button.click()

# Validating if the check-in success message is displayed
assert wait.until(EC.presence_of_element_located
                  ((AppiumBy.XPATH, "//*[@text='Checked IN Successful']"))).is_displayed(), "Check-IN success message is not displayed"

# Clicking the OK button to close the success message
driver.find_element(by=AppiumBy.XPATH, value="//*[@content-desc='OK']").click()

navigate_back() # Navigating back to the HR app icon
HR_app_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='HR']")))
HR_app_icon.click()

# Click in the Leave Application icon and validating if it is displayed
leave_application_icon = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@content-desc='Leave Application']")))
assert leave_application_icon.is_displayed(), "Leave Application Icon is not displayed"
leave_application_icon.click()

 ### Creating a new leave application ###

# Click on the new leave application button
new_add_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='']"))).click()
leave_application_add_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Application']"))).click()

# Selecting the leave type from the dropdown
leave_type_field = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Leave Type*']"))).click()
select_leave_type("Compensatory Leave")

## Selecting the From date ##
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='From Date*']"))).click()
year_calendar = wait.until(EC.presence_of_element_located((AppiumBy.ID, "android:id/date_picker_header_year"))).click()    

# Selecting the year in the calendar
select_year(2029)    
# Selecting the month in the calendar
click_prev_month(5) # Navigating backwards five months

# Selecting the date in the calendar
select_calendar_date(2)

# Clicking the OK button to confirm the date selection   
calendar_OK_button = driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='OK']").click()

## Selecting the From date ##
wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='To Date*']"))).click()

# Selecting the date in the calendar
select_calendar_date(7)
# Clicking the OK button to confirm the date selection   
calendar_OK_button = driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='OK']").click()

# Clicking the apply button to submit the leave application
apply_button = driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Apply']").click()

confirmation_messg = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//*[@text='Request successful']")))
assert confirmation_messg.is_displayed(), "Leave application confirmation message is not displayed"

# Taking a screenshot of the confirmation message
driver.get_screenshot_as_file("ss2.png")

# Clicking the OK button to close the confirmation message
confirmation_messg_OK_button = driver.find_element(by=AppiumBy.XPATH, value= "//*[@text='OK']").click()

# Navigating back to the leave application screen
navigate_back(3)

# Locating the app close button and validating if it is displayed
app_close_button = driver.find_element(by=AppiumBy.XPATH, value= "//*[@content-desc='OK']")
assert app_close_button.is_displayed(), "App close button is not displayed"

# Click the app close button to close the application
app_close_button.click()

