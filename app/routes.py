import git

from app import app

@app.route('/')
@app.route('/index')
def index():
	return "Hello :)"

@app.route('/git/pull')
def git_pull():
	repo = git.Repo('~/tracker.colinmcglone.ca')
	repo.remotes.origin.pull()