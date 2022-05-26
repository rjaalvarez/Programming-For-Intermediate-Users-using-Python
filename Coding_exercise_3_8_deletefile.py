import os

if os.path.exists("myFile.txt"):
    os.remove("myFile.txt")
else:
    print("File does not exists.")