__author__ = 'igor.sa'

from selenium import webdriver
import time
from appscript import app


class Navigator:
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://wwws.minhaseconomias.com.br")

        time.sleep(10)

    def execute_login(self, user, password):
        elem = self.browser.find_element_by_name("email")
        elem.send_keys(user)

        elem = self.browser.find_element_by_id("senha")
        elem.send_keys(password)

        elem = self.browser.find_element_by_name("OK")
        elem.click()

        time.sleep(40)

    def import_transaction_file(self, transaction_file_path):
        self.browser.execute_script("AppMessenger.fireEvent('panelchanged', 1);") # transacoes

        time.sleep(5)

        elem = self.browser.find_elements_by_xpath("//*[contains(@class,'x-btn x-importar x-btn-noicon')]") # importar
        elem[0].click()

        elem = self.browser.find_element_by_xpath("//b[contains(text(),'Avan')]") # avancar
        elem.click()

        elem = self.browser.find_element_by_name("file")
        elem.send_keys(transaction_file_path)


        elem = self.browser.find_elements_by_xpath("//*[contains(@class,'x-form-trigger x-form-arrow-trigger')]")
        elem[7].click()

        app('Firefox').activate()
        app('System Events').keystroke('\r')

        elem = self.browser.find_element_by_xpath("//b[contains(text(),'Avan')]") # avancar
        elem.click()

        time.sleep(20) # uploading...

        elem = self.browser.find_elements_by_link_text("aqui") # clicking at aqui link
        elem[0].click()

        elem = self.browser.find_elements_by_xpath("//*[contains(text(),'Importar arquivo')]") # clicar no importar arquivo
        elem[-1].click()

        time.sleep(20)

    def close(self):
        self.browser.close()