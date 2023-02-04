import requests

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
print(requests.get("https://newhouse.591.com.tw/home/housing/info?hid=120031", headers=headers).status_code)
