from flask import Flask,render_template,request ,jsonify
import requests 

app = Flask(__name__)

apikey="3d5c3498"
@app.route('/detail/<name>')
def detail(name=None):
	URL="http://www.omdbapi.com/"
	PARAMS = {'apikey':apikey,'t':name,'plot' : 'full'}
	r = requests.get(url = URL, params = PARAMS)
	data = r.json()
	return render_template('despmain.html', data=data)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/search/<name>')
def search(name=None):
	return render_template('search.html',name=name)

@app.route('/moviesearch' ,methods=['GET'])
def moviesearch():
	name = request.args.get('name')
	page = request.args.get('page')
	URL = "http://www.omdbapi.com/"
	PARAMS = {'apikey':apikey,'s':name,'page' :page}
	r = requests.get(url = URL, params = PARAMS)
	data = r.json()
	return jsonify(data)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404
