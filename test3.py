from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
import time

while True:
    driver = 0
    try:
      service = Service(executable_path='C:/Users/Law/Desktop/chromedriver-win64/chromedriver.exe')
      driver = webdriver.Chrome(service=service)
      driver.get("https://bcrmprod.ja.org/prod/webui/webshellpage.aspx?databasename=2313p#pageType=p&#pageId=27cf8c30-fbc2-43db-8cd2-9339028d3a68&recordId=3b0ad4d9-3079-4f05-9e38-ff5c58ae5e8d")
      driver.maximize_window()

      time.sleep(2)  # Allow initial load

      username_field = driver.find_element(By.ID, 'splash-login-username')
      username_field.send_keys('Lawrence.Jia')
      password_field = driver.find_element(By.ID, 'splash-login-password')
      password_field.send_keys('ASDFlaw7264270978;')
      password_field.send_keys(Keys.RETURN)

      time.sleep(5)  # Allow time for login to process

      test_btn = driver.find_element(By.ID, 'bbui-gen-manageshortcuts-405')
      test_btn.click()
      time.sleep(2)

      menu_btn = driver.find_element(By.ID, 'bbui-gen-shortcut-406')
      menu_btn.click()
      time.sleep(3)

      btn1 = driver.find_element(By.ID, 'ext-comp-1207')
      btn1.click()
      time.sleep(45)  # Wait for the navigation to complete

      btn2 = driver.find_element(By.ID, 'ext-gen653')
      btn2.click()
      time.sleep(7)

      btn3 = driver.find_element(By.XPATH, '//div[contains(@class, "x-grid3-row")]//*[text()="Constituent Page"]')
      btn3.click()
      time.sleep(7)

      btn4 = driver.find_element(By.XPATH, '//button[contains(@class, "x-btn-text")][normalize-space(text())="OK"]')
      btn4.click()
      time.sleep(7)

      wait = WebDriverWait(driver, 20)


      try:
          while True:
              try:
                  print("Checking for 'Personal Info' tab...")
                  # Get all elements and filter for the visible one with the right text
                  elements = wait.until(
                      EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.x-tab-right span.x-tab-strip-text'))
                  )
                  personal_info_tab = next((el for el in elements if el.is_displayed() and 'Personal Info' in el.text), None)

                  if personal_info_tab:
                      print('Found it.')
                      personal_info_tab = wait.until(EC.element_to_be_clickable(personal_info_tab))
                      print("Clicking 'Personal Info' tab...")
                      personal_info_tab.click()
                  else:
                      print("Personal Info tab not found, retrying...")
                      continue

                  buttons = wait.until(
                      EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.x-btn-text'))
                  )
                  # Filter buttons to find the one that is visible and has the correct text
                  mark_inactive_button = next((btn for btn in buttons if btn.is_displayed() and 'Mark inactive' in btn.text), None)

                  if mark_inactive_button:
                      print("Found 'Mark inactive' button.")
                      mark_inactive_button = wait.until(EC.element_to_be_clickable(mark_inactive_button))
                      mark_inactive_button.click()
                  else:
                      print("'Mark inactive' button not found, retrying...")
                      continue

                  btn7 = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "x-form-twin-triggers")]')))
                  btn7.click()

                  btn8 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='x-combo-list-item' and @title='Inactive - Record no longer active']")))
                  btn8.click()

                  btn9 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "x-btn-text")][normalize-space(text())="Save"]')))
                  btn9.click()

                  # Ensure the next record button is interactable before clicking
                  btn10 = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "x-btn-text bbui-adhocquery-browse-next")][normalize-space(text())="Next record"]')))
                  btn10.click()
                  # Wait for the page to stabilize after clicking 'Next record'
                  time.sleep(5)  # Consider replacing with a more dynamic wait if possible

              except (StaleElementReferenceException, NoSuchElementException) as e:
                  print(f"Encountered an error with element, retrying: {e}")
                  continue  # Skip the rest of the loop and try again
              except Exception as e:
                  print(f"An error occurred: {type(e).__name__}, {e}")
                  break  # Break the loop on other exceptions

      finally:
          print("Cleaning up, closing driver...")
          driver.quit()
    finally:
        if driver:
            driver.quit()