import hashlib,sys,string

wordlist = open('facebook-firstnames.txt','r')
print "START"
hal = hashlib.md5()
hau = hashlib.md5()
for word in wordlist:
    has = open('eHarmony.txt','r')
    hal.update(word)
    hau.update(word.upper())
    for ehash in has:
        if(ehash == hal.hexdigest()):
            print word +' :'+ ehash
        else:
            if(ehash == hau.hexdigest()):
                print '(Upper)'+ word +' :'+ ehash
    has.close()
wordlist.close()
print "END"
