from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

branch = "xx-x"
account = "xx-x"
password = "xx"

browser = webdriver.Chrome() # Get local session of firefox
browser.get("https://www2.bancobrasil.com.br/aapf/login.jsp?aapf.IDH=sim&perfil=1") # Load page
assert "[bb.com.br]" in browser.title
elem = browser.find_element_by_name("dependenciaOrigem") # Find the query box
elem.send_keys(branch + account + Keys.TAB + password + Keys.RETURN)
try:
    
    time.sleep(60) # Let the page load, will be added to the API
except NoSuchElementException:
    assert 0, "error"
browser.close()