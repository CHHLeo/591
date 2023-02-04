import csv
from pytrends.request import TrendReq
import sys
import requests
import json
import googlemaps
from statistics import mean
from stem import Signal
from stem.control import Controller
import random
import threading
import time
from datetime import date, timedelta, datetime
from multiprocessing import Manager, Process, Pool, Lock
import os
import pickle

#max_name = "實 價 登錄"
pytrends = TrendReq(tz=-480)
#print(pytrends.trending_searches(pn='united_states'))
print(pytrends.realtime_trending_searches(pn='US'))
sys.exit(0)

max_name = "樂居"
file_name = "all_csv_only_fang_final_rate_591_20221225_29_thread_all.csv"

lock = threading.Lock()
available_proxy_list = list()
cat = 29

# load available proxy list
#with open('available_proxy_list.pickle', 'rb') as f:
#    available_proxy_list = pickle.load(f)

def exec(i):
    global available_proxy_list
    while True:
        try:
            pytrends = TrendReq(tz=-480)
            break
        except Exception as kk:
            time.sleep(random.randint(1,5))
            continue
    g = [max_name]
    g.append(i[0])
    tag0 = False
    tag1 = False
    #random.seed(datetime.now())
    #random.shuffle(available_proxy_list)
    #pytrends.proxies = available_proxy_list
    while True:
        try:
            if not tag0:
                pytrends.build_payload(g, cat=cat, timeframe='today 12-m', geo='TW', gprop='')
                tag0 = True
            if not tag1:
                interest = pytrends.interest_over_time()
                interest_mean = list(interest.mean().items())[1][1]
                tag1 = True

            ll = list(interest.items())[1][1]
            len_ll = len(ll)
            before_mean = sum(list(ll)[:int(len_ll/2)])/len(list(ll)[:int(len_ll/2)])
            after_mean = sum(list(ll)[int(len_ll/2):])/len(list(ll)[int(len_ll/2):])

            if before_mean != 0:
                kok_rate = after_mean/before_mean
            else:
                kok_rate = 99999
            break
        except Exception as kk:
            time.sleep(random.randint(1,5))
            creds = str(random.randint(10000,0x7fffffff)) + ":" + "foobar"
            pytrends.proxies = []
            pytrends.proxies.insert(0 , 'socks5h://{}@localhost:9050'.format(creds))
            continue

    i.append(before_mean)
    i.append(after_mean)
    i.append(kok_rate)
    i.append(interest_mean)

    # save data
    lock.acquire()
    with open(file_name, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(i)

    with open(file_name, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        lines= len(list(reader))
        print(lines)
    lock.release()
