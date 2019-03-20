import zipfile
import os
import fnmatch
import re
import glob
import time
import sys

if len(sys.argv) < 2:
	print ()
	print ("UUID2Name v0.1 by Petro Dudi (pdudis@gmail.com).")
	print ("Substitutes the UUID filenames of .i6z files with their Entity names.")
	print ()
	print ("Usage: UUID2Name.py <path to folder with UUID .i6z filenames>")
	sys.exit()
else:
	aPath = sys.argv[1]

os.chdir(aPath)

mypath = aPath + '\*.i6z'
myfiles = glob.glob(mypath)

history = []
filecount = 0

for file in myfiles:
	logme = open("Process_Log.csv", "a")
	myzipfile = zipfile.ZipFile(file, 'r')
	for name in myzipfile.namelist():
		if fnmatch.fnmatch(name, 'manifest.xml'):
			zopen = myzipfile.open(name)
			for line in zopen:
				m = re.search(b'(?<=\.i6d\"\>)(.*?)(?=\<\/name\>)', line)
				if m:
					entity_name = m.group(0).decode('utf-8')
					zopen.close()
					for fileitem in history:
						if fileitem.upper() == entity_name.upper():
							filecount = filecount + 1
							entity_name = entity_name + '_' + str(filecount)
					history.append(entity_name)
					conv_string = file + " -> " + entity_name
					conv_string_csv = file + ";" + entity_name
					print (conv_string)
					logme.write("%s\n" % conv_string_csv)
					break
					
	logme.close()		
	myzipfile.close()
	entity_filename = entity_name + '.i6z'
	
	os.rename(file, entity_filename)