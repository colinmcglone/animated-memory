import git

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