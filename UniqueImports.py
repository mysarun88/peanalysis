
import pefile
import os 
import sys

#input function
fileDir = sys.argv[1]
print fileDir

#list all the files in the directory
fileList = os.listdir(fileDir)
listdll = []
listFunc = []
excal = "!"
for f in fileList:
	pe = pefile.PE(os.path.abspath(os.path.join(fileDir, f)))
	print "==========================="
	print f
	print "==========================="
	
	try:
		#print pe.DIRECTORY_ENTRY_IMPORT
		for imp in pe.DIRECTORY_ENTRY_IMPORT:
			listdll.append(imp.dll)
			for func in imp.imports:
				listFunc.append(str(imp.dll)+excal+str(func.name))
	except AttributeError:
		print f + "has some problems or does not have imports"
		

print "==========================="
print "Common dll"
print "==========================="
slistdll =set(listdll)
for s in slistdll:
	print s

print "==========================="
print "Common functions"
print "==========================="

slistFunc = set (listFunc)

for s in slistFunc:
	print s
