# This script is for debugging/development

import logging

from turtlecoin.wallet import TurtleCoinWallet

logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

wallet = TurtleCoinWallet(password='test')
balance = wallet.get_balance()
print(balance)
