import tkinter as tk
import sys, os
from modules.generalfun import ip_address,get_host,passwordGenerator
from modules.news import get_news
from modules.weather import weather
from modules.responces import jokes,help1
from modules.text_converter import main_speak
from modules.img2pdf import main_f
import webbrowser
from random import randint
root = tk.Tk()
welcome={
    "Hi":["Hi There !","Hi !","Hi How can i help you ?"],
    "BotStart":["hi","start bot","start"],
    "News":["get me news","read news","news","news today"],
    "Jokes":["tell me a joke","joke","tell a joke"]
}

sys.path.append(os.path.abspath(os.path.join('..', 'config')))

def copy_to_clipboard(str):
    root.clipboard_clear()
    root.clipboard_append(str)
    root.update()
def Bot_Responce(User_Input):

    # Starting The Bot

    if (User_Input.lower() == "/start") or (User_Input.lower() in welcome["BotStart"]) :
        BotResponce = welcome["Hi"][randint(0,2)]
        text.insert(tk.END,"\n"+"Bot : "+BotResponce)
        main_speak(BotResponce)

    # Clear The Screen

    elif (User_Input.lower() == "/clear"):
        text.delete('1.0', tk.END)
        text.insert(tk.END,"\n"+help1+"\n")

    # Printing The News

    elif (User_Input.lower() == "/news") or (User_Input.lower() in welcome["News"]):
        responce =get_news(5)
        if (responce == -1):
            text.insert(tk.END,"\n"+"Bot : "+"Please Check Your Internet Connection")
            text.insert(tk.END,"\n")
        else:
            text.insert(tk.END,"\n"+"\n Here Are The Top 5 News Headline's \n")
            for i in responce:
                text.insert(tk.END,"\n"+"-> "+i+"\n")

    # Generate a Random Joke

    elif (User_Input.lower() == "/joke") or (User_Input.lower() in welcome["Jokes"]):
        no = randint(0,94)
        text.insert(tk.END,"\n"+"\n {} \n".format(jokes[no]))

    # Make The Bot Speak Somthing

    elif( "/speak" in User_Input.lower().split(" ")):
        temp = User_Input[7:]
        main_speak(temp)

    # Open The Web Browser With A Link

    elif( "/open" in User_Input.lower().split(" ")):
        temp = User_Input[6:]
        webbrowser.open(temp,new=1)
        text.insert(tk.END,"\n"+"Bot : "+"Opened "+temp)
        text.insert(tk.END,"\n")

    # Find Weather of A City

    elif ( "/weather" == User_Input.lower()[0:8]):
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

    # Open Google With A Search Keyword

    elif ( "search for" == User_Input.lower()[0:10]):
        webbrowser.open("https://www.google.com/search?q="+User_Input[10:])
        text.insert(tk.END,"\n"+"Opened Google With The Search Query - "+User_Input[10:]+"\n")

    elif ("/password" in User_Input.lower()):
        for i in User_Input.split(' '):
            if (i.isdigit()):
                responce = modules.generalfun.passwordGenerator(i)
                text.insert(tk.END,"\n"+"Password Saved To Clipboard - "+responce+"\n")
                copy_to_clipboard(str(responce))
                break
            else:
                continue
        else:
            responce = modules.generalfun.passwordGenerator(8)
            text.insert(tk.END,"\n"+"Password Saved To Clipboard - "+responce+"\n")
            copy_to_clipboard(responce)
        text.insert(tk.END,"\n"+"")

    elif ("/ipaddress" in User_Input.lower()):
        temp = User_Input.split(' ')
        result = modules.generalfun.ip_address(temp[1])
        text.insert(tk.END,"\n"+"Bot :"+"\n")
        text.insert(tk.END,"\n"+result+"\n")

    elif (User_Input.lower()== "/host"):
        result=get_host()
        text.insert(tk.END,"\n"+"Bot :"+"\n")
        text.insert(tk.END,"\n"+result+"\n")

    elif (User_Input.lower() in "/img2pdf")or(User_Input.lower() == "/img2pdf"):

        main_f()



def sendmessage(event):
    text.config(state='normal')
    text.insert(tk.END,"\n"+"You : "+e.get())
    text.insert(tk.END,"\n")
    Bot_Responce(str(e.get()))
    text.config(state='disabled')

def func(event):
    print("You hit return.")

text =tk.Text(root,bg="#FFF",width=80,bd=5)
text.insert(tk.END,"\n"+help1+"\n")
text.grid(row=0,column=0,columnspan=2)
e=tk.Entry(root,width=80,bd=5)
root.bind('<Return>', sendmessage)
send=tk.Button(root,text="Send",bg="#FFF",bd=3,width=15,command=sendmessage).grid(row=1,column=1)
e.grid(row=1,column=0)
root.title("Utility Bot")
tk.mainloop()
