#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      W8-64
#
# Created:     07/01/2019
# Copyright:   (c) W8-64 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
def returnDir():
    dirs=['C:\\Recycler\\','C:\\Recycled\\','C:\\$Recycle.Bin\\']
    for recycleDir in dirs:
        if os.path.isdir(recycleDir):
            return recycleDir
    return None

def main():
    dirList  = os.listdir(returnDir())

if __name__ == '__main__':
    main()
