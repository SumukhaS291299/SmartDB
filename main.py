import os
import tkinter
from tkinter import Tk
from SET_Properties import Installation,GITINIT
import pickle
from tkinter.messagebox import showinfo


def main():
    global Dash
    Dash = Tk()
    Dash.geometry("400x500")
    Dash.resizable(True, True)
    Dash.title("SumuDB")
    Dash.configure(bg='cyan')
    WelcomeText = tkinter.Label(Dash,text="Welcome to SumuDB",font=("Helvetica", 16),relief=tkinter.SUNKEN)
    WelcomeText.pack(anchor=tkinter.NW,pady=5,padx=5)
    refresh = tkinter.Button(Dash, text="Refresh", command=refreshWindow)
    refresh.pack(anchor=tkinter.NE,pady=20,padx=20)
    setInstall = tkinter.Button(Dash,text="Installation",command=ShowIns)
    setInstall.pack(ipadx=10,ipady=12,pady=20,padx=10,anchor=tkinter.NW)

    GetInit = tkinter.Button(Dash, text="Push to Git Repo", command=GIT)
    GetInit.pack(ipadx=6, ipady=6, pady=5, padx=5, anchor=tkinter.NW)
    GitLocDisplat()

    Quit = tkinter.Button(Dash,text="EXIT",command=exit)
    Quit.pack(side=tkinter.BOTTOM,ipadx=10,ipady=10,padx=5,pady=5)

    Dash.mainloop()

def exit():
    quit()

def GIT():
    GitLocLabel.destroy()
    GitRemoteLabel.destroy()
    CWD = os.getcwd()
    GITINIT(CWD)
    GitLocDisplat()


def refreshWindow():
    global GitLocLabel,GitRemoteLabel
    GitLocLabel.destroy()
    GitRemoteLabel.destroy()
    GitLocDisplat()

def GitLocDisplat():
    global Dash
    try:
        global GitLocLabel
        Gitlocdisp = pickle.load(open("GITLoc.dat","rb"))
        GitLocLabel = tkinter.Label(Dash, text="Git local Location:  " + Gitlocdisp)
        GitLocLabel.pack(side=tkinter.BOTTOM)
    except FileNotFoundError:
        GitLocLabel = tkinter.Label(Dash, text="Git local Location not set or file locked please restart")
        GitLocLabel.pack(side=tkinter.BOTTOM)
        showinfo("Make sure you have made an auth keys and ran : git remote set-url origin https://<username>:<Token>@github.com/<username>/<Repo_name>.git" )
        # git remote set-url origin https://SumukhaS291299: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@github.com/SumukhaS291299/SumuDb.git

    try:
        global GitRemoteLabel
        GitRemoteTxt = pickle.load(open("GITRemote.dat","rb"))
        # print("GitRemoteTxt",GitRemoteTxt)
        GitRemoteLabel = tkinter.Label(Dash, text="Git Remote Location:  " + GitRemoteTxt)
        GitRemoteLabel.pack(side=tkinter.BOTTOM)
    except FileNotFoundError:
        GitRemoteLabel = tkinter.Label(Dash, text="Git Remote Location not set or file location not set please restart")
        GitRemoteLabel.pack(side=tkinter.BOTTOM)

def ShowIns():
    global Dash
    Installation()

if __name__ == "__main__":
   main()





# win.winfo_width()
# win.winfo_height()
# pack()  place()