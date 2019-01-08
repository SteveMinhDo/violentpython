#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      W8-64
#
# Created:     31/12/2018
# Copyright:   (c) W8-64 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from _winreg import *

def hex2addr(val):
  address = ''
  for ch in val:
    address += ('%02x '% ord(ch))
    address = address.replace(' ',':')[0:17]
  return address

def main():

  print 'Reading recent WiFi connections...'
  netlist = 'SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged'
  try:
    key = OpenKey(HKEY_LOCAL_MACHINE, netlist,0,KEY_READ | KEY_WOW64_64KEY )
  except:
    key = OpenKey(HKEY_LOCAL_MACHINE, netlist,0,KEY_READ | KEY_WOW64_32KEY )
  print '\n**Networks You have Joined:'
  for i in range(100):
  	try:

	  	guid = EnumKey(key, i)
	 	netKey = OpenKey(key, str(guid))
	  	(n, addr, t) = EnumValue(netKey, 5)
	  	(n, name, t) = EnumValue(netKey, 4)
	  	macAddress = hex2addr(addr)
	  	ssid = str(name)
	  	print '[*] ' + ssid + ', ' + macAddress
	  	CloseKey(netKey)

	except Exception,e:
	  	print '[-] Error ='+str(e)

if __name__ == '__main__':
	main()
