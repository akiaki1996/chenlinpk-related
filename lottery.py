import csv
import pandas as pd
import random
import math



def basic30r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0728_30r.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        if math.isnan(row[1]['numbers']):
            continue
        total = total + row[1]['numbers']
    print(total)
    for row in df.iterrows():
        num = []
        times = row[1]['numbers']
        while(times > 0):
            temp = random.randint(1, total + 1)
            if temp not in memo:
                memo.add(temp)
                num.append(temp)
                times = times - 1
        
        lottery[row[1]['id']] = num
        
    #print(lottery)
    with open('./results/0728_30r_res.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)


def basic50r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0728_50r.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        if math.isnan(row[1]['numbers']):
            continue
        total = total + row[1]['numbers']
    print(total)
    for row in df.iterrows():
        num = []
        times = row[1]['numbers']
        while(times > 0):
            temp = random.randint(1, total + 1)
            if temp not in memo:
                memo.add(temp)
                num.append(temp)
                times = times - 1
        
        lottery[row[1]['id']] = num
        
    #print(lottery)
    with open('./results/0728_50r_res.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)

def basic80r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0728_80r.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        if math.isnan(row[1]['numbers']):
            continue
        total = total + row[1]['numbers']
    print(total)
    for row in df.iterrows():
        num = []
        times = row[1]['numbers']
        while(times > 0):
            temp = random.randint(1, total + 1)
            if temp not in memo:
                memo.add(temp)
                num.append(temp)
                times = times - 1
        
        lottery[row[1]['id']] = num
        
    #print(lottery)
    with open('./results/0728_80r_res.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)


def basic150r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0728_150r.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        if math.isnan(row[1]['numbers']):
            continue
        total = total + row[1]['numbers']
    print(total)
    for row in df.iterrows():
        num = []
        times = row[1]['numbers']
        while(times > 0):
            temp = random.randint(1, total + 1)
            if temp not in memo:
                memo.add(temp)
                num.append(temp)
                times = times - 1
        
        lottery[row[1]['id']] = num
        
    #print(lottery)
    with open('./results/0728_150r_res.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)


def basic300r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0728_300r.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        if math.isnan(row[1]['numbers']):
            continue
        total = total + row[1]['numbers']
    print(total)
    for row in df.iterrows():
        num = []
        times = row[1]['numbers']
        while(times > 0):
            temp = random.randint(1, total + 1)
            if temp not in memo:
                memo.add(temp)
                num.append(temp)
                times = times - 1
        
        lottery[row[1]['id']] = num
        
    #print(lottery)
    with open('./results/0728_300r_res.csv', 'w', newline='',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)







def sunny():
    lottery = {}
    memo = set()
    total = 0
    df = pd.read_csv('./intermediate/0728_200r.csv', encoding='utf-8', header = 0)
    for row in df.iterrows():
        
        if row[1]['money'] >= 200:
            total = total + 1
    print(total)
    for row in df.iterrows():
        #print(lottery)
        if row[1]['money'] >= 200:
            while(True):
                temp = random.randint(1, total)
                if temp not in memo:
                    #print(lottery)
                    memo.add(temp) 
                    lottery[row[1]['id']] = temp
                    break
    print(lottery)
    with open('./results/0728_200r.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)

if __name__=='__main__':
    # basic30r()
    # basic50r()
    # basic80r()
    # basic150r()
    sunny()

