import string

lastname =open('facebook-lastnames.txt','r')
newtxt =open("new.txt",'w')

for x in range(0,10000):
    for name in lastname:
        newtxt.write(name.strip()+str(x)+"\n")
        print name.strip()+str(x)
lastname.close()
newtxt.close()
    
