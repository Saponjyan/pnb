'''cs50
Flask
Flask-Session
requests
python passenger_wsgi.py
Enter to the virtual environment.To enter to virtual environment, run the command:
source /home/zngxfdcg/virtualenv/pnb/3.10/bin/activate && cd /home/zngxfdcg/pnb
'''
import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify, send_file
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required
from datetime import datetime

import json
#####################################################################################
# для фонового бота
# import logging
# from logging.handlers import RotatingFileHandler

# # Настройка логирования
# log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# # # Указать путь к файлу для логов
# log_file = 'app.log'

# # # Создание объекта логирования
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# # Создание обработчика для записи в файл
# file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024*10, backupCount=5)
# file_handler.setFormatter(log_formatter)
# logger.addHandler(file_handler)

# # Убираем вывод логов в консоль
# logger.propagate = False

##########################################################################################
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///pnb.db")




@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
# @login_required
def index():
    return redirect("/pnb")



@app.route("/pnb", methods=["GET", "POST"])
def pnb():
    """pnb"""

    pcounts = int(db.execute(f"SELECT COUNT(*) FROM users WHERE choose = 'pinky';")[0]['COUNT(*)'])
    bcounts = int(db.execute(f"SELECT COUNT(*) FROM users WHERE choose = 'brain';")[0]['COUNT(*)'])
    pnbcounts = int(db.execute(f"SELECT COUNT(*) FROM users WHERE choose = 'pnb';")[0]['COUNT(*)'])
    pcount = pcounts / ((pcounts + bcounts + pnbcounts)/100)
    bcount = bcounts / ((pcounts + bcounts + pnbcounts)/100)
    pnbcount = int(100 - int(pcount) - int(bcount))

    return render_template("pnb.html",pcount = pcount, bcount = bcount,pnbcount = pnbcount)



@app.route("/pcount", methods=["GET", "POST"])
def pcount():
    """pcount"""
    try:
        w_adress = request.cookies['wallet']
        ip_address = request.remote_addr
        choose = "pinky"
        db.execute("INSERT INTO users (time, wallet, ip, choose) VALUES ( :time, :wallet, :ip, :choose)",
                        time=str(datetime.now()),
                        wallet=w_adress,
                        ip=ip_address,
                        choose=choose)
    except Exception as e: pass
    return redirect("/")

@app.route("/bcount", methods=["GET", "POST"])
def bcount():
    """bcount"""
    try:
        w_adress = request.cookies['wallet']
        ip_address = request.remote_addr
        choose = "brain"
        db.execute("INSERT INTO users (time, wallet, ip, choose) VALUES ( :time, :wallet, :ip, :choose)",
                        time=str(datetime.now()),
                        wallet=w_adress,
                        ip=ip_address,
                        choose=choose)
    except Exception as e: pass
    return redirect("/")

@app.route("/pnbcount", methods=["GET", "POST"])
def pnbcount():
    """pnbcount"""
    try:
        w_adress = request.cookies['wallet']
        ip_address = request.remote_addr
        choose = "pnb"
        db.execute("INSERT INTO users (time, wallet, ip, choose) VALUES ( :time, :wallet, :ip, :choose)",
                        time=str(datetime.now()),
                        wallet=w_adress,
                        ip=ip_address,
                        choose=choose)
    except Exception as e: pass
    return redirect("/")





@app.route("/sorry", methods=["GET", "POST"])
def sorry():
    """sorry"""
    if request.method == "POST":
        return render_template("sorry.html")
    else:
        return render_template("sorry.html")



@app.route("/logo", methods=["GET", "POST"])
def logo():
    """logo pnb"""
    return send_file('static/images/logo/brain_32_32.png', mimetype='image/jpeg')
if __name__ == '__main__':
    app.run(debug=True)


