'''
YouTube video downloader with Tkinter GUI
'''

# Importing modules
import os
from pytube import *
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from threading import *

file_size = 0


def progress(stream=None, chunk=None, remaining=None):
    file_downloaded = file_size - remaining
    percent = round((file_downloaded / file_size) * 100, 1)
    dButton.config(text=f'{percent}% downloaded')


def startDownload():
    global file_size
    try:
        URL = urlField.get()
        dButton.config(text="Please wait....")
        dButton.config(state=DISABLED)
        path_save = askdirectory()

        if path_save is NONE:
            return
        ob = YouTube(URL, on_progress_callback=progress)
        strm = ob.streams[0]
        x = ob.description.split("|")
        file_size = strm.filesize
        dfile_size = file_size
        dfile_size /= 1000000
        dfile_size = round(dfile_size, 2)
        label.config(text="Size: " + str(dfile_size) + 'MB')
        label.pack(side=TOP, pady=10)
        desc.config(text=ob.title + '\n\n' + 'Label: ' + ob.author + '\n\n' + 'length: '
                    + str(round(ob.length / 60, 1)) + ' mins\n\n' + 'Views: ' + str(ob.views))
        desc.pack(side=TOP, pady=10)
        strm.download(path_save, strm.title)
        dButton.config(state=NORMAL)
        showinfo("Download Finished", "Downloaded Successfully")
        urlField.delete(0, END)
        label.pack_forget()
        desc.pack_forget()
        dButton.config(text="Start Download")
    except Exception as e:
        print(e)
        print("Some Error Occured !!")

def startDownloadthread():
    thread = Thread(target=startDownload)
    thread.start()



main = Tk()

main.title("YouTube video Downloader ~~ Punit Choudhary")
main.config(bg = '#3498DB')

main.iconbitmap("logo.ico")
main.geometry("530x550")

file = PhotoImage(file='logo2.png')
headingIcon = Label(main, image=file)
headingIcon.pack(side=TOP)

urlField = Entry(main, font=("Times New Roman", 18), justify=CENTER)
urlField.pack(side=TOP, fill=X, padx=10, pady=15)

dButton = Button(main, text="Start Download", font=(
    "Times New Roman", 18), relief='ridge', activeforeground='red', command=startDownloadthread)
dButton.pack(side=TOP)
label = Label(main, text='')
desc = Label(main, text='')
author = Label(main, text="Punit-Choudhary")
author.config(font=("Courier", 44))
author.pack(side=BOTTOM)
main.mainloop()