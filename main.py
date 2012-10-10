from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
#import urllib2
from appscript import app
from stat import S_ISREG, ST_CTIME, ST_MODE
import sys



def get_last_downloaded_file(download_dir):
    dirlist = os.listdir(download_dir)
    max_ctime = 0;
    last_downloaded_fp = ""
    for fp in dirlist:
        if os.path.splitext(fp)[1] == ".ofx":
            info = os.stat(os.path.join(download_dir, fp))
            ctime = info[ST_CTIME]
            if max_ctime < ctime:
                max_ctime = ctime
                last_downloaded_fp = fp
    return last_downloaded_fp




download_dir = "/Users/igor/Downloads"
branch = "xx"
account = "xx"
password = "xx"

me_email = "igordeoliveirasa@gmail.com"
me_password = "xx"

browser = webdriver.Firefox()
browser.get("https://www2.bancobrasil.com.br/aapf/login.jsp")
time.sleep(20)
elem.send_keys(branch)

elem = browser.find_element_by_name("numeroContratoOrigem")
elem.send_keys(account)

elem = browser.find_element_by_name("senhaConta")
elem.send_keys(password)

elem = browser.find_element_by_name("botaoEntrar.x")
elem.click()
time.sleep(5)

browser.get("https://www2.bancobrasil.com.br/aapf/extrato/009-00.jsp?ac=sim&disponivelSMS=sim&codigoImagem=27919#ancoraTitulo")
time.sleep(5)

elem = browser.find_element_by_name("dia")
elem.send_keys("1")

elem = browser.find_element_by_xpath('//input[@name="tipoExtrato"][@value="2"]')
elem.click()

elem = browser.find_element_by_name("botaoConfirma.x")
elem.click()

time.sleep(5)


app('Firefox').activate()
app('System Events').keystroke('\r')

time.sleep(5)
last_downloaded_file = get_last_downloaded_file(download_dir)
last_downloaded_file_path = os.path.join(download_dir, last_downloaded_file)
print last_downloaded_file_path

browser.get("https://wwws.minhaseconomias.com.br")

time.sleep(20)

elem = browser.find_element_by_name("email")
elem.send_keys(me_email)

elem = browser.find_element_by_id("senha")
elem.send_keys(me_password)

elem = browser.find_element_by_name("OK")
elem.click()

time.sleep(20)

try:
    
    time.sleep(60)
except NoSuchElementException:
    assert 0, "error"
browser.close()
