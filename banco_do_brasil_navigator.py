__author__ = 'igor.sa'

from selenium import webdriver
import time
from appscript import app
import osutils


class Navigator:
    def __init__(self):
        self.browser = webdriver.Firefox()

        self.browser.get("https://www2.bancobrasil.com.br/aapf/login.jsp")
        time.sleep(20)

    def execute_login(self, branch, account, password):
        elem = self.browser.find_element_by_name("dependenciaOrigem")
        elem.send_keys(branch)

        elem = self.browser.find_element_by_name("numeroContratoOrigem")
        elem.send_keys(account)

        elem = self.browser.find_element_by_name("senhaConta")
        elem.send_keys(password)

        elem = self.browser.find_element_by_name("botaoEntrar.x")
        elem.click()
        time.sleep(5)


    def export_transactions(self, default_download_dir_path):
        self.browser.get("https://www2.bancobrasil.com.br/aapf/extrato/009-00.jsp?ac=sim&disponivelSMS=sim&codigoImagem=27919#ancoraTitulo")
        time.sleep(5)

        elem = self.browser.find_element_by_name("dia")
        elem.send_keys("1")

        elem = self.browser.find_element_by_xpath('//input[@name="tipoExtrato"][@value="2"]')
        elem.click()

        elem = self.browser.find_element_by_name("botaoConfirma.x")
        elem.click()

        time.sleep(20)

        app('Firefox').activate()
        app('System Events').keystroke('\r')

        return osutils.get_last_created_file(default_download_dir_path, ".ofx")

    def close(self):
        self.browser.close()
