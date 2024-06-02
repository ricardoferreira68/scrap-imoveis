import codecs
import logging
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def create_file():
    with open('dodos_de_ap_de_belem_extraidos_do_zapimoveis.txt', 'w') as file_apartment_links:
        header = 'garagem;piscina;endereco;nome_do_edificio;bairro;area_privativa;quarto;banheiro;lavabo;suite;sacada;sacada_gourmet;andar;valor_condominio;iptu;preco;observacao;url'

        file_apartment_links.write(header+'\n')


def write_row_in_file(row):
    with codecs.open('dodos_de_ap_de_belem_extraidos_do_zapimoveis.txt', 'a', encoding='utf-8') as file_apartment_links:
        file_apartment_links.write(row)


def close_cookies_policy_popup(driver):
    try:
        time.sleep(2)
        cookei_alert = driver.find_element(By.XPATH, '//*[@id="cookie-notifier-cta"]')  
        cookei_alert.click()
    except Exception as e:
        logging.info(repr(e))


def expand_all_features(driver):
    try:
        time.sleep(2)
        all_features = driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/div[4]/div/a')  
        all_features.click()
    except Exception as e:
        logging.info(repr(e))


def get_garage(driver):
    garage = ''
    try:
        garage_xpath = '//p[@itemprop="numberOfParkingSpaces"]'
        garage = driver.find_element(By.XPATH, garage_xpath).text
        garage = int(garage.split()[0])
    except Exception as e:
        logging.info(repr(e))
    return garage


def get_pool(driver):
    pool = ''
    try:
        pool_xpath = '//p[@itemprop="pool"]'
        pool = driver.find_element(By.XPATH, pool_xpath).text
        pool = 'Sim'
    except Exception as e:
        logging.info(repr(e))
    return pool


