from tkinter import *

root = Tk()
window = Toplevel(root)
window.resizable(width=FALSE, height=FALSE)
window.title("Log-In")
window.geometry("200x150")
window.attributes("-topmost", True)
username = "abc" #that's the given username
password = "cba" #that's the given password

#username entry
username_entry = Entry(window)
username_entry.pack()

#password entry
password_entry = Entry(window, show='*')
password_entry.pack()

def trylogin(): #this method is called when the button is pressed
    #to get what's written inside the entries, I use get()
    #check if both username and password in the entries are same of the given ones
    if username == username_entry.get() and password == password_entry.get():
        print("Correct")
    else:
        print("Wrong")

#when you press this button, trylogin is called
button = Button(window, text="check", command = trylogin)
button.pack()

#App starter
root.mainloop()