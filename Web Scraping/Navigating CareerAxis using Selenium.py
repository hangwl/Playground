from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

username = "" # student\_____
password = "" # password

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://careeraxis.ntu.edu.sg/")
print(driver.title) 

time.sleep(1)

print(driver.title)
driver.find_element("name", "UserName").send_keys(username)
driver.find_element("name", "Password").send_keys(password)
driver.find_element("css selector", "span.submit, input[type=\"submit\"]").click()

print("logged in successfully") 

driver.get("https://careeraxis.ntu.edu.sg/students/jobs/TypeOfWork/2210/internship")

main = driver.find_element("id", "main")
print(main.text)

time.sleep(5)
driver.quit()

