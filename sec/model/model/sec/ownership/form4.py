import json
import datetime
from xsdata.models.datatype import XmlDate
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.parsers.config import ParserConfig
from dataclasses import asdict
from ownership5_document import OwnershipDocument


XML_DOC = "e:/Můj disk/investice/_documents/sec_tech_spec/edgar_ownership/schema/samples/wk-form4_1718743112.xml"


def load_xml_to_dataclass(file_path: str):
    config = ParserConfig(fail_on_unknown_properties=False)
    parser = XmlParser(config=config)

    # Parse the XML file into the OwnershipDocument dataclass
    with open(file_path, "r", encoding="utf-8") as file:
        xml_content = file.read()
    ownership_document = parser.from_string(xml_content, OwnershipDocument)
    return ownership_document


def dataclass_to_dict(dataclass_instance):
    data = asdict(dataclass_instance)
    k = get_all_keys(data)
    print(list(k))
    return json.loads(json.dumps(data, default=str))


def save_json_to_file(data, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, default=serialize_datetime)
    print(f"JSON data saved to {file_path}")


def serialize_datetime(obj):
    if isinstance(obj, datetime.datetime):
        print("Datetime")
        return obj.isoformat()
    elif isinstance(obj, XmlDate):
        print("XmlDate")
        return obj.get_date().isoformat()
    raise TypeError("Type not serializable")


def get_all_keys(d, parent_key="", sep="."):
    keys = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        keys.append(new_key)
        if isinstance(v, dict):
            keys.extend(get_all_keys(v, new_key, sep=sep))
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    keys.extend(get_all_keys(item, f"{new_key}[{i}]", sep=sep))
    return keys


def main():
    ownership_document = load_xml_to_dataclass(XML_DOC)
    data = dataclass_to_dict(ownership_document)
    # save_json_to_file(data, "d:/ownership_document.json")
    # print(type(ownership_document.period_of_report))
    exit()
    print(ownership_document.issuer.issuer_name)
    print(ownership_document.issuer.issuer_trading_symbol)
    for ro in ownership_document.reporting_owner:
        print(ro.reporting_owner_id.rpt_owner_cik)
        print(ro.reporting_owner_id.rpt_owner_name)
        print(ro.reporting_owner_relationship)


if __name__ == "__main__":
    main()
