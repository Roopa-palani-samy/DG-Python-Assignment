#  9.Implement a program dirtree.py that takes a directory as argument and prints all the files
# in that directory recursively as a tree. Hint: Use os.listdir and os.path.isdir functions.

import os
import fnmatch
class Dirtree:
    def findfiles(self,directory):
        for root, dirs, files in os.walk(".") :
            if os.path.isdir(directory) :
                print(os.listdir(directory))

d=Dirtree()
d.findfiles("roopa")