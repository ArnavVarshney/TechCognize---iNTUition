#GUI_Support file

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

#GUI file

import sys
import runpy
import threading
from threading import Thread
import os
import signal
from PIL import Image

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_GUI():
    #Starting point when module is the main routine
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    #Starting point when module is imported by another program
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        #This class configures and populates the toplevel window top is the toplevel containing window.
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font13 = "-family {Century Gothic} -size 12 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font14 = "-family {Century Gothic} -size 10 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Century Gothic} -size 9 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("500x300+836+190")
        top.title("TechCognize")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#efefef")
        self.Frame1.configure(highlightbackground="#ffffff")
        self.Frame1.configure(highlightcolor="#646464646464")

        self.TLabel1 = ttk.Label(self.Frame1)
        self.TLabel1.place(relx=0.0, rely=0.0, height=40, width=500)
        self.TLabel1.configure(background="#383838")
        self.TLabel1.configure(foreground="#ffffff")
        self.TLabel1.configure(font=font9)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(text=''' TechCognize''')

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.0, rely=0.133, height=20, width=500)
        self.Label1.configure(background="#ff9f0f")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")

        pid = 0

        def callback_threaded_launch():
                Thread(target=callback_launch).start()
                pid = os.getpid()
                print(pid)

        def callback_launch():
                runpy.run_path("hack.py")

        self.LAUNCH = tk.Button(self.Frame1)
        self.LAUNCH.place(relx=0.14, rely=0.3, height=83, width=246)
        self.LAUNCH.configure(activebackground="#ececec")
        self.LAUNCH.configure(activeforeground="#000000")
        self.LAUNCH.configure(background="#7c7c7c")
        self.LAUNCH.configure(state="normal")
        self.LAUNCH.configure(command=callback_threaded_launch)
        self.LAUNCH.configure(disabledforeground="#878584")
        self.LAUNCH.configure(font=font13)
        self.LAUNCH.configure(foreground="#ffffff")
        self.LAUNCH.configure(highlightbackground="#ff801f")
        self.LAUNCH.configure(highlightcolor="#ff801f")
        self.LAUNCH.configure(pady="0")
        self.LAUNCH.configure(text='''LAUNCH >''')

        def callback_threaded_kill():
                Thread(target=callback_kill).start()

        def callback_kill():
                os.kill(pid, signal.SIGTERM)

        self.EXIT = tk.Button(self.Frame1)
        self.EXIT.place(relx=0.64, rely=0.3, height=168, width=86)
        self.EXIT.configure(activebackground="#ececec")
        self.EXIT.configure(activeforeground="#000000")
        self.EXIT.configure(background="#ff9f0f")
        self.EXIT.configure(command=callback_threaded_kill)
        self.EXIT.configure(disabledforeground="#a3a3a3")
        self.EXIT.configure(font=font13)
        self.EXIT.configure(foreground="#ffffff")
        self.EXIT.configure(highlightbackground="#d9d9d9")
        self.EXIT.configure(highlightcolor="black")
        self.EXIT.configure(pady="0")
        self.EXIT.configure(text='''EXIT       X''')
        self.EXIT.configure(wraplength="50")

        def callback_threaded_info():
                Thread(target=callback_info).start()

        def callback_info():
                img = Image.open('usage.jpg')
                img.show()
		
        self.INFO = tk.Button(self.Frame1)
        self.INFO.place(relx=0.14, rely=0.6, height=80, width=246)
        self.INFO.configure(activebackground="#ececec")
        self.INFO.configure(activeforeground="#000000")
        self.INFO.configure(background="#ffffff")
        self.INFO.configure(command=callback_threaded_info)
        self.INFO.configure(disabledforeground="#a3a3a3")
        self.INFO.configure(font=font14)
        self.INFO.configure(foreground="#000000")
        self.INFO.configure(highlightbackground="#d9d9d9")
        self.INFO.configure(highlightcolor="black")
        self.INFO.configure(pady="0")
        self.INFO.configure(text='''INFO i''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

if __name__ == '__main__':
    vp_start_GUI()

