import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def fetch(driver):
    listing_wrapper__content = driver.find_element(By.CLASS_NAME, "listing-wrapper__content")
    delta_y = listing_wrapper__content.rect['y']
    for _ in range(100):
        ActionChains(driver).scroll_by_amount(0, delta_y).perform()
        time.sleep(1)
    driver.implicitly_wait(5)
    number_of_apartments = driver.page_source.count("<div data-position=")
    print(number_of_apartments)
    driver.implicitly_wait(5)
    for i in range(1, number_of_apartments+1):
        try:
            item = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div['+str(i)+']/div/a').get_attribute('href')
            # print(item)
            with open('apartment_links.txt', 'a') as file_apartment_links:
                file_apartment_links.write(item+'\n')
            time.sleep(0.1)
        except NoSuchElementException:
            continue

link = 'https://www.zapimoveis.com.br/venda/apartamentos/pa+belem/?__ab=exp-aa-test:control,novopos:new,super-high:new,olx:control,score-rkg:control&transacao=venda&onde=,Par%C3%A1,Bel%C3%A9m,,,,,city,BR%3EPara%3ENULL%3EBelem,-1.456343,-48.501299,&tipos=apartamento_residencial&pagina=1'
service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-geolocation')
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(link)
time.sleep(10)
try:
    cookei_alert = driver.find_element(By.XPATH, '//*[@id="cookie-notifier-cta"]')  
    cookei_alert.click()
except Exception as e:
    print("no cookie popup", e)
page = 0
while True:
    page += 1
    print(f'Page: {page}')
    fetch(driver)
    pagination_button_xpath = '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/section/nav/button[2]'
    try:
        driver.find_element(By.XPATH, pagination_button_xpath)
    except Exception as e:
        print(repr(e))
        break
    try:
        pagination_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, pagination_button_xpath)))
        # print(pagination_button)
        pagination_button.click()
    except Exception as e:
        print(e)
        break
    time.sleep(5)
driver.quit()
