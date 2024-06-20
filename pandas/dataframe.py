import pandas as pd
from icecream import ic
import csv
from dataclasses import dataclass

CVS_PATH = "e:/Můj disk/investice/data/U10524922_20210901_20211231.csv"
# import csv file from local disk
# open in unicode encoding unix format
# columns are separeted by semicolon
# some data are closed in quotation marks
# there are several tables in one CSV file
# the structure could be recognizable by value in the first column
# each strucutre should be louded in its own pandas dataframe


def load_data_from_csv(file_path):
    data_objects = []
    table = {}
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        first_row = None
        header = None
        structures = []
        for row in csv_reader:
            if len(row) <= 3:
                pass
            if first_row is None or first_row != row[0]:
                first_row = row[0]
                table = {"row": row}


def loadCsvFile(filePtah):
    pass


def main():
    loadCsvFile(CVS_PATH)


if __name__ == "__main__":
    main()
