from utilities.ninja_utilities import Utilities
from tkinter import END
from tkinter import messagebox as messagebox


def showClientId(trading_login_entry, client_id_entry, email_entry):
    email_entry.delete(0, END)
    client_id_entry.delete(0, END)
    trading_login = trading_login_entry.get()
    if trading_login == '':
        messagebox.showerror(title='Warning', message='Please recheck the login!')
    else:
        try:
            Uti = Utilities()
            client_id = Uti.scrapId(trading_login)
            client_email = Uti.scrapEmail(trading_login)
            email_entry.insert(END, client_email)
            client_id_entry.insert(END, client_id)
        except AttributeError:
            messagebox.showerror(title='Warning', message='Please recheck the login!')
