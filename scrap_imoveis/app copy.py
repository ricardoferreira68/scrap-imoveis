from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = 'https://www.zapimoveis.com.br/venda/apartamentos/pa+belem/?transacao=venda&onde=,Par%C3%A1,Bel%C3%A9m,,,,,city,BR%3EPara%3ENULL%3EBelem,-1.456343,-48.501299,&tipos=apartamento_residencial&itl_id=1000072&itl_name=zap_-_botao-cta_buscar_to_zap_resultado-pesquisa'
driver.get(url=url)
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/section/nav/button[2]/span/svg')))
driver.implicitly_wait(10)
# //*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div[1]/div/a
# //*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div[2]/div/a
for i in range(1, 16):
    print(driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div['+str(i)+']/div/a').get_attribute('href'))
    driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/form/div[2]/div[4]/div[1]/div/div['+str(i)+']/div/a').click()
    # driver.implicitly_wait(10)
    # driver.back()
    driver.implicitly_wait(2)
print(driver.find_element(By.CLASS_NAME, 'l-pagination'))