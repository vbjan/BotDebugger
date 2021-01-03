import selenium.webdriver as webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

PATH = "/usr/bin/chromedriver"
#PATH = "/Users/jan-philippvonbassewitz/bot_automation/chromedriver"
driver = webdriver.Chrome(PATH)
print("Bot is successfully initialized")

driver.get('https://www.asvz.ch/426-sportfahrplan?f[0]=facility:45598&f[1]=sport:122920')
time.sleep(2)
driver.quit()
print("Bot has successfully opened webpage and quit")
