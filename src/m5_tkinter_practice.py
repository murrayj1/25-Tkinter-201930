"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Jacob Murray.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def print_hello():
    print('Hello')


def print_goodbye():
    print('Goodbye')


def print_button2(entry_box):
    if (entry_box.get()=="ok"):
        print_hello()
    else:
        print_goodbye()


def print_button3(entry_box1, entry_box2):
    s = entry_box2.get()                    # entry_box1 contains what is being printed n times
    n = int(s)                              # entry_box2 contains the integer n
    for _ in range(n):
        print(entry_box1.get())


def main():
    """ Constructs a GUI with stuff on it. """
    # -------------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    # -------------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # -------------------------------------------------------------------------
    frame1 = ttk.Frame(root,padding=30, relief = 'groove')
    frame1.grid()
    # -------------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # -------------------------------------------------------------------------
    button1 = ttk.Button(frame1, text='Button 1')
    button1.grid()
    # -------------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # -------------------------------------------------------------------------
    button1['command'] = lambda: print_hello()

    # -------------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # -------------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()
    button2 = ttk.Button(frame1, text='Button 2')
    button2.grid()
    button2['command'] = lambda: print_button2(my_entry_box)



    # -------------------------------------------------------------------------
    # Done: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # -------------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    button3 = ttk.Button(frame1, text='Button 3')
    button3.grid()
    my_entry_box_2 = ttk.Entry(frame1)
    my_entry_box_2.grid()
    button3['command'] = lambda: print_button3(my_entry_box, my_entry_box_2)
    root.mainloop()

    # -------------------------------------------------------------------------
    # Done: 8. As time permits, do other interesting GUI things!
    # -------------------------------------------------------------------------



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
