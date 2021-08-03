from dotenv import load_dotenv
from flask import Flask, render_template

import os, requests

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host=os.environ.get('SERVER_HOST'), port=os.environ.get('SERVER_PORT'), debug=True)
