import pyperclip
import  pyshorteners
from tkinter import *


root = Tk()
root.geometry("400x200")
root.title("Black ___URL CUTTER___ Abra ")
root.configure(bg="#67aa25")
url = StringVar()
url_address = StringVar()

def URL_Shortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)



def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)


Label(root, text="Keep IT Short - URL Shortener", font="Shruti").pack(pady=10)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Generate the Short U R L", command=URL_Shortener).pack(pady=7)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command = copyurl).pack(pady=5)

root.mainloop()
