import zipfile
import argparse
from threading import Thread
def extractFile(zFile,password):
    try:
        print password
        zFile.extractall(pwd=password)
        print '[+] Found password ' + password
    except:
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zname", help="this is the zip file")
    parser.add_argument("dname", help="this is the dictionary file")
    args = parser.parse_args()
    zname = args.zname
    dname = args.dname
    zFile = zipfile.ZipFile(zname)
    print 'zname ' + zname
    passFile = open(dname)
    for line in passFile.readlines():
        #print "line" + line
        #print "zFile" + zFile
        password = line.strip("\n").strip(' ')
        t = Thread(target=extractFile, args = (zFile, password))
        t.start()
if __name__ == "__main__":
    main()
