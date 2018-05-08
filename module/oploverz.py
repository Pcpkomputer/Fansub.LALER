from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *

def oploverz(x):
	tautan=x
	nama_regex=re.compile(r"sorattl title-download\">(oploverz[a-zA-Z\s]..[a-zA-z\s\d]*)")
	elsfile_regex=re.compile(r"<a href=\"(https://94lauin.com/.....)\" rel=\"noopener\" target=\"_blank\">Elsfile")
	gd_regex=re.compile(r"<a href=\"(https://94lauin.com/.....)\" rel=\"noopener\" target=\"_blank\">Google Drive")
	zippy_regex=re.compile(r"<a href=\"(https://94lauin.com/.....)\" rel=\"noopener\"\s+target=\"_blank\">[\sZippyshare]+")
	mirror_regex=re.compile(r"<a href=\"(https://94lauin.com/.....)\" rel=\"noopener\" target=\"_blank\">Mirr")
	req = Request(tautan, headers={'User-Agent': 'Mozilla/5.0'})
	url = urlopen(req)
	html=BeautifulSoup(url, 'html.parser')
	html=str(html).replace(r'<strong>',r'')
	html=str(html).replace(r'</strong>',r'')
	elsfile=re.findall(elsfile_regex,str(html))
	googledrive=re.findall(gd_regex,str(html))
	zippyshare=re.findall(zippy_regex,str(html))
	mirror=re.findall(mirror_regex,str(html))
	print(mirror)
	namarilis=re.findall(nama_regex,str(html))
	uin98=re.compile(r"!function\(a\).*\(\".link-content\"\).*\"(.*)\",e=")
	namatabel=[]
	elsfiletabel=[]
	gdtabel=[]
	zippytabel=[]
	mirrortabel=[]
	for namarilis in namarilis:
	    namatabel.append(namarilis)
	for elsfile in elsfile:
	    req = Request(elsfile, headers={'User-Agent': 'Mozilla/5.0'})
	    url = urlopen(req)
	    html=BeautifulSoup(url, 'html.parser')
	    hasil=re.search(uin98,str(html))
	    elsfiletabel.append(hasil.group(1))
	for gd in googledrive:
	    req = Request(gd, headers={'User-Agent': 'Mozilla/5.0'})
	    url = urlopen(req)
	    html=BeautifulSoup(url, 'html.parser')
	    hasil=re.search(uin98,str(html))
	    gdtabel.append(hasil.group(1))
	for zippy in zippyshare:
	    req = Request(zippy, headers={'User-Agent': 'Mozilla/5.0'})
	    url = urlopen(req)
	    html=BeautifulSoup(url, 'html.parser')
	    hasil=re.search(uin98,str(html))
	    zippytabel.append(hasil.group(1))
	for mirror in mirror:
	    req = Request(mirror, headers={'User-Agent': 'Mozilla/5.0'})
	    url = urlopen(req)
	    html=BeautifulSoup(url, 'html.parser')
	    hasil=re.search(uin98,str(html))
	    mirrortabel.append(hasil.group(1))
	return(namatabel,elsfiletabel,gdtabel,zippytabel,mirrortabel)