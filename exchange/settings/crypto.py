import os

from django.utils import timezone

from exchange.settings import env

CRYPTO_TESTNET = False
FORCE_WALLET_ADDRESS_GENERATE = False

BTC_SAFE_ADDR = env('BTC_SAFE_ADDR')

ETH_SAFE_ADDR = env('ETH_SAFE_ADDR')


BTC_BLOCK_GENERATION_TIME = 5 * 60.0
BTC_NODE_CONNECTION_RETRIES = 5
SAT_PER_BYTES_UPDATE_PERIOD = 120  # 2min
SAT_PER_BYTES_MIN_LIMIT = 3
SAT_PER_BYTES_MAX_LIMIT = 60
SAT_PER_BYTES_RATIO = 1


# Ethereum & ERC
WEB3_INFURA_API_KEY = env('INFURA_API_KEY', default='')
WEB3_INFURA_API_SECRET = env('INFURA_API_SECRET', default='')
ETH_CHAIN_ID = 1  # 3 for Ropsten
ETH_TX_GAS = 21000
ETH_BLOCK_GENERATION_TIME = 15.0
ETH_ERC20_ACCUMULATION_PERIOD = 60.0
ETH_GAS_PRICE_UPDATE_PERIOD = 30
ETH_GAS_PRICE_COEFFICIENT = 0.1
ETH_MAX_GAS_PRICE = 200000000000  # wei
ETH_MIN_GAS_PRICE = 20000000000  # wei

ETHERSCAN_KEY = env('ETHERSCAN_KEY', default='')

LATEST_ADDRESSES_REGENERATION = timezone.datetime(2021, 1, 28, 11, 20)

CRYPTO_KEY_OLD = env('CRYPTO_KEY_OLD', default='')
CRYPTO_KEY = env('CRYPTO_KEY', default='')

# Infura auto client setup
os.environ['WEB3_INFURA_API_KEY'] = WEB3_INFURA_API_KEY
os.environ['WEB3_INFURA_API_SECRET'] = WEB3_INFURA_API_SECRET
os.environ['WEB3_INFURA_SCHEME'] = 'https'

MIN_COST_ORDER_CANCEL = 0.0000001