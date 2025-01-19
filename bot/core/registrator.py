import os.path
import ua_generator


from bot.utils import (
    get_data_from_file, save_invalid_accounts,remove_directory,
    append_addresses_to_farm,generate_evm_wallet,
    get_address_by_private_key,generate_password, ProfileDatabase, logger
)
from bot.config import settings

async def register_profiles_from_txt(db: ProfileDatabase) -> None:
    pk_list = get_data_from_file('register')

    proxy_list = get_data_from_file('proxy') if settings.USE_PROXY else []
    invalid_pk = []

    for i, wallet_private_key in enumerate(pk_list):
        wallet_address =  get_address_by_private_key(wallet_private_key)
        proxy = proxy_list[i] if len(proxy_list) > i else None
        if wallet_address:
            name = wallet_address[:11]
            path = os.path.join(settings.PATH_TO_PROFILES, f"acc_{name}")
            user_agent = str(ua_generator.generate(device='desktop', platform='windows', browser='chrome'))
            password = generate_password()

            if not remove_directory(name):
                invalid_pk.append(f"{wallet_private_key}:{proxy}")
            else:
                append_addresses_to_farm(wallet_address)
                await db.delete_profile_by_name(name)
                await db.add_profile(name, path, proxy, user_agent, wallet_address, wallet_private_key, password, 0)

        else:
            invalid_pk.append(f"{wallet_private_key} {proxy}")

    if invalid_pk:
        logger.warning(f"Invalid private keys found: {len(invalid_pk)}. Check logs for more details")
        save_invalid_accounts(invalid_pk)

    if pk_list:
        logger.success("Profiles successfully added! Run bot to create them")
    else:
        logger.warning("No private keys found")


async def register_profiles(db: ProfileDatabase) -> None:
    print("-> Enter the number of accounts")
    while True:
        action = input("-> ")

        if not action.isdigit():
            logger.warning("Option must be number")
        elif 1 > int(action) > 1000:
            logger.warning("Option must be 1 to 1000")
        else:
            action = int(action)
            break

    proxy_list = get_data_from_file('proxy') if settings.USE_PROXY else []
    invalid_pk = []

    for i in range(action):
        wallet_address, wallet_private_key = generate_evm_wallet()
        name = wallet_address[:11]
        path = os.path.join(settings.PATH_TO_PROFILES, f"acc_{name}")
        proxy = proxy_list[i] if len(proxy_list) > i else None
        user_agent = str(ua_generator.generate(device='desktop', platform='windows', browser='chrome'))
        password = generate_password()

        if not remove_directory(name):
            invalid_pk.append(f"{wallet_private_key} {proxy}")
        else:
            append_addresses_to_farm(wallet_address)
            await db.delete_profile_by_name(name)
            await db.add_profile(name, path, proxy, user_agent, wallet_address, wallet_private_key, password, 0)

    if invalid_pk:
        logger.warning(f"Invalid private keys found: {len(invalid_pk)}. Check logs for more details")
        save_invalid_accounts(invalid_pk)

    logger.success("Profiles successfully added! Run bot to create them")