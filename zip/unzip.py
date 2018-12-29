import zipfile
zFile = zipfile.ZipFile("readme.zip")
passFile = open("dic.txt")
for line in passFile.readlines():
    password = line.strip("\n")
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password  + '\n'
        exit(0)
    except Exception, e:
        pass
print "[-] No password available"
