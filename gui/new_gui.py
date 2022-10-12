from tkinter import Tk, ttk, StringVar, Entry, PhotoImage, Button, Radiobutton
from tkinter.scrolledtext import ScrolledText
import threading
from utilities.ninja_utilities import Utilities
from utilities.functions import add_task, show_client_id
from utilities.salesforce_monitor import monitor_final


class GUI:
    def __init__(self):
        login_session = Utilities().login()
        root = Tk()
        variable = StringVar(root)
        variable.set("Type")
        root.resizable(False, False)
        root['background'] = '#202023'
        root.iconbitmap(r'images/Ninja.ico')
        root.title("NINJA 2.1.0")
        root.geometry("1050x550")
        window_width = 1050
        window_height = 550
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Style configure
        style = ttk.Style()
        style.theme_use('vista')
        style.configure('Yellow.TLabel', background="#202023", foreground="white", fieldbackground="#202023", font=('Arial', 10, 'bold'))
        style.configure('White.TLabel', background="#202023", foreground="#569cd6", fieldbackground="#202023", font=('Arial', 12, 'bold'))
        style.configure('White_small.TLabel', background="#202023", foreground="#f44747", fieldbackground="#202023", font=('Arial', 10, 'bold'))

        # label configure
        ttk.Label(root, text="#        Email                                          Client ID        First Name                Last Name                Status                                                 Actions", style='White.TLabel').place(x=25, y=190)
        ttk.Label(root, text="Email", style='Yellow.TLabel').place(x=25, y=20)
        ttk.Label(root, text="Client ID", style='Yellow.TLabel').place(x=25, y=60)
        ttk.Label(root, text="First Name", style='Yellow.TLabel').place(x=25, y=100)
        ttk.Label(root, text="Last Name", style="Yellow.TLabel").place(x=25, y=140)
        ttk.Label(root, text="Login", style="Yellow.TLabel").place(x=270, y=26)

        # Entry configure
        email_entry = Entry(root, bg='#202023', fg='#4ec9b0', font=('Arial', 10))
        trading_login_entry = Entry(root, bg='#202023', fg='#4ec9b0', font=('Arial', 10))
        client_id_entry = Entry(root, bg='#202023', fg='#4ec9b0', font=('Arial', 10))
        first_name_entry = Entry(root, bg='#202023', fg='#4ec9b0', font=('Arial', 10))
        last_name_entry = Entry(root, bg='#202023', fg='#4ec9b0', font=('Arial', 10))
        log_box_entry = ScrolledText(root, height=9, width=65, background='#202023', foreground='#4ec9b0', font=('Arial', 12), state='disabled')

        # Entry place
        trading_login_entry.place(x=270, y=55, height=28, width=79)
        first_name_entry.place(x=105, y=95, height=28, width=130)
        last_name_entry.place(x=105, y=135, height=28, width=130)
        email_entry.place(x=105, y=15, height=28, width=130)
        client_id_entry.place(x=105, y=55, height=28, width=130)
        log_box_entry.place(x=440, y=5)

        # Image root
        del_btn = PhotoImage(file='images/del1.png')
        run_btn = PhotoImage(file='images/run1.png')
        id_btn = PhotoImage(file='images/id.png')
        eye_btn = PhotoImage(file='images/eye.png')
        trans_btn = PhotoImage(file='images/trans.png')

        # Button configure
        Button(root, bg='#202023', fg='#b5cea8', text="SHOW", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: threading.Thread(target=show_client_id, args=(trading_login_entry, client_id_entry, email_entry)).start()).place(x=355, y=55, height=30, width=80)
        Button(root, bg='#202023', fg='#b5cea8', text="ADD TASK", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: add_task(variable, trans_btn, del_btn, run_btn, id_btn, eye_btn, email_entry, client_id_entry, first_name_entry, last_name_entry, root, login_session)).place(x=270, y=95, height=30, width=80)
        Button(root, bg='#202023', fg='#b5cea8', text="MONITOR", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: threading.Thread(target=monitor_final).start()).place(x=355, y=95, height=30, width=80)
        Radiobutton(root, bg='#202023', fg='#b5cea8', relief='flat', activebackground='#202023', activeforeground='#b5cea8', text='China', value='China', font=('Arial', 10, 'bold'), variable=variable).place(x=260, y=140)
        Radiobutton(root, bg='#202023', fg='#b5cea8', relief='flat', activebackground='#202023', activeforeground='#b5cea8', text='Other', value='Other', font=('Arial', 10, 'bold'), variable=variable).place(x=330, y=140)

        root.mainloop()
