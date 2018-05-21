from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import requests
import re
from re import *


def checker(x):
    intercelestial=re.search(r"intercelestial",str(x))
    sweetlantern=re.search(r"sweetlantern",str(x))
    spaste=re.search(r"spaste",str(x))
    if intercelestial:
        return 'intercelestial'
    elif sweetlantern:
        return 'sweetlantern'
    elif spaste:
        return 'spaste'
    else:
        return 'false'
    

class pahein:
    def __init__(self, params):
        self.link=params
        self.request=Request(self.link,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'})
        self.open=urlopen(self.request)
        self.html=BeautifulSoup(self.open, 'html.parser')
        self.utf8=self.html.encode('utf-8')
        
    def berkas(self, x):
        self.title=re.findall(r"<b>([^</b>]+)</b>[^<br/>]+<br.>\s+",str(x))
        self.ukuran=re.findall(r"<b>[^</b>]+</b>([^<br/>]+)<br.>\s+",str(x))
        title=[]
        for x in zip(self.title,self.ukuran):
            title.append(''.join(x))
        return title
    def utb(self,x):
        self.utb=re.findall(r"href=\"([^\"]+)\"[^UTB]+UTB</a>",str(x))
        return self.utb
    def gd(self,x):
        self.gd=re.findall(r"href=\"([^\"]+)\"[^GD]+GD</a>",str(x))
        return self.gd
    def mg(self,x):
        self.mg=re.findall(r"href=\"([^\"]+)\"[^MG]+MG</a>",str(x))
        return self.mg

def pahein_hajar(params):
    html=pahein(params)
    ########################
    berkas=html.berkas(html.utf8)
    utb=html.utb(html.utf8)
    gd=html.gd(html.utf8)
    mg=html.mg(html.utf8)
    ########################
    googledrive=[]
    utebe=[]
    mega=[]
    #######################
    for x in mg:
        a=checker(x)
        if a=='sweetlantern':
            attrvalue=re.search(r"\?id=(.*)",str(x)).group(1)
            r=requests.Session()
            post=r.post('http://sweetlantern.com/the-death-of-the-universe/', data={'get':attrvalue}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            spacetica=re.search(r"changeLink\(\){var\s+a='([^']+)';window.open",str(post)).group(1)
            url=requests.get(spacetica, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            link=re.search(r"style=\"text-align:center; font-size:\d+%;\"><b><a href=\"([^\"]+)\"",str(url)).group(1)
            mega.append(link)
        if a=='intercelestial':
            attrvalue=re.search(r"\?id=(.*)",str(x)).group(1)
            r=requests.Session()
            post=r.post('http://intercelestial.com/the-birth-of-a-star/', data={'get':attrvalue}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            spacetica=re.search(r"changeLink\(\){var\s+a='([^']+)';window.open",str(post)).group(1)
            url=requests.get(spacetica, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            link=re.search(r"style=\"text-align:center; font-size:\d+%;\"><b><a href=\"([^\"]+)\"",str(url)).group(1)
            mega.append(link)
        if a=='spaste':
            requestid=re.search(r"\?c=(.*)",str(x)).group(1)
            r=requests.Session()
            #Find the required data bounce, token dsb#
            html=r.get(x,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            turn=re.search(r"<input type=\"hidden\" name=\"turn\" value=\"(\d)+\"",str(html)).group(1)
            bounce=re.search(r"<input type=\"hidden\" name=\"bounce\" value=\"([^\"]+)\"",str(html)).group(1)
            token=re.search(r"<input type=\"hidden\" name=\"token\" value=\"([^\"]+)\"",str(html)).group(1)
            ##########################################
            headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '228',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.spaste.com',
            'Origin': 'http://www.spaste.com',
            'Referer': 'http://www.spaste.com/site/checkPasteUrl?c='+requestid,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                }

            data={
            'sPasteCaptcha': 'cef5c5410314eac13fba68c40bef24fd',
            'userEnterHashHere': '306',
            'turn': turn,
            'bounce': bounce,
            'token': token,
            'detector': 'http://www.spaste.com/site/checkBlockedDotCom',
            'pasteUrlForm[submit]': 'submit',
                }
            bypass=r.post('http://www.spaste.com/site/checkPasteUrl?c='+requestid, headers=headers, data=data).text
            link=re.search(r"<a target=\"_blank\" style=[^h]+href=\"([^\"]+)\">",str(bypass)).group(1)
            mega.append(link)
    #####################################################
            
    #######################
    for x in utb:
        a=checker(x)
        if a=='sweetlantern':
            attrvalue=re.search(r"\?id=(.*)",str(x)).group(1)
            r=requests.Session()
            post=r.post('http://sweetlantern.com/the-death-of-the-universe/', data={'get':attrvalue}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            spacetica=re.search(r"changeLink\(\){var\s+a='([^']+)';window.open",str(post)).group(1)
            url=requests.get(spacetica, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            link=re.search(r"style=\"text-align:center; font-size:\d+%;\"><b><a href=\"([^\"]+)\"",str(url)).group(1)
            utebe.append(link)
        if a=='intercelestial':
            attrvalue=re.search(r"\?id=(.*)",str(x)).group(1)
            r=requests.Session()
            post=r.post('http://intercelestial.com/the-birth-of-a-star/', data={'get':attrvalue}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            spacetica=re.search(r"changeLink\(\){var\s+a='([^']+)';window.open",str(post)).group(1)
            url=requests.get(spacetica, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            link=re.search(r"style=\"text-align:center; font-size:\d+%;\"><b><a href=\"([^\"]+)\"",str(url)).group(1)
            utebe.append(link)
        if a=='spaste':
            requestid=re.search(r"\?c=(.*)",str(x)).group(1)
            r=requests.Session()
            #Find the required data bounce, token dsb#
            html=r.get(x,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            turn=re.search(r"<input type=\"hidden\" name=\"turn\" value=\"(\d)+\"",str(html)).group(1)
            bounce=re.search(r"<input type=\"hidden\" name=\"bounce\" value=\"([^\"]+)\"",str(html)).group(1)
            token=re.search(r"<input type=\"hidden\" name=\"token\" value=\"([^\"]+)\"",str(html)).group(1)
            ##########################################
            headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '228',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.spaste.com',
            'Origin': 'http://www.spaste.com',
            'Referer': 'http://www.spaste.com/site/checkPasteUrl?c='+requestid,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                }

            data={
            'sPasteCaptcha': 'cef5c5410314eac13fba68c40bef24fd',
            'userEnterHashHere': '306',
            'turn': turn,
            'bounce': bounce,
            'token': token,
            'detector': 'http://www.spaste.com/site/checkBlockedDotCom',
            'pasteUrlForm[submit]': 'submit',
                }
            bypass=r.post('http://www.spaste.com/site/checkPasteUrl?c='+requestid, headers=headers, data=data).text
            link=re.search(r"<a target=\"_blank\" style=[^h]+href=\"([^\"]+)\">",str(bypass)).group(1)
            utebe.append(link)
    #####################################################
            
    for x in gd:
        a=checker(x)
        if a=='sweetlantern':
            attrvalue=re.search(r"\?id=(.*)",str(x)).group(1)
            r=requests.Session()
            post=r.post('http://sweetlantern.com/the-death-of-the-universe/', data={'get':attrvalue}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            spacetica=re.search(r"changeLink\(\){var\s+a='([^']+)';window.open",str(post)).group(1)
            url=requests.get(spacetica, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            link=re.search(r"style=\"text-align:center; font-size:\d+%;\"><b><a href=\"([^\"]+)\"",str(url)).group(1)
            googledrive.append(link)
        if a=='intercelestial':
            attrvalue=re.search(r"\?id=(.*)",str(x)).group(1)
            r=requests.Session()
            post=r.post('http://intercelestial.com/the-birth-of-a-star/', data={'get':attrvalue}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            spacetica=re.search(r"changeLink\(\){var\s+a='([^']+)';window.open",str(post)).group(1)
            url=requests.get(spacetica, headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            link=re.search(r"style=\"text-align:center; font-size:\d+%;\"><b><a href=\"([^\"]+)\"",str(url)).group(1)
            googledrive.append(link)
        if a=='spaste':
            requestid=re.search(r"\?c=(.*)",str(x)).group(1)
            r=requests.Session()
            #Find the required data bounce, token dsb#
            html=r.get(x,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}).text
            turn=re.search(r"<input type=\"hidden\" name=\"turn\" value=\"(\d)+\"",str(html)).group(1)
            bounce=re.search(r"<input type=\"hidden\" name=\"bounce\" value=\"([^\"]+)\"",str(html)).group(1)
            token=re.search(r"<input type=\"hidden\" name=\"token\" value=\"([^\"]+)\"",str(html)).group(1)
            ##########################################
            headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '228',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.spaste.com',
            'Origin': 'http://www.spaste.com',
            'Referer': 'http://www.spaste.com/site/checkPasteUrl?c='+requestid,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
                }

            data={
            'sPasteCaptcha': 'cef5c5410314eac13fba68c40bef24fd',
            'userEnterHashHere': '306',
            'turn': turn,
            'bounce': bounce,
            'token': token,
            'detector': 'http://www.spaste.com/site/checkBlockedDotCom',
            'pasteUrlForm[submit]': 'submit',
                }
            bypass=r.post('http://www.spaste.com/site/checkPasteUrl?c='+requestid, headers=headers, data=data).text
            link=re.search(r"<a target=\"_blank\" style=[^h]+href=\"([^\"]+)\">",str(bypass)).group(1)
            googledrive.append(link)
    return(berkas, googledrive, utebe, mega)

    
