from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

proxy_http = "127.0.0.1:9050"

profile = webdriver.FirefoxProfile()
ip, port = proxy_http.split(':')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', ip)
profile.set_preference('network.proxy.socks_port', int(port))

driver = webdriver.Firefox(firefox_profile=profile)

driver.get("https://www.whatsmyip.org/")