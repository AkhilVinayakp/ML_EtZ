# test for data gathering
from urllib.parse import urlparse
import requests
import json
import random
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

input_url = "https://www.redfin.com/city/11203/CA/Los-Angeles/filter/sort=lo-days"


parsed_url = urlparse(input_url)
region_id = parsed_url.path.lstrip("/").split("/")[1]

headers = {
    'authority': 'www.redfin.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.7',
    # 'cookie': 'RF_CORVAIR_LAST_VERSION=507.2.0; RF_BROWSER_ID=8LaVONdOS2KLoaxeGJtMIw; RF_BROWSER_ID_GREAT_FIRST_VISIT_TIMESTAMP=2024-01-26T00%3A02%3A21.049208; RF_BID_UPDATED=1; searchMode=1; sortOrder=1; aws-waf-token=dbfa1d11-74d6-4822-838d-85cedb5f010e:HgoAgZE3mjgDAAAA:3BQphAc7wJLbWOQe+N4Lno/z2wufXVzyGAEe/R5m91zy0mvVqC6iewPSfSplBI3R9+7YV0ST88WqDNIEmF9zAd7Zvz3/ue/QEK6YVTNOIzE/Cyf/9XWfOPS6CkgUg3I7fws4Q0lrjyHe/8hEKA04Zk/DbYzKMiSjy46Xnwvf9eOeZbjs12norb0Db+R8bzqNp7KUT398bpNO70mOi2GeJe9sgg==; RF_LAST_NAV=0; RF_MARKET=socal; FEED_COUNT=%5B%22%22%2C%22f%22%5D; RF_VISITED=true; collapsedMapView=1; userPreferences=parcels%3Dtrue%26schools%3Dfalse%26mapStyle%3Ds%26statistics%3Dtrue%26agcTooltip%3Dfalse%26agentReset%3Dfalse%26ldpRegister%3Dfalse%26afCard%3D2%26schoolType%3D0%26viewedSwipeableHomeCardsDate%3D1706256187980; RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A4%2C%22events-touch%22%3Atrue%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D; sortOption=special_blend',
    'referer': 'https://www.redfin.com/city/16904/CA/San-Diego/filter/sort=lo-days',
    'sec-ch-ua': '"Not A(Brand";v="99", "Brave";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
}

url = f"https://www.redfin.com/stingray/api/gis?al=1&include_nearby_homes=true&market=socal&num_homes=350&ord=lo-days&page_number=1&region_id={region_id}&region_type=6&sf=1,2,3,5,6,7&start=0&status=9&uipt=1,2,3,4,5,6,7,8&v=8"

def get_header(conf):
    headers['sec-ch-ua-platform'] = random.choice(conf.get("agents"))
    headers['sec-ch-ua-platform'] = f"{random.choice(conf.get('platform'))}"
    return headers


def load_conf():
    print(f"{Fore.BLUE} Looking for config file")
    if not os.path.exists("configs.json"):
        print(f"{Fore.RED} file not found in directory {os.getcwd()}")
    with open("configs.json") as fp:
        data = json.load(fp)
    print(f"{Fore.GREEN} config file loaded successfully")
    return data


def sent_request():
    conf = load_conf()
    header = get_header(conf)
    print("senting req to", url)
    res = requests.get(url=url, headers=header)
    print(res.status_code)

def stress_test():
    pass


def parse_data(res):
    pass

sent_request()