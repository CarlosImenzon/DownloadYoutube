from pytube import YouTube
from tkinter import filedialog
import os, sys, subprocess
from tkinter import messagebox as mb

# Variables
currentDirectory=os.getcwd()
songsList=[]

# methods

# ------------------------------------------------------------------
'''
Method to add the title to the download queue. A tuple is created
with the title and the link, then it is added to a list of songs.

Parameters:
    - listLink: is the download queue.
    - inputLink: field where the link to download is pasted.
'''
def addQueue(listLink, inputLink, bar):
    bar['value'] = 0
    try:
        titleLink=(getTitleCurrent(inputLink.get()), inputLink.get())
    except:
        mb.showerror(message="Verifique la URL ingresada", title="URL no disponible")
    else:
        if listLink.size() < 10:
            songsList.append(titleLink)
            listLink.insert(0, titleLink[0])
            clearTextInput(inputLink)
        else:
            mb.showinfo(message="Debera iniciar la descarga", title="Cola de descarga llena")

# ------------------------------------------------------------------
'''
Method to start downloading the song.

Parameters:
    - listLink: is the download queue.
    - linkDestiny: directory where the audio is saved.
    - labelTitDinamic: indicates the song that was downloaded.
'''
def startDownload(buttons, listLink, linkDestiny, bar, root):
    if len(songsList) == 0:
        mb.showinfo(message="Agregue una URL para poder descargar", title="Cola de descarga vacia")
    else:
        disableButtons(buttons)
        totalSongs = len(songsList)
        while (len(songsList) >0):
            bar['value']+=100/totalSongs
            url = songsList.pop(0)
            downloadAudio(url[1], linkDestiny)
            listLink.delete(listLink.size()-1)
            root.update()
        enableButtons(buttons)
        mb.showinfo(message="Se ha descargado con exito", title="Descarga completa")

# ------------------------------------------------------------------
'''
Method to download the audio.

Parameters:
    - currentLink: YouTube link.
    - linkDestiny: directory where the audio is saved.
'''
def downloadAudio(currentLink, linkDestiny):
    try:
        yt=YouTube(currentLink,
            use_oauth=False,
            allow_oauth_cache=True)
    except:
        mb.showinfo(title="Video no disponible", message="Prueba otra URL")
    else:
        yt.streams.filter(only_audio=True)
        stream = yt.streams.get_audio_only()
        stream.download(output_path=linkDestiny)

# ------------------------------------------------------------------
'''
Method that gets the title of the video.

Parameters:
    - currentLink: YouTube link.

Return:
    return the title.
'''
def getTitleCurrent(currentLink):
    yt=YouTube(currentLink)
    titleImg=yt.title
    return titleImg

# ------------------------------------------------------------------
'''
Field clearing method.

Parameters:
    - inputLink: field where the link to download is pasted.
'''
def clearTextInput(inputLink):
    inputLink.delete(0,"end")

# ------------------------------------------------------------------
'''
Method to delete a selected link within the download queue.
If there is an element selected, it deletes it, otherwise, it deletes the first one.

Parameters:
    - listLink: is the download queue.
'''
def deleteSelection(listLink):
    if len(listLink.curselection()) == 1:
        posItem=listLink.curselection()[0]
        calcItem = len(songsList) - posItem -1
        listLink.delete(listLink.curselection())
        songsList.pop(calcItem)
    else:
        listLink.delete(0)
        calcItem = len(songsList)-1
        songsList.pop(calcItem)
# ------------------------------------------------------------------
'''
Method to open the downloads directory. 
Opens the window corresponding to the operating system.

Parameters:
    - listLink: open directory of last download.
'''
def openFile(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])

# ------------------------------------------------------------------
'''
Method to select the download directory.

Parameters:
    - listLink: is the download queue.
'''
def selectDirectory(linkDestiny):
    global currentDirectory
    linkDestiny.config(state='normal')
    currentDirectoryAux = filedialog.askdirectory(title="Seleccionar el destino")
    if currentDirectoryAux == () or currentDirectoryAux == "":
        linkDestiny.insert("1", currentDirectory)
    else:
        clearTextInput(linkDestiny)
        currentDirectory=currentDirectoryAux
        linkDestiny.insert("1", currentDirectoryAux)
    linkDestiny.config(state='readonly')

# ------------------------------------------------------------------
'''
Method to get the path of the downloads directory.

Return:
    returns the path of the destination directory.
'''
def getDirectory():
    return currentDirectory

# ------------------------------------------------------------------
'''
Methods to enable and disable buttons.

Parameters:
    buttons: tuple composed of the buttons.
'''
def disableButtons(buttons):
    buttons[0]['state'] = "disabled"
    buttons[1]['state'] = "disabled"
    buttons[2]['state'] = "disabled"
    buttons[3]['state'] = "disabled"
    buttons[4]['state'] = "disabled"
    buttons[5]['state'] = "disabled"

def enableButtons(buttons):
    buttons[0]['state'] = "normal"
    buttons[1]['state'] = "normal"
    buttons[2]['state'] = "normal"
    buttons[3]['state'] = "normal"
    buttons[4]['state'] = "normal"
    buttons[5]['state'] = "normal"

# ------------------------------------------------------------------
"""
Get absolute path to resource, works for dev and for PyInstaller
"""
def resource_path(relative_path):
    
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)