
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
noOfFiles = 0
totFiles = 0
for f in fileList:
	pe = pefile.PE(os.path.abspath(os.path.join(fileDir, f)))
	noOfFiles = noOfFiles + 1
	totFiles = totFiles + 1
	try:
		#print pe.DIRECTORY_ENTRY_IMPORT
		for imp in pe.DIRECTORY_ENTRY_IMPORT:
			listdll.append(imp.dll)
			for func in imp.imports:
				listFunc.append(str(imp.dll)+excal+str(func.name))
	except AttributeError:
		print f + "has some problems or does not have imports"
		noOfFiles = noOfFiles - 1	
print "Files processed" + str(totFiles) + " Files not processed" + str(totFiles-noOfFiles)
if noOfFiles > 0:
	print "==========================="
	print "Common dll's in all files"
	print "==========================="
	slistdll = []
	s1listdll = []
	
	for s in listdll:
		if (listdll.count(s) == noOfFiles):
			slistdll.append (s)
	s1listdll =set(slistdll)
	for s in s1listdll:
		print s 
	print "==========================="
	print "Common functions in all files"
	print "==========================="

	s1listFunc = []
	slistFunc = []
	
	for s in listFunc:
		if(listFunc.count(s) == noOfFiles):
			slistFunc.append(s)
	s1listFunc = set(slistFunc)
	for s in s1listFunc:
		print s
		
	
