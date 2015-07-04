import json

from flask import render_template

def home():
	some_other = {}
	some_other['name'] = 'Bob'

	some_person = {}
	some_person['name'] = 'Alice'

	some_list = (some_other, some_person)

	return render_template('old_things.html', name=json.dumps(some_person))

def index():
	return render_template('index.html')