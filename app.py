from flask import Flask, render_template,request,redirect,url_for
import pip._vendor.requests as requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dogs')
def dogs():
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    data = response.json()
    image = data["message"]
    print(data)
    return render_template('dogs.html', dogImage = image)

@app.route('/cats')
def cats():
    response = requests.get('https://cataas.com//cat?json=true')
    data = response.json()
    print(data)
    catPhoto = data["_id"]
    return render_template('cats.html', catImage = catPhoto)
if __name__ == "__main__":
    app.run(debug=True)