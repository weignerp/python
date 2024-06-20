import json
import xmltodict
import os
import os.path 
from os import path

xml_full_filepath = "d:/data/asisteam/katastr/zmena/KatastrZmena.xml"
json_full_filepath = "d:/data/asisteam/katastr/zmena/KatastrZmena.json"

try:
    with open(xml_full_filepath, encoding="UTF-8") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
except Exception as e:
    print(f'An exception occurred by file: {xml_full_filepath}\n{e}') 
    exit(0)                       

# print('Filepath:',f)        
try:
    with open(json_full_filepath, "w", encoding='utf8') as json_file:
        json.dump(data_dict['Rows'], json_file, ensure_ascii=False)              
except Exception as e:
    print(f'Nelze zkonvertovat soubor: {json_full_filepath}\n{e}')                
    
    # sqlf.close()
    # exit(0)