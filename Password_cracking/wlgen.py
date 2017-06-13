import string,sys

wlist = open (sys.argv[1],'r')
wwlist =  open ('genlist','w')

for word in wlist:
	aa = (word.strip()).upper()
	wwlist.write(aa+"\n")
#	for i in range(0,99):
#		wwlist.write(aa+str(i)+'\n')
#	for ia in range(1940,2050):
#		wwlist.write(aa+str(ia)+'\n')
		

wlist.close()
wwlist.close()
