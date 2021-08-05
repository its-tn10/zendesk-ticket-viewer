from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for

import os, requests, utils

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('view'))

@app.route('/view/', defaults={'page': 1})
@app.route('/view/<int:page>')
def view(page):
    try:
        tickets = utils.get_page(page)

        return render_template('table.html', tickets=tickets[1], pages=tickets[0])
    except Exception as error:
        return render_template('error.html', error=str(error))

@app.route('/ticket/<int:ticket_id>')
def ticket(ticket_id):
    try:
        ticket = utils.get_ticket(ticket_id)
        ticket['created_at'] = utils.parse_timestamp(ticket['created_at'], '%m/%d/%Y, %H:%M:%S')

        return render_template('ticket.html', ticket=ticket)
    except Exception as error:
        return render_template('error.html', error=str(error))

if __name__ == '__main__':
    app.run(host=os.environ.get('SERVER_HOST'), port=os.environ.get('SERVER_PORT'), debug=True)
