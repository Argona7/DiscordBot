import os
import string
import random


from web3 import Web3
from eth_keys import keys
# from eth_account import Account
from datetime import datetime
from typing import Union, Tuple
from bot.utils.logger import logger


def generate_evm_wallet() -> Tuple[str,str]:
    private_key = keys.PrivateKey(Web3.keccak(os.urandom(32)))
    address = private_key.public_key.to_checksum_address()


    return address, private_key.to_hex()

def get_address_by_private_key(private_key: str) -> Union[str, None]:
    try:
        private_key = keys.PrivateKey(bytes.fromhex(private_key))
        address = private_key.public_key.to_checksum_address()
        return address

    except ValueError:
        logger.error(f"Invalid private key: {private_key}")
        return None

# def generate_evm_wallet() -> Tuple[str, str]:
#     account = Account.create()
#
#     return account.address, account.key.hex()
#
# def get_address_by_private_key(private_key: str) -> Union[str, None]:
#     try:
#         account = Account.from_key(private_key)
#         return account.address
#
#     except ValueError:
#         logger.error(f"Invalid private key: {private_key}")
#         return None


def generate_password(length: int = 8) -> str:
    all_characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def get_date() -> str:
    now = datetime.now()
    date = now.strftime("%d_%m_%y")
    return date

def transform_profile_to_wallet(profiles: list) -> list:
    transform_profiles = []
    for profile in profiles:
        transform_profiles.append([profile[4], profile[5]])

    return transform_profiles

def detect_type_of_value(profiles: list) -> str:
    profile_types = []
    for profile in profiles:
        if len(profile) == 42:
            profile_types.append('address')
        elif len(profile) == 64:
            profile_types.append('private_key')
        else:
            profile_types.append('name')

    if len(set(profile_types)) == 1:
        return profile_types[0]

    return 'unknown'

