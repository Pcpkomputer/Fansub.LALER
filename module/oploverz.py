from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *
from module.bypasser.yudhaLIB import yudhaLIB

def oploverz(x):
        tautan=x
        nama_regex=re.compile(r"sorattl title-download\">(oploverz[a-zA-Z\s]..[a-zA-z\s\d]*)")
        elsfile_regex=re.compile(r"<a href=\"([^\"]+)\" rel=\"[^\"]+\" target=\"[^\"]+\">[\sElsfile]+</a>")
        gd_regex=re.compile(r"<a href=\"([^\"]+)\" rel=\"[^\"]+\" target=\"[^\"]+\">[\sGoogle Drive]+</a>")
        zippy_regex=re.compile(r"<a href=\"([^\"]+)\" rel=\"[^\"]+\" target=\"[^\"]+\">[\sZippyshare]+</a>")
        mirror_regex=re.compile(r"<a href=\"([^\"]+)\" rel=\"[^\"]+\" target=\"[^\"]+\">[\sMirror]+</a>")
        req = Request(tautan, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        html=str(html).replace(r'<strong>',r'')
        html=str(html).replace(r'</strong>',r'')
        #html2=str(html).replace(r' rel="noopener" target="_blank"','')
        elsfile=re.findall(elsfile_regex,str(html))
        googledrive=re.findall(gd_regex,str(html))
        zippyshare=re.findall(zippy_regex,str(html))
        mirror=re.findall(mirror_regex,str(html))
        namarilis=re.findall(nama_regex,str(html))
        print(googledrive)
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
            if re.search(r"uin98",str(elsfile)):
                    hasil=re.search(uin98,str(html))
                    elsfiletabel.append(hasil.group(1))
            if re.search(r"hexafile.net",str(elsfile)):
                    val=yudhaLIB(elsfile)
                    elsfiletabel.append(val)
        for gd in googledrive:
            req = Request(gd, headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            if re.search(r"uin98",str(gd)):
                    hasil=re.search(uin98,str(html))
                    gdtabel.append(hasil.group(1))
            if re.search(r"hexafile.net",str(gd)):
                    val=yudhaLIB(gd)
                    gdtabel.append(val)
        for zippy in zippyshare:
            req = Request(zippy, headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            if re.search(r"uin98",str(zippy)):
                    hasil=re.search(uin98,str(html))
                    zippytabel.append(hasil.group(1))
            if re.search(r"hexafile.net",str(zippy)):
                    val=yudhaLIB(zippy)
                    zippytabel.append(val)
        for mirror in mirror:
            req = Request(mirror, headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            if re.search(r"uin98",str(mirror)):
                    hasil=re.search(uin98,str(html))
                    elsfiletabel.append(hasil.group(1))
            if re.search(r"hexafile.net",str(mirror)):
                    val=yudhaLIB(mirror)
                    mirrortabel.append(val)
        return(namatabel,elsfiletabel,gdtabel,zippytabel,mirrortabel)
