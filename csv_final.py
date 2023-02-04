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
from main_exec import exec

file_name = "all_csv_only_fang_final_rate_591_20221225_29_thread_all.csv"

if __name__ == '__main__':

    if os.path.exists(file_name):
        os.remove(file_name)

    # init final output file
    with open(file_name, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["fange", "url", "price", "city", "before_mean", "after_mean", "before_after_rate", "interest"])

    with open("all_csv_only_fang_20221225_591.csv", 'r', encoding="utf-8") as r:

        # get input data
        reader = csv.reader(r)
        input_list = []
        for c, i in enumerate(reader):
            if not i:
                continue
            input_list.append(i)
    
        for inp in input_list:
            inp[0] = inp[0].replace("｡", "").replace("・", "")

        # execute and save output
        exec_threads = [threading.Thread(target=exec, args = (i,), daemon=False) for i in input_list]
        for x in exec_threads:
            while threading.active_count() > 20:
                time.sleep(random.randint(1,5))
            x.start()
