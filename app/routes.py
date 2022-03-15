import git
import os

from app import app
from pathlib import Path
from flask import request

@app.route('/')
@app.route('/index')
def index():
	return "Hello :)"

@app.route('/git/pull', methods=['GET', 'POST'])
def git_pull():
	if request.method == 'POST':
		return 'test'

	g_path = os.getcwd()
	g = git.Git(g_path)
	g.pull('origin', 'master')
	Path(os.getcwd()+'/tmp/restart.txt').touch()
	return 'pulling...'

@app.route('/errors')
def errors():
	e_path = os.getcwd()+'/app/static/error.log'
	errors = Path(e_path).read_text()

	return errors

@app.route('/new_test')
def test():
	return 'wowzers!'