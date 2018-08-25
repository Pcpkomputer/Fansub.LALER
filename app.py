from flask import Flask,request,url_for,redirect,render_template
from flask_cors import CORS
from yudhaLIB._bypasser import yudhaLIB
from yudhaLIB._fansublaler import _fansublaler
from yudhaLIB._pencarian import _pencarian
import re

app=Flask(__name__)
CORS(app)


@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/api',methods=['GET','POST'])
def api():
    if request.args.get('fansub'):
        kueri=request.args.get('kueri')
        fansub=request.args.get('fansub')
        if fansub=='oploverz':
            return _pencarian(fansub,kueri)
        if fansub=='samehadaku':
            return _pencarian(fansub,kueri)
        if fansub=='awsubs':
            return _pencarian(fansub,kueri)
        if fansub=='anitoki':
            return _pencarian(fansub,kueri)
    if request.args.get('redirect'):
        res=yudhaLIB(request.args.get('redirect'))
        return redirect(res)

    if request.args.get('mode'):
        if request.args.get('mode')=='bypass':
            try:
                url=request.args.get('url')
                if re.search(r"oploverz",str(url)):
                    res=_fansublaler('oploverz',request.args.get('url'))
                    return str(res)
                if re.search(r"samehadaku",str(url)):
                    res=_fansublaler('samehadaku',request.args.get('url'))
                    return str(res)
                if re.search(r"awsubs",str(url)):
                    res=_fansublaler('awsubs',request.args.get('url'))
                    return str(res)
                if re.search(r"anitoki",str(url)):
                    res=_fansublaler('anitoki',request.args.get('url'))
                    return str(res)
                else:
                    return 'error'
            except Exception as r:
                return str(r)

        if request.args.get('mode')=='kueri':
           q=request.args.get('q')
           return str(q)
        else:
            return 'API v1.5.0 FansubLALER'
    else:
        return 'API v1.5.0 FansubLALER'

if __name__=='__main__':
    app.run(debug=True)
