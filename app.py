from flask import Flask, render_template
from flask_paginate import Pagination, get_page_args
import requests
import csv

# Request csv data
data = requests.get('https://gist.githubusercontent.com/the-akira/6b1eeb40ad6a0790460000eb0ae40073/raw/27ddb6bb25acb1b455987c882554f7d54a16c7ac/programming_languages.csv')

app = Flask(__name__)

# Convert csv object into Python List
languages = list(csv.reader(data.text.strip().split('\n')))

def get_lang(offset=0, per_page=10):
    return languages[offset: offset + per_page]

@app.route('/')
def index():
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(languages)
    pag_langs = get_lang(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('home.html',languages=pag_langs,page=page,per_page=per_page,pagination=pagination)

if __name__ == '__main__':
    app.run(debug=True)