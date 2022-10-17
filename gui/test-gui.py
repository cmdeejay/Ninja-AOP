import customtkinter
import threading
from canvas import Canvas
from user import Username
# from utilities.ninja_utilities import Utilities
# from utilities.functions import add_task, show_client_id
# from utilities.salesforce_monitor import monitor_final


class GUI(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        # login_session = Utilities().login()
        super().__init__(*args, **kwargs)
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("theme/default_theme.json")
        # variable = StringVar(root)
        # variable.set("Type")
        # self.resizable(False, False)
        self['background'] = '#282c3c'
        # root.iconbitmap(r'images/Ninja.ico')
        self.title("NINJA 2.1.0")
        self._window_width = 1050
        self._window_height = 550
        self._screen_width = self.winfo_screenwidth()
        self._screen_height = self.winfo_screenheight()
        self._center_x = int(self._screen_width / 2 - self._window_width / 2)
        self._center_y = int(self._screen_height / 2 - self._window_height / 2)
        self.geometry(f'{self._window_width}x{self._window_height}+{self._center_x}+{self._center_y}')

        # self.grid_columnconfigure(1, weight=5)

        # frame
        self._left_frame = Canvas(master=self)
        self._left_frame.grid(column=1, padx=0, pady=0, sticky="E", rowspan=9)

        self._dashboard_button = customtkinter.CTkButton(master=self, text="Dashboard", text_color="white")
        self._dashboard_button.grid(row=0, column=0, padx=30, pady=3, sticky="W")

        self._dashboard_button = customtkinter.CTkButton(master=self, text="New Task", text_color="white")
        self._dashboard_button.grid(row=6, column=0, padx=30, pady=3, sticky="W")

        self._dashboard_button = customtkinter.CTkButton(master=self, text="History", text_color="white")
        self._dashboard_button.grid(row=1, column=0, padx=30, pady=3, sticky="W")

        self._trading_login_entry = customtkinter.CTkEntry(master=self,
                                                           placeholder_text="Trading account",
                                                           text_font= ("Hack NF", -12),
                                                           bg="#202023",
                                                           fg="#4ec9b0",
                                                           corner_radius=10)
        self._trading_login_entry.grid(row=5, column=0, padx=30, pady=3, sticky="W")

        self._dashboard_name = customtkinter.CTkLabel(master=self, text=f"{Username.user}", text_color="white", text_font=("Hack NF", -11))
        self._dashboard_name.grid(row=7, column=0, padx=30, pady=3, sticky="WS")
        # # label configure
        # ttk.Label(root, text="#        Email                                          Client ID        First Name                Last Name                Status                                                 Actions", style='White.TLabel').place(x=25, y=190)
        # ttk.Label(root, text="Email", style='Yellow.TLabel').place(x=25, y=20)
        # ttk.Label(root, text="Client ID", style='Yellow.TLabel').place(x=25, y=60)
        # ttk.Label(root, text="First Name", style='Yellow.TLabel').place(x=25, y=100)
        # ttk.Label(root, text="Last Name", style="Yellow.TLabel").place(x=25, y=140)
        # ttk.Label(root, text="Login", style="Yellow.TLabel").place(x=270, y=26)
        #
        # Entry configure
        # self._email_entry = customtkinter.CTkEntry(master=self, placeholder_text='Email', bg='#4ec9b0', fg='#202023',)
        # self._trading_login_entry = customtkinter.CTkEntry(master=self, placeholder_text='Trading account', bg='#202023', fg='#4ec9b0',)
        # self._client_id_entry = customtkinter.CTkEntry(master=self, placeholder_text='Client id',  bg='#202023', fg='#4ec9b0',)
        # self._first_name_entry = customtkinter.CTkEntry(master=self, placeholder_text='First name', bg='#202023', fg='#4ec9b0',)
        # self._last_name_entry = customtkinter.CTkEntry(master=self, placeholder_text='Last name', bg='#202023', fg='#4ec9b0',)
        # log_box_entry = customtkinter.CTkScrolledText(master=root, height=9, width=65, background='#202023', foreground='#4ec9b0', font=('Arial', 12), state='disabled')

        # # Entry place
        # self._trading_login_entry.grid(row=0, column=10, padx=40, pady=20, sticky="NE")
        # self._first_name_entry.grid(row=0, column=0, padx=20, pady=5)
        # self._last_name_entry.grid(row=0, column=1, padx=5, pady=5)
        # self._email_entry.grid(row=1, column=1, padx=5, pady=5)
        # self._client_id_entry.grid(row=1, column=0, padx=5, pady=5)

        # self._trading_login_entry.place(x=870, y=15, height=28, width=130)
        # self._first_name_entry.place(x=55, y=55, height=28, width=130)
        # self._last_name_entry.place(x=200, y=55, height=28, width=130)
        # self._email_entry.place(x=55, y=15, height=28, width=130)
        # self._client_id_entry.place(x=200, y=15, height=28, width=130)
        # log_box_entry.place(x=440, y=5)
        #
        # # Image root
        # del_btn = PhotoImage(file='images/del1.png')
        # run_btn = PhotoImage(file='images/run1.png')
        # id_btn = PhotoImage(file='images/id.png')
        # eye_btn = PhotoImage(file='images/eye.png')
        # trans_btn = PhotoImage(file='images/trans.png')
        #
        # # Button configure
        # Button(root, bg='#202023', fg='#b5cea8', text="SHOW", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: threading.Thread(target=show_client_id, args=(trading_login_entry, client_id_entry, email_entry)).start()).place(x=355, y=55, height=30, width=80)
        # Button(root, bg='#202023', fg='#b5cea8', text="ADD TASK", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: add_task(variable, trans_btn, del_btn, run_btn, id_btn, eye_btn, email_entry, client_id_entry, first_name_entry, last_name_entry, root, login_session)).place(x=270, y=95, height=30, width=80)
        # Button(root, bg='#202023', fg='#b5cea8', text="MONITOR", activebackground='#202023', activeforeground='#b5cea8', font=('Arial', 9, 'bold'), command=lambda: threading.Thread(target=monitor_final).start()).place(x=355, y=95, height=30, width=80)
        # Radiobutton(root, bg='#202023', fg='#b5cea8', relief='flat', activebackground='#202023', activeforeground='#b5cea8', text='China', value='China', font=('Arial', 10, 'bold'), variable=variable).place(x=260, y=140)
        # Radiobutton(root, bg='#202023', fg='#b5cea8', relief='flat', activebackground='#202023', activeforeground='#b5cea8', text='Other', value='Other', font=('Arial', 10, 'bold'), variable=variable).place(x=330, y=140)


gui = GUI()
gui.mainloop()
