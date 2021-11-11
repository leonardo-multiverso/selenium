from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from parsel import Selector
import csv

arquivo = csv.writer(open('output.csv', 'w', encoding='utf-8'))
arquivo.writerow(['Produto', 'Preco', 'Link'])

driver = webdriver.Firefox()

driver.get('https://mercadolivre.com.br/')

busca = driver.find_element_by_name('as_word')
busca.send_keys('batata')
busca.send_keys(Keys.RETURN)
sleep(4)

driver.find_element_by_class_name('andes-tooltip-button-close').click()
driver.find_element_by_class_name('andes-checkbox__mimic').click()

produtos = driver.find_elements_by_xpath('//div[@class="ui-search-item__group ui-search-item__group--title"]/a')
produtos = [produto.get_attribute('href') for produto in produtos]

cont = 0
for produto in produtos:
    driver.get(produto)
    sleep(2)

    response = Selector(text=driver.page_source)
    nome = response.xpath('//h1/text()').extract()[0]
    inteiro = response.xpath('//span[@class="price-tag-fraction"]/text()').extract()[0]
    centavo = response.xpath('//span[@class="price-tag-cents"]/text()').extract()[0]
    arquivo.writerow([nome, inteiro + ',' + centavo, produto])
    cont += 1
    if cont >= 10:
        break

# driver.close()