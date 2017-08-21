from os import listdir
from os.path import isfile, join
import os
from shutil import copyfile

dirSet = ["gain", "kanmiyeon", "kangminkyeong"]
sourcePath = '/Users/sinsanghun/Desktop/project3/image/'
destPath = '/Users/sinsanghun/Desktop/project3/label/'

newDirName = 0

for targetDir in dirSet:
    onlyFiles = [f for f in listdir(sourcePath+targetDir) if f!=".DS_Store"]

    newName = 0
    newTargetDir = destPath+targetDir
    os.mkdir(newTargetDir)

    for name in onlyFiles:
        print ('copy '+sourcePath+targetDir+'/'+name)
        copyfile(sourcePath+targetDir+'/'+name,newTargetDir+'/'+str(newDirName)+'_'+str(newName)+'.JPG')
        newName+=1
    newDirName+=1