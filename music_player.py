from tkinter import *
from tkinter.filedialog import askdirectory         
import os
import pygame
from mutagen.id3 import *
from tkinter import messagebox

app=Tk()
app.title('Music_Player')
app.geometry('500x580')

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(app,textvariable=v,height=3,width=50,bg='white',font='ariel 14')

index = 0

listb=Listbox(app,height=20,width=50)
listb.pack()

def about_command():
    label = messagebox.showinfo('About','This text Editor is created by Ducat')

def directorychooser():
  global count
  global index
    
  directory = askdirectory()
  if(directory):
    count=0
    index=0
    listb.delete(0, END)
    del listofsongs[:]
    del realnames[:]

    os.chdir(directory)

    for  files in os.listdir(directory):

        try:
         if files.endswith(".mp3"):

              realdir = os.path.realpath(files)
              audio = ID3(realdir)
              realnames.append(audio['TIT2'].text[0])
              listofsongs.append(files)
        except:
            print(files+" is not a song")

    if listofsongs == [] :
       okay=tkMessageBox.askretrycancel("No songs found","no songs")
       if(okay==True):
           directorychooser()

    else:
        listb.delete(0, END)
        realnames.reverse()
        for i in listofsongs:
            count = count + 1
        pygame.mixer.init()
        pygame.mixer.music.load(listofsongs[0])

        pygame.mixer.music.play()
        try:
            updatelabel()
        except NameError:
            print("")
  else:
    return 1

try:
        directorychooser()
except WindowsError:
         print("thank you")

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    return songname
 
def nextsong():
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
def prevsong():
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    return songname

def restart():
    global index
    index
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.rewind()

def pause():
    global index
    index
    pygame.mixer.music.pause()

def decreaseMusicVolume(self):

    global index
    index =1
    pygame.mixer.music.get_volume(0.5)
    self.musicVolume = 'decreased'
    pygame.mixer.music.load(listofsongs[index])

def show_value(self):
    i = vol.get()
    pygame.mixer.music.set_volume(i)

vol = Scale(app,from_ = 10,to = 0,orient = VERTICAL ,resolution = 5,command = show_value)
vol.place(x=85, y = 380)
vol.set(5)
    
def unpause():
    global index
    index
    pygame.mixer.music.unpause()

def play():
    global index
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def exit1():
    app.destroy()

la=Label(app,text='Welcome')
la.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listb.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


#button
menu =Menu(app)
app.config(menu = menu)

filemenu = Menu(menu)
menu.add_cascade(label='Files',menu=filemenu)
filemenu.add_cascade(label='Folder')

filemenu2 = Menu(menu)
menu.add_cascade(label='I Quit',menu=filemenu2)
filemenu2.add_command(label='Exit',command=exit1)

filemenu3 = Menu(menu)
menu.add_cascade(label='About',menu=filemenu3)
filemenu3.add_command(label='Developer',command=about_command)

# menu close....

play=Button(app,text='Play',width=10,command=play)
play.pack()

Next=Button(app,text='Next',width=10,command=nextsong)
Next.pack()

Previous=Button(app,text='prevsong',width=10,command=prevsong)
Previous.pack()

Pause=Button(app,text='Pause',width=10,command=pause)
Pause.pack()

Pause=Button(app,text='Unpause',width=10,command=unpause)
Pause.pack()

Restart=Button(app,text='Reversve',width=10,command=restart)
Restart.pack()

Stop=Button(app,text='Stop',width=10,command=stopsong)
Stop.pack()
#button look
Stop.bind("<Button-1>",stopsong)

songlabel.pack()

app.mainloop()
