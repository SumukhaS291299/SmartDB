import os
import tkinter
from tkinter import filedialog as fd
from tkinter import Tk
import pickle
from tkinter.messagebox import showinfo


def Installation():
    global installWnd,GitRemGet
    installWnd = Tk()
    installWnd.geometry("600x600")
    installWnd.resizable(True, True)
    installWnd.title("Install SumuDB")
    InstallProgress  = tkinter.Label(installWnd,text="Starting Installation...",font=("Helvetica", 14))
    InstallProgress.pack(ipadx=10, ipady=10)
    FileLocation = tkinter.Button(installWnd,text="Set File Location",command=setFileLocation)
    FileLocation.pack(ipadx=10, ipady=10)
    GitRemote = tkinter.Label(installWnd,text="Your Git Remote HTTPS link",font=("Helvetica", 14))
    GitRemote.pack(ipadx=3, ipady=3,side=tkinter.LEFT)
    GitRemGet = tkinter.Entry(installWnd,bd=8)
    GitRemGet.pack(ipadx=3, ipady=3,pady=5,padx=5,side=tkinter.LEFT)
    GitRemBttn = tkinter.Button(installWnd,text="Ok",command=GetRemoteLoc)
    GitRemBttn.pack(side=tkinter.LEFT,padx=10,pady=10)


    installWnd.mainloop()

def GetRemoteLoc():
    global GitRemGet
    RemoteLoc = GitRemGet.get()
    if RemoteLoc == "":
        return
    pickle.dump(RemoteLoc, open("GITRemote.dat", "wb"))
    print(RemoteLoc)



def setFileLocation():
    global installWnd
    Filelocation = fd.askdirectory()
    FileLocationSet =  tkinter.Label(installWnd,text="Location set : "+Filelocation)
    FileLocationSet.pack(ipadx=10, ipady=20)
    print(Filelocation)
    installWnd.update()
    FileLocationSet.after(5000)
    FileLocationSet.destroy()
    installWnd.update()
    pickle.dump(Filelocation,open("GITLoc.dat","wb"))

def GITINIT(currentDir):
    global GitLocalDir,GitRemoteDir
    GitLocalDir = pickle.load(open("GITLoc.dat","rb"))
    GitRemoteDir = pickle.load(open("GITRemote.dat", "rb"))
    changeDir =  GitLocalDir
    print("changeDir",changeDir)
    os.chdir(changeDir)
    os.system("git init")
    GetPush(currentDir)

def GetPush(currentDir):
    os.system("git remote add origin "+GitRemoteDir)
    os.system("git remote -v")
    os.system("git add .")
    showinfo("Result", os.popen("git commit -m \"First commit\"").read())
    os.system("git push origin master")
    # showinfo("Result", .read())
    os.chdir(currentDir)


# Installation()

