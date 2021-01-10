import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

# This example requires Selenium WebDriver 3.13 or newer
chrome_options = Options()
# chrome_options.add_encoded_extension("gighmmpiobklfepjocnamgkkbiglidom")
# chrome_options.add_argument("load-extension=/User/ljj/Library/Application Support/Google/Chrome/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom")
chrome_options.add_extension("/Users/ljj/Documents/Courses/CS/LeetCode/Selenium-Scripts/MorningTask/extension_4_25_1_0.crx")

with webdriver.Chrome(options=chrome_options) as driver:
    wait = WebDriverWait(driver, 10)
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.youtube.com/playlist?list=PL0tDb4jw6kPyN_Umwu7oZK44EFq-nvdwu")
    driver.find_element_by_css_selector("#content > a").click()

    time.sleep(60*15)
