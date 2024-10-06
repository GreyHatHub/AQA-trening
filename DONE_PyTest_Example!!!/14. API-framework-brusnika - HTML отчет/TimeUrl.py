import requests
import time
import urllib3
import json
import pandas as pd
import numpy
import datetime
import sys
import os
templates=[]
import warnings
warnings.filterwarnings('ignore')
############ PROXY for Burp ############
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {
    "http": "127.0.0.1:8080",
    "https": "127.0.0.1:8080",
    }

############### LOADER #################
# Проверка, что был передан хотя бы один аргумент
if len(sys.argv) < 2:
    filename = 'UrlList.json' 
else:
    filename = sys.argv[1]

if os.path.exists(filename) == False:
    print("Файл не найден. Укажите нужный файл.")
    sys.exit(1)

print(f"Загружен файл: '{filename}'")

with open(filename, 'r', encoding='utf-8') as f:
    templates = json.load(f)
########################################

if "Cookie" in templates["Auth"]:
    Cookie = templates["Auth"]["Cookie"]
if "Token_monitor" in templates["Auth"]: 
    Token_monitor = templates["Auth"]["Token_monitor"]
if "Token_proc" in templates["Auth"]: 
    Token_proc = templates["Auth"]["Token_proc"]

################ PANDAS ###############

data = {'Name': [],
        'Status Code': [],
        'Delta-Time': [],
        'DefDelta': [],
        'Size': [],
        'Metod': [],
        'URL': [],
        'Body': []}

def highlight_status_code(val): 
    if val >= 500: 
        return 'background-color: red' 
    elif val >=400 and val < 500:
        return 'background-color: yellow' 
    else:
        return ''
    
def highlight(value):
    # print(type(value['Delta-Time']), type(value['DefDelta']))
    # print(value['Delta-Time'], value['DefDelta'])
    if value['Delta-Time'] > value['DefDelta']: 
        return ['background-color: red' if x == value['Delta-Time'] else 'background-color: silver' for x in value]
    else:
        return ['background-color: yellow' if x == value['Delta-Time'] else '' for x in value]

def save_to_file(request, response, delta, defdelta: float):
    data['Name'].append(request["name"])
    data['Status Code'].append(response.status_code)
    data['Delta-Time'].append(delta)
    data['DefDelta'].append(defdelta)
    if "content-length" in  page_response.headers:
        data['Size'].append(f'{int(response.headers["content-length"])/1024:.2f} kB')
    else:
        data['Size'].append(f'{len(response.text)/1024:.2f} kB')
    data['Metod'].append(list(request["metod"])[0].upper())
    data['URL'].append(request["url"])
    if "data" in request: 
        data['Body'].append(request["data"])
    else:
        data['Body'].append("  ---  ")
    
    df = pd.DataFrame(data)
    
    styled_df= df.style.applymap(highlight_status_code, subset=['Status Code'])
    styled_df.apply(highlight, axis=1)
    styled_df.applymap(lambda x: 'background-color: lime' if x < 4 else '', subset=['Delta-Time'])
    styled_df.set_caption(f"{datetime.datetime.now()}")
    
    #Сохраняем таблицу с подсветкой в HTML файл
    styled_df.to_html(f'time_metrik_{datetime.date.today()}_{os.path.splitext(os.path.basename(filename))[0]}.html',  index=False, na_rep="", escape=False)
    
    #Сохраняем таблицу в xlsx файл
    # styled_df.to_excel('table_with_highlight.xlsx', engine='openpyxl', index=False)    
    
########################################

for a in templates["link"]:
    page_url = a["url"]

    page_load_delta = 4   
    if "delta" in a:
        page_load_delta = a["delta"]*1.05
        
    if a["Auth"]=="Token_monitor":
        headers = {
            'Host': 'process-monitor.brusnika.ru',
            'Token': Token_monitor,
            'Content-Type': 'application/json'
            }
    elif a["Auth"]=="Token_proc":
        headers = {
            'Host': 'erp-core.staging.brusnika.tech',
            'Authorization': f'Bearer {Token_proc}',
            'Content-Type': 'application/json'
            }
    elif a["Auth"]=="cookie":
        headers = {
            'Cookie': Cookie,
            'Content-Type': 'application/json'
            }
        
    start_time = time.time()
    page_response = None
    page_load_time = None
   
    if list(a["metod"].keys())[0] == "get":
        if a["proxy"]=="false":
            page_response = requests.get(url=page_url, headers=headers)
        else:
            page_response = requests.get(url=page_url, headers=headers, verify=False, proxies=proxies)
        end_time = time.time()
        page_load_time = end_time - start_time
        if page_load_time >= page_load_delta:    
            if "content-length" in  page_response.headers:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec, {int(page_response.headers["content-length"])/1024:.2f} kB    <<<----')
            else:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec    <<<----')
            #print(f'page: {page_url}')
        else:
            if "content-length" in  page_response.headers:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec, {int(page_response.headers["content-length"])/1024:.2f} kB')
            else:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec')
            
    if list(a["metod"].keys())[0] == "post":
        if a["proxy"]=="false":
            page_response = requests.post(url=page_url, json=a["data"], headers=headers)
        else:
            page_response = requests.post(url=page_url, json=a["data"], headers=headers, verify=False, proxies=proxies)
        end_time = time.time()
        page_load_time = end_time - start_time        
        if page_load_time >= page_load_delta:    
            if "content-length" in  page_response.headers:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec, {int(page_response.headers["content-length"])/1024:.2f} kB    <<<----')
            else:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec    <<<----')
            #print(f'page: {page_url}')
            #print(f'parametrs: {a["data"]}')
        else:
            if "content-length" in  page_response.headers:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec, {int(page_response.headers["content-length"])/1024:.2f} kB')
            else:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec')
    
    if list(a["metod"].keys())[0] =="put":
        if a["proxy"]=="false":
            page_response = requests.put(url=page_url, json=a["data"], headers=headers)
        else:
            page_response = requests.put(url=page_url, json=a["data"], headers=headers, verify=False, proxies=proxies)
        end_time = time.time()
        page_load_time = end_time - start_time        
        if page_load_time >= page_load_delta:    
            if "content-length" in  page_response.headers:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec, {int(page_response.headers["content-length"])/1024:.2f} kB    <<<----')
            else:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec    <<<----')
            #print(f'page: {page_url}')
            #print(f'parametrs: {a["data"]}')
        else:
            if "content-length" in  page_response.headers:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec, {int(page_response.headers["content-length"])/1024:.2f} kB')
            else:
                print(f'{page_response.status_code} --- {a["name"]}, Load time: {page_load_time:.2f} sec')
       
    save_to_file(a,page_response, page_load_time, page_load_delta)

print("")
