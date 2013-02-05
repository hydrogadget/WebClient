from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, Response

import requests
import json

TASK_SERVICE_URL = 'http://localhost:5000'

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = False

@app.route('/')
def show_dashboard():
    entries = []
    return render_template('show_dashboard.html', entries=entries)

# Okay, I don't really understand Python syntax, and routes seem overly tricky, so this probably won't work. If someone knows how to fix it, please do
@app.route('/scheduler')
def show_scheduler():
		 entries = []
		 return render_template('show_scheduler.html', entries=entries)

# Oh god, super hacky proxy thing, don't judge me - eventually will have nginx
@app.route('/current/event', methods=['GET'])
def current_event():
    r = requests.get(TASK_SERVICE_URL + '/current/event')
    return Response(json.dumps(r.json()), status=200, mimetype='application/json')
    
# Oh god, again with the super hacky proxy thing...
@app.route('/add/priority', methods=['POST'])
def add_priority():
    
    event = {'valve':request.form['valve'],
             'command':request.form['command'],
             'duration':request.form['duration'],
             'start_time':request.form['start_time']
             }

    r = requests.post(TASK_SERVICE_URL + "/add/priority", data=event)
    return Response('hi', status=200, mimetype='text/plain')
    
@app.route('/mobile')
def show_mobile_remote():
    return render_template('mobile_remote.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

