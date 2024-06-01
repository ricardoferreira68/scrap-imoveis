import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def close_cookies_policy_popup(driver):
    try:
        time.sleep(2)
        cookei_alert = driver.find_element(By.XPATH, '//*[@id="cookie-notifier-cta"]')  
        cookei_alert.click()
    except Exception as e:
        logging.info(repr(e))

def get_details_content_info(driver):
    details_content_info = ''
    try:
        details_content_info_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div'  # 'Em contrução'
        details_content_info = driver.find_element(By.XPATH, details_content_info_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return details_content_info


def get_address(driver):
    address = ''
    try:
        address_info_value_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/p'
        address = driver.find_element(By.XPATH, address_info_value_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return address


def get_neighborhood(driver):
    neighborhood = ''
    try:
        neighborhood_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/div/nav/ol/li[4]/a'
        neighborhood = driver.find_element(By.XPATH, neighborhood_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return neighborhood


def get_private_area(driver):
    private_area = ''
    try:
        private_area_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/div/div/p[1]/span[2]'
        private_area = driver.find_element(By.XPATH, private_area_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return private_area


def get_bedroom(driver):
    bedroom = ''
    try:
        bedroom_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/div/div/p[2]/span[2]'
        bedroom = driver.find_element(By.XPATH, bedroom_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return bedroom


def get_bathroom(driver):
    bathroom = ''
    try:
        bathroom_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/div/div/p[3]/span[2]'
        bathroom = driver.find_element(By.XPATH, bathroom_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return bathroom


def get_garage(driver):
    garage = ''
    try:
        garage_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/div/div/p[4]/span[2]'
        garage = driver.find_element(By.XPATH, garage_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return garage


def get_floor(driver):
    floor = ''
    try:
        floor_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/div/div/p[5]/span[2]'
        floor = driver.find_element(By.XPATH, floor_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return floor


def get_balcony(driver):
    balcony = ''
    try:
        balcony_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/div/div/p[6]/span[2]'
        balcony = driver.find_element(By.XPATH, balcony_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return balcony


def get_condo_fee_price(driver):
    condo_fee_price = ''
    try:
        condo_fee_price_xpath = '//*[@id="condo-fee-price"]'
        condo_fee_price = driver.find_element(By.XPATH, condo_fee_price_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return condo_fee_price


def get_IPTU_price(driver):
    IPTU_price = ''
    try:
        IPTU_price_xpath = '//*[@id="iptu-price"]'
        IPTU_price = driver.find_element(By.XPATH, IPTU_price_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return IPTU_price


def get_price(driver):
    price = ''
    try:
        price_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[3]/div/div[1]/div[1]/p[2]'
        price = driver.find_element(By.XPATH, price_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return price


def create_file():
    with open('dodos_de_ap_de_belem_extraidos_do_zapimoveis.txt', 'w') as file_apartment_links:
        header = 'observacao;endereco;bairro;area_privativa;quarto;banheiro;garagem;andar;sacada;valor_condominio;iptu;preco;url'
        file_apartment_links.write(header+'\n')


def write_row_in_file(row):
    with open('dodos_de_ap_de_belem_extraidos_do_zapimoveis.txt', 'a') as file_apartment_links:
        file_apartment_links.write(row)


def fetch(link):
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    time.sleep(2)
    driver.get(link)
    close_cookies_policy_popup(driver)
    details_content_info = get_details_content_info(driver)
    address = get_address(driver)
    neighborhood = get_neighborhood(driver)
    private_area = get_private_area(driver)
    bedroom = get_bedroom(driver)
    bathroom = get_bathroom(driver)
    garage = get_garage(driver)
    floor = get_floor(driver)
    balcony = get_balcony(driver)
    condo_fee_price = get_condo_fee_price(driver)
    IPTU_price = get_IPTU_price(driver)
    price = get_price(driver)
    driver.close()

    row = f'{details_content_info};{address};{neighborhood};{private_area};{bedroom};{bathroom};{garage};{floor};{balcony};{condo_fee_price};{IPTU_price};{price};{link}'
    write_row_in_file(row)

    # print(f'Observação: {details_content_info}')
    # print(f'Endereço: {address}')
    # print(f'Bairro: {neighborhood}')
    # print(f'Área privativa: {private_area}')
    # print(f'Quarto: {bedroom}')
    # print(f'Banheiro: {bathroom}')
    # print(f'garagem: {garage}')
    # print(f'Andar: {floor}')
    # print(f'Sacada: {balcony}')
    # print(f'Valor condomínio: {condo_fee_price}')
    # print(f'IPTU: {IPTU_price}')
    # print(f'Preço: {price}')


service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-geolocation')
create_file()
APARTMENT_LINKS_FILE = 'apartment_links.txt'
try:
    with open(APARTMENT_LINKS_FILE, 'r') as apartment_links_file:
        for link in apartment_links_file:
            fetch(link)
except Exception as e:
    logging.critical(e)

"""
url             = ''
building_name   = ''
suite           = ''
closet          = ''
toilet          = ''
service_area    = ''
dependence_maid = ''
pool            = ''
party_room      = ''
sports_court    = ''
playground      = ''
gym             = ''
"""
