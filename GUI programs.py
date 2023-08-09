#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Creating a main window

import tkinter
m = tkinter.Tk()
'''
widgets are added here
'''
m.mainloop()


### In[8]:
##
##
###Create a button 
##
import tkinter as tk
r = tk.Tk()
r.title('Counting Seconds')
button = tk.Button(r, text='Stop', width=25, command=r.destroy,bg="yellow",fg ='red')
button.pack()
r.mainloop()
##
##
### In[10]:
##
##
#Create a check button
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='salem', variable=var1).grid(row=0, sticky="e")
var2 = IntVar()
Checkbutton(master, text='other', variable=var2).grid(row=1, sticky="w")
mainloop()


# In[11]:


#Create a Radio button
from tkinter import *
root = Tk()
v = IntVar()
Radiobutton(root, text='male', variable=v, value=1).pack(anchor=W)
Radiobutton(root, text='female', variable=v, value=2).pack(anchor=W)
mainloop()


# In[12]:


###Create a entry box
from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()


# In[13]:


#create a frame
from tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )
redbutton = Button(frame, text = 'Red', fg ='red')
redbutton.pack( side = LEFT)
greenbutton = Button(frame, text = 'Brown', fg='brown')
greenbutton.pack( side = LEFT )
bluebutton = Button(frame, text ='Blue', fg ='blue')
bluebutton.pack( side = LEFT )
blackbutton = Button(bottomframe, text ='Black', fg ='black')
blackbutton.pack( side = BOTTOM)
root.mainloop()


# In[16]:


#Label
from tkinter import *
root = Tk()
w = Label(root, text='IMAGECON INDIA......!')
w.pack()
root.mainloop()


# In[17]:


#create a list box
from tkinter import *

top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()
top.mainloop()


# In[20]:


#Menu button
from tkinter import *

top = Tk()
mb = Menubutton ( top, text = "ABCD")
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu
cVar = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.pack()
top.mainloop()


# In[ ]:

#Message
from tkinter import *
main = Tk()
ourMessage ='This is our Message'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
main.mainloop( )

#Scale
from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()


#Scrollbar
from tkinter import *  
  
top = Tk()  
sb = Scrollbar(top)  
sb.pack(side = RIGHT, fill = Y)  
  
mylist = Listbox(top, yscrollcommand = sb.set )  
  
for line in range(30):  
    mylist.insert(END, "Number " + str(line))  
  
mylist.pack( side = LEFT )  
sb.config( command = mylist.yview )  
  
mainloop()
#Text
from tkinter import *
root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, 'IMAGECON ACADEMY\nNEXT GEN TRAINING\n')
mainloop()

#Top level
from tkinter import *
root = Tk()
root.title('IMAGECON')
top = Toplevel()
top.title('Python')
top.mainloop()

#Spinbox
from tkinter import *
master = Tk()
w = Spinbox(master, from_ = 0, to = 10)
w.pack()
mainloop()

#Panned window
from tkinter import *
m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 10)
left = Entry(m1, bd = 1)
m1.add(left)
m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)
top = Scale( m2, orient = HORIZONTAL)
m2.add(top)
mainloop()






