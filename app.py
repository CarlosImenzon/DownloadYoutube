from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
import logicModule

# Background colors
bgPrimary="#34495E"
bgEntry="#CACFD2"

# Font
fontPrimary = ("Times", 14, "italic")
fontEntry = ("Times", 12, "italic")

# Interface root
root = Tk()
path = logicModule.resource_path("logo.ico")
root.iconbitmap(path)
root.title('Descargar desde Youtube')

# Window size, positioning and not resizable
widthWindow = 800
tallWindow = 550

xWindow = root.winfo_screenwidth() // 2 - widthWindow // 2
yWindow = root.winfo_screenheight() // 2 - tallWindow // 2

posicion = str(widthWindow) + "x" + str(tallWindow) + "+" + str(xWindow) + "+" + str(yWindow)
root.geometry(posicion)

root.geometry('%dx%d' % (widthWindow, tallWindow))
root.resizable(width=0, height=0)

# Canvas
frame = ttk.Frame(root)
frame.pack()

frameUp=Canvas(frame, width=800, height=550, background=bgPrimary)
frameUp.pack()

frameBottom=Canvas(frame, width=800, height=100, background=bgPrimary)
frameBottom.pack()

# Widgets
labelLink = Label(frameUp, text="Ingrese la URL de YouTube que desea descargar", background=bgPrimary, fg="#fff", font=fontPrimary)
inputLink = Entry(frameUp, width=80, bg=bgEntry, font=fontEntry)
btnAdd = Button(frameUp, text="Agregar", background="#1E8449", fg="#fff", font=fontPrimary, command=lambda:logicModule.addQueue(listLink, inputLink, bar))
btnClear = Button(frameUp, text="Limpiar", background="#CD6155", fg="#fff", font=fontPrimary, command=lambda:logicModule.clearTextInput(inputLink))

labelQueue = Label(frameUp, text="Cola de descarga", background=bgPrimary, fg="#fff", font=fontPrimary)
btnDelete = Button(frameUp, text="Borrar", background="#E74C3C", fg="#fff", font=fontPrimary, command=lambda:logicModule.deleteSelection(listLink))
listLink = Listbox(frame, width=80, height=10, bg=bgEntry, font=fontEntry)

btnDestiny = Button(frameUp, text="Seleccionar destino", background="#D35400", fg="#fff", font=fontPrimary, width=15, command=lambda:logicModule.selectDirectory(linkDestiny))
linkDestiny = Entry(frameUp, width=58, background=bgEntry, font=fontEntry)
linkDestiny.insert("1", logicModule.getDirectory())
linkDestiny.config(state='readonly')

labelInfoTit = Label(frameUp, text="Progreso: ", background=bgPrimary, fg="#fff", font=fontPrimary)
bar = Progressbar(frameUp, orient=HORIZONTAL, length=500)
bar.pack(padx=10, pady=10)

btnDownloadStart = Button(frameUp, text="Comenzar Descarga", background="#1E8449", fg="#fff", font=fontPrimary, command=lambda:logicModule.startDownload(buttons, listLink, linkDestiny.get(), bar, root))
btnDirDownload = Button(frameUp, text="Abrir Descargas", background="#2874A6", fg="#fff", font=fontPrimary, command=lambda:logicModule.openFile(logicModule.getDirectory()))
buttons = (btnAdd, btnClear, btnDelete, btnDestiny, btnDownloadStart, btnDirDownload)

# Positioning
frameUp.create_window(400, 30, window=labelLink)
frameUp.create_window(400, 60, window=inputLink)
frameUp.create_window(350, 100, window=btnAdd)
frameUp.create_window(450, 100, window=btnClear)

frameUp.create_window(689, 132, window=btnDelete)
frameUp.create_window(143, 140, window=labelQueue)
frameUp.create_window(400, 260, window=listLink)

frameUp.create_window(313, 390, window=linkDestiny)
frameUp.create_window(643, 390, window=btnDestiny)

frameUp.create_window(400, 430, window=labelInfoTit)
frameUp.create_window(400, 460, window=bar)

frameUp.create_window(300, 510, window=btnDownloadStart)
frameUp.create_window(500, 510, window=btnDirDownload)


# Interface infinite loop
root.mainloop()