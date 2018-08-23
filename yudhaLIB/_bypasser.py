import re
import requests

__GET=re.compile(r"(www.tetew.info|www.anjay.info|hexafile.net|greget.space)")
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

def yudhaLIB(x):
    link=x
    val=pengecek(link)
    while re.search(__GET,str(val)):
        val=pengecek(val)
    else:
        return val
