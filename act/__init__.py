import sys
import os
def main():
	args = ""
	for a in sys.argv[1:]:
		args += " " + str(a) 
	os.system("actDeact -a " + args)
