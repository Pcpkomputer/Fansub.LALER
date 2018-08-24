import re
import requests
from yudhaLIB._bypasser import yudhaLIB

class fansub:
    req=requests.Session()
    def samehadaku(self,url):
        html=self.req.get(url).text
        regex=re.compile(r"<strong>(?P<resolusi>[^<]+)</strong>(\s+|)<(span|a) style=\"[^h]+href=\"(?P<link1>[^\"]+)\"[^>]+>(?P<host1>[^<]+)</a>[^h]+href=\"(?P<link2>[^\"]+)\"[^>]+>(?P<host2>[^<]+)</a>[^h]+href=\"(?P<link3>[^\"]+)\"[^>]+>(?P<host3>[^<]+)</a>[^h]+href=\"(?P<link4>[^\"]+)\"[^>]+>(?P<host4>[^<]+)</a>[^h]+href=\"(?P<link5>[^\"]+)\"[^>]+>(?P<host5>[^<]+)</a>[^h]+href=\"(?P<link6>[^\"]+)\"[^>]+>(?P<host6>[^<]+)</a>")
        a=re.findall(r"(<strong>[^<]+</strong>(\s+|)<(span|a) style=\"[^h]+href=\"[^\"]+\"[^>]+>[^<]+</a>[^h]+href=\"[^\"]+\"[^>]+>[^<]+</a>[^h]+href=\"[^\"]+\"[^>]+>[^<]+</a>[^h]+href=\"[^\"]+\"[^>]+>[^<]+</a>[^h]+href=\"[^\"]+\"[^>]+>[^<]+</a>[^h]+href=\"[^\"]+\"[^>]+>[^<]+</a>)",str(html))
        html=''
        for x in range(4):
            res=re.search(regex,str(a[x][0]))
            html+='''
 <div class="mb-1">
<span class="uk-badge" style="
font-size: 9px;
border-radius: 0px;
margin-left: 6px;
background-color: #c5c5c5;
height: 15px;">{}</span>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">{}</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">{}</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">{}</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">{}</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">{}</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">{}</a>
</div>
'''.format(res.group('resolusi'),yudhaLIB(res.group('link1')),res.group('host1'),yudhaLIB(res.group('link2')),res.group('host2'),yudhaLIB(res.group('link3')),res.group('host3'),yudhaLIB(res.group('link4')),res.group('host4'),yudhaLIB(res.group('link5')),res.group('host5'),yudhaLIB(res.group('link6')),res.group('host6'))
        return html
            
            
    def oploverz(self,url):
        html=self.req.get(url).text
        judul=re.findall(r"<div class=\"sorattl title-download\">([^<]+)</div>",str(html))
        elsfile=re.findall(r"<a href=\"([^\"]+)\"[^>]+>[^E]+Elsfile",str(html))
        zippyshare=re.findall(r"<a href=\"([^\"]+)\"[^>]+>[^Z]+Zippyshare",str(html))
        googledrive=re.findall(r"<a href=\"([^\"]+)\"[^>]+>[^G]+Google Drive",str(html))
        mirror=re.findall(r"<a href=\"([^\"]+)\"[^>]+>[^M]+Mirr",str(html))
        while(len(judul)>len(elsfile)):
              elsfile.append('placeholder')
        while(len(judul)>len(zippyshare)):
              zippyshare.append('placeholder')
        while(len(judul)>len(googledrive)):
              googledrive.append('placeholder')
        while(len(judul)>len(mirror)):
              mirror.append('placeholder')
        html='';
        for x in list(zip(judul,elsfile,zippyshare,googledrive,mirror)):
              html+='''
 <div class="mb-1">
<span class="uk-badge" style="
font-size: 9px;
border-radius: 0px;
margin-left: 6px;
background-color: #c5c5c5;
height: 15px;">{}</span>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">Elsfile</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">Zippyshare</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">Googledrive</a>
<a href="{}" style="margin-left:5px;font-size:10px;color: #848484;">MirrorCreator</a>
</div>
'''.format(x[0],yudhaLIB(x[1]),yudhaLIB(x[2]),yudhaLIB(x[3]),yudhaLIB(x[4]))
        return html
        
    def awsubs(self,url):
        return 'samehada'
    def animepahe(self,url):
        return 'samehada'
    def anitoki(self,url):
        return 'samehada'
    def drivenime(self,url):
        return 'samehada'

def _fansublaler(f,url):
    if f=='samehadaku':
        return fansub().samehadaku(url)
    if f=='oploverz':
        return fansub().oploverz(url)
    if f=='awsubs':
        return fansub().awsubs(url)
    if f=='animepahe':
        return fansub().animepahe(url)
    if f=='anitoki':
        return fansub.anitoki(url)
    if f=='drivenime':
        return fansub.drivenime(url)
    
if __name__=='__main__':
    _fansublaler('oploverz','https://www.oploverz.in/isekai-maou-to-shoukan-shoujo-no-dorei-majutsu-04-subtitle-indonesia/')
    
