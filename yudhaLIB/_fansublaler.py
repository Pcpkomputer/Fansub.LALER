import re
import requests
from yudhaLIB._bypasser import yudhaLIB
import base64

encode=lambda x: base64.b64encode(x)
decode=lambda x: base64.b64decode(x)

class fansub:
    req=requests.Session()
    def samehadaku(self,url):
        html=self.req.get(url).text
        judul=re.findall(r"<li([^>]+>|>)<strong>([^<]+)</strong>[\s<]+[^h]+href[^>]+>[^<]+</a></span>[^<]+<span",html)
        zs=re.findall(r"href=\"([^\"]+)\"[^>]+>(\s+|)ZS",html)
        gd=re.findall(r"href=\"([^\"]+)\"[^>]+>(\s+|)GD",html)
        uf=re.findall(r"href=\"([^\"]+)\"[^>]+>(\s+|)UF",html)
        cu=re.findall(r"href=\"([^\"]+)\"[^>]+>(\s+|)CU",html)
        sc=re.findall(r"href=\"([^\"]+)\"[^>]+>(\s+|)SC",html)
        mu=re.findall(r"href=\"([^\"]+)\"[^>]+>(\s+|)MU",html)

        judul=[x[1] for x in judul]
        zs=[x[0] for x in zs]
        gd=[x[0] for x in gd]
        uf=[x[0] for x in uf]
        cu=[x[0] for x in cu]
        sc=[x[0] for x in sc]
        mu=[x[0] for x in mu]

        while(len(judul)>len(zs)):
            zs.append('placeholder')
        while(len(judul)>len(gd)):
            gd.append('placeholder')
        while(len(judul)>len(uf)):
            uf.append('placeholder')
        while(len(judul)>len(cu)):
            cu.append('placeholder')
        while(len(judul)>len(sc)):
            sc.append('placeholder')
        while(len(judul)>len(mu)):
            mu.append('placeholder')
        
        html='<div style="padding:10px;">'

        for x in list(zip(judul,zs,gd,uf,cu,sc,mu)):
            html+='''
 <div class="mb-1">
<span class="uk-badge" style="
font-size: 9px;
border-radius: 0px;
margin-left: 6px;
background-color: #c5c5c5;
height: 15px;">{}</span>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Zippyshare</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Googledrive</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Uploadfiles</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">ClickUpload</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Sendit.Cloud</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Megaupload</a>
</div>
'''.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6])
        html+='</div>'
        return html
            
            
    def oploverz(self,url):
        html=self.req.get(url).text
        html=re.sub(r"<strong>","",str(html))
        html=re.sub(r"</strong>","",str(html))
        html=re.sub(r"rel=\"noopener\">(\s+)","rel=\"noopener\">",str(html))
        judul=re.findall(r"<div class=\"sorattl title-download\">([^<]+)</div>",str(html))
        elsfile=re.findall(r"<a href=\"([^\"]+)\"[^>]+>Elsfile",str(html))
        zippyshare=re.findall(r"<a href=\"([^\"]+)\"[^>]+>Zippyshare",str(html))
        googledrive=re.findall(r"<a href=\"([^\"]+)\"[^>]+>Google Drive",str(html))
        mirror=re.findall(r"<a href=\"([^\"]+)\"[^>]+>Mirr",str(html))
        while(len(judul)>len(elsfile)):
              elsfile.append('placeholder')
        while(len(judul)>len(zippyshare)):
              zippyshare.append('placeholder')
        while(len(judul)>len(googledrive)):
              googledrive.append('placeholder')
        while(len(judul)>len(mirror)):
              mirror.append('placeholder')
        html='<div style="padding:10px;">'
        for x in list(zip(judul,elsfile,zippyshare,googledrive,mirror)):
              html+='''
 <div class="mb-1">
<span class="uk-badge" style="
font-size: 9px;
border-radius: 0px;
margin-left: 6px;
background-color: #c5c5c5;
height: 15px;">{}</span>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Elsfile</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Zippyshare</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Googledrive</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">MirrorCreator</a>
</div>
'''.format(x[0],x[1],x[2],x[3],x[4])
        html+='</div>'
        return html
        
    def awsubs(self,url):
        html=self.req.get(url).text
        judul=re.findall(r"<div class=\"dl-title\"[^[]+([^<]+)<",str(html))
        
        solidfiles=re.findall(r"<a href=([^>]+)>Solidfiles</a>",str(html))
        solidfiles=[re.sub(r'"','',str(x)) for x in solidfiles]
        solidfiles=[re.sub(r'\srel=nofollow','',str(x)) for x in solidfiles]
        
        mirror=re.findall(r"<a href=([^>]+)>Mirror</a>",str(html))
        mirror=[re.sub(r'"','',str(x)) for x in mirror]
        mirror=[re.sub(r'\srel=nofollow','',str(x)) for x in mirror]
        
        zippyshare=re.findall(r"<a href=([^>]+)>Zippy",str(html))
        zippyshare=[re.sub(r'"','',str(x)) for x in zippyshare]
        zippyshare=[re.sub(r'\srel=nofollow','',str(x)) for x in zippyshare]

        googledrive=re.findall(r"<a href=([^>]+)>Google",str(html))
        googledrive=[re.sub(r'"','',str(x)) for x in googledrive]
        googledrive=[re.sub(r'\srel=nofollow','',str(x)) for x in googledrive]

        while(len(judul)>len(solidfiles)):
            solidfiles.append('placeholder')
        while(len(judul)>len(mirror)):
            mirror.append('placeholder')
        while(len(judul)>len(zippyshare)):
            zippyshare.append('placeholder')
        while(len(judul)>len(googledrive)):
            googledrive.append('placeholder')
        html='<div style="padding:10px;">'
        escape=lambda x: re.sub(r"&","%26",str(x))
        for x in list(zip(judul,solidfiles,mirror,zippyshare,googledrive)):
             html+='''
 <div class="mb-1">
<span class="uk-badge" style="
font-size: 9px;
border-radius: 0px;
margin-left: 6px;
background-color: #c5c5c5;
height: 15px;">{}</span>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Solidfiles</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">MirrorCreator</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Zippyshare</a>
<a href="api?redirect={}" style="margin-left:5px;font-size:10px;color: #848484;">Googledrive</a>
</div>
'''.format(x[0],escape(x[1]),escape(x[2]),escape(x[3]),escape(x[4]))
        html+='</div>'
        return html
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
    _fansublaler('awsubs','http://awsubs.co/shichisei-no-subaru-episode-8-subtitle-indonesia/')
    
