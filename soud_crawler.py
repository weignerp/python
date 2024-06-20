import os
import csv
import requests
from dataclasses import dataclass
from lxml import html
from icecream import ic


@dataclass
class DataObject:
    url: str
    name: str
    address: str
    rows: list


def load_data_from_csv(file_path):
    data_objects = []
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter="\t")
        for row in csv_reader:
            if len(row) >= 3:
                data_objects.append(
                    DataObject(url=row[0], name=row[1], address=row[2], rows=[])
                )
    return data_objects


def file_exists(file_path):
    try:
        with open(file_path):
            pass
    except FileNotFoundError:
        return False
    return True


def crawl_and_extract(obj):
    response = requests.get(obj.url, verify=False)
    if response.status_code == 200:
        response.encoding = "utf-8"
        data = response.content
        file_name = os.path.join(script_dir, obj.name + ".html")
        # save_file(data, file_name)
        tree = html.fromstring(data.decode("utf-8"))
        div_elements = tree.xpath("//article[@class='article']//div//div")
        extracted_data = []
        for div in div_elements:
            paragraph_elements = div.xpath(".//p")
            for paragraph in paragraph_elements:
                text_content = paragraph.xpath("string()")
                if not text_content is None:
                    if "\xa0" in text_content:
                        text_content = text_content.replace("\xa0", " ")
                    text_content = (
                        text_content.replace("\n", ";").replace("'", "").strip()
                    )
                    if text_content != "":
                        obj.rows.append(text_content)
    else:
        ic(f"Failed to retrieve data from {obj.url}")


script_dir = os.path.dirname(os.path.realpath(__file__))

# Example usage
file_path = os.path.join(script_dir, "data.csv")


def save_to_text_file(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        for obj in data:
            file.write("-----------------\n")
            file.write("url:\t" + obj.url + "\t")
            file.write("name:\t" + obj.name + "\t")
            file.write("address:\t" + obj.address + "\t")
            for item in obj.rows:
                file.write(item + "\n")


def save_file(data, file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(data.decode("utf-8"))


if file_exists(file_path):
    data = load_data_from_csv(file_path)
    for k, obj in enumerate(data):
        ic(f"Extracted data from {obj.url}:")
        crawl_and_extract(data[k])
    save_to_text_file(data, os.path.join(script_dir, "export.txt"))
else:
    ic("File does not exist.")
