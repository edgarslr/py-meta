#!/usr/bin/env python

# -*- coding: utf-8 -*-

from tkinter import *

import re

import tkinter.scrolledtext as scrolledtext

from tkinter import filedialog

from PIL import Image

from PIL.ExifTags import TAGS

import warnings

 

warnings.filterwarnings("ignore", "(Possibly )?corrupt EXIF data", UserWarning)

 

class App:

    def __init__(self):

        self.ventana = Tk()

        self.ventana.title("EXIF DATA VIEWER")

        self.ventana.configure(bg="light blue")

        self.ventana.geometry("565x371")

        self.file_label = Label(self.ventana,text="NO FILE SELECTED",bg="light green")

        self.file_label.pack(side=TOP)

        self.display = scrolledtext.ScrolledText(self.ventana,bg="black",fg="light green",width=65,height=20)

        self.display.pack(side=TOP)

        self.btn_search = Button(self.ventana,text="SEARCH FILE",bg="orange",width=30,command=self.open_file)

        self.btn_search.pack(side=TOP)

 

        self.ventana.mainloop()

 

    def open_file(self):

        file = filedialog.askopenfilename(initialdir="/imagenes",title="SELECT FILE",

                                        filetypes=(("jpeg files","*.jpg"),("all files","*.*")))

        if file != "":

            self.file_label.configure(text=(file).split("/")[-1])

            self.extract_data(file)

 

    def extract_data(self,f):

        self.display.delete('1.0',END)

        try:

            image = Image.open(f)

            exifdata = image._getexif()

            if exifdata is not None:

                self.display.insert(END,"-"*26+"METADATA INFO"+"-"*26+"\n")

                for tag_id in exifdata:

                    tag = TAGS.get(tag_id, tag_id)

                    data = exifdata.get(tag_id)

                    if isinstance(data, bytes):

                        data = data.decode('UTF8','replace')

                    try:

                        self.display.insert(END,f"{tag:26}: {data}"+"\n")

                    except:

                        data = re.sub('[^a-zA-Z0-9 \n\.]', '', data)

                        self.display.insert(END,f"{tag:26}: {data}"+"\n")

                self.display.insert(END,"-"*65)

            else:

                self.display.insert(END,'NO DATA')

        except:

            self.display.insert(END,'ERROR')

 

 

if __name__=="__main__":

    App()