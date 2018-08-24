import re
import requests

__GET=re.compile(r"(awcar.icu|bolaoke.club|short.awsubs|www.tetew.info|www.anjay.info|hexafile.net|greget.space|awsubsco.cf)")
headers={"User-Agent" : "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"}
req=requests.Session()

class jamu:
    def hexafile_net(self,x):
        self.html=req.get(x,headers=headers).text
        self.link=re.search(r"\"([^\"]+)\",e=0,f=a",str(self.html)).group(1)
        return self.link
    def tetew_info(self,x):
        self.html=req.get(x,headers=headers).text
        self.link=re.search(r";window.location=\"([^\"]+)\";}count--",str(self.html)).group(1)
        return self.link
    def anjay_info(self,x):
        self.html=req.get(x,headers=headers).text
        self.link=re.search(r";window.location=\"([^\"]+)\";}count--",str(self.html)).group(1)
        return self.link
    def greget_space(self,x):
        self.html=req.get(x,headers=headers).text
        self.link=re.search(r"<div class=\"download-link\"[^>]+><a href=\"([^\"]+)\"",str(self.html)).group(1)
        return self.link
    def awsubsco_cf(self,x):
        self.html=req.get(x,headers=headers).text
        self.link=re.search(r"var d_link[^']+'([^']+)\';",str(self.html)).group(1)
        self.link=re.sub(r"%3A",":",str(self.link))
        self.link=re.sub(r"%2F","/",str(self.link))
        return self.link
    def short_awsubs(self,x):
        self.html=req.get(x,headers=headers).text
        self.link=re.search(r"window.location=\"([^\"]+)\";}count--;",str(self.html)).group(1)
        return self.link
    def bolaoke_club(self,x):
        self.html=req.get(x,headers=headers).text
        self.id=re.search(r"/?id=(.*)",str(x)).group(1)
        self.html=req.post('http://www.bolaoke.club/prancis-berharap-pada-paul-pogba/',headers=headers,data={'get':self.id}).text
        self.link=re.search(r"function changeLink\(\){var a='([^']+)';window",str(self.html)).group(1)
        self.link=req.get(self.link,headers=headers).url
        return self.link
    def awcar_icu(self,x):
        self.html=req.get(x,headers=headers).text
        self.id=re.search(r"/?id=(.*)",str(x)).group(1)
        self.html=req.post('http://awcar.icu/prepared-razors-lamborghini-recall-aventador-sv/',headers=headers,data={'get':self.id}).text
        self.link=re.search(r"function changeLink\(\){var a='([^']+)';window",str(self.html)).group(1)
        self.link=req.get(self.link,headers=headers).url
        return self.link
        
    
def pengecek(x):
    if re.search(r"greget.space/\?r=.*",str(x)):
        l=req.get(x,headers=headers).url
        return l
    if re.search(r"greget.space",str(x)):
        bypass=jamu()
        return bypass.greget_space(x)
    if re.search(r"hexafile.net",str(x)):
        bypass=jamu()
        return bypass.hexafile_net(x)
    if re.search(r"tetew.info", str(x)):
        bypass=jamu()
        return bypass.tetew_info(x)
    if re.search(r"anjay.info", str(x)):
        bypass=jamu()
        return bypass.anjay_info(x)
    if re.search(r"awsubsco.cf",str(x)):
        bypass=jamu()
        return bypass.awsubsco_cf(x)
    if re.search(r"short.awsubs",str(x)):
        bypass=jamu()
        return bypass.short_awsubs(x)
    if re.search(r"bolaoke.club",str(x)):
        bypass=jamu()
        return bypass.bolaoke_club(x)
    if re.search(r"awcar.icu",str(x)):
        bypass=jamu()
        return bypass.awcar_icu(x)

def yudhaLIB(x):
    link=x
    link=req.get(link,headers=headers).url
    val=pengecek(link)
    while re.search(__GET,str(val)):
        val=pengecek(val)
    else:
        return val

