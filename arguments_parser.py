__author__ = 'igor.sa'

from optparse import OptionParser
import sys, os

KEY_BANK_BRANCH = "BANK_BRANCH"
KEY_BANK_ACCOUNT = "BANK_ACCOUNT"
KEY_BANK_PASSWORD = "BANK_PASSWORD"
KEY_DOWNLOAD_DIRECTORY = "DOWNLOAD_DIRECTORY"
KEY_MINHAS_ECONOMIAS_USER = "MINHAS_ECONOMIAS_USER"
KEY_MINHAS_ECONOMIAS_PASSWORD = "MINHAS_ECONOMIAS_PASSWORD"


class Arguments:
    bank_branch = None
    bank_account = None
    bank_password = None

    download_directory_path = None
    minhas_economias_user = None
    minhas_economias_password = None

def parse_args():
    parser = OptionParser()

    parser.add_option("--branch", dest="branch",help="Informe sua agencia bancaria")
    parser.add_option("--account", dest="account",help="Informe sua conta bancaria")
    parser.add_option("--password", dest="password",help="Informe sua senha bancaria")
    parser.add_option("--download_dir", dest="download_dir",help="Informe o diretorio de destino")
    parser.add_option("--me_user", dest="me_user",help="Informe o e-mail/usuario de cadastro do minhaseconomias.com.br")
    parser.add_option("--me_password", dest="me_password",help="Informe a senha de cadastro do minhaseconomias.com.br")

    (options, args) = parser.parse_args()

    if not options.branch:
        raise parser.error("Informe sua agencia bancaria (--branch <valor>)")

    if not options.account:
        raise parser.error("Informe sua conta bancaria (--account <valor>)")

    if not options.password:
        raise parser.error("Informe sua senha bancaria (--password <valor>)")

    if not options.download_dir:
        raise parser.error("Informe o diretorio de destino (--download_dir \"<valor>\")")

    if not options.me_user:
        raise parser.error("Informe o e-mail/user de cadastro do minhaseconomias.com.br (--me_user \"<valor>\")")

    if not options.me_password:
        raise parser.error("Informe a senha de cadastro do minhaseconomias.com.br (--me_password \"<valor>\")")

    if not os.path.isdir(options.download_dir):
        print "Informe um diretorio para download valido."
        sys.exit(1)

    ret = Arguments()

    ret.bank_branch = options.branch
    ret.bank_account = options.account
    ret.bank_password = options.password

    ret.minhas_economias_user = options.me_user
    ret.minhas_economias_password = options.me_password

    ret.download_directory_path = options.download_dir

    return ret