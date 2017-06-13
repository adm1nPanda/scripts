import requests
from bs4 import BeautifulSoup
import os
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def r_find(addr,x):

	r= requests.get(addr+x,stream=True)
	
	if r.headers['Content-Type'] != 'text/html; charset=utf-8':
		if not os.path.exists(addr):
			os.makedirs(addr)
		if not os.path.isfile(addr+x):
			try:
				print bcolors.OKGREEN+'Extracting file'+bcolors.ENDC,
				#print addr+x
			except TypeError:
				print bcolors.FAIL + 'Type error when getting file - ' + bcolors.ENDC + addr
			extractFile = open(addr+x,'w')
			extractFile.write(r.content)
			extractFile.close
			return
		else:
			print bcolors.OKBLUE + 'skipping file - ' + bcolors.ENDC + addr,x
			return
	addr = addr+x
	soup = BeautifulSoup(r.content,"html.parser")

	for a in soup.find_all('a'):
		x = a.get('href')
			
		if x != '../':
			try:
				print addr,x
				if not os.path.isdir(addr+x):
					r_find(addr,x)
			except TypeError:
				print 'Type Error for - '+ addr

if len(sys.argv) >= 2:
	base_addr = sys.argv[1] 
	r_find(base_addr,'')
	print 'Finished Extracting'
else:
	print 'usage - python pull.py <URL>'

