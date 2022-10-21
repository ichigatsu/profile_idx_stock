# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


import time
import re
import requests

import json
import pandas as pd
from pandas import json_normalize

options = webdriver.ChromeOptions()
options.add_argument("--enable-javascript")
# options.add_argument('headless')

driver = webdriver.Chrome('C:/BrowserDrivers/chromedriver', options=options)
base_url = 'https://www.idx.co.id/umbraco/Surface/ListedCompany/GetCompanyProfiles?draw=2&columns[0][data]=KodeEmiten&columns[0][name]=&columns[0][searchable]=true&columns[0][orderable]=false&columns[0][search][value]=&columns[0][search][regex]=false&columns[1][data]=KodeEmiten&columns[1][name]=&columns[1][searchable]=true&columns[1][orderable]=false&columns[1][search][value]=&columns[1][search][regex]=false&columns[2][data]=NamaEmiten&columns[2][name]=&columns[2][searchable]=true&columns[2][orderable]=false&columns[2][search][value]=&columns[2][search][regex]=false&columns[3][data]=TanggalPencatatan&columns[3][name]=&columns[3][searchable]=true&columns[3][orderable]=false&columns[3][search][value]=&columns[3][search][regex]=false&start=0&length=1000&search[value]=&search[regex]=false&_=1666248063999'
driver.get(base_url)

# %%

content = driver.page_source
content = driver.find_element_by_tag_name('pre').text
parsed_json = json.loads(content)
df = json_normalize(parsed_json['data'])
df.to_excel("C:\\idx.xlsx")



