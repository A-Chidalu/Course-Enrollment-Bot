# Course-Enrollment-Bot
A Python Bot to automatically enroll a user into a specified course

## How it works
This program uses selenium webdriver to access York University's course enrollment site and tries to enroll in the specified course

## Installation
### YOU MUST USE GOOGLE CHROME BROWSER TO USE THIS PROGRAM
1. Check what google chrome version you have you can do this by following the picture below
![Google-chrome](https://github.com/A-Chidalu/Course-Enrollment-Bot/blob/master/img/google-chrome-pic.PNG)

2. Go to https://sites.google.com/a/chromium.org/chromedriver/downloads and install the correct google chrome driver for your version of google chrome. For example my google chrome version is **81.0.4044.122** so I will install version **81.0.4044.69** on the website provided. Note: The versions dont have to match exactly, only the first two numbers have to match.

3. Install the google chrome webdriver, extract the files, and place the chromedriver.exe in a location you will remember.

4. Have Python 3 or Greater installed on your machine
5. Clone the repository
6. run the command `pip3 install -r requirements.txt`

## Getting Started
Getting started with this program is simple. When all the dependancies have finished installing, simply run `python window.py`
You window that looks like this:
![Empty-window](https://github.com/A-Chidalu/Course-Enrollment-Bot/blob/master/img/window.PNG)
Fill out your **York Passport Username and Password**, browse to the correct location of the web driver, and click submit.
Your course will be automatically enrolled

## Future Updates
-In a Future Realease the program will continously try to enroll in a course a user-selected number of times, and text the result of each attempt to a users cell-phone number
