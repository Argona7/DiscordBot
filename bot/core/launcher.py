import sys
import os
import asyncio

from art import text2art
from termcolor import colored, cprint
from bot.utils import ProfileDatabase, logger, get_data_from_file, accounts_to_excel, transform_profile_to_wallet, detect_type_of_value, get_folders_in_directory
from bot.config import settings

def print_banner():
    cprint(text2art("DISCORD BOT"), color="magenta")

    print(
        f"{colored('Argona <crypto/> moves:', color='light_yellow')} "
        f"{colored('https://t.me/ArgonaResearch', color='light_green')}"
    )


    print('''-> Choose Option to continue (1/2/3/4):
        1. Run bot
        2. Register profiles
        3. Register profiles from txt
        4. Save profiles to spreadsheet
        ''')

async def process() -> None:
    from bot.core import register_profiles, register_profiles_from_txt

    print_banner()
    while True:
        action = input("-> ")

        if not action.isdigit():
            logger.warning("Option must be number")
        elif action not in ["1", "2", "3", "4"]:
            logger.warning("Option must be 1 or 2 or 3 or 4")
        else:
            action = int(action)
            break



    db = ProfileDatabase()
    profiles_db: list = await db.get_profiles()

    if action == 1:
        if profiles_db:
            transformed_profiles = transform_profile_to_wallet(profiles_db)
            profiles_farm: list = get_data_from_file('farm')
            profile_type = detect_type_of_value(profiles_farm)
            valid_profiles = []

            for i in range(len(transformed_profiles)):
                if profile_type == 'address':
                    if transformed_profiles[i][0] in profiles_farm:
                        valid_profiles.append(profiles_db[i])
                elif profile_type == 'private_key':
                    if transformed_profiles[i][1] in profiles_farm:
                        valid_profiles.append(profiles_db[i])

                else:
                    sys.exit(logger.error("Invalid profiles type in farm.txt"))


            await run_profiles(valid_profiles, db)

        else:
            sys.exit(logger.error("No profiles found. Please register profiles first."))

    elif action == 2:
        await register_profiles(db)

    elif action == 3:
        await register_profiles_from_txt(db)

    elif action == 4:
        if accounts_to_excel(profiles_db):
            logger.success("Profiles successfully saved to spreadsheet!")


async def run_profiles(profiles: list, db: ProfileDatabase) -> None:
    from bot.core import start

    tasks = []
    semaphore = asyncio.Semaphore(settings.MAX_THREADS)

    for profile in profiles:
        tasks.append(asyncio.create_task(start(profile, db, semaphore)))

    await asyncio.gather(*tasks)


