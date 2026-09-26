import os
from flask import Flask, render_template
from generator.novel import generate_novel

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('novel.html', novel=generate_novel())

@app.get('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
