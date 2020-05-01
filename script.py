"""
Create a virtual environment: py -m venv env
Activate Virtual Environment: .\env\Scripts\activate
Deactivate Virutal Environment: deactivate

"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from simple_chalk import chalk, green
import argparse
from pathlib import Path
import os

#Parsing the command line arguments passed
parser = argparse.ArgumentParser()
parser.add_argument("username")
parser.add_argument("password")
parser.add_argument("course_code")
parser.add_argument("file_path", type=Path)
p = parser.parse_args()

PATH = p.file_path

driver = webdriver.Chrome(PATH)
    
WEBSITE = "https://wrem.sis.yorku.ca/Apps/WebObjects/REM.woa/wa/DirectAction/rem"


#Defining important variables
york_user_name = p.username
york_password = p.password
COURSE_KEY_CODE = p.course_code
success_message = "The course has been successfully added."
error_message = "The course has not been added."
reason_message = "The course you are trying to add is full. Please refer to the online course timetable for alternate choices and try again."

#Opening up the website
driver.get(WEBSITE)

#Logging into the website
username_textfield = driver.find_element_by_id("mli")
password_textfield = driver.find_element_by_id("password")
username_textfield.send_keys(york_user_name)
password_textfield.send_keys(york_password)
password_textfield.send_keys(Keys.RETURN)
#Finished Logging in

#Waiting 5 seconds for the pages to successfully switch
time.sleep(5)


#Choosing Summer2020 In the list of options
selection_table = Select(driver.find_element_by_name('5.5.1.27.1.11.0'))
ACADEMIC_SESSION="Summer 2020"
selection_table.select_by_visible_text(ACADEMIC_SESSION)
continue_button = driver.find_element_by_name("5.5.1.27.1.13")
continue_button.click()

time.sleep(5)

#Choosing to Add a course
add_course_button = driver.find_element_by_name("5.1.27.1.23")
add_course_button.click()

#Enrolling in the proper course
course_input_textfield = driver.find_element_by_name("5.1.27.7.7")
course_input_textfield.send_keys(COURSE_KEY_CODE)

add_selected_course = driver.find_element_by_name("5.1.27.7.9")
add_selected_course.click()

time.sleep(3)

#Confirming 'Yes' We want to enroll
confirm_yes_button = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[6]/td[2]/input[1]")
course_title_chosen = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[5]/td[2]/span")
course_title = course_title_chosen.text
confirm_yes_button.click()

time.sleep(2)
#Checking the result of trying to enroll in the selected course
result_of_adding_course = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/span/font/b")

if result_of_adding_course.text == error_message:
    print(chalk.red("The course: " + course_title +  " could not be added for the following reason:"))
    reason_for_failure = driver.find_element_by_xpath("/html/body/form/div[1]/table/tbody/tr[4]/td[2]/table/tbody/tr/td/table[2]/tbody/tr[2]/td[2]/span/font/b")
    print(chalk.red(reason_for_failure.text))
    message_to_send = "The course: " + course_title +  " could not be added for the following reason:"+ reason_for_failure.text
    os.system(f'text-me.py "{message_to_send}"')
else:
    print(green(result_of_adding_course.text))
    message_to_send = success_message
    os.system(f'text-me.py "{message_to_send}"')

driver.quit()
    




