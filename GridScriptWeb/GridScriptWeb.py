from Tkinter import*
from tkFileDialog import*
import os
import pickle
import pyError
import win32com.shell.shell as shell
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

def settings_open():
    os.chdir('settings')
    os.startfile('settings.exe')
    os.chdir('..')

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    try:
        t = text.get(0.0, END)
        f = open(filename, 'w')
        f.write(t)
        f.close()
    except:
        saveAs()

def saveAs():   
    os.chdir('projects')
    f = asksaveasfile(mode = 'w', defaultextension = '.gsw')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        pyError.newError('Grid Script Error', 'There was an error saving your file', 'We are not sure what happend',40,20)
    os.chdir('..')

def openFile():
    os.chdir('projects')
    try:
        f = askopenfile(mode = 'r')
        print f
        t = f.read()
        print t 
        text.delete(0.0, END)
        text.insert(0.0, t)
    except:
        pyError.newError('Grid Script Error', 'There was an error opening your file', 'make sure its a .gs, .gsw or .txt file',40,20)

    os.chdir('..')

def run():
    os.chdir('projects')
    f = asksaveasfile(mode = 'w', defaultextension = '.gsw')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        print('error')
    os.chdir('..')
    abs_path = os.path.abspath(f.name)
    os.chdir('Compiler')
    pickle_out = open('file_path.gsrf', 'w')
    pickle.dump(abs_path, pickle_out)
    pickle_out.close()    
    os.startfile('Compiler.exe')
    os.chdir('..')
    

app = Tk()
app.title('Grid Script Web IDE')
app.geometry('1000x1000')

text = Text(app, width = 1000, height = 1000)
text.pack()

menubar = Menu(app)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = newFile)
filemenu.add_command(label = 'Open', command = openFile)
filemenu.add_command(label = 'Save', command = saveFile)
filemenu.add_command(label = 'Save As', command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Quit', command = app.quit)
menubar.add_cascade(label = 'File', menu = filemenu)
#settings = Menu(menubar)
#settings.add_command(label = 'Settings', command = settings_open)
#menubar.add_cascade(label = 'Settings', menu = settings)
Run = Menu(menubar)
Run.add_command(label = 'Run Program', command = run)
menubar.add_cascade(label = 'Run', menu = Run)

app.config(menu = menubar)

app.mainloop()