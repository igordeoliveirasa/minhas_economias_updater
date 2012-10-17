__author__ = 'igor.sa'

from selenium import webdriver
import time
from appscript import app, k
import osutils


class Navigator:
    
    MONTH_JAN = "JAN"
    MONTH_FEB = "FEV"
    MONTH_MAR = "MAR"
    MONTH_APR = "ABR"
    MONTH_MAY = "MAI"
    MONTH_JUN = "JUN"
    MONTH_JUL = "JUL"
    MONTH_AUG = "AGO"
    MONTH_SEP = "SET"
    MONTH_OCT = "OUT"
    MONTH_NOV = "NOV"
    MONTH_DEC = "DEZ"

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


    def export_transactions(self, default_download_dir_path, from_day = None, month = None):
        self.browser.get("https://www2.bancobrasil.com.br/aapf/extrato/009-00.jsp?ac=sim&disponivelSMS=sim&codigoImagem=27919#ancoraTitulo")
        time.sleep(5)

        if from_day == None:
            from_day = "%d" % from_day

        elem = self.browser.find_element_by_name("dia")
        elem.send_keys(from_day)

        elem = self.browser.find_element_by_xpath('//input[@name="tipoExtrato"][@value="2"]')
        elem.click()


        if month != None:
            elem = self.browser.find_element_by_name("mes")
            elem.click()

            app('Firefox').activate()
            app('System Events').keystroke(month)
            app('Firefox').activate()
            app('System Events').keystroke('\r')


        elem = self.browser.find_element_by_name("botaoConfirma.x")
        elem.click()

        time.sleep(20)

        app('Firefox').activate()
        app('System Events').keystroke('\r')

        return osutils.get_last_created_file(default_download_dir_path, ".ofx")

    def close(self):
        self.browser.close()
