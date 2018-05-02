from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *

def awsubs(x):
    tautan=x
    solidfiles_regex = re.compile(r"href=\"(.*)\">Solidfiles</a>")
    datafile_regex= re.compile(r"rel=\"nofollow.*blue;\"><a\s+href=\"(.+)\">Datafile")
    gd_regex = re.compile(r"style=\"color: blue;\">.</span.*</span><a\s*href=\"(.*)\">GoogleDrive")
    namarilis_regex = re.compile(r"480px;\">(.*)</div>\s*<div class=\"dl-item\"")
    req = Request(x, headers={'User-Agent': 'Mozilla/5.0'})
    url = urlopen(req)
    html=BeautifulSoup(url, 'html.parser')
    #print(html)
    solidfiles=re.findall(solidfiles_regex,str(html))
    googledrive=re.findall(gd_regex,str(html))
    namarilis=re.findall(namarilis_regex,str(html))
    datafile=re.findall(datafile_regex,str(html))
    #print(datafile)
    solidtabel=[]
    gdtabel=[]
    datafiletabel=[]
    namarilistabel=[]
    for dt in datafile:
        try:
            shortawsubs=re.compile(r"<center style=.*<a href=\"(.*)\"\s*rel=\"nofollow\"")
            sflink=re.compile(r"var d_link\s*=\s*'(.*)';")
            dotco=re.search(r"awsubs.co",str(dt))
            safelink=re.search(r"safelink",str(dt))
            solid=re.search(r"solidfiles",str(dt))
            bitly=re.search(r"bit.ly",str(dt))
            idsly=re.search(r"idsly",str(dt))
            safelinku=re.search(r"safelinku",str(dt))
            bolaz=re.search(r"bola",str(dt))
            bola=re.compile(r"\(\"#pleasewaits\"\).fadeOut.+var a='(.+)';window.open")
            if bolaz:
                safe=dt.replace(r'" rel="nofollow','')
                safe=safe.replace(r'amp;','')
                req = Request(safe, headers={'User-Agent': 'Mozilla/5.0'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(bola, str(html))
                auth=re.search(r"bit.ly",str(hasil.group(1)))
                if auth:
                    req = Request(hasil.group(1), headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                    url = urlopen(req)
                    html =BeautifulSoup(url, 'html.parser')
                    hasilbit=re.search(shortawsubs, str(html))
                    datafiletabel.append(hasilbit.group(1))
                else:
                    datafiletabel.append(hasil.group(1))       
            if safelinku:
                dt=dt
                datafiletabel.append(dt)
            if dotco:
                req = Request(dt, headers={'User-Agent': 'Mozilla/5.0'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(shortawsubs, str(html))
                datafiletabel.append(hasil.group(1))
            if safelink:
                #print(dt)
                #safe=dt.replace(r'link.safelinkconverter.com/review.php?',r'awsubsco.cf/en/cost/safelinku.net?')
                #safe=safe.replace(r'" rel="nofollow','')
                #safe=safe.replace(r'amp;','')
                req = Request(dt, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(sflink,str(html))
                hasil=hasil.group(1)
                hasil=hasil.replace(r'%3A',r':')
                hasil=hasil.replace(r'%2F',r'/')
                bitly=re.search(r"bit.ly",str(hasil))
                solid=re.search(r"solidfiles",str(hasil))
                idsly=re.search(r"idsly",str(hasil))
                safelinku=re.search(r"safelinku",str(hasil))
                if safelinku:
                    hasil=hasil
                    datafiletabel.append(hasil)
                if bitly:
                    req = Request(hasil, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                    url = urlopen(req)
                    html =BeautifulSoup(url, 'html.parser')
                    hasilbit=re.search(shortawsubs, str(html))
                    datafiletabel.append(hasilbit.group(1))
                if solid:
                    hasil=hasil
                    datafiletabel.append(hasil)
                if idsly:
                    hasil=hasil
                    datafiletabel.append(hasil)
            #if solid:
            #    dt=dt
            #    datafiletabel.append(gd)
            if bitly:
                req = Request(dt, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasilbit=re.search(shortawsubs, str(html))
                datafiletabel.append(hasilbit.group(1))
            if idsly:
                dt=dt
                datafiletabel.append(gd)
        except Exception as ex:
            print('debug1')
            print(ex)


    for gd in googledrive:
        try:
            shortawsubs=re.compile(r"<center style=.*<a href=\"(.*)\"\s*rel=\"nofollow\"")
            sflink=re.compile(r"var d_link\s*=\s*'(.*)';")
            dotco=re.search(r"awsubs.co",str(gd))
            safelink=re.search(r"safelink",str(gd))
            solid=re.search(r"solidfiles",str(gd))
            bitly=re.search(r"bit.ly",str(gd))
            idsly=re.search(r"idsly",str(gd))
            safelinku=re.search(r"safelinku",str(gd))
            bolaz=re.search(r"bola",str(gd))
            bola=re.compile(r"\(\"#pleasewaits\"\).fadeOut.+var a='(.+)';window.open")
            if bolaz:
                safe=gd.replace(r'" rel="nofollow','')
                safe=safe.replace(r'amp;','')
                req = Request(safe, headers={'User-Agent': 'Mozilla/5.0'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(bola, str(html))
                auth=re.search(r"bit.ly",str(hasil.group(1)))
                if auth:
                    req = Request(hasil.group(1), headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                    url = urlopen(req)
                    html =BeautifulSoup(url, 'html.parser')
                    hasilbit=re.search(shortawsubs, str(html))
                    gdtabel.append(hasilbit.group(1))
                else:
                    gdtabel.append(hasil.group(1))
            if safelinku:
                gd=gd
                gdtabel.append(gd)
            if dotco:
                req = Request(gd, headers={'User-Agent': 'Mozilla/5.0'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(shortawsubs, str(html))
                gdtabel.append(hasil.group(1))
            if safelink:
                #safe=gd.replace(r'link.safelinkconverter.com/review.php?',r'awsubsco.cf/en/cost/drive.google.com?')
                safe=gd.replace(r'" rel="nofollow','')
                safe=safe.replace(r'amp;','')
                req = Request(safe, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(sflink,str(html))
                hasil=hasil.group(1)
                hasil=hasil.replace(r'%3A',r':')
                hasil=hasil.replace(r'%2F',r'/')
                bitly=re.search(r"bit.ly",str(hasil))
                solid=re.search(r"solidfiles",str(hasil))
                idsly=re.search(r"idsly",str(hasil))
                if bitly:
                    req = Request(hasil, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                    url = urlopen(req)
                    html =BeautifulSoup(url, 'html.parser')
                    hasilbit=re.search(shortawsubs, str(html))
                    gdtabel.append(hasilbit.group(1))
                    #print(hasilbit.group(1))
                if solid:
                    hasil=hasil
                    gdtabel.append(hasil)
                if idsly:
                    hasil=hasil
                    gdtabel.append(hasil)
            #if solid:
            #    gd=gd
            #    gdtabel.append(gd)
            if bitly:
                req = Request(gd, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasilbit=re.search(shortawsubs, str(html))
                gdtabel.append(hasilbit.group(1))
            if idsly:
                gd=gd
                gdtabel.append(gd)
        except Exception as ex:
            #print('debug2')
            #print(ex)
            pass
            
    for x in namarilis:
        namarilistabel.append(x)
        
    for sf in solidfiles:
        try:
            shortawsubs=re.compile(r"<center style=.*<a href=\"(.*)\"\s*rel=\"nofollow\"")
            sflink=re.compile(r"var d_link\s*=\s*'(.*)';")
            dotco=re.search(r"awsubs.co",str(sf))
            safelink=re.search(r"safelink",str(sf))
            solid=re.search(r"solidfiles",str(sf))
            bitly=re.search(r"bit.ly",str(sf))
            idsly=re.search(r"idsly",str(sf))
            safelinku=re.search(r"safelinku",str(sf))
            bolaz=re.search(r"bola",str(sf))
            bola=re.compile(r"\(\"#pleasewaits\"\).fadeOut.+var a='(.+)';window.open")
            if bolaz:
                safe=sf.replace(r'" rel="nofollow','')
                safe=safe.replace(r'amp;','')
                req = Request(safe, headers={'User-Agent': 'Mozilla/5.0'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(bola, str(html))
                auth=re.search(r"bit.ly",str(hasil.group(1)))
                if auth:
                    req = Request(hasil.group(1), headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                    url = urlopen(req)
                    html =BeautifulSoup(url, 'html.parser')
                    hasilbit=re.search(shortawsubs, str(html))
                    solidtabel.append(hasilbit.group(1))
                else:
                    solidtabel.append(hasil.group(1))
            if safelinku:
                sf=sf
                solidtabel.append(sf)
            if dotco:
                req = Request(sf, headers={'User-Agent': 'Mozilla/5.0'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(shortawsubs, str(html))
                solidtabel.append(hasil.group(1))
            if safelink:
                #safe=sf.replace(r'link.safelinkconverter.com/review.php?',r'awsubsco.cf/en/cost/solidfiles.com?')
                safe=sf.replace(r'" rel="nofollow','')
                safe=safe.replace(r'amp;','')
                req = Request(safe, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasil=re.search(sflink,str(html))
                hasil=hasil.group(1)
                hasil=hasil.replace(r'%3A',r':')
                hasil=hasil.replace(r'%2F',r'/')
                bitly=re.search(r"bit.ly",str(hasil))
                solid=re.search(r"solidfiles",str(hasil))
                idsly=re.search(r"idsly",str(hasil))
                if bitly:
                    req = Request(hasil, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                    url = urlopen(req)
                    html =BeautifulSoup(url, 'html.parser')
                    hasilbit=re.search(shortawsubs, str(html))
                    solidtabel.append(hasilbit.group(1))
                if solid:
                    hasil=hasil
                    solidtabel.append(hasil)
                if idsly:
                    hasil=hasil
                    solidtabel.append(hasil)
            #if solid:
            #    sf=sf
            #    print(sf)
            #    solidtabel.append(sf)
            if bitly:
                req = Request(sf, headers={'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'})
                url = urlopen(req)
                html =BeautifulSoup(url, 'html.parser')
                hasilbit=re.search(shortawsubs, str(html))
                solidtabel.append(hasilbit.group(1))
            '''if idsly:
                sf=sf
                solidtabel.append(sf)'''
        except Exception as ex:
            print('debug3')
            print(ex)

    ###debuggin purpose
    #for x in solidtabel:
    #    print(x)
    #for x in namarilistabel:

    #HANDLING TEMPLATE

    """tabel0=[]
    tabel1=[]
    tabel2=[]
    tabel3=[]
    tabel4=[]
    for x in range(1):
        try:
            tabel0.append(solidtabel[0])
            tabel0.append(gdtabel[0])
            tabel0.append(datafiletabel[0])
            tabel1.append(solidtabel[1])
            tabel1.append(gdtabel[1])
            tabel1.append(datafiletabel[1])
            tabel2.append(solidtabel[2])
            tabel2.append(gdtabel[2])
            tabel2.append(datafiletabel[2])
            tabel3.append(solidtabel[3])
            tabel3.append(gdtabel[3])
            tabel3.append(datafiletabel[3])
            tabel4.append(solidtabel[4])
            tabel4.append(gdtabel[4])
            tabel4.append(datafiletabel[4])
        except Exception as e:
            pass"""
    return(namarilistabel,solidtabel,gdtabel,datafiletabel)

#if __name__ == '__main__':
#    awsubs('http://awsubs.co/gegege-no-kitarou-2018-episode-4-subtitle-indonesia/')
