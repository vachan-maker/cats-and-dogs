from flask import Flask, render_template,request,redirect,url_for
import pip._vendor.requests 

app = Flask(__name__)

@app.route('/')
def index():
    return 