import requests
import json
from bs4 import BeautifulSoup

def download_data():
    response =  requests.get("http://www.bwb.de/content/language1/html/1133.php")
    content = response.text
    bs = BeautifulSoup(content)
    table =  bs.table
    data = {}
    for row in table.find_all("tr")[1:]:
        key = row.find_all("td")[0].text.strip()
        value =row.find_all("td")[1].text.strip()
        data[key] = value
    print(json.dumps(data, indent=2))


def download_data_by_postal_code(postal_code):
    payload = {"PLZ": postal_code}
    response = requests.get("http://www.bwb.de/content/language1/html/3255.php", params=payload)
    bs = BeautifulSoup(response.text)
    data_table =  bs.find_all("table")[4]
    key_row = data_table.find_all("tr")[0]
    keys = [content.text.strip() for content in key_row.find_all("td")]
    data = []
    for row in data_table.find_all("tr")[4:-5]:
        datum = {}
        tds = row.find_all("td")
        for i in range(len(keys)):
            datum[keys[i]] = tds[i].text.strip()
        data.append(datum)
    print json.dumps(data, indent=2)

def main():
    #download_data()
    download_data_by_postal_code(10249)


if __name__ == "__main__":
    main()
