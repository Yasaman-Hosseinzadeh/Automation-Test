from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC,wait
import time

driver = webdriver.Firefox()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(20)
driver.maximize_window()

RadioButtonExample_Radio1 = driver.find_element(By.XPATH,'//body/div[1]/div[1]/fieldset[1]/label[1]/input[1]').click()
RadioButtonExample_Radio2 = driver.find_element(By.XPATH,'//body/div[1]/div[1]/fieldset[1]/label[2]/input[1]').click()
RadioButtonExample_Radio3 = driver.find_element(By.XPATH,'//body/div[1]/div[1]/fieldset[1]/label[3]/input[1]').click()

SuggessionClassExample = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[2]/fieldset[1]/input[1]').send_keys("selenium learning class")

DropdownExample = driver.find_element(By.CSS_SELECTOR,'#dropdown-class-example').click()
DropdownExample_Option1 = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[3]/fieldset[1]/select[1]/option[2]').click()
DropdownExample_Option2 = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[3]/fieldset[1]/select[1]/option[3]').click()
DropdownExample_Option3 = driver.find_element(By.XPATH,'/html[1]/body[1]/div[1]/div[3]/fieldset[1]/select[1]/option[4]').click()

CheckboxOption1 = RadioButtonExample_Radio1 = driver.find_element(By.CSS_SELECTOR,'#checkBoxOption1').click()
CheckboxOption2 = RadioButtonExample_Radio1 = driver.find_element(By.CSS_SELECTOR,'#checkBoxOption2').click()
CheckboxOption3 = RadioButtonExample_Radio1 = driver.find_element(By.CSS_SELECTOR,'#checkBoxOption3').click()

SwitchWindowExample = driver.find_element(By.CSS_SELECTOR,'#openwindow').click()

SwitchTabExample = driver.find_element(By.CSS_SELECTOR,'#opentab').click()

SwitchToAlertExample = driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Yasaman Hosseinzadeh")
driver.find_element(By.CSS_SELECTOR,'#alertbtn').click()

