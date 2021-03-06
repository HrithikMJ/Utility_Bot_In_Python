import tkinter as tk
from tkinter import messagebox
import sys, os
from modules.generalfun import ip_address,get_host,passwordGenerator
from modules.news import get_news
from modules.weather import weather
from modules.responces import jokes,help1,filess,welcome,joke,news,bot_start,bot_dk,bot_go
from modules.text_converter import main_speak
import webbrowser
from random import randint
started=False
main_sc={}
with open("colorscheme.txt") as f:
    for line in f:
        (key,val) = line.split()
        main_sc[int(key)] = val
sys.path.append(os.path.abspath(os.path.join('..', 'config')))
root = tk.Tk()
def copy_to_clipboard(str):
    root.clipboard_clear()
    root.clipboard_append(str)
    root.update()

def Bot_Responce(User_Input):
    global main_sc, started,root

    # Starting The Bot
    if (User_Input.lower() == "/start") or (User_Input.lower() in bot_start) :
        if not started:
            text.delete('1.0', tk.END)
            started=True
        i=randint(0,3)
        BotResponce = welcome[i]
        text.insert(tk.END,"\n"+"Bot : "+BotResponce)
        main_speak(BotResponce)
        e.delete(0,"end")

    # Clear The Screen

    elif (User_Input.lower() == "/clear"):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        text.delete('1.0', tk.END)
        e.delete(0,"end")

    # Printing The News
    elif (User_Input.lower() == "/news") or (User_Input.lower() in news):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        responce =get_news(5)
        if (responce == -1):
            text.insert(tk.END,"\n"+"Bot : "+"Please Check Your Internet Connection")
            text.insert(tk.END,"\n")
        else:
            text.insert(tk.END,"\n"+"\n Here Are The Top 5 News Headline's \n")
            for i in responce:
                text.insert(tk.END,"\n"+"-> "+i+"\n")
        e.delete(0,"end")
    # Generate a Random Joke

    elif (User_Input.lower() == "/joke") or (User_Input.lower() in joke):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        no = randint(0,94)
        text.insert(tk.END,"\n"+"\n {} \n".format(jokes[no]))
        e.delete(0,"end")

    # Make The Bot Speak Somthing

    elif( "/speak" in User_Input.lower().split(" ")):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        temp = User_Input[7:]
        main_speak(temp)
        e.delete(0,"end")

    # Open The Web Browser With A Link

    elif( "/open" in User_Input.lower().split(" ")):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        temp = User_Input[6:]
        webbrowser.open(temp,new=1)
        text.insert(tk.END,"\n"+"Bot : "+"Opened "+temp)
        text.insert(tk.END,"\n")
        e.delete(0,"end")

    # Find Weather of A City

    elif ( "/weather" == User_Input.lower()[0:8]):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        temp = User_Input[9:]
        responce = weather(temp)
        if (responce == -1):
            text.insert(tk.END,"\n"+"Bot : Enter A Valid City Name or Check Your Internet Connection"+"\n")
        elif (responce == 1):
            text.insert(tk.END,"\n"+"Please Check Your Internet Connection"+"\n")
        else:
            for i in responce.values():
                text.insert(tk.END,"\n"+i)
            text.insert(tk.END,"\n")
        e.delete(0,"end")

    # Open Google With A Search Keyword

    elif ( "search for" == User_Input.lower()[0:10]):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        webbrowser.open("https://www.google.com/search?q="+User_Input[10:])
        text.insert(tk.END,"\n"+"Opened Google With The Search Query - "+User_Input[10:]+"\n")
        e.delete(0,"end")

    elif ("/password" in User_Input.lower()):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        for i in User_Input.split(' '):
            if (i.isdigit()):
                responce =passwordGenerator(i)
                text.insert(tk.END,"\n"+"Password Saved To Clipboard - "+responce+"\n")
                copy_to_clipboard(str(responce))
                break
            else:
                continue
        else:
            responce =passwordGenerator(8)
            text.insert(tk.END,"\n"+"Password Saved To Clipboard - "+responce+"\n")
            copy_to_clipboard(responce)
        text.insert(tk.END,"\n"+"")
        e.delete(0,"end")

    elif ("/ipaddress" in User_Input.lower()):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        temp = User_Input.split(' ')
        result =ip_address(temp[1])
        text.insert(tk.END,"\n"+"Bot :"+"\n")
        text.insert(tk.END,"\n"+result+"\n")
        e.delete(0,"end")

    elif (User_Input.lower()== "/host"):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        result=get_host()
        text.insert(tk.END,"\n"+"Bot :"+"\n")
        text.insert(tk.END,"\n"+result+"\n")
        e.delete(0,"end")

    elif (User_Input.lower()== "/help") or (User_Input.lower() == "/h"):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        started=False
        text.insert(tk.END,"\n"+"Bot :"+"\n")
        text.insert(tk.END,"\n"+help1+"\n")
        e.delete(0,"end")

    elif (User_Input.lower() == "/exit") or (User_Input.lower() in bot_go):
        root.after(2,root.destroy)

    elif (User_Input.lower() in "/dark"):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        filess(1)
        a=messagebox.askquestion(title="Warning", message="The program should be restarted to to see changes!")
        if a=='yes':
            os.execl(sys.executable, sys.executable, *sys.argv)
        e.delete(0,"end")
    elif (User_Input.lower() in "/light"):
        if not started:
            text.delete('1.0', tk.END)
            started=True
        filess(0)
        a=messagebox.askquestion(title="Warning", message="The program should be restarted to to see changes!")
        if a=='yes':
            os.execl(sys.executable, sys.executable, *sys.argv)
        e.delete(0,"end")

    else:
        if not started:
            text.delete('1.0', tk.END)
            started=True
        text.insert(tk.END,"\n"+"Bot :"+"\n")
        er=bot_dk[randint(0,8)]
        text.insert(tk.END,"\n"+er+"\n")
        text.insert(tk.END,"\n"+"InVaLiD InPuT!!!"+"\n")
        text.insert(tk.END,"\n"+"Try agiain:((((("+"\n")
        e.delete(0,"end")

def sendmessage(event):
    global started
    if not started:
        text.delete('1.0', tk.END)
        started=True

    text.config(state='normal')
    text.insert(tk.END,"\n"+"You : "+e.get())
    text.insert(tk.END,"\n")
    Bot_Responce(str(e.get()))
    text.config(state='disabled')


text =tk.Text(root,bg=main_sc[1],width=100,bd=5,fg=main_sc[4])
text.insert(tk.END,"\n"+help1+"\n")
text.grid(row=0,column=0,columnspan =2)
e=tk.Entry(root,width=80,bd=5,bg=main_sc[1],fg=main_sc[4])
root.bind('<Return>', sendmessage)
send=tk.Button(root,text="Send",bg=main_sc[3],fg=main_sc[1],bd=3,width=15,command=sendmessage).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Utility Bot")
tk.mainloop()
