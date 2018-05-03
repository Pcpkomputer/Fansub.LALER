from flask import Flask, render_template, url_for, request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import re
from os import environ
from re import *
from module.oploverz import oploverz
from module.awsubs import awsubs
from module.samehadaku import samehada
from module.animepahe import animepahe

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def antarmuka():
	error=None
	try:
		if request.method=="POST":
			link=request.form['tautan']
			oplo=re.search(r"oploverz",str(link))
			samehad=re.search(r"samehada",str(link))
			awsu=re.search(r"awsubs",str(link))
			anipahe=re.search(r"animepahe",str(link))
			anipahe_auth=False
			oplo_auth=False
			awsu_auth=False
			samehadaku_auth=False
			if anipahe:
				anipahe_auth=True
				p720,p480=animepahe(link)
				return render_template("konten.html",p720=p720,p480=p480,anipahe_auth=anipahe_auth)
			if samehad:
				samehadaku_auth=True
				nama_same, uf, cu, gd, zs, sc, mu=samehada(link)
				return render_template("konten.html",nama_same=nama_same,uf=uf, cu=cu, gd=gd, zs=zs, sc=sc, mu=mu, samehadaku_auth=samehadaku_auth)
			if awsu:
				awsu_auth=True
				nama, solidfiles, drive, datafile=awsubs(link)
				return render_template("konten.html",nama=nama,solidfiles=solidfiles,drive=drive,datafile=datafile, awsu_auth=awsu_auth)
			if oplo:
				oplo_auth=True
				nama_oplo, elsfile, drive_oplo, zippy, mirror=oploverz(link)
				return render_template("konten.html",nama_oplo=nama_oplo,elsfile=elsfile,drive_oplo=drive_oplo,zippy=zippy,mirror=mirror, oplo_auth=oplo_auth)
			else:
				error="Sehat, Mas?"
				e=error
				return render_template("konten.html", e=e)


	except Exception as e:
		#error="GOBLOK"
		return render_template("konten.html", e=e)
	return render_template('konten.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
