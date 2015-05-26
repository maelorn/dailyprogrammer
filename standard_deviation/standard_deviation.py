import sys
import math
# for python 3 just do import statistics statistics.stdev(l)


def stdev(*args):
	# mean of the list
	mean = sum(*args)/len(*args)

	# squared difference

	sdiff = [ (x - mean)*(x-mean) for x in l]
	print(math.sqrt(sum(sdiff)/10))


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("give argument list")
	l = [int(x) for x in sys.argv[1:]]
	stdev(l)