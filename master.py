import os
import Database

root = 'lib'
files = []
for file in os.listdir(root):
	files.append(root + "/" + file)

Database.make(files)