import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from faker import Faker
# Initialize Faker
fake = Faker('en_IN')
# Specify the path to the webdriver executable
# Replace 'chromedriver.exe' with the appropriate driver for your browser
driver_path = 'C:\chromedriver\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
# Set implicit wait time (in seconds)
# driver.implicitly_wait(10)  # Adjust the wait time as needed

# Navigate to the URL of the website
driver.get('https://www.chapter-living.com/')
book_button = driver.find_element(By.XPATH, '//*[@id="btn-main-book-a-room-pink"]/span')
book_button.click()
# driver.implicitly_wait(10)

# Wait for the new page to load
try:
    # Wait for the URL of the new page to contain a specific substring (replace 'example.com' with the expected domain of the next page)
    WebDriverWait(driver, 10).until(EC.url_contains('https://www.chapter-living.com/booking/'))
    print("Next page opened successfully.")

    # Now you can continue with your Selenium operations on the new page
    # For example, you can find elements on the new page and perform further actions or validations here
except Exception as e:
    print("Error occurred while waiting for the next page:", e)
x=driver.find_element(By.ID,"BookingAvailabilityForm_Residence")
drop=Select(x)
# select by visible text
drop.select_by_visible_text("CHAPTER KINGS CROSS")
time.sleep(3)
x2=driver.find_element(By.ID,"BookingAvailabilityForm_BookingPeriod")
drop2=Select(x2)
time.sleep(3)
drop2.select_by_visible_text("SEP 24 - AUG 25 (51 WEEKS)")

# Find the checkbox using XPath (replace with the appropriate locator)
time.sleep(5)
# checkbox = driver.find_element(By.ID, "filter-room-type-ensuite")
checkbox=driver.find_element(By.XPATH,'//*[@id="filter-room-type-ensuite"]')
# checkbox = driver.find_element(By.CSS_SELECTOR, "#filter-room-type-ensuite")
# Execute JavaScript code to click on the checkbox
driver.execute_script("arguments[0].click();", checkbox)
time.sleep(5)
# checkbox.click()
time.sleep(3)
if checkbox.is_selected():
    print("Checkbox is checked.")
else:
    print("Checkbox is not checked.")

# Check the checkbox if it's not already checked
# if not checkbox.is_selected():
#     checkbox.click()
driver.implicitly_wait(10)
apply_btn=driver.find_element(By.XPATH,'//*[@id="modal-room-1"]/div[4]/div/div[2]/a')

driver.implicitly_wait(20)
apply_btn.click()

driver.implicitly_wait(10)
# Find the input fields and fill them with fake data
first_name_input = driver.find_element(By.ID,'applicant_first_name')
last_name_input = driver.find_element(By.ID,'applicant_last_name')
country_code_input=driver.find_element(By.XPATH,'//body/div[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/form[1]/ul[1]/li[6]/ul[1]/li[1]/div[1]/div[1]/div[1]/div[1]/input[1]')

# country_code_input=driver.find_element(By.CLASS_NAME,'country-code ui-field--touched')
# country_code = driver.find_element(By.XPATH, '//input[@class="country-code ui-field--touched"]')

phone_number_input = driver.find_element(By.ID,'phone_numbers[0][phone_number]-base')
email_input = driver.find_element(By.ID,'applicant_username')
password_input = driver.find_element(By.ID,'applicant_password')
confirm_pwd_input = driver.find_element(By.ID,'applicant_password_confirm')
# Generate fake data
fake_first_name = fake.first_name()
fake_last_name = fake.last_name()
fake_country_code = fake.country_code()
fake_phone_number = fake.phone_number()
fake_email = fake.email()
fake_password = fake.password()
fake_password = fake_password
# Fill in the form
first_name_input.send_keys(fake_first_name)
last_name_input.send_keys(fake_last_name)
country_code_input.send_keys(fake_country_code)
# time.sleep(3)
# phone_number_2_digit.send_keys('91')
phone_number_input.send_keys(fake_phone_number)
email_input.send_keys(fake_email)
password_input.send_keys(fake_password)
confirm_pwd_input.send_keys(fake_password)
# checkbox_btn= driver.find_element(By.ID, "create-app-btn")
# time.sleep(3)
# checkbox_btn.click()
checkbox_btn= driver.find_element(By.XPATH,'//*[@id="agrees_to_terms"]')
driver.implicitly_wait(10)
checkbox_btn.click()
# create_account_btn=driver.find_element(By.XPATH,'//*[@id="create-app-btn"]').click()
wait = WebDriverWait(driver, 10)
overlay = wait.until(EC.invisibility_of_element_located((By.ID, "overlay-cnfrm-793bc5")))
time.sleep(3)
# Now click the button
# checkbox_btn.click()
time.sleep(3)
create_account_btn = driver.find_element(By.ID, "create-app-btn").click()
time.sleep(5)
# agree_the_term_btn=driver.find_element(By.XPATH,'//*[@id="confirm-cnfrm-ba2259"]/div/a[1]')
agree_the_term_btn=driver.find_element(By.XPATH,"//a[contains(text(),'I agree to the terms')]")
agree_the_term_btn.click()
driver.implicitly_wait(10)
# time.sleep(5)
print("its work")
# Wait for the content to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'sus-unit-space-details')))

# Find all div elements with class "sus-unit-space-details"
div_elements = driver.find_elements(By.CLASS_NAME, 'sus-unit-space-details')

# Initialize an empty list to store building details
building_details_list = []

# Loop through each div element
for div_element in div_elements:
    # Find the dt element with class "title" within the div
    dt_element = div_element.find_element(By.CLASS_NAME, 'title')

    # Find the dd element with class "value" within the div
    dd_element = div_element.find_element(By.CLASS_NAME, 'value')

    # Extract the building details
    building_details = {
        'title': dt_element.text.strip(),
        'value': dd_element.text.strip()
    }

    # Append the building details to the list
    building_details_list.append(building_details)

# Print the extracted building details
print('Building Details:', building_details_list)

driver.close()
