from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup
import re
from re import *

def bagilagi_bypass(x):
    url = 'https://bagilagi.com/5-makanan-untuk-jantung-lebih-sehat/'
    s = requests.Session()

    header_info = {
    "user-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }

    r = s.post(url, data={'get':x},headers = header_info)
    return(r.text)

