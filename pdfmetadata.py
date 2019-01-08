#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      W8-64
#
# Created:     08/01/2019
# Copyright:   (c) W8-64 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pdf
import optparse
from pdf import PdfFileReader

def printMeta(fileName):
    pdfFile = PdfFileReader(file(fileName,'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print '[*] PDF MetaData for: ' + str(fileName)

    for metaItem in docInfo:
        print '[+] ' + metaItem + ':' + docInfo[metaItem]
def main():
    parser = optparse.OptionParser('usage %prog' + "-F <PDF file name>")
    parser.add_option('-F', dest='fileName', type='string',help='specify PDF file name')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName == None:
        print parser.usage
    else:
        printMeta(fileName)

if __name__ == '__main__':
    main()