def get_address(driver):
    address = ''
    try:
        address_info_value_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[5]/div[1]/p'
        address = driver.find_element(By.XPATH, address_info_value_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return address


def get_building_name(driver):
    building_name = ''
    try:
        description_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/section/div[2]/div/div'
        description = driver.find_element(By.XPATH, description_xpath).text
        regex_torre_duas_palavras = r'(?i)Torre\s(\w+\s\w+)'
        regex_torre_uma_palavra = r'(?i)Torre\s\w+'
        regex_edificio = r'(?i)(Edif\w{1}cio|Edif\w{1}cio:|Ed|Ed\.|Ed:)\s(\w+\s\w+)(?!\n)'
        regex_condominio_tres_palavras = r'(?i)(Condom\w{1}nio|Condom\w{1}nio:|Cond|cond\.|Cond:)\s(\w+\s\w+\s\w+)(?!completo|completíssimo|\n)'
        regex_condominio_duas_palavras = r'(?i)(Condom\w{1}nio|Condom\w{1}nio:|Cond|cond\.|Cond:)\s(\w+\s\w+)(?!completo|completíssimo|\n)'
        regex_condominio_uma_palavra = r'(?i)(Condom\w{1}nio|Condom\w{1}nio:|Cond|cond\.|Cond:)\s(\w+)(?!completo|completíssimo|\n)'
        regex_predio = r'(?i)(Pr\w{1}dio|Pr\w{1}dio:|Pred|Pred\.|Pred:)\s(\w+\s\w+)(?!\n)'
        regex_residence = r'(?i)(\w+)\s(Residence)(?!\n)'
        regex_village_uma_palavra = r'(?i)Village\s(\w+)(?!\n)'
        if re.search(regex_torre_duas_palavras, description):
            building_name = re.search(regex_torre_duas_palavras, description).group()
        elif re.search(regex_torre_uma_palavra, description):
            building_name = re.search(regex_torre_uma_palavra, description).group()
        elif re.search(regex_edificio, description):
            building_name = re.search(regex_edificio, description).group()
        elif re.search(regex_condominio_tres_palavras, description):
            building_name = re.search(regex_condominio_tres_palavras, description).group()
        elif re.search(regex_condominio_duas_palavras, description):
            building_name = re.search(regex_condominio_duas_palavras, description).group()
        elif re.search(regex_condominio_uma_palavra, description):
            building_name = re.search(regex_condominio_uma_palavra, description).group()
        elif re.search(regex_predio, description):
            building_name = re.search(regex_predio, description).group()
        elif re.search(regex_residence, description):
            building_name = re.search(regex_residence, description).group()
        elif re.search(regex_village_uma_palavra, description):
            building_name = re.search(regex_village_uma_palavra, description).group()
    except Exception as e:
        logging.info(repr(e))
    return building_name


def get_neighborhood(driver):
    neighborhood = ''
    try:
        neighborhood_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[2]/div/nav/ol/li[4]/a'
        neighborhood = driver.find_element(By.XPATH, neighborhood_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return neighborhood


def get_floor_size(driver):
    floor_size = 0
    try:
        floor_size_xpath = '//p[@itemprop="floorSize"]'
        floor_size = driver.find_element(By.XPATH, floor_size_xpath).text
        floor_size = int(floor_size.split()[0])
    except Exception as e:
        logging.info(repr(e))
    return floor_size


def get_bedroom(driver):
    bedroom = 0
    try:
        bedroom_xpath = '//p[@itemprop="numberOfRooms"]'
        bedroom = driver.find_element(By.XPATH, bedroom_xpath).text
        bedroom = int(bedroom.split()[0])
    except Exception as e:
        logging.info(repr(e))
    return bedroom


def get_bathroom(driver):
    bathroom = 0
    try:
        bathroom_xpath = '//p[@itemprop="numberOfBathroomsTotal"]'
        bathroom = driver.find_element(By.XPATH, bathroom_xpath).text
        bathroom = int(bathroom.split()[0])
    except Exception as e:
        logging.info(repr(e))
    return bathroom


def get_toilet(driver):
    toilet = ''
    try:
        description_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/section/div[2]/div/div'
        description = driver.find_element(By.XPATH, description_xpath).text
        regex_lavabo = r'(?i)Lavabo'
        if re.search(regex_lavabo, description):
            toilet = 'Sim'
    except Exception as e:
        logging.info(repr(e))
    return toilet


def get_suite(driver):
    suite = ''
    try:
        description_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/section/div[2]/div/div'
        description = driver.find_element(By.XPATH, description_xpath).text
        regex_number_of_suite = r'(?i)(\d+)\s(Suite|Suíte)'
        regex_suite = r'(?i)(Suite|Suíte)'
        if re.search(regex_number_of_suite, description):
            suite = re.search(regex_number_of_suite, description).group(1)
            suite = int(suite.split()[0])
        elif re.search(regex_suite, description):
            suite = 1
    except Exception as e:
        logging.info(repr(e))
    return suite


def get_balcony(driver):
    balcony = ''
    try:
        balcony_xpath = '//p[@itemprop="balcony"]'
        driver.find_element(By.XPATH, balcony_xpath)
        balcony = 'Sim'
    except Exception as e:
        try:
            description_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/section/div[2]/div/div'
            description = driver.find_element(By.XPATH, description_xpath).text
            regex_sacada = r'(?i)(Varanda|Sacada)'
            if re.search(regex_sacada, description):
                balcony = 'Sim'
        except Exception as e:
            logging.info(repr(e))
    return balcony


def get_gourmet_balcony(driver):
    gourmet_balcony = ''
    try:
        gourmet_balcony_xpath = '//p[@itemprop="gourmetBalcony"]'
        driver.find_element(By.XPATH, gourmet_balcony_xpath)
        gourmet_balcony = 'Sim'
    except Exception as e:
        try:
            description_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/section/div[2]/div/div'
            description = driver.find_element(By.XPATH, description_xpath).text
            regex_varanda_gourmet = r'(?i)(Varanda|Sacada)\s(Gourmet)'
            if re.search(regex_varanda_gourmet, description):
                gourmet_balcony = 'Sim'
        except Exception as e:
            logging.info(repr(e))
    return gourmet_balcony


def get_floor(driver):
    floor = ''
    try:
        floor_xpath = '//p[@itemprop="floorLevel"]'
        floor = driver.find_element(By.XPATH, floor_xpath).text
    except Exception as e:
        try:
            description_xpath = '/html/body/div[2]/div[1]/div[1]/div[2]/section/div[2]/div/div'
            description = driver.find_element(By.XPATH, description_xpath).text
            regex_floor_number = r'(?i)(\d+(?:º|o){1,})\s(Andar|andar)'
            regex_floar_high = r'(?i)(Andar|andar)\s(Alto|alto)'
            if re.search(regex_floor_number, description):
                floor = re.search(regex_floor_number, description).group()
            elif re.search(regex_floar_high, description):
                floor = re.search(regex_floar_high, description).group()
        except Exception as e:
            logging.info(repr(e))
    return floor


def get_condo_fee_price(driver):
    condo_fee_price = ''
    try:
        condo_fee_price_xpath = '//*[@id="condo-fee-price"]'
        condo_fee_price = driver.find_element(By.XPATH, condo_fee_price_xpath).text
        condo_fee_price = int(condo_fee_price.replace('R$','').replace('.','').split()[0])
    except Exception as e:
        condo_fee_price = ''
        logging.info(repr(e))
    return condo_fee_price


def get_IPTU_price(driver):
    IPTU_price = ''
    try:
        IPTU_price_xpath = '//*[@id="iptu-price"]'
        IPTU_price = driver.find_element(By.XPATH, IPTU_price_xpath).text
        IPTU_price = int(IPTU_price.replace('R$','').replace('.','').split()[0])
    except Exception as e:
        IPTU_price = ''
        logging.info(repr(e))
    return IPTU_price


def get_price(driver):
    price = ''
    try:
        price_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[3]/div/div[1]/div[1]/p[2]'
        price = driver.find_element(By.XPATH, price_xpath).text
        price = price.replace('R$','').replace('.','').split()[0].replace(' ','')
    except Exception as e:
        price = ''
        logging.info(repr(e))
    return price


def get_details_content_info(driver):
    details_content_info = ''
    try:
        details_content_info_xpath = '/html/body/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div'
        details_content_info = driver.find_element(By.XPATH, details_content_info_xpath).text
    except Exception as e:
        logging.info(repr(e))
    return details_content_info


def fetch(index, link):
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    time.sleep(2)
    driver.get(link)
    close_cookies_policy_popup(driver)
    expand_all_features(driver)

    garage = get_garage(driver)
    pool = get_pool(driver)
    address = get_address(driver)
    building_name = get_building_name(driver)
    neighborhood = get_neighborhood(driver)
    floor_size = get_floor_size(driver)
    bedroom = get_bedroom(driver)
    bathroom = get_bathroom(driver)
    toilet = get_toilet(driver)
    suite = get_suite(driver)
    balcony = get_balcony(driver)
    gourmet_balcony = get_gourmet_balcony(driver)
    floor = get_floor(driver)
    condo_fee_price = get_condo_fee_price(driver)
    IPTU_price = get_IPTU_price(driver)
    price = get_price(driver)
    details_content_info = get_details_content_info(driver)
    driver.close()

    row = f'{garage};"{pool}";"{address}";"{building_name}";"{neighborhood}";{floor_size};{bedroom};{bathroom};"{toilet}";{suite};"{balcony}";"{gourmet_balcony}";"{floor}";{condo_fee_price};{IPTU_price};{price};"{details_content_info}";{link}'
    write_row_in_file(row)
    if index%10 == 0:
        print('...', end='')
        print(index, end='')

    # print(f'garagem: {garage}')
    # print(f'Piscina: {pool}')
    # print(f'Endereço: {address}')
    # print(f'Condomínio: {building_name}')
    # print(f'Bairro: {neighborhood}')
    # print(f'Área privativa: {floor_size}')
    # print(f'Quarto: {bedroom}')
    # print(f'Banheiro: {bathroom}')
    # print(f'Lavabo: {toilet}')
    # print(f'Suíte: {suite}')
    # print(f'Sacada: {balcony}')
    # print(f'Sacada Gourmet: {gourmet_balcony}')
    # print(f'Andar: {floor}')
    # print(f'Valor condomínio: {condo_fee_price}')
    # print(f'IPTU: {IPTU_price}')
    # print(f'Preço: {price}')
    # print(f'Observação: {details_content_info}')


service = Service()
options = webdriver.ChromeOptions()
options.add_argument('--disable-notifications')
options.add_argument('--disable-geolocation')
create_file()
APARTMENT_LINKS_FILE = 'apartment_links_001.txt'
print('Start run!')
try:
    with open(APARTMENT_LINKS_FILE, 'r') as apartment_links_file:
        for index, link in enumerate(apartment_links_file):
            fetch(index, link)
except Exception as e:
    logging.critical(e)

"""
closet          = ''
service_area    = ''
dependence_maid = ''
party_room      = ''
sports_court    = ''
playground      = ''
gym             = ''



<div class="description__content--text false" data-testid="description-content">
"""
