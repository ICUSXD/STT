
import tkinter as tk
from tkinter import END, N, ttk
#import pyaudio
import speech_recognition as sr
r = sr.Recognizer()

#전송 클래스
def setinput():
    a = enter.get()
    log.insert(END,a  + "\n")
    enter.delete(0, END)

def setenterinput(event):
    a = enter.get()
    log.insert(END,a + "\n")
    enter.delete(0, END)
    
def voicerecog():
    with sr.Microphone() as source:
        print("입력")
        audio = r.listen(source)
    try:
        sound  = r.recognize_google(audio, language='ko')
        log.insert(END, sound + "\n")
        print(r.recognize_google(audio, language='ko'))
    except sr.UnknownValueError:
        print("Error")
    except sr.RequestError as e:
        print("Req Error")



#루트 창 설정
root=tk.Tk()
root.title("SPEECH RECOGNITION")
root.geometry("1000x300")

#입력창
enter = tk.Entry(root, width = 100)
enter.place(y="270", width=700, height=25)
enter.bind("<Return>",setenterinput)

#로그창
log = tk.Text(root, width = 100)
log.place(width=700, height=270)
#log.configure(state='disabled')


#전송 버튼
startbt = tk.Button(root, text="입력", command=setinput)
startbt.place(x="700", y="267")

#음성인식 시작 버튼
startbt = tk.Button(root, text="시작", command=voicerecog)
startbt.place(x="700", y="140")

#마이크 설정(미완성)
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(enumerate(sr.Microphone.list_microphone_names()))
    Mic=["{1} {0}".format(index, name)]
    combobox = ttk.Combobox(root)
    combobox.config(height=5)
    combobox.config(values=Mic)
    combobox.config(state="readonly")
    combobox.set("Default Mic")
    combobox.place(x="780", y="270")   

root.mainloop()





'''
with sr.Microphone() as source:
    print("입력")
    audio = r.listen(source)
    print("입력 종료")
    
try:
    print(r.recognize_google(audio, language='ko'))
except sr.UnknownValueError:
    print("Error")
except sr.RequestError as e:
    print("Req Error")
'''
