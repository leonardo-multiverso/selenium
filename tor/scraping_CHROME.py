from selenium import webdriver

proxy_http = "127.0.0.1:9050"

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5://' + proxy_http)

driver = webdriver.Chrome('/opt/chromedriver', options=options)

#driver.get("https://www.whatsmyip.org/")
driver.get("https://www.multiversobi.com.br/")