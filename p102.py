import os
#print (dir(os))
import shutil


directory = os.getcwd()
print ("current working directory is",directory)
#os.mkdir("")
#files = os.listdir("/Users/homefolder/Documents")
#print (files)
#path = os.path.exists ("/Users/homefolder/Documents")
#print(path)

source = "/Users/homefolder/Documents"
destination = "/Users/homefolder/Documents/sig"
files  = os.listdir(source)
for i in files:
    name,ext = os.path.splitext(i)
    if ext == "":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "Document_Files" + '/' + i

        if os.path.exists(path2):
            print("moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating and moving")
            shutil.move(path1,path3)