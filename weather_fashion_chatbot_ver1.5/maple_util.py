import requests
from datetime import datetime, timedelta

def get_yesterday_date():
    yesterday_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    return yesterday_date

def get_character_data(character_name):
    headers = {
        "x-nxopen-api-key": "test_e6f5684cbfb6237d5d3ff8740d5ee712aeb8ddd9ba8877df5e1d291949e7e6a280553df27fa82c9e2a239d36cabd158b"
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
        "x-nxopen-api-key": "test_e6f5684cbfb6237d5d3ff8740d5ee712aeb8ddd9ba8877df5e1d291949e7e6a280553df27fa82c9e2a239d36cabd158b"
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
        "x-nxopen-api-key": "test_e6f5684cbfb6237d5d3ff8740d5ee712aeb8ddd9ba8877df5e1d291949e7e6a280553df27fa82c9e2a239d36cabd158b"
    }

    url_string = f"https://open.api.nexon.com/maplestory/v1/character/stat?ocid={ocid}&date={date}"
    response = requests.get(url_string, headers=headers)

    try:
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as err:
        return f"Error: {err}"
