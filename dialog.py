import threading
from time import sleep
import sys
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

#Author : Reebal Javed Khan
# used to display some text/info passed as second argument to python executable
# example
# python dialog.py hello
#           will display hello in a window for 1 second (default)
# I use it along nmcli to display if wifi has been enabled or disabled on pressing key combination using xkeybinds
# as I use dwm I don't need to use window size or position 

n=len(sys.argv) # get number of arguments passed from commandline
arg1="" # initiliazing an empty string
if(n==2): 
  arg1=sys.argv[1] # if an extra argument in passed while running this program pass it to arg1
win = Gtk.Window() # create a gtk window
win.connect("destroy", Gtk.main_quit) # allow destruction of this window
labelx=Gtk.Label() # create label
labelx.set_text(arg1) # add arg1 as text to label
win.add(labelx) # add label to window
win.show_all() # show the window

def thread_function(name):
    sleep(1)
    Gtk.main_quit()
## applied threading and sleep for 1 second to display the window for 1 second
## after that kill the window and exit the program
x = threading.Thread(target=thread_function, args=(1,)) # thread initialization
x.start() # Start thread and let thread sleep for N seconds
Gtk.main() # Start main Gtk
x.join()
