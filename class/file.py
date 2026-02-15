import os

class files:
    def __init__(self,folder,file):
        self.folder=folder
        self.file=file

        os.mkdir(self.folder)
        os.chdir(self.folder)
        with open(self.file,"w") as fw:
            pass
        

    def writedata(self):
        print(os.getcwd())
        # os.chdir(self.folder)
        data = input("Enter any data: ")
        with open(self.file, "w") as fw:
            fw.write(data)
        print("Data written in file")

    def copydata(self,dest):
        # os.chdir(self.folder)
        with open(self.file,"r") as fr:
            with open(dest,"w") as fw:
                fw.write(fr.read())
            fw.close()
        fw.close()
        print("Data Copied")
        o=input("Do you want to display data: ")
        if o=="yes":
            self.ReadDestData(dest)
        else:
            pass

    def ReadDestData(self,destfile):
        print(os.getcwd())
        with open(destfile,"r") as fr:
            print(fr.read())
            fr.close()
        print(f"All data from {destfile} are read!")

    def rename(self,file):
        print(os.getcwd())
        newname=input("Enter new name: ")
        os.rename(file,newname)
        print("File renamed sucessfully!")

    def delfile(self,f):
        os.remove(f)
        print((f"File {f} deleted Sucessfully!"))

folder=input("Enter folder name: ")
file=input("Enter file name: ")
dfile=input("Enter new name: ")
f1=files(folder,file)
f1.writedata()
f1.copydata(dfile)
f1.rename(dfile)
f1.delfile(file)