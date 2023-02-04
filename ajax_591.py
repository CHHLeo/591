import requests
from bs4 import BeautifulSoup
import re
import sys
import json
import time
import os
import csv
from pytrends.request import TrendReq
import googlemaps
from datetime import datetime
from stem import Signal
from stem.control import Controller
import math
import re

headers = {
"Host": "newhouse.591.com.tw",
"Connection": "keep-alive",
"sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
"Accept": "*/*",
"X-Requested-With": "XMLHttpRequest",
"sec-ch-ua-mobile": "?0",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Dest": "empty",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
"Cookie": "webp=1; PHPSESSID=27e0ca462adc3e6638af33c3445a51af; T591_TOKEN=27e0ca462adc3e6638af33c3445a51af; tw591__privacy_agree=0; regionCookieId=3; user_index_role=1; user_browse_recent=a%3A5%3A%7Bi%3A0%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A1%3Bs%3A7%3A%22post_id%22%3Bs%3A8%3A%2210768327%22%3B%7Di%3A1%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A9252799%3B%7Di%3A2%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A9211619%3B%7Di%3A3%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A9211789%3B%7Di%3A4%3Ba%3A2%3A%7Bs%3A4%3A%22type%22%3Bi%3A2%3Bs%3A7%3A%22post_id%22%3Bi%3A9014682%3B%7D%7D; bid[pc][101.10.94.95]=3126; urlJumpIp=1; urlJumpIpByTxt=%E5%8F%B0%E5%8C%97%E5%B8%82; 591_new_session=eyJpdiI6ImFidWx0OWo5MHE4QW5XWmxcL3J5dE5RPT0iLCJ2YWx1ZSI6Iklqa3RPWDdtXC9lTCtlVnFtSmFOZXQ4WmRxK3E3M2xNUkplVXkweGg0RnZtVGc5ZHhhMlIybVI0U1wvUTdBcUxDOHJHQjNjZDE0Y2NqSUYzNEtXdXRBV2c9PSIsIm1hYyI6ImE0MTBkZTQ5ZWRkZWY4MmFhOWU5Mzk1YTMzYjk1ODA1MWFkNDE0OTc5NmExODg3NTVjZmI0ZmFjZTY4NjZkYWQifQ%3D%3D",
}

detail_headers = {
"Accept": "*/*",
"Accept-Encoding": "gzip, deflate, br",
"Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6",
"Connection": "keep-alive",
"Host": "bff.591.com.tw",
"Origin": "https://newhouse.591.com.tw",
"Referer": "https://newhouse.591.com.tw/",
"Sec-Fetch-Dest": "empty",
"Sec-Fetch-Mode": "cors",
"Sec-Fetch-Site": "same-site",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
"device": "pc",
"deviceid": "usabuflo3ik72h3kimovm1vuq1",
"sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="102"',
"sec-ch-ua-mobile": "?0",
"sec-ch-ua-platform": "Windows",
}

all_index = [['Taipei', '1'],['NewTaipei', '3'],['TaoYuan', '6'],['Kaoshiong', '17'],['jilong', '2']]
list_591 = []
end_date_set = set()
for city in all_index:

    lll = json.loads(requests.get("https://newhouse.591.com.tw/home/housing/search?rid="+city[1]+"&sid=&page=1&bid=3126", headers=headers).text)['data']
    total_count = lll['total']
    pages = math.ceil(total_count/20)
    for page in range(pages):
        while True:
            try:
                lll = json.loads(requests.get("https://newhouse.591.com.tw/home/housing/search?rid="+city[1]+"&sid=&page="+str(page+1)+"&bid=3126", headers=headers).text)['data']
                items = lll['items']
                if not items:
                    continue
                for fang in items:
                    fang_name = fang['build_name']
                    hid = fang['hid']
                    if requests.get("https://newhouse.591.com.tw/home/housing/info?hid="+str(hid), headers=headers).status_code != 200:
                        continue
                    detail_url = "https://bff.591.com.tw/v1/housing/detail-info?id="+str(hid)+"&is_auth=0&bid"
                    price = fang['price']
                    sss = json.loads(requests.get(detail_url, headers=detail_headers).text)
                    end_date = sss['data']['deal_time']['date']
                    if end_date == "時間待定":
                        continue

                    limit_end_date = re.search("20(.*?)年.*", end_date)
                    if limit_end_date != None:
                        limit_end_date = limit_end_date.group(1)
                        if int(limit_end_date) > 23:
                            continue

                    end_date_set.add(end_date)

                    if "~" in str(price):
                        price = float(re.search("(.*)~(.*)", price).group(1))
                    if not isinstance(price, (int, float)):
                        price = 0
                    list_591.append([fang_name, "https://newhouse.591.com.tw/home/housing/info?hid=" + str(hid), price, city])
                break
            except Exception as e:
                print(e)
                print(hid)
                continue

print(len(list_591))
with open("591_fang.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    for i in list_591:
        writer.writerow(i)
