from multiprocess import multiprocess, read_args, write_res
import pickle, sys

def fn(name):
	return name

if __name__ == '__main__':
	write_res(multiprocess(fn, read_args()))
	
