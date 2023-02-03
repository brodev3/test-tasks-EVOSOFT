import undetected_chromedriver.v2 as uc
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
import time
import os
import csv
from bs4 import BeautifulSoup as b
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


url = 'https://www.nseindia.com/'
filteredNames = []
filteredPrices = []

def parserhtml(html):
    soup = b(html, 'html.parser')
    allNames = soup.tbody.find_all('a', target="_blank")
    for name in allNames:
            filteredNames.append(name.text)
    allPrice = soup.tbody.find_all('td', class_="bold text-right")
    for price in allPrice:
            filteredPrices.append(price.text)

def findend(html):
    soup = b(html, 'html.parser')
    allNames = soup.find('div', class_="advance")
    adv = int(allNames.find('span', id="liveMrkStockAdv").text)
    dec = int(allNames.find('span', id="liveMrkStockDec").text)
    Chng = int(allNames.find('span', id="liveMrkStockUnChng").text)
    res = adv+dec+Chng
    return res

def mouse(element):
    element = ActionChains(driver).move_to_element(element)
    element.perform()

def scroll(count):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="equityStockTable"]/tbody/tr[{count}]')))
    actions.move_to_element(element).perform()

if __name__ == '__main__':
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument(f"--load-extension={os.path.abspath(os.curdir)}\proxy_auth_plugin")
    driver = uc.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options )
    wait = WebDriverWait(driver, timeout= 10)
    driver.implicitly_wait(10)
    driver.get(url)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="link_2"]')))
    element = driver.find_element(By.XPATH, '//*[@id="link_2"]')
    ActionChains(driver) \
        .move_to_element(element) \
        .perform()
    element = driver.find_element(By.XPATH, '//*[@href="/market-data/pre-open-market-cm-and-emerge-market"]')
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="togglecpm plus"]')))
    html = driver.page_source
    parserhtml(html)
    csvFile = open('results.csv', 'w')
    with csvFile:
        writer = csv.writer(csvFile, delimiter=";", lineterminator='\n')
        writer.writerows([['Имя', "Цена"]])
        writer = csv.writer(csvFile, delimiter=";", lineterminator='\n')
        for i in range(len(filteredNames)):
            writer.writerows([[filteredNames[i], filteredPrices[i]]])
    print("Writing to csv complete")
    print("Начало имитации пользовательского сценария по примеру")
    element = driver.find_element(By.XPATH, '//*[@class="navbar-brand mr-auto"]')
    mouse(element)
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class ="stockChart"]')))
    element = driver.find_element(By.XPATH, '//*[@href="https://itunes.apple.com/us/app/nse-nmf-ii/id1227619380?mt=8"]')
    actions = ActionChains(driver)
    print("График находится в области отображения, поэтому прокручиваем до подвала сайта")
    time.sleep(3)
    actions.move_to_element(element).perform()
    mouse(element)
    time.sleep(3)
    element = driver.find_element(By.XPATH, '//*[@href="#NIFTYBANK"]')
    actions.move_to_element(element).perform()
    element.click()
    #time.sleep(3000000000)
    element = driver.find_element(By.XPATH, '//*[@href="/market-data/live-equity-market?symbol=NIFTY BANK"]')
    element.click()
    time.sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="equitieStockSelect"]')))
    mouse(element)
    element.click()
    time.sleep(1)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@data-nse-translate-symbol="NIFTY ALPHA 50"]')))
    element.click()
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="equityStockTable"]')))
    element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="equitieStockSelect"]')))
    mouse(element)
    element.click()
    html = driver.page_source
    time.sleep(1)
    allitem = findend(html)+1
    scroll(20)
    scroll(35)
    scroll(45)
    scroll(51)
    print("Имитация окончена")
    driver.quit()







