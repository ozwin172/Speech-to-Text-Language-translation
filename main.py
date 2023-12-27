from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os
from PIL import Image, ImageTk
import googletrans
import textblob
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator

mainwindow=Tk()
mainwindow.title('FYP')
mainwindow.geometry('500x500')
mainwindow.configure(bg="steelblue1")
# canvas = Canvas(mainwindow, width = 3000, height = 1000)
# anvas.pack()
# img = PhotoImage(file='practicals\language.png')
# canvas.create_image(0,0, anchor=NW, image=img)

language = googletrans.LANGUAGES
languageV = list(language.values())
lan1 = language.keys()


def speech():
    while True:
        print("1")
        r = sr.Recognizer()
        print("2")
        with sr.Microphone() as source:
            print("3")
            audio = r.listen(source)
            print("4")
            try:
                print("5")
                text = r.recognize_google(audio)
                print("6")
            except:
                print("7")
                pass
            print("8")
            return text


def talk():
    language = "en"
    one = gTTS(text=text_translate.get(1.0, END),
               lang=language,
               slow=False)
    one.save("convert.wav")
    os.system("convert.wav")


Label(mainwindow, text='SPEECH TO TEXT', font=("Roboto 14", 15), bg='white smoke').place(x=670, y=50)

text1 = Text(mainwindow, font=100, height=10, width=40, bg='gainsboro', bd=5)
text1.place(x=200, y=320)

recordbutton = Button(mainwindow, text='Record', fg='white', width=15, bg='black', font="Roboto 14", height=1,
                      command=lambda: text1.insert(END, speech()))
recordbutton.place(x=360, y=580)

text_translate = Text(mainwindow, font=20, height=10, width=40, bg='gainsboro', bd=5)
text_translate.place(x=800, y=320)
combo = ttk.Combobox(mainwindow, values=languageV, font="Roboto 14", state="'r'")
combo.place(x=900, y=220)
combo.set("SELECT LANGUAGE")

talkbutton = Button(mainwindow, text="Translate", font="Roboto 15 bold", width=15, bg="red", fg="white", command=talk)
talkbutton.place(x=50, y=50)

label1 = Label(mainwindow, text="English", font="segoe 30 bold", bg="white", width=18, bd=5,
               relief=GROOVE)
label1.place(x=800, y=260)


def label_change():
    c = combo.get()
    label1.configure(text=c)
    mainwindow.after(1000, label_change)


def translate_now():
    global language
    try:
        destLang = "en"
        text_ = text1.get(1.0, END)
        c2 = combo.get()
        if (text_):
            words = textblob.TextBlob(text_)
            translator = Translator()
            srcLang = translator.detect(words)
            for i, j in language.items():
                if (j == c2):
                    lan_ = i
                    destLang = str(lan_)
            result = translator.translate(words, src=srcLang.lang, dest=destLang)
            text_translate.delete(1.0, END)
            text_translate.insert(END, result.text)
    except Exception as e:
        messagebox.showerror("Error", e)


translate_btn = Button(mainwindow, text="Translate", font="Roboto 15 bold", width=15, bg="red", fg="white",
                       command=translate_now)
translate_btn.place(x=960, y=580)

label_change()
mainwindow.update()
mainwindow.mainloop()