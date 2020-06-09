import traininghelper as th
import glob
import os
Dir ="Enter image/textfile Directory here"
newTxtFile = "val.txt"
os.chdir(Dir)
newFile = open(newTxtFile, "w+")
for file in glob.glob("*.txt"):
    jpgfile = Dir + th.txtToJpg(file) + "\n"
    newFile.write(jpgfile)      
    print(jpgfile)
