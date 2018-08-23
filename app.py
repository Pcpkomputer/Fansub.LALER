from flask import Flask,request,url_for,redirect,render_template
from flask_cors import CORS
from yudhaLIB._bypasser import *
from yudhaLIB._fansublaler import _fansublaler
from yudhaLIB._pencarian import *

app=Flask(__name__)
CORS(app)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/api',methods=['GET','POST'])
def api():
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