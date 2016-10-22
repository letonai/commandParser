import os,time,re
import subprocess as sp

FILE="/home/pi/command.list"

class CommandParser(object):

	def __init__(self):
		print "hi"

	def getCommand(self,command):
		file = open(FILE,"r+")
		cmd = file.readlines()
		
		i=0
		for c in cmd:
			c=c.rstrip('\n')
			if c.startswith(command):
				return str(c.split(":")[1])
	 
			i=+1
		file.close()
		return False
	
	def getList(self):
		file = open(FILE,"r+")
	        cmd = file.readlines()
		lst=""
		for c in cmd:
			c=c.rstrip('\n')
			lst+=","+str(c.split(':')[0])
		return	re.sub("^,","",lst)
	
	def runAndReturn(self,command):
		ret=str(sp.check_output([command],shell=True)[:-1])
		return ret
	
	
	
	
#	print "Comando: "+getCommand("carga")
#	print getList()
#	print runAndReturn(getCommand("ip"))
