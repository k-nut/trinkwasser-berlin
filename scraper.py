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


def main():
    download_data()


if __name__ == "__main__":
    main()
