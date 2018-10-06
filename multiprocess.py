from multiprocessing import Pool

import sys, pickle

def multiprocess(fn, args_list):
	with Pool() as pool:
		res_list = pool.starmap(fn, args_list)
	return res_list

def read_args():
	return pickle.loads(sys.stdin.buffer.read())

def write_res(res):
	return sys.stdout.buffer.write(pickle.dumps(res))
	
