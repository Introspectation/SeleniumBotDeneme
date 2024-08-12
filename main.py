from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#init webDriver
driver = webdriver.Chrome()

#access the website
driver.get("https://freebitco.in/signup/?op=s")

#waitfor few seconds to observe
time.sleep(9.56)

#close the popup
try:
    no_thanks_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pushpad_deny_button"))
    )
    no_thanks_button.click()
    print("popup closed")
except Exception as e:
    print(f"popup not found or not closed: {e}")

#find the login menu button
login_menu_button = driver.find_element(By.CLASS_NAME, "login_menu_button")

#Scroll to the login menu button to ensure it's in the view
driver.execute_script("arguments[0].scrollIntoView()", login_menu_button)

#Wait until the login menu is clickable, then click
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "login_menu_button"))).click()
    print("Login clikced menu")
except Exception as e:
    print(f"Login clikced menu not found or not closed: {e}")

#Wait for the login form to appear
time.sleep(2.678)

#Find and fill in the login details
email_field = driver.find_element(By.ID,"login_form_btc_address")
password_field = driver.find_element(By.ID, "login_form_password")

email_field.send_keys("X@gmail.com")
password_field.send_keys("PASSWORD")

#click on login but
try:
    login_button = driver.find_element(By.ID, "login_button")
    login_button.click()
    print("login clicked")
except Exception as e:
    print(f"login error: {e}")

#wait for the captcha to appear and try to click it
try:
    hcaptcha_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "h-captcha"))
    )
    hcaptcha_checkbox.click()
    print("hcaptcha checkbox clicked")
except Exception as e:
    print(f"hcaptcha not found or not closed: {e}")

#wait a bit to see if captcha is passed
time.sleep(4.231)

#attempt to press the roll! button
try:
    roll_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "free_play_form_button"))
    )
    roll_button.click()
    print("roll button clicked")
except Exception as e:
    print(f"roll button not found or not closed: {e}")

#wait for login to complete and observe the page
time.sleep(60.551)

#close
driver.quit()