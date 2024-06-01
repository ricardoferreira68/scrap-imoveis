import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
link_list = ["https://www.zapimoveis.com.br/venda/apartamentos/pa+belem/?transacao=venda&onde=,Par%C3%A1,Bel%C3%A9m,,,,,city,BR%3EPara%3ENULL%3EBelem,-1.456343,-48.501299,&tipos=apartamento_residencial&itl_id=1000072&itl_name=zap_-_botao-cta_buscar_to_zap_resultado-pesquisa",]

def fetch_links(link):
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(link)
    actions = ActionChains(driver)
    for _ in range(100):
        actions.send_keys(Keys.SPACE).perform()
        time.sleep(0.5)

    driver.implicitly_wait(60)

    bottomFooter = driver.find_element(By.CLASS_NAME, 'footer')
    driver.execute_script('arguments[0].scrollIntoView();', bottomFooter)

    apartment = driver.page_source.count("<div data-position=")
    print(apartment)

    driver.implicitly_wait(60)
    
    for i in range(1, apartment+1):
        try:
            item = driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div['+str(i)+']/div/a').get_attribute('href')
            print(item)
            time.sleep(1)
        except NoSuchElementException:
            continue
    # driver.implicitly_wait(100)

    '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/section/nav/button[2]'

fetch_links(link_list[0])
