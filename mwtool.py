#!/usr/bin/env python3
import sys
import notes_dictionaries as notesDict


runBoo = True
first = True


def clearTerminal():
	print(chr(27) + "[2J")


def init():
	global first
	if first:
		clearTerminal()
		showOptions()
	first = False


def showOptions():
	clearTerminal()
	for line in open(str(sys.argv[0])):
		if '##' in line:
			if "if '##' in line:" not in line:
				print(line)
	print('\n\n')





## MWTool Command Line Interface
while runBoo:
	init()
	arg = str(input('Command: '))

	## m 			show the magic words (words to be listed)
	if 'm' == arg:
		showOptions()
		dicti = notesDict.magicWords
		for i, j in dicti.items():
			print(i + "\t\t" + j)

	## s 			show all the special notes
	## u 			update annotations list
	## q 			close the program
	if 'q' == arg:
		sys.exit(1)


	else:
		print()










