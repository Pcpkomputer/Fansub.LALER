from urllib.request import urlopen, Request
import urllib.parse
from bs4 import BeautifulSoup
import argparse
import re
from re import *
from flask import jsonify,json

def query_awsubs(x):
    url_query='http://awsubs.co/?s='+x
    #quoted=urllib.parse.quote(url_query)
    #quoted=quoted.replace('%3A',':')
    #quoted=quoted.replace('%3Fs%3D','?s=')
    grabber=re.compile(r"<div class=\"kirizona\">\s+<h2><a href=\"([^\"]+)\"")
    req = Request(url_query, headers={'User-Agent': 'Mozilla/5.0'})
    reqs = urlopen(req)
    html = BeautifulSoup(reqs, 'html.parser')
    link = re.findall(grabber,str(html))
    return jsonify(results=link)
