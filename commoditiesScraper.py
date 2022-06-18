import requests
import urllib.parse
from bs4 import BeautifulSoup
from datetime import datetime, timezone
import pandas as pd
import random
import time
import csv


START_DATE = input("Enter Start Date value : ")
END_DATE = input("Enter End Date value : ")
SAVE_FORMAT = input("Save Data in CSV(1) format or Excel Sheet(2) Type(1 or 2) : ")
FILE_NAME=input("File Name : ")


# ID used for the AJAX request to get the data
commodityType = {
    "Crude Oil":8849,
    "Brent Oil":8833,
    "Natural Gas":8862,
    "Gold": 8830,
    "Silver": 8836,
    "Copper":8831
}

# Some needed headers to get the request working
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/plain, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest'
}


def create_payload(start, end, interval, type_):
    """
    Generates a string of form-data for the post request
    :param start: string of date in format of 01/01/1990
    :param end: string of date in format of 01/01/1990
    :param interval: "DAILY" or "MONTHLY"
    :param type_: Any key from commodityType
    :return: string
    """

    if not interval or not type_:
        raise RuntimeError("Invalid interval or type_")
    start = urllib.parse.quote(start, safe='')
    end = urllib.parse.quote(end, safe='')
    payload = 'curr_id=' + str(commodityType[type_]) + '&st_date=' + start + \
              '&end_date=' + end + \
              '&interval_sec=Daily' + interval + \
              '&sort_col=date&sort_ord=DESC&action=historical_data'
    return payload


def get_crudeoil_data(start_date, end_date):
    response = requests.post("https://www.investing.com/instruments/HistoricalDataAjax",
                             data=create_payload(start_date, end_date, "DAILY", "Crude Oil"),
                             headers=headers)
    return response.text

def get_brentoil_data(start_date, end_date):
    response = requests.post("https://www.investing.com/instruments/HistoricalDataAjax",
                             data=create_payload(start_date, end_date, "DAILY", "Brent Oil"),
                             headers=headers)
    return response.text

def get_naturalgas_data(start_date, end_date):
    response = requests.post("https://www.investing.com/instruments/HistoricalDataAjax",
                             data=create_payload(start_date, end_date, "DAILY", "Natural Gas"),
                             headers=headers)
    return response.text

def get_gold_data(start_date, end_date):
    response = requests.post("https://www.investing.com/instruments/HistoricalDataAjax",
                             data=create_payload(start_date, end_date, "DAILY", "Gold"),
                             headers=headers)
    return response.text

def get_silver_data(start_date, end_date):
    response = requests.post("https://www.investing.com/instruments/HistoricalDataAjax",
                             data=create_payload(start_date, end_date, "DAILY", "Silver"),
                             headers=headers)
    return response.text

def get_copper_data(start_date, end_date):
    response = requests.post("https://www.investing.com/instruments/HistoricalDataAjax",
                             data=create_payload(start_date, end_date, "DAILY", "Copper"),
                             headers=headers)
    return response.text

# Grab the Raw HTML from the site
crudeoil_data = BeautifulSoup(get_crudeoil_data(START_DATE, END_DATE), 'html.parser')
brentoil_data = BeautifulSoup(get_brentoil_data(START_DATE, END_DATE), 'html.parser')
naturalgas_data = BeautifulSoup(get_naturalgas_data(START_DATE, END_DATE), 'html.parser')
gold_data = BeautifulSoup(get_gold_data(START_DATE, END_DATE), 'html.parser')
silver_data = BeautifulSoup(get_silver_data(START_DATE, END_DATE), 'html.parser')
copper_data = BeautifulSoup(get_copper_data(START_DATE, END_DATE), 'html.parser')

# Used to store the data so we can cleanly insert into the Database.
prices = {}

for row in crudeoil_data.find_all('td', class_="first left bold noWrap"):
    date = datetime.strptime(row.get_text(), '%b %d, %Y').replace(tzinfo=timezone.utc).date().isoformat()
#     print(date)
    price_cr = str(row.find_next_sibling().get_text()).replace(",", "")
    prices[date] = {"Crude Oil": price_cr}
        
for row in brentoil_data.find_all('td', class_="first left bold noWrap"):
    date = datetime.strptime(row.get_text(), '%b %d, %Y').replace(tzinfo=timezone.utc).date().isoformat()    
#     print(date)
    price_b = str(row.find_next_sibling().get_text()).replace(",", "")
    if date not in prices:  # Could be that there are no gold data for the current date. If so, give gold value of null
        prices[date] = {"Brent Oil": price_b}
    else:
        prices[date].update({"Brent Oil": price_b})


for row in naturalgas_data.find_all('td', class_="first left bold noWrap"):
    date = datetime.strptime(row.get_text(), '%b %d, %Y').replace(tzinfo=timezone.utc).date().isoformat()
#     print(date)
    price_ng = str(row.find_next_sibling().get_text()).replace(",", "")
    if date not in prices:  # Could be that there are no gold data for the current date. If so, give gold value of null
        prices[date] = {"Natural Gas": price_ng}

    else:
        prices[date].update({"Natural Gas": price_ng})

        
for row in gold_data.find_all('td', class_="first left bold noWrap"):
    date = datetime.strptime(row.get_text(), '%b %d, %Y').replace(tzinfo=timezone.utc).date().isoformat()
#     print(date)
    price_g = str(row.find_next_sibling().get_text()).replace(",", "")
    if date not in prices:  # Could be that there are no gold data for the current date. If so, give gold value of null
        prices[date] = {"Gold": price_g}

    else:
        prices[date].update({"Gold": price_g})


for row in silver_data.find_all('td', class_="first left bold noWrap"):
    date = datetime.strptime(row.get_text(), '%b %d, %Y').replace(tzinfo=timezone.utc).date().isoformat()    
#     print(date)
    price_s = str(row.find_next_sibling().get_text()).replace(",", "")
    if date not in prices:  # Could be that there are no gold data for the current date. If so, give gold value of null
        prices[date] = {"Silver": price_s}
    else:
        prices[date].update({"Silver": price_s})

for row in copper_data.find_all('td', class_="first left bold noWrap"):
    date = datetime.strptime(row.get_text(), '%b %d, %Y').replace(tzinfo=timezone.utc).date().isoformat()
#     print(date)
    price_co = str(row.find_next_sibling().get_text()).replace(",", "")
    if date not in prices:  # Could be that there are no gold data for the current date. If so, give gold value of null
        prices[date] = {"Copper": price_co}
    
    else:
        prices[date].update({"Copper": price_co})

# print(prices)
commodities=[]
# comm={}
# i=0
for key,val in prices.items():
#             print(val)
#     print(val)
    commodity = {'Date': key}
    commodity.update(val)
    commodities.append(commodity)
if SAVE_FORMAT=="1":
    
    csv_file = FILE_NAME+".csv"
    commodities_columns=["Date","Crude Oil","Brent Oil","Natural Gas","Gold","Silver","Copper"]
    try:

        with open(csv_file, 'w') as csvfile:
            w = csv.DictWriter( csvfile, fieldnames=commodities_columns )
            w.writeheader()
            for com in commodities:
                row = com
                w.writerow(row)
            print("************Done************")
    except IOError:
        print("I/O error")
elif SAVE_FORMAT=="2":
    try:
        df=pd.DataFrame(commodities)
        excel_file = FILE_NAME+".xlsx"
        # print (df)

        df.to_excel(excel_file)
        print("************Done************")
    except IOError:
        print("I/O error")

