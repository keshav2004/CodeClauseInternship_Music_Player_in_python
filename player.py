import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os


root = Tk()
root.geometry("485x700+290+10")
root.title("Music Player")
root.configure(background="red")

mixer.init()

## created function, will open the file
def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)

## function which play music and active the playlist and print the name
def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()



## size will not change
#root.resizable(False,False) 

## for white background for menu bar
lower_frame = Frame(root,bg="#FFFFFF",width=485,height=180)
lower_frame.place(x=0,y=400)

## logo image at the top
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)


## for gif
frameCnt = 30
frames = [PhotoImage(file='gif2.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)


## menu image at the menu section
Menu = PhotoImage(file="menu.png")
Label(root,image=Menu).place(x=0,y=400,width=485,height=200)

Frame_music = Frame(root,  bd = 2, relief = RIDGE)
Frame_music.place(x=0,y=585,width=485,height=100)

Scroll = Scrollbar(Frame_music)

## Browse Music button
Button(root, text="Browse Music", width=59, height=1, font=("calibri",12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)
Playlist = Listbox(Frame_music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)

## Play Button
ButtonPlay = PhotoImage(file="play.png")
Button(root, image=ButtonPlay, bg="Red", bd=0, height = 60, width =60,command=PlayMusic).place(x=215, y=487)

## Pause Button
ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="Red", bd=0, height = 60, width =60,command=mixer.music.pause).place(x=300, y=487)

## Stop Button
ButtonStop = PhotoImage(file="stop.png")
Button(root, image=ButtonStop, bg="Red", bd=0, height = 60, width =60,command=mixer.music.stop).place(x=130, y=487)


Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()
