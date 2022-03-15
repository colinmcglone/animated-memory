import sys, os

e_path = os.getdwd()+'app/static/error.log'
errfile = open(e_path, 'a')
os.close(sys.stderr.fileno())
os.dup2(errfile.fileno(), sys.stderr.fileno())

INTERP = os.path.join(os.environ['HOME'], 'tracker.colinmcglone.ca', 'venv', 'bin', 'python3')
if sys.executable != INTERP:
	os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('app')
from app import app as application
