#!/usr/bin/env python3
import os
from operator import itemgetter
import notes_dictionaries as notesDict


PATH_TO_USE = ".."


class FileLineWrapper(object):

	def __init__(self, f):
		self.f = f
		self.line = 0

	def close(self):
		return self.f.close()

	def readline(self):
		self.line += 1
		return self.f.readline()


def printOsTree():
	for path, dirs, files in os.walk(PATH_TO_USE):
		print(path)
		for f in files:
			print('\t' + f)

def list_files():
	file_paths = []
	for root, directories, files in os.walk(PATH_TO_USE):
		for filename in files:
			filepath = os.path.join(root, filename)
			if "pycache" not in filepath:
				file_paths.append(filepath)

	return file_paths

def printlist(alist):
	for i in alist:
		print(i)


def list_notes():
	paternList = notesDict.magicFileExtentions
	fulllist = list_files()
	alist = []
	for i in fulllist:
		for extention in paternList:
			if extention in i:
				alist.append(i)
	return alist


def makeStringBeaultiful(string):
	st = ""
	st = string.replace("\n", "").strip()
	return st


## DONE Verify all super/subfolder for magicwords in files
## DONE Generate a dictionary with folder/file: magicwords
def pathContent_dict():
	noteslist = sorted(list_notes())
	magicTasksDisct = {}
	for key, content in notesDict.magicWords.items():
		for i in noteslist:
			# f = FileLineWrapper()
			openlist = []
			openlist = open(i).readlines()
			for line in openlist:
				if content in line:
					keyLineAndMagicWord = "[" + str(openlist.index(line) + 1) + "]" + makeStringBeaultiful(line)
					valuePath = i
					magicTasksDisct[keyLineAndMagicWord] = valuePath
	return magicTasksDisct




## Show TODOS list
def showPathContentDict_list():
	retlist = []
	Ksize = 0
	Vsize = 0
	for k, v in pathContent_dict().items():
		if len(k) > Ksize:
			Ksize = len(k)
		if len(v) > Vsize:
			Vsize = len(v) - 7
	for key, content in notesDict.magicWords.items():
		retlist.append("\t\t\t" + content + ":\n\n" + "*" * (Ksize + Vsize + 5))

		for k, v in sorted(pathContent_dict().items(), key=itemgetter(1)):
			if content in k:
				formatStr = '{0:' + str(Vsize) + '} ==> {1:10}'
				retlist.append(formatStr.format(v.replace(".notes", "").replace("../", ""), k))
				# retlist.append("_" * (Ksize + Vsize))
		retlist.append("" + "*" * (Ksize + Vsize + 5) + "\n\n")
	return retlist

printlist(showPathContentDict_list())

## TODO: implement export print file with date
## TODO: Generate a JSON file with all magicwords found



