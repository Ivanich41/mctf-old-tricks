import string
from flask import Flask, render_template, session, request, abort
import os
import random
import secrets

app = Flask(__name__)
secret = secrets.token_urlsafe(16)
app.config['SECRET_KEY'] = secret 

def newCookie():
    cookie = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(25))
    session['data'] = cookie
    print(session['data'])


@app.route("/", methods=["GET"])
def home():
    if not session.get("data"):
        newCookie()
    return render_template('home.html')


@app.route("/flag", methods=["GET"])
def check():
	if not session.get("data"):
		newCookie()
	headersa = dict(request.headers)
	if "Links" in headersa['User-Agent']:
		return render_template('flag.html', FLAG = os.environ["FLAG"])
	else:
		return "Ты правда думал, что всё так просто?"
    
@app.route('/data.html')
def data():
    if request.headers.get('X-Requested-With') != 'XMLHttpRequest':
        abort(403) # Запретить доступ, если запрос не AJAX
    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=False, host=os.environ['IP'], port=os.environ['PORT'])

