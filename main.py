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
#assert "[bb.com.br]" in browser.title
elem = browser.find_element_by_name("dependenciaOrigem")
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


#req = urllib2.Request('http://www.example.com/')
#r = urllib2.urlopen(req)
#print r.read()

app('Firefox').activate()
app('System Events').keystroke('\r')

#popup = browser.switch_to_alert()
#assert alert.text == 'Server Login Error...'
#popup.accept()


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
# get all entries in the directory w/ stats
#entries = (os.path.join(download_dir, fn) for fn in os.listdir(download_dir))
#entries = ((os.stat(path), path) for path in entries)

# leave only regular files, insert creation date
#entries = ((stat[ST_CTIME], path)
#           for stat, path in entries if S_ISREG(stat[ST_MODE]))
#NOTE: on Windows `ST_CTIME` is a creation date 
#  but on Unix it could be something else
#NOTE: use `ST_MTIME` to sort by a modification date

#for cdate, path in sorted(entries):
#    print time.ctime(cdate), os.path.basename(path)


try:
    
    time.sleep(60)
except NoSuchElementException:
    assert 0, "error"
browser.close()