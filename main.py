
import subprocess, pickle

from subprocess import PIPE


if __name__ == '__main__':
	p = subprocess.Popen(['python', 'process.py'], stdin=PIPE, stdout=PIPE, stderr=PIPE)	
	output, err = p.communicate(pickle.dumps([['alex'], ['apple'], ['app']]))
	print('Output:', pickle.loads(output) if output else '')
	print('Error:', err.decode())
