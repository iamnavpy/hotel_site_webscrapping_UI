import time

import pymongo as pymongo
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
driver.get('https://chapterkingscross.prospectportal.global/Apartments/module/application_unit_info/')

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
# driver.implicitly_wait(20)
time.sleep(10)
checkbox_btn.click()
# create_account_btn=driver.find_element(By.XPATH,'//*[@id="create-app-btn"]').click()
wait = WebDriverWait(driver, 10)
overlay = wait.until(EC.invisibility_of_element_located((By.ID, "overlay-cnfrm-793bc5")))
time.sleep(5)
# Now click the button
# checkbox_btn.click()

create_account_btn = driver.find_element(By.ID, "create-app-btn").click()
time.sleep(5)
# agree_the_term_btn=driver.find_element(By.XPATH,'//*[@id="confirm-cnfrm-ba2259"]/div/a[1]')
agree_the_term_btn=driver.find_element(By.XPATH,"//a[contains(text(),'I agree to the terms')]")
agree_the_term_btn.click()
# driver.implicitly_wait(10)
#start page extract
time.sleep(10)
# Find all div elements with class 'sus-col-40 left'
divs = driver.find_elements_by_xpath('//div[@class="sus-col-40 left"]')

# Initialize lists to store the extracted data
building_list = []
rent_list = []
deposit_list = []
amenities_list = []

# Loop through each div element
for div in divs:
    # Find all dt elements with class 'title' and corresponding dd elements with class 'value'
    dt_elements = div.find_elements_by_xpath('.//dt[@class="title"]')
    dd_elements = div.find_elements_by_xpath('.//dd[@class="value"]')

    # Extract the text from the dt and dd elements
    for dt, dd in zip(dt_elements, dd_elements):
        if dt.text.strip() == 'Building':
            building_list.append(dd.text.strip())
        elif dt.text.strip() == 'Rent':
            rent_list.append(dd.text.strip())
        elif dt.text.strip() == 'Deposit':
            deposit_list.append(dd.text.strip())
        elif dt.text.strip() == 'Amenities':
            amenities_list.append(dd.text.strip())

# Create a DataFrame
df = pd.DataFrame({
    'Building': building_list,
    'Rent': rent_list,
    'Deposit': deposit_list,
    'Amenities': amenities_list
})

# Print the DataFrame
print(df)
# Find all div elements with class 'sus-col-40 left'
divs = driver.find_elements_by_xpath('//div[@class="sus-col-40 left"]')

# Initialize lists to store the extracted data
building_list = []
rent_list = []
deposit_list = []
amenities_list = []

# Loop through each div element
for div in divs:
    # Find all dt elements with class 'title' and corresponding dd elements with class 'value'
    dt_elements = div.find_elements_by_xpath('.//dt[@class="title"]')
    dd_elements = div.find_elements_by_xpath('.//dd[@class="value"]')

    # Extract the text from the dt and dd elements
    for dt, dd in zip(dt_elements, dd_elements):
        if dt.text.strip() == 'Building':
            building_list.append(dd.text.strip())
        elif dt.text.strip() == 'Rent':
            rent_list.append(dd.text.strip())
        elif dt.text.strip() == 'Deposit':
            deposit_list.append(dd.text.strip())
        elif dt.text.strip() == 'Amenities':
            amenities_list.append(dd.text.strip())

# Create a DataFrame
df = pd.DataFrame({
    'Building': building_list,
    'Rent': rent_list,
    'Deposit': deposit_list,
    'Amenities': amenities_list
})

# Close the WebDriver
driver.quit()

# Connect to MongoDB Atlas
client = pymongo.MongoClient("mongodb+srv://n4naveenmishra:Redhat%231234@cluster0.kyu9cn2.mongodb.net/")

# Select the database and collection
db = client['universityliving']
collection = db['booking']

# Convert the DataFrame to a dictionary
data = df.to_dict(orient='records')

# Insert the data into the collection
collection.insert_many(data)

# Close the MongoDB connection
client.close()
# Close the WebDriver

driver.quit()