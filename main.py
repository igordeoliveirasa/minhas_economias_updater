from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
import os
#import urllib2
from appscript import app
from stat import S_ISREG, ST_CTIME, ST_MODE
import sys
from optparse import OptionParser


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



parser = OptionParser()

parser.add_option("--branch", dest="branch",help="Informe sua agencia bancaria")
parser.add_option("--account", dest="account",help="Informe sua conta bancaria")
parser.add_option("--password", dest="password",help="Informe sua senha bancaria")
parser.add_option("--downloaddir", dest="download_dir",help="Informe o diretorio de destino")
parser.add_option("--me_email", dest="me_email",help="Informe o e-mail de cadastro do minhaseconomias.com.br")
parser.add_option("--me_password", dest="me_password",help="Informe a senha de cadastro do minhaseconomias.com.br")
    
(options, args) = parser.parse_args()

if not options.branch:
    raise parser.error("Informe sua agencia bancaria (--branch <valor>)")

if not options.account:
    raise parser.error("Informe sua conta bancaria (--account <valor>)")

if not options.password:
    raise parser.error("Informe sua senha bancaria (--password <valor>)")

if not options.download_dir:
    raise parser.error("Informe o diretorio de destino (--downloaddir \"<valor>\")")

if not options.me_email:
    raise parser.error("Informe o e-mail de cadastro do minhaseconomias.com.br (--me_email \"<valor>\")")

if not options.me_password:
    raise parser.error("Informe a senha de cadastro do minhaseconomias.com.br (--me_password \"<valor>\")")


download_dir = options.download_dir
branch = options.branch
account = options.account
password = options.password

me_email = options.me_email
me_password = options.me_password

if not os.path.isdir(download_dir):
    print "Informe um diretorio para download valido."
    sys.exit(1)



browser = webdriver.Firefox()

'''
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
'''

last_downloaded_file = get_last_downloaded_file(download_dir)
last_downloaded_file_path = os.path.join(download_dir, last_downloaded_file)
print last_downloaded_file_path

browser.get("https://wwws.minhaseconomias.com.br")

time.sleep(10)

elem = browser.find_element_by_name("email")
elem.send_keys(me_email)

elem = browser.find_element_by_id("senha")
elem.send_keys(me_password)

elem = browser.find_element_by_name("OK")
elem.click()

time.sleep(40)


browser.execute_script("AppMessenger.fireEvent('panelchanged', 1);") # transacoes

time.sleep(5)

elem = browser.find_elements_by_xpath("//*[contains(@class,'x-btn x-importar x-btn-noicon')]") # importar
elem[0].click()

elem = browser.find_element_by_xpath("//b[contains(text(),'Avan')]") # avancar
elem.click()

elem = browser.find_element_by_name("file")
elem.send_keys(last_downloaded_file_path)

#elem = browser.find_elements_by_xpath("//input[@type='text'][@size='20'][@autocomplete='off']")
#elem[-3].send_keys(last_downloaded_file_path)



#elem = browser.find_elements_by_xpath("//input[@size='24']") # drop down
#elem[-1].send_keys("CC BB")
elem = browser.find_elements_by_xpath("//*[contains(@class,'x-form-trigger x-form-arrow-trigger')]")
elem[7].click()

app('Firefox').activate()
app('System Events').keystroke('\r')

elem = browser.find_element_by_xpath("//b[contains(text(),'Avan')]") # avancar
elem.click()



#elem = browser.find_elements_by_tag_name("input")
#for i in elem:
#    if i.get_attribute("class") == "x-form-text x-form-field x-form-focus":
#        i.send_keys("CC BB")
#        break
    
#elem.click()

#elem = browser.find_element_by_xpath("//b[contains(text(),'Avan')]") # avancar
#elem.click()


browser.close()
