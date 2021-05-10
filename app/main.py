from flask import Flask, send_file, request, redirect, url_for
import io
import base64
import logging
import sys, os
sys.path.append('./')
from utils import *

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/send_mail")
def send_mail_app():
    send_mail()
    return hello()

@app.route('/pixel.gif')
def returnPixel():
    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
    gif_str = base64.b64decode(gif)
    app.logger.info("Action Tracked")
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')

@app.route('/pixelwithParams.gif')
def returnPixelparams():
    headerUser = request.headers.get('User-Agent')
    headerHost = request.headers.get('Host')
    logging.info(headerUser)
    gif = 'R0lGODlhAQABAIAAAP///////yH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='
    gif_str = base64.b64decode(gif)
    return send_file(io.BytesIO(gif_str), mimetype='image/gif')