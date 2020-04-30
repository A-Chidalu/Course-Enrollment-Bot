from tkinter import *
from tkinter import filedialog
import os

window = Tk()

window.title("York Course Enrollment Bot")
window.geometry("500x250")

title_label = Label(window, text="York Course Enroller", pady=8)
username_label = Label(window, text="York username:", pady=8)
password_label = Label(window, text="York password:", pady=8)
username_textfield = Entry(window,width=30)
password_textfield = Entry(window,width=30, show="*")
course_code_label = Label(window, text="Course to Enroll in(course code):", pady=8)
course_code_textfield = Entry(window,width=10)
path_to_driver_label = Label(window, text="Path To webdriver:", pady=8)


title_label.grid(row=0, column=1)
username_label.grid(row=1, column=0)
password_label.grid(row=2, column=0)
username_textfield.grid(row=1, column=1)
password_textfield.grid(row=2, column=1)
course_code_label.grid(row=3, column=0)
course_code_textfield.grid(row=3, column=1)
path_to_driver_label.grid(row=4, column=0)

YORK_USERNAME = ""
YORK_PASSWORD = ""
COURSE_CODE = ""

PATH_TO_DRIVER = ""
def browse_for_driver():
    window.filename = filedialog.askopenfilename(initialdir="/", title="Select webdriver", filetypes=[("Exe Files", "*.exe")] )
    return window.filename

def validate():
    if not check_username():
        alert_popup("No Username Provided", "Please Provide a valid Username", "")
        return
    else:
        YORK_USERNAME = username_textfield.get()
    if not check_password():
        alert_popup("No Password Provided", "Please Provide a valid Password", "")
        return
    else:
        YORK_PASSWORD = password_textfield.get()
    if not check_course_code():
        alert_popup("Invalid Course Code Provided", "Please Provide a valid course code.", "")
        return
    else:
        COURSE_CODE = course_code_textfield.get()
    if not PATH_TO_DRIVER:
        alert_popup("No Path To driver provided", "Please Provide a valid driver path.", "")
        return
    
    run_script(YORK_USERNAME, YORK_PASSWORD, PATH_TO_DRIVER)

def start_browsing():
    global PATH_TO_DRIVER
    PATH_TO_DRIVER = browse_for_driver()
    if not PATH_TO_DRIVER:
        alert_popup("No Path To driver provided", "Please Provide a valid driver path.", "")
        return
    
        
def check_username():
   return len(username_textfield.get()) != 0

def check_password():
    return len(password_textfield.get()) != 0

def check_course_code():
     return len(password_textfield.get()) != 6

def alert_popup(title, message, path):
    """Generate a pop-up window for special messages."""
    root = Tk()
    root.title(title)
    w = 400     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    m = message
    m += '\n'
    m += path
    w = Label(root, text=m, width=120, height=10)
    w.pack()
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop() 

def run_script(YORK_USERNAME, YORK_PASSWORD, PATH_TO_DRIVER):
    os.system(f'script.py {YORK_USERNAME} {YORK_PASSWORD} "{PATH_TO_DRIVER}"')



submit_button = Button(window, text="Submit Form", command=validate)
browse_button = Button(window, text="Browse", command=start_browsing)

submit_button.grid(row=5, column=1)
browse_button.grid(row=4, column=1)


window.mainloop()