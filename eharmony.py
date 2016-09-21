import hashlib,sys,string

wordlist = open('hash.txt','r')
print "START"

for word in wordlist:
    has = open('eHarmony.txt','r')
    hal = hashlib.md5(word.strip())
    hau = hashlib.md5((word.upper()).strip())
    for ehash in has:
        if ehash == hal.hexdigest():
            print word.strip() +' :'+ ehash
        else:
            if ehash == hau.hexdigest():
                print '(Upper)'+ word.strip() +' :'+ ehash
    has.close()
wordlist.close()
print "END"
