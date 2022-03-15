import git
import os

from app import app
from pathlib import Path

@app.route('/')
@app.route('/index')
def index():
	return "Hello :)"

@app.route('/git/pull')
def git_pull():
	g = git.Git('~/tracker.colinmcglone.ca')
	g.pull('origin', 'master')
	Path('~/tmp/restart.txt').touch()
	return 'pulling...'

@app.route('/errors')
def errors():
	e_path = os.getcwd()+'/app/static/error.log'
	errors = Path(e_path).read_text()

	return errors