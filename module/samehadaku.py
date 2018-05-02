from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *

def samehada(x):
    tautan=x
    nama_regex=re.compile(r"<strong>(.+)</strong>.*<span\s+style=\"color: #ff0000;\"><a href")
    uf_regex=re.compile(r"<a href=\"(.+)\" rel=\"nofollow noopener\s+noreferrer\" style=\"color: #ff0000;\" target=\"_blank\">UF</a>")
    cu_regex=re.compile(r"\| <a\s+href=\"(.*)\" rel.*target=\"_blank\">CU</a>")
    gd_regex=re.compile(r"href=\"(http://www.siotong.com/.....)\" rel=\"nofollow noopener\s+noreferrer\" style=\"color: #ff0000;\" target=\"_blank\">GD</a>")
    zs_regex=re.compile(r"href=\"(http://www.siotong.com/.....)\" rel=\"noopener noreferrer\s+nofollow\" style=\"color: #ff0000;\" target=\"_blank\">ZS</a>")
    sc_regex=re.compile(r"href=\"(http://www.siotong.com/.....)\" rel=\"noopener noreferrer\s+nofollow\" style=\"color: #ff0000;\" target=\"_blank\">SC</a>")
    mu_regex=re.compile(r"href=\"(http://www.siotong.com/.....)\" rel=\"noopener noreferrer\s+nofollow\" style=\"color: #ff0000;\" target=\"_blank\">MU</a>")
    req = Request(tautan, headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req)
    html=BeautifulSoup(url, 'html.parser')
    nama=re.findall(nama_regex,str(html))
    uf=re.findall(uf_regex,str(html))
    cu=re.findall(cu_regex,str(html))
    gd=re.findall(gd_regex,str(html))
    zs=re.findall(zs_regex,str(html))
    sc=re.findall(sc_regex,str(html))
    mu=re.findall(mu_regex,str(html))
    ############
    g_greget=re.compile(r"{clearInterval\(countdown\);window.location=\"(.+)\";}count--;}")
    ############
    namatabel=[]
    uftabel=[]
    cutabel=[]
    gdtabel=[]
    zstabel=[]
    sctabel=[]
    mutabel=[]
    ############
    for x in nama:
        namatabel.append(x)
    for uf in uf:
        req = Request(uf, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        greget=re.search(g_greget,str(html))
        greget_auth=re.search(r"greget",greget.group(1))
        if greget:
            req = Request(greget.group(1), headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            greget=re.search(g_greget,str(html))
            uftabel.append(greget.group(1))
            
    for cu in cu:
        req = Request(cu, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        greget=re.search(g_greget,str(html))
        greget_auth=re.search(r"greget",greget.group(1))
        if greget:
            req = Request(greget.group(1), headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            greget=re.search(g_greget,str(html))
            cutabel.append(greget.group(1))
            
    for gd in gd:
        req = Request(gd, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        greget=re.search(g_greget,str(html))
        greget_auth=re.search(r"greget",greget.group(1))
        if greget:
            req = Request(greget.group(1), headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            greget=re.search(g_greget,str(html))
            gdtabel.append(greget.group(1))
            
    for zs in zs:
        req = Request(zs, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        greget=re.search(g_greget,str(html))
        greget_auth=re.search(r"greget",greget.group(1))
        if greget:
            req = Request(greget.group(1), headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            greget=re.search(g_greget,str(html))
            zstabel.append(greget.group(1))
            
    for sc in sc:
        req = Request(sc, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        greget=re.search(g_greget,str(html))
        greget_auth=re.search(r"greget",greget.group(1))
        if greget:
            req = Request(greget.group(1), headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            greget=re.search(g_greget,str(html))
            sctabel.append(greget.group(1))

    for mu in mu:
        req = Request(mu, headers={'User-Agent': 'Mozilla/5.0'})
        url = urlopen(req)
        html=BeautifulSoup(url, 'html.parser')
        greget=re.search(g_greget,str(html))
        greget_auth=re.search(r"greget",greget.group(1))
        if greget:
            req = Request(greget.group(1), headers={'User-Agent': 'Mozilla/5.0'})
            url = urlopen(req)
            html=BeautifulSoup(url, 'html.parser')
            greget=re.search(g_greget,str(html))
            mutabel.append(greget.group(1))
    return(namatabel, uftabel, cutabel, gdtabel, zstabel, sctabel, mutabel)