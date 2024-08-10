# app.py
from flask import Flask, request, render_template, jsonify
from scraper import scrape_website

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape')
def scrape():
    url = request.args.get('url')
    if url:
        pages = scrape_website(url)
        return jsonify(count=len(pages), pages=pages)
    return jsonify(count=0, pages=[])

if __name__ == '__main__':
    app.run(debug=True)
    