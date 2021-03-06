from Tkinter import*
from tkFileDialog import*
import os
import pickle
import pyError
import win32com.shell.shell as shell
import tkFont
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

def saveAs():
    os.chdir('projects')
    f = asksaveasfile(mode = 'w', defaultextension = '.gsw')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        pyError.newError('Grid Script Error', 'There was an error saving your file', 'We are not sure what happend',40,20)
    os.chdir('..')

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
    saveAs()

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

def runTemp():
    os.chdir('Compiler')
    f = open('temp.gsw', 'w')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        print('error')
    pickle_out = open('file_path.gsrf', 'w')
    pickle.dump('temp.gsw', pickle_out)
    pickle_out.close()    
    os.startfile('Compiler.exe')
    os.chdir('..')

app = Tk()
app.title('Grid Script Web IDE')
app.geometry('1000x1000')

text = Text(app, width = 1000, height = 1000)
text.pack()

def bold():
    self.text.tag_configure("bold", fg = 'red')


menubar = Menu(app)
filemenu = Menu(menubar)
filemenu.add_command(label = 'New', command = newFile)
filemenu.add_command(label = 'Open', command = openFile)
filemenu.add_command(label = 'Save', command = saveAs)
filemenu.add_separator()
filemenu.add_command(label = 'Quit', command = app.quit)
menubar.add_cascade(label = 'File', menu = filemenu)
Run = Menu(menubar)
Run.add_command(label = 'Run Program as exec', command = run)
Run.add_command(label = 'Run Program as temp', command = runTemp)
menubar.add_cascade(label = 'Run', menu = Run)

app.config(menu = menubar)

app.mainloop()
