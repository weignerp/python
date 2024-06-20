# download json from https://data.sec.gov/api/xbrl/companyfacts/CIK${0001490281}.json
# where variable is int the brackets
# the content is in json format
# result in dir comapny_facts
# the name of the file is CIK${0001490281}.json

import json
from urllib import response
from fake_useragent import UserAgent

import requests


COMPANY_FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK"
FOLDER = "D:/workspace/vscode-workspace/python/python/sec/model/model/company_facts"


# https://data.sec.gov/api/xbrl/companyconcept/CIK0001490281/us-gaap/AccountsPayableCurrent.json
# https://data.sec.gov/api/xbrl/frames/us-gaap/AccountsPayableCurrent/USD/CY2019Q1I.json
def get_company_facts(cik):
    try:
        ua = UserAgent()
        response_data = requests.get(
            COMPANY_FACTS_URL + cik + ".json", headers={"User-Agent": ua.chrome}
        )
    except Exception as e:
        print(f"Error: {e}")
        return None

    try:
        data = response_data.text
    except Exception as e:
        print(f"Error: {e}")
        return None

    try:
        json_data = json.loads(data)
    except Exception as e:
        print(f"Error: {e}")
        return None

    return json_data


def save_company_facts(cik, json_data):
    if json_data is None:
        print("JSON data is None, cannot save.")
        return

    file_path = FOLDER + "/" + cik + ".json"
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(json_data, file, indent=4)
    except Exception as e:
        print(f"Error saving JSON data to {file_path}: {e}")
    else:
        print(f"JSON data saved to {file_path}")


def main():
    CIK = "0001490281"
    data = get_company_facts(CIK)
    save_company_facts(CIK, data)


if __name__ == "__main__":
    main()
