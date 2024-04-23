from core.currency import CoinParams
from cryptocoins.coins.ulc.connection import get_w3_ultron_connection
from cryptocoins.coins.ulc.consts import ULC, CODE
from cryptocoins.coins.ulc.wallet import ulc_wallet_creation_wrapper, is_valid_ulc_address
from cryptocoins.utils.register import register_coin

w3 = get_w3_ultron_connection()

ULC_CURRENCY = register_coin(
    currency_id=ULC,
    currency_code=CODE,
    address_validation_fn=is_valid_ulc_address,
    wallet_creation_fn=ulc_wallet_creation_wrapper,
    latest_block_fn=lambda currency: w3.eth.get_block_number(),
    blocks_diff_alert=100,
)
