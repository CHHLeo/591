import csv
import os
import sys
import jieba
#from opencc import OpenCC

txt_files = [f for f in os.listdir('.') if f.endswith('591_fang.csv')]
all_csv = []
for fang in txt_files:
    with open(fang, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        for r in list(reader):
            if not r:
                continue
            for ind in range(len(all_csv)):
                if r[0] == all_csv[ind][0]:
                    all_csv[ind][1] += " / " + r[1]
                    break
            else:
                all_csv.append(r)

with open("all_csv_only_fang_20221225_591.csv", 'w', newline='', encoding="utf-8") as r:
    writer = csv.writer(r)
    for i in all_csv:
        seg_list = jieba.cut(i[0])
        i[0] = " ".join(seg_list)
        writer.writerow(i)
