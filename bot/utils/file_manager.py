import os
import shutil
import openpyxl
from pathlib import Path
from typing import Union
from bot.config import settings
from bot.utils import logger

def get_data_from_file(name: str) -> Union[list[str], None]:
    file_path = os.path.join(os.path.join(Path(__file__).parent.parent.parent, "data"), f"{name}.txt")
    if not os.path.exists(file_path):
        open (file_path, 'a').close()
        return []
    else:
        clean_empty_lines(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            pk_list = file.readlines()
            pk_list = [pk.strip() for pk in pk_list]

        return pk_list if pk_list else []


def save_invalid_accounts(invalid_accounts: list) -> None:
    file_path = os.path.join(os.path.join(Path(__file__).parent.parent.parent, "logs"), "invalid_accounts.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        for account in invalid_accounts:
            file.write(f"{account}\n")

def remove_directory(name: str) -> bool:
    dir_path = os.path.join(settings.PATH_TO_PROFILES, name)
    if os.path.isdir(dir_path):
        try:
            shutil.rmtree(dir_path)
            return True
        except Exception as e:
            logger.error("Error while removing directory: ", e)
            return False
    else:
        return True

def get_folders_in_directory(path) -> list[str]:
    return [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]

def append_addresses_to_farm(account: str) -> None:
    file_path = os.path.join(os.path.join(Path(__file__).parent.parent.parent, "data"), f"farm.txt")
    clean_empty_lines(file_path)
    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(account + "\n")

def clean_empty_lines(file_path: str) -> None:
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        cleaned_lines = [line for line in lines if line.strip()]
        file.seek(0)
        file.writelines(cleaned_lines)
        file.truncate()

def accounts_to_excel(accounts: list) -> bool:
    data = [("name", "path", "proxy", "user_agent", "wallet_address", "wallet_private_key", "password", "status"), *accounts]

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Profiles"

    for row in data:
        ws.append(row)

    try:
        file_path = os.path.join(os.path.join(Path(__file__).parent.parent.parent, "data"), "profiles.xlsx")
        if os.path.exists(file_path):
            os.remove(file_path)

        wb.save(file_path)
        return True
    except Exception as e:
        logger.error(f"Error when creating excel spreadsheet: {e}")
        return False

