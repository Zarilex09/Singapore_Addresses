import requests
import pandas as pd
from pandas import json_normalize
import string 
from itertools import chain


access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjEwNTU2LCJ1c2VyX2lkIjoxMDU1NiwiZW1haWwiOiJqaWF5b25nLmxpbkBwcmlzbXBsdXMuc2ciLCJmb3JldmVyIjpmYWxzZSwiaXNzIjoiaHR0cDpcL1wvb20yLmRmZS5vbmVtYXAuc2dcL2FwaVwvdjJcL3VzZXJcL3Nlc3Npb24iLCJpYXQiOjE2ODkxNDk0MjIsImV4cCI6MTY4OTU4MTQyMiwibmJmIjoxNjg5MTQ5NDIyLCJqdGkiOiI5NzYzNjc2NDM4OGRjMTQyMjc0YjA5NDEzNTkxMTU1NSJ9.O0FTvCFBBBI5a4BVqXQrRmd8Om4kiNN1_6FsD6J1Vzg"
expiry_timestamp = "1689408622"

alphabet = string.ascii_lowercase[:27]
directory = {}
temp = []
postal_codes = []

def fill_directory():
    for i in alphabet:
        val = i 
        url = f"https://developers.onemap.sg/commonapi/search?searchVal={val}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
        response = requests.get(url)
        data = response.json()
        entries = data['found']
        pages = data['totalNumPages']
        directory[val.upper()] = (entries,pages)

def fill_postal_codes(start,end):
    #for i in range(start,end):
        #postal_codes.append('0'+str(i))
    for i in range(start,end):
        postal_codes.append(str(i))
    print("done1")

def fill_directory2():
    for i in postal_codes: 
        url = f"https://developers.onemap.sg/commonapi/search?searchVal={i}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
        response = requests.get(url)
        data = response.json()
        entries = data['found']
        pages = data['totalNumPages']
        if pages>0:
            directory[i] = (entries,pages)
            print(i)
    print("done2")

def fill_df():
    for k,v in directory.items():
        print(k)
        val = k
        for i in range(1,v[1]+1):
            url = f"https://developers.onemap.sg/commonapi/search?searchVal={val}&returnGeom=Y&getAddrDetails=Y&pageNum={i}"
            response = requests.get(url)
            data = response.json()
            temp.append(data['results'])
            print(i)
    temp2 = list(chain(*temp))
    df = pd.DataFrame(temp2)
    print(df)
    df.to_excel('output10.xlsx',index=False)

fill_postal_codes(804500,809999)
fill_postal_codes(818900,819999)
fill_postal_codes(820000,825200)
fill_postal_codes(828500,829999)
fill_directory2()
fill_df()

















