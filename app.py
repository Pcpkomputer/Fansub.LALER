from flask import Flask, render_template, url_for, request, redirect, jsonify, json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import argparse
import os
import psycopg2
import re
from os import environ
from re import *
from module.oploverz import oploverz
from module.awsubs import awsubs
from module.samehadaku import samehada
from module.animepahe import animepahe
from module.anitoki import anitoki
from module.drivenime import drivenime
from module.query.oploverz import query_oploverz
from module.query.samehadaku import query_samehadaku
from module.query.awsubs import query_awsubs
from module.query.anitoki import query_anitoki
from module.query.drivenime import drivenime_query
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import form, BooleanField, StringField, TextField, PasswordField, validators
from wtforms.validators import InputRequired, Email, Length
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from module.bypasser.bagilagi import bagilagi_bypass
from module.direct.zippyshare import zippyshare_direct
from module.direct.googledrive import googledrive_direct
from module.pahein import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'apasehanjenggkjelas'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:p@localhost/fansublaler"
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'

class FormDaftar(FlaskForm):
	email = StringField('email', validators=[InputRequired(), Email(message='Email Salah'), Length(max=50)])
	username = StringField('username', validators=[InputRequired(), Length(min = 4, max=15)])
	password = PasswordField('password', validators=[InputRequired(), Length(min = 4, max=80)])
	
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(80), nullable=False)

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.username

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/api')
def api():
	mode = request.args.get('mode')
	if mode=='directlink':
		hosting = request.args.get('hosting')
		link = request.args.get('link')
		if hosting=='zippyshare':
			hasil=zippyshare_direct(link)
			return hasil
		if hosting=='googledrive':
			hasil=googledrive_direct(link)
			return hasil

	if mode=='dashboard':
		fansub = request.args.get('fansub')
		query = request.args.get('query')
		if fansub=='drivenime':
			hasil=drivenime_query(query)
			return hasil
		if fansub=='anitoki':
			hasil=query_anitoki(query)
			return hasil
		if fansub=='awsubs':
			hasil=query_awsubs(query)
			return hasil
		if fansub=='oploverz':
			hasil=query_oploverz(query)
			return hasil
		if fansub=='samehadaku':
			hasil=query_samehadaku(query)
			return hasil
		if fansub is None:
			return '????????????????????'
		elif query is None:
			return '????????????????????'
		return jsonify(tes='tes'+str(fansub)+str(query))
	else:
		return 'API FansubLaler v1.0.0'
	return 'API FansubLaler v1.0.0'

@app.route('/dashboard')
@login_required
def dashboard():
	return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('antarmuka'))

@app.route('/register', methods=["GET","POST"])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('dashboard'))
	form = FormDaftar()
	if form.validate_on_submit():
		try:
			email=form.email.data
			username=form.username.data
			password=form.password.data
			user = User(username,email,password)
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('login'))
		except Exception as e:
			duplikat=re.search(r"duplicate key value violates",str(e))
			if duplikat:
				e="Maaf, email atau username telah terdaftar"
			return render_template('register.html', form=form, e=e)

	return render_template('register.html', form=form)

@app.route('/login', methods=["GET","POST"])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('dashboard'))
	if request.method=="POST":
		username=request.form['username']
		password=request.form['password']
		user = User.query.filter_by(username=username).first()
		if not user:
			s='Tidak ditemukan username tersebut silakan mendaftar'
			return render_template('login.html', s=s)
		if user.password==password:
			login_user(user)
			return redirect(url_for('antarmuka'))
		else:
			e='Password yang dimasukkan salah'
			return render_template('login.html', e=e)
	return render_template('login.html')



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
			anitoket=re.search(r"anitoki",str(link))
			drivememeq=re.search(r"drivenime",str(link))
			pahein=re.search(r"pahe.in",str(link))
			pahein_auth=False
			drivenime_auth=False
			anitoki_auth=False
			anipahe_auth=False
			oplo_auth=False
			awsu_auth=False
			samehadaku_auth=False
			if pahein:
				pahein_auth=True
				pahein_berkas, pahein_gd, pahein_utb, pahein_mega=pahein_hajar(link)
				return render_template("konten.html", pahein_berkas=pahein_berkas, pahein_gd=pahein_gd, pahein_utb=pahein_utb, pahein_mega=pahein_mega, pahein_auth=pahein_auth)
			if drivememeq:
				drivenime_auth=True
				drivenime_reso,drivenime_gd=drivenime(link)
				return render_template("konten.html", drivenime_reso=drivenime_reso, drivenime_gd=drivenime_gd, drivenime_auth=drivenime_auth)
			if anitoket:
				anitoki_auth=True
				namatoket, gdtoket, dttoket, zippytoket, uppittoket, mirrortoket=anitoki(link)
				return render_template("konten.html", namatoket=namatoket, gdtoket=gdtoket, dttoket=dttoket, zippytoket=zippytoket, uppittoket=uppittoket, mirrortoket=mirrortoket, anitoki_auth=anitoki_auth)
			if anipahe:
				anipahe_auth=True
				p720,p480=animepahe(link)
				return render_template("konten.html",p720=p720,p480=p480,anipahe_auth=anipahe_auth)
			if samehad:
				samehadaku_auth=True
				nama_same, cu, gd, zs, mu=samehada(link)
				return render_template("konten.html",nama_same=nama_same, cu=cu, gd=gd, zs=zs, mu=mu, samehadaku_auth=samehadaku_auth)
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
