import logging

import requests
from django.conf import settings

from core.consts.currencies import ERC20_ULC_CURRENCIES
from core.currency import Currency
from lib.services.etherscan_client import EtherscanClient

log = logging.getLogger(__name__)

class UltronscanClient(EtherscanClient):
    def __init__(self):
        self.url = 'https://scan.ultronsmartchain.io/api?'

    def _make_request(self, uri=''):
        res = {}
        try:
            res = requests.get(f'{self.url}{uri}')  # Removed API key from URL
            res = res.json()
        except Exception as e:
            log.exception('Can\'t fetch data from Ultronscan')  # Updated error log message
        return res

    def get_token_params(self, currency_code):
        return ERC20_ULC_CURRENCIES.get(Currency.get(currency_code))

