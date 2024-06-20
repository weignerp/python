import json
import xmltodict
import os
import os.path 
from os import path

'''
with open("d://workspace/vscode-workspace/python/python/00001/VYSTUP/DATA/00040088.xml", encoding="UTF-8") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())


print(data_dict.keys())
print(data_dict['are:Ares_odpovedi']['are:Odpoved']['are:Vypis_VREO'].keys())    
['are:Uvod', 'are:Zakladni_udaje', 'are:Statutarni_organ', 'are:Jiny_organ']
# exit(0)

    
# json_data = json.dumps(data_dict['are:Ares_odpovedi']['are:Odpoved']['are:Vypis_VREO'], ensure_ascii=False) ##.encode('utf8')

with open("d://data.json", "w", encoding='utf8') as json_file:
        json.dump(data_dict['are:Ares_odpovedi']['are:Odpoved']['are:Vypis_VREO'], json_file, ensure_ascii=False)
'''        



# dirlist = ['1095000', '1100000', '1105000', '1110000', '1115000', '1120000', '1125000', '1130000', '1135000', '1140000', '1145000']
# dirlist = ['1000000', '1005000', '1010000', '1015000', '1020000', '1025000', '1030000', '1035000', '1040000', '1045000', '1050000', '1055000', '1060000', '1065000', '1070000', '1075000', '1080000', '1085000', '1090000']
# dirlist = ['900000', '905000', '910000', '915000', '920000', '925000', '930000', '935000', '940000', '945000', '950000', '955000', '960000', '965000', '970000', '975000', '980000', '985000', '990000', '995000']
# dirlist = ['800000', '805000', '810000', '815000', '820000', '825000', '830000', '835000', '840000', '845000', '850000', '855000', '860000', '865000', '870000', '875000', '880000', '885000', '890000', '895000']
# dirlist = ['700000', '705000', '710000', '715000', '720000', '725000', '730000', '735000', '740000', '745000', '750000', '755000', '760000', '765000', '770000', '775000', '780000', '785000', '790000', '795000']
# dirlist = ['600000', '605000', '610000', '615000', '620000', '625000', '630000', '635000', '640000', '645000', '650000', '655000', '660000', '665000', '670000', '675000', '680000', '685000', '690000', '695000']
# dirlist = ['500000', '505000', '510000', '515000', '520000', '525000', '530000', '535000', '540000', '545000', '550000', '555000', '560000', '565000', '570000', '575000', '580000', '585000', '590000', '595000']
# dirlist = ['400000', '405000', '410000', '415000', '420000', '425000', '430000', '435000', '440000', '445000', '450000', '455000', '460000', '465000', '470000', '475000', '480000', '485000', '490000', '495000']
# dirlist = ['300000', '305000', '310000', '315000', '320000', '325000', '330000', '335000', '340000', '345000', '350000', '355000', '360000', '365000', '370000', '375000', '380000', '385000', '390000', '395000']
# dirlist = ['200000', '205000', '210000', '215000', '220000', '225000', '230000', '235000', '240000', '245000', '250000', '255000', '260000', '265000', '270000', '275000', '280000', '285000', '290000', '295000']
# dirlist = ['90000', '95000', '100000', '105000', '110000', '115000', '120000', '125000', '130000', '135000', '140000', '145000', '150000', '155000', '160000', '165000', '170000', '175000', '180000', '185000', '190000', '195000']
# dirlist = ['05000', '10000', '15000', '20000', '25000', '30000', '35000', '40000', '45000', '50000', '55000', '60000', '65000', '70000', '75000', '80000', '85000']
for dir_number in dirlist:
    json_dir = 'd:/workspace/clb-eclipse-workspace/asisteam-bi-data/src/data/no-sync/ares_json/' + dir_number    
    dirname = 'd:/workspace/clb-eclipse-workspace/asisteam-bi-data/src/data/no-sync/ares_export/' + dir_number +'/VYSTUP/DATA/'
    sql_file = open('d:/workspace/clb-eclipse-workspace/asisteam-bi-data/src/data/no-sync/ares_json/' + dir_number +'.sql', "w")
    if path.isdir(json_dir) == False:
        os.makedirs(json_dir)

    for root, dirs, files in os.walk(dirname):
        for file_name in files:
            write_sql = True 
            xml_full_filepath = os.path.join(root, file_name)
            file_name_no_ext = file_name.split(".") 
            json_full_filepath = json_dir +'/'+ file_name_no_ext[0] + '.json'
            if path.isfile(json_full_filepath):
                sql = "INSERT INTO ares.tmp_data (zaznam) VALUES (pg_read_binary_file('" + json_full_filepath + "'));\n"
                sql_file.write(sql)                 
                print(f'Skipping converting json file, alerady converted: {json_full_filepath}')
                continue
            # print('Read path:', path)
            try:
                with open(xml_full_filepath, encoding="UTF-8") as xml_file:
                    data_dict = xmltodict.parse(xml_file.read())
            except Exception as e:
                print(f'An exception occurred by file: {xml_full_filepath}\n{e}') 
                sql_file.close()
                exit(0)                       
           
            # print('Filepath:',f)        
            try:
                with open(json_full_filepath, "w", encoding='utf8') as json_file:
                    json.dump(data_dict['are:Ares_odpovedi']['are:Odpoved']['are:Vypis_VREO'], json_file, ensure_ascii=False)              
            except Exception as e:
                print(f'Nelze zkonvertovat soubor: {json_full_filepath}\n{e}')                
                write_sql = False
                # sqlf.close()
                # exit(0)
            if write_sql:
                sql = "INSERT INTO ares.tmp_data (zaznam) VALUES (pg_read_binary_file('" + json_full_filepath + "'));\n"
                sql_file.write(sql)
            # exit(0)
        print(f'Dir done: {dir_number}')
    sql_file.close()
    