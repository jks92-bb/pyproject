import requests
from datetime import datetime, timedelta

def get_yesterday_date():
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    return yesterday_date

def get_character_data(character_name):
    headers = {
        "x-nxopen-api-key": "키값"
    }

    url_string = f"https://open.api.nexon.com/maplestory/v1/id?character_name={character_name}"
    response = requests.get(url_string, headers=headers)

    try:
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as err:
        return f"Error: {err}"

def get_character_basic(ocid, date):
    headers = {
        "x-nxopen-api-key": "키값"
    }

    url_string = f"https://open.api.nexon.com/maplestory/v1/character/basic?ocid={ocid}&date={date}"
    response = requests.get(url_string, headers=headers)

    try:
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as err:
        return f"Error: {err}"

def get_character_stat(ocid, date):
    headers = {
        "x-nxopen-api-key": "키값"
    }

    url_string = f"https://open.api.nexon.com/maplestory/v1/character/stat?ocid={ocid}&date={date}"
    response = requests.get(url_string, headers=headers)

    try:
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as err:
        return f"Error: {err}"
