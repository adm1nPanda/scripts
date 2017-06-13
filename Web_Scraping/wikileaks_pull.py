#———————————
# Script to pull files off wikileaks.org
# usage - python wikileaks_pull.py <url>
# 
# Script pulls all files EXCEPT html files from Wikileaks via HTTP.
# 
# Feel free to make any changes to the code
#———————————




import requests						#Importing required libraries
from bs4 import BeautifulSoup
import os
import sys

class bcolors:						#Class to add color codes to print statement
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def r_find(addr,x):					#Recursive function to traverse directory or download files

	r= requests.get(addr+x,stream=True)		#Get only HTTP headers of file

	#Check if not HTML file	
	if r.headers['Content-Type'] != 'text/html; charset=utf-8' and x != 'index.html':
		if not os.path.exists(addr):		#If local directory doesn’t exist create it
			os.makedirs(addr)
		if not os.path.isfile(addr+x):		#If file, then download
			try:
				print bcolors.OKGREEN+'Extracting file'+bcolors.ENDC,
				print addr+x
			except TypeError:
				print bcolors.FAIL + 'Type error when getting file - ' + bcolors.ENDC + addr
			extractFile = open(addr+x,'w')
			extractFile.write(r.content)
			extractFile.close
			return
		else:					#If file already present in local directory, skip it
			print bcolors.OKBLUE + 'skipping file - ' + bcolors.ENDC + addr,x
			return
	else:						#If not file then find the next recursion tree
		addr = addr+x				
		soup = BeautifulSoup(r.content,"html.parser")

		for a in soup.find_all('a'):
			x = a.get('href')
			if x[0] == '#':
				break 	
			if x != '../':			#Don’t choose the backward recursion
				try:
					r_find(addr,x)	#recursive call
				except TypeError:	
					print 'Type Error for - '+ addr


#Pass the URL as an argument
if len(sys.argv) >= 2:
	base_addr = sys.argv[1] 
	r_find(base_addr,'')
	print 'Finished Extracting'
else:
	print 'usage - python pull.py <URL>'

