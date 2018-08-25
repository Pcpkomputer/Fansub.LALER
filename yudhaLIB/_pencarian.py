import re
import requests

class fansub:
    req=requests.Session()
    def oploverz(self,query):
        url='https://www.oploverz.in/?s={}&post_type=post'.format(query)
        html=self.req.get(url).text
        arr=re.findall(r"<div class=\"thumb\">(\s+|)<a href=\"([^\"]+)\" title=\"([^\"]+)\">",str(html))
        arr=[(x[1],x[2]) for x in arr]
        html='<div style="padding:15px;">'
        for i in arr:
            html+='''
<span id="{}" class="uk-badge kueri" style="
                                    font-size: 10px;
                                    border-radius: 0px;
                                    width: 100%;
                                    margin-bottom: 10px;
                                    margin-left: 6px;
                                    /* height: 15px; */
                                    height: auto;
                                    ">{}</span>
'''.format(i[0],i[1])
        html+='</div>'
        return html
    def samehadaku(self,query):
        url='https://www.samehadaku.tv/?s={}'.format(query)
        html=self.req.get(url).text
        arr=re.findall(r"<a href=\"([^\"]+)\" title=\"([^\"]+)\" class=\"post-thumb\">",str(html))
        html='<div style="padding:15px;">'
        for i in arr:
            html+='''
<span id="{}" class="uk-badge kueri" style="
                                    font-size: 10px;
                                    border-radius: 0px;
                                    width: 100%;
                                    margin-bottom: 10px;
                                    margin-left: 6px;
                                    /* height: 15px; */
                                    height: auto;
                                    ">{}</span>
'''.format(i[0],i[1])
        html+='</div>'
        return html
    def awsubs(self,query):
        url='http://awsubs.co/?s={}&post_type=release'.format(query)
        html=self.req.get(url).text
        arr=re.findall(r"<div class=\"kirizona\">\s+<h2><a href=\"([^\"]+)\" title=\"([^\"]+)\">",str(html))
        html='<div style="padding:15px;">'
        for i in arr:
            html+='''
<span id="{}" class="uk-badge kueri" style="
                                    font-size: 10px;
                                    border-radius: 0px;
                                    width: 100%;
                                    margin-bottom: 10px;
                                    margin-left: 6px;
                                    /* height: 15px; */
                                    height: auto;
                                    ">{}</span>
'''.format(i[0],i[1])
        html+='</div>'
        return html
    def anitoki(self,query):
        url='http://anitoki.com/?s={}&post_type=release'.format(query)
        html=self.req.get(url).text
        arr=re.findall(r"<div class=\"thumb\">\s+<a href=\"([^\"]+)\" title=\"([^\"]+)\">",str(html))
        html='<div style="padding:15px;">'
        for i in arr:
            html+='''
<span id="{}" class="uk-badge kueri" style="
                                    font-size: 10px;
                                    border-radius: 0px;
                                    width: 100%;
                                    margin-bottom: 10px;
                                    margin-left: 6px;
                                    /* height: 15px; */
                                    height: auto;
                                    ">{}</span>
'''.format(i[0],i[1])
        html+='</div>'
        return html

def _pencarian(f,query):
    if f=='oploverz':
        return fansub().oploverz(query)
    if f=='samehadaku':
        return fansub().samehadaku(query)
    if f=='awsubs':
        return fansub().awsubs(query)
    if f=='anitoki':
        return fansub().anitoki(query)
    else:
        return 'error'
