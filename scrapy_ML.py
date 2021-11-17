from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector
import csv

arquivo = csv.writer(open('lista.csv', 'w', encoding='utf-8'))
arquivo.writerow(['Produto', 'Valor', 'Loja', 'Link'])

driver = webdriver.Chrome()

def MercadoLivre(driver):
    driver.get('https://mercadolivre.com.br/')

    busca = driver.find_element_by_name('as_word')
    busca.send_keys('adaptador p2')
    busca.send_keys(Keys.RETURN)
    sleep(1)
    url = driver.current_url
    url = url.split('#')[0]
    url += '_Frete_Full_OrderId_PRICE_NoIndex_True'
    
    driver.get(url)

    fonte = Selector(text=driver.page_source)

    if len(fonte.xpath('//div[@class="ui-search-item__group ui-search-item__group--title"]/a').extract()) > 0:
        produtos = driver.find_elements_by_xpath('//div[@class="ui-search-item__group ui-search-item__group--title"]/a')
    else:
        produtos = driver.find_elements_by_xpath('//div[@class="andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core ui-search-result--advertisement andes-card--padding-default andes-card--animated"]/a')

    produtos = [produto.get_attribute('href') for produto in produtos]

    cont = 0
    for produto in produtos:
        driver.get(produto)
        sleep(2)

        response = Selector(text=driver.page_source)
        nome = response.xpath('//h1/text()').extract()[0]
        inteiro = response.xpath('//span[@class="price-tag-fraction"]/text()').extract()[0]
        centavo = response.xpath('//span[@class="price-tag-cents"]/text()').extract()[0]
        if 'loja' not in nome:
            arquivo.writerow([nome, inteiro + ',' + centavo, 'MercadoLivre', produto])
        cont += 1
        if cont >= 20:
            break



if __name__ == '__main__':
    MercadoLivre(driver)
    driver.close()