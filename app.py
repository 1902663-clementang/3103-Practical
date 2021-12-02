import re
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import escape
import cgi

inlist = '<>'

app = Flask(__name__, template_folder='template')

dic = {}


@app.route("/")
def login():
    return render_template('search.html')



@app.route("/searchPost",  methods=['POST'])
def logining():
    search = request.form.get('Search')
    if "'" in search or '"'in search:
        return render_template('search.html')
    else:
        return render_template('dashboard.html' , username = search)



if __name__== "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
