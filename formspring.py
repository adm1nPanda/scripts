import hashlib,sys,string

wordlist = open(sys.argv[1],'r')
writefile = open('formspring-plains.txt','a')
found = 0
xx = ["00","01","02","03","04","05","06","07","08","09"]
for words in wordlist:
	i=0
	
	while i<100:
		has = open("formspring.txt",'r')
		if i<10:
			salted = xx[i]+words.strip()
		else:		
			salted = str(i)+words.strip()

		ha = hashlib.sha256(salted)
		brutetext = ha.hexdigest().strip()

		for dbhash in has:
			if (dbhash.strip() == brutetext):
				print "found : hash - " + dbhash.strip() + "  plaintext - " + words.strip()
				writefile.write("found : hash - " + dbhash.strip() + "  plaintext - " + words.strip())
				found +=1
			#print salted +'  ' + dbhash.strip() + '  ' + brutetext
		i+=1
		has.close()	

writefile.write("\n found hashes : "+str(found))
wordlist.close()
writefile.close()
