from flask import Flask, render_template, url_for, request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from re import *
from module.oploverz import oploverz
from module.awsubs import awsubs

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def antarmuka():
	error=None
	try:
		if request.method=="POST":
			link=request.form['tautan']
			"""x1="480p"
			x2="720p"
			x3="720p 10bit"
			x4="480p mp4"
			x5="720p mp4"""
			oplo=re.search(r"oploverz",str(link))
			awsubs=re.search(r"awsubs",str(link))
			if awsubs:
				nama, solidfiles, drive, datafile=awsubs(link)
				return render_template("konten.html",nama=nama,solidfiles=solidfiles,drive=drive,datafile=datafile)
			if oplo:
				nama_oplo, elsfile, drive_oplo, zippy, mirror=oploverz(link)
				return render_template("konten.html",nama_oplo=nama_oplo,elsfile=elsfile,drive_oplo=drive_oplo,zippy=zippy,mirror=mirror)
			else:
				error="Sehat, Mas?"
				e=error
				return render_template("konten.html", e=e)


	except Exception as e:
		#error="GOBLOK"
		return render_template('konten.html', e=e, error=error)
	return render_template('konten.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
