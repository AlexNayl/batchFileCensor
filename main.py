from argparse import ArgumentParser
import sys
from pathlib import Path
#Requires Python 3.4 or later

INPUT_DIRECTORY_PATH = 'in'
OUTPUT_DIRECTORY_PATH = 'out'
PROHIBITED_LIST_PATH = 'prohibitedList.txt'

#Argument handeling
argParser = ArgumentParser(description = 'Removes prohibited words from text encoded files.')
argParser.add_argument('directory', help = 'Local directory containing input files and prohibited word list, see README for further details.')

directory = argParser.parse_args().directory

#Check that the user has passed a valid working directory
if not Path(directory).is_dir():
	print("Fatal Error: The directory \'" + directory +"\' does not exist.")
	sys.exit()

#Check that the directory has an in folder
if not Path(directory, INPUT_DIRECTORY_PATH).is_dir():
	print("Fatal Error: Directory formating invalid, '"+INPUT_DIRECTORY_PATH+"' not found.")
	sys.exit()

#Check that the directory has a prohibited list file
if not (Path(directory, PROHIBITED_LIST_PATH).is_file()):
	print("Fatal Error: Directory formating invalid, '" + PROHIBITED_LIST_PATH +"' not found.")
	sys.exit()

#holding array for all input file paths
files = []

#For each file in the input folder, check if its a file (not a directory) and add it to the list
for currentPath in Path(directory, INPUT_DIRECTORY_PATH).iterdir():
	if(Path(currentPath).is_file):
		files.append(currentPath)
		#do somthing with the file

#check if there are actual files in the list
if len(files) < 1:
	print("Error: Input directory empty, nothing to work on!")

#if the output directory doesnt allready exist, make it
if not Path(directory, OUTPUT_DIRECTORY_PATH).is_dir():
	Path.mkdir(Path(directory, OUTPUT_DIRECTORY_PATH))
	print("Warn: Output directory not found, 'out' folder created.")