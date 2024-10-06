from flask import Flask, render_template,request,redirect,url_for
import pip._vendor.requests 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def dogs():
    return render_template('dogs.html')

if __name__ == "__main__":
    app.run(debug=True)