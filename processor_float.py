import pandas as pd
import sqlite3
from sqlite3 import Error
import csv



def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    
    return conn

def create_db(conn):
    sql = """CREATE TABLE if NOT EXISTS pk2023(
    id INT NOT NULL,
    name CHAR(255) NOT NULL,
    money INT
    );
    """
    cursor = conn.cursor()
    cursor.execute(sql)

def insert_db(conn, mergePk, mergeId):
    #cursor = conn.cursor()
    for key in mergePk:
        #print(key, mergeId[key], mergePk[key])
        sql = "INSERT INTO pk2023 VALUES(?,?,?)"

        conn.execute(sql,[key, mergeId[key], mergePk[key]])
        conn.commit()

def cleanData(data):
    pkList = {} #tele, money
    idList = {} #tele, id
    
    for row in data.iterrows():
        #print(row[1])
        #print(type(row[1][0]))
        if row[1][2] in idList: # tele number already exist in dict
            value = pkList[row[1][2]]
            value = value + float(row[1][0])
            
            pkList[row[1][2]] = value

        else:
            idList[row[1][2]] = row[1][1]
            #print(float(row[1][0].replace(",","").replace(".","")))
            pkList[row[1][2]] = float(row[1][0])
            
           
    lottery(pkList, idList)
    
    return pkList, idList

def lottery(pkList, idList):
    lotteryList = {} #tele, number
    header = ['tele', 'numbers', 'id', 'money']
    for star in pkList:
        num = []
        #print(pkList[star])
        if(pkList[star] // 300 > 0):
            num.append(pkList[star] // 300)
            num.append(pkList[star] // 150)
            lotteryList[star] = num
    
    with open('0527lottery.csv', 'w', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for l in lotteryList:
            data = [l, lotteryList[l], idList[l], pkList[l]]
            
            writer.writerow(data)
    

if __name__=='__main__':
    data = pd.read_csv(r'files/0527pk.csv', sep=',', header=0, names=['money', 'name', 'tele'], encoding = 'utf-8')
    mergePk, mergeId = cleanData(data)
    conn = create_connection('lynn20230527pk.db')
    if conn is not None:
        create_db(conn)
        insert_db(conn, mergePk, mergeId)
    conn.close()