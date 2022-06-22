import tkinter as tk
from tkinter import END, N, ttk
import pyaudio
import speech_recognition as sr
from pythonosc.udp_client import SimpleUDPClient
r = sr.Recognizer()

ip = "127.0.0.1"
port = 9000
client = SimpleUDPClient(ip, port)  # Create client

#Class Setup
def setinput():
    a = enter.get()
    log.insert(END,a  + "\n")
    enter.delete(0, END)
    sendosc()
    
def setenterinput(event):
    a = enter.get()
    log.insert(END,a + "\n")
    enter.delete(0, END)
    sendosc()

def coor:
    
     
    
    
def sendosc():
    a = enter.get()
    a = str(a)
    client.send_message("/avatar/parameters/stt", [a])
    
def voicerecog():
    with sr.Microphone() as source:
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
    #enumerate(sr.Microphone.list_microphone_names())
    #Mic=["{0}".format(name)]
    combobox = ttk.Combobox(root, values=name)
    combobox.config(height=5)
    combobox.config(state="readonly")
    combobox.set("Default Mic")
    combobox.place(x="780", y="270")   

root.mainloop()




#default Tiling:0.007874016 Offset:0.992126 max x=127 y=112 min:x=37 y=111 
