from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import requests
import json

color1= "white"
color2 = "yellow"
color3 = "black"
window = Tk()
window.title("BitTracker")
window.geometry("320x350")
window.configure(bg = color1)
def info():
    api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CEUR%2CINR%2CCAD"
    r = requests.get(api_link)
    dic = r.json()
    # usd
    usd_value = float(dic["USD"])
    print (usd_value)
    usd_formatted_value = "${: ,.3f}".format(usd_value)
    usd["text"] = usd_formatted_value
    # eur
    euro_value = float(dic["EUR"])
    print (euro_value)
    euro_formatted_value = "€{: ,.3f}".format(euro_value)
    eur["text"] =euro_formatted_value
    # cad
    cad_value = float(dic["CAD"])
    print (cad_value)
    cad_formatted_value = "Can${: ,.3f}".format(cad_value)
    can["text"] =cad_formatted_value
    # inr
    inr_value = float(dic["INR"])
    print (cad_value)
    inr_formatted_value = "₹{: ,.3f}".format(inr_value)
    ind["text"] =inr_formatted_value
    frame_body.after(1000,info)
frame_head = Frame(window , width = 320 ,height = 50 , bg = color2)
frame_head.grid(row=1 , column = 0)
frame_body = Frame(window , width = 320 ,height = 300 , bg = color3)
frame_body.grid(row=2 , column = 0)
image1 = Image.open('bit.png')
image1 = image1.resize((30 , 30))
image1 = ImageTk.PhotoImage(image1)
icon = Label(frame_head , image = image1, bg = color2)
icon.place(x = 10 , y = 10)
name = Label (frame_head , text = "BitCoin tracker", fg = "black",bg = color2 , width = 14 , height =1,anchor = "center" , font = ("poppins 18"))
name.place(x = 70 , y = 8)
usd = Label(frame_body , text = "$1000" , width = 14 , height = 1, font =("arial 30 bold") , bg = color3 , fg = "white",anchor = "center")
usd.place(x = 0 , y = 28)
ind = Label(frame_body , text = "$1000" , width = 14 , height = 1, font =("arial 15 bold") , bg = color3 , fg = "white",anchor = "center")
ind.place(x = 10 , y = 98)
eur = Label(frame_body , text = "$1000" , width = 14 , height = 1, font =("arial 15 bold") , bg = color3 , fg = "white",anchor = "center")
eur.place(x = 10 , y = 138)
can = Label(frame_body ,text = "$1000" , width = 14 , height = 1, font =("arial 15 bold") , bg = color3 , fg = "white",anchor = "center")
can.place(x = 10 , y = 178)
info()
window.mainloop()
