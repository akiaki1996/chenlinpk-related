import csv
import pandas as pd
import random


def album():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('0610lottery.csv', encoding='utf-8', header=0)
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

    print(lottery)

    print(random.randint(1, 90))


def polariod():
    total = 0
    lottery = {}
    memo = set()
    df = pd.read_csv('0527lottery.csv', encoding='utf-8', header = 0)
    for row in df.iterrows():
        print(type(row[1]['numbers']))
        total = total + row[1]['numbers'][0]
    print(total)

if __name__=='__main__':
    polariod()
