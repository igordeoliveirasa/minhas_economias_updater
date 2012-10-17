from selenium import webdriver
import time
from appscript import app
import sys
import arguments_parser
import banco_do_brasil_navigator
import minhas_economias_navigator

if __name__ == "__main__":
    arguments = arguments_parser.parse_args()

    bb_navigator = banco_do_brasil_navigator.Navigator()
    bb_navigator.execute_login(arguments.bank_branch, arguments.bank_account, arguments.bank_password)
    transactions_file_path = bb_navigator.export_transactions(arguments.download_directory_path)
    bb_navigator.close()

    minhas_economias_navigator = minhas_economias_navigator.Navigator()
    minhas_economias_navigator.execute_login(arguments.minhas_economias_user, arguments.minhas_economias_password)
    minhas_economias_navigator.import_transaction_file(transactions_file_path)
    minhas_economias_navigator.close()