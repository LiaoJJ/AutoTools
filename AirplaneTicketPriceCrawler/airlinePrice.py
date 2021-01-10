import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait

sys.path.append("../")
from AutoCrawler.send_an_email import send_email

MONITOR_DATE = "2020-11-18"
receiver = "jjliao14@gmail.com"

def run():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.xiamenair.com/zh-cn/nticket.html?tripType=OW&orgCodeArr%5B0%5D=XMN&dstCodeArr%5B0%5D=SIN&orgDateArr%5B0%5D="+MONITOR_DATE+"&dstDate=&isInter=true&adtNum=1&chdNum=0&JFCabinFirst=false&acntCd=&mode=Money&partner=false&jcgm=false")
    price = int(driver.find_element_by_css_selector("li:nth-of-type(2) strong").get_attribute("textContent"))
    driver.close()
    return price


def main():
    prev = -1
    while True:
        try:
            price = run()
            print(time.strftime("[%I:%M:%S %p]", time.localtime()), " "+MONITOR_DATE+" price: ", price)
            if prev != -1 and price < prev:
                send_email("Airplane price down, current price is " + str(price), "current price is " + str(price),
                           receiver)
            prev = price
            time.sleep(60)
        except:
            pass
            time.sleep(600)


main()
