import csv
import pandas as pd
import random


def album():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0610lottery.csv', encoding='utf-8', header=0)
    for row in df.iterrows():
        total = total + row[1]['numbers']
        

    for row in df.iterrows():
        num = []
        times = row[1]['numbers']
        while(times > 0):
            temp = random.randint(1, 90)
            if temp not in memo:
                memo.add(temp)
                num.append(temp)
                times = times - 1
        lottery[row[1]['id']] = num
    with open('./results/0610_album_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)
    


def polariod():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0527_polariod_lottery.csv', encoding='utf-8', header = 0)
    for row in df.iterrows():
        print(row)
        total = total + row[1]['numbers']
    
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
    with open('./results/0527_polariod_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)

def photo():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0527_photo_lottery.csv', encoding='utf-8', header = 0)
    for row in df.iterrows():
        print(row)
        total = total + row[1]['numbers']
    
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
    with open('./results/0527_photo_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)

def basic30r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0715_30_lottery.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        print(row[1])
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
    with open('./results/0715_30_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)

def basic80r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0715_80_lottery.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        #print(row[1])
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
    with open('./results/0715_80_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)



def basic150r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0715_150_lottery.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        #print(row[1])
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
    with open('./results/0715_150_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)



def basic300r():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('./intermediate/0715_300_lottery.csv', encoding='utf-8', header = 0)
    #print(df.head())
    for row in df.iterrows():
        #print(row[1])
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
    with open('./results/0715_300_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in lottery.items():
            writer.writerow(row)

if __name__=='__main__':
    basic300r()
