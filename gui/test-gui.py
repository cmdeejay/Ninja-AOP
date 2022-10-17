import customtkinter
import threading
from canvas import Canvas
from user import Username
# from utilities.ninja_utilities import Utilities
# from utilities.functions import add_task, show_client_id
# from utilities.salesforce_monitor import monitor_final
from PIL import Image, ImageTk


class GUI(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        # login_session = Utilities().login()
        super().__init__(*args, **kwargs)
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("theme/default_theme.json")
        # variable = StringVar(root)
        # variable.set("Type")
        self.resizable(False, False)
        self['background'] = '#282c3c'
        # root.iconbitmap(r'images/Ninja.ico')
        self.title("NINJA 2.1.0")
        self._window_width = 1055
        self._window_height = 555
        self._screen_width = self.winfo_screenwidth()
        self._screen_height = self.winfo_screenheight()
        self._center_x = int(self._screen_width / 2 - self._window_width / 2)
        self._center_y = int(self._screen_height / 2 - self._window_height / 2)
        self.geometry(f'{self._window_width}x{self._window_height}+{self._center_x}+{self._center_y}')

        # self.grid_columnconfigure(1, weight=5)

        # frame
        self._left_frame = Canvas(master=self)
        self._left_frame.grid(column=1, padx=0, pady=0, sticky="E", rowspan=15)

        self._logo_image = Image.open("logo.png").resize((60, 60))
        self._dashboard_image = Image.open("Dashboard.png").resize((22, 22))
        self._history_image = Image.open("History.png").resize((22, 22))
        self._add_image = Image.open("Add.png").resize((22, 22))

        self._logo_image = ImageTk.PhotoImage(self._logo_image)
        self._dashboard_image = ImageTk.PhotoImage(self._dashboard_image)
        self._history_image = ImageTk.PhotoImage(self._history_image)
        self._add_image = ImageTk.PhotoImage(self._add_image)

        self._dashboard_button = customtkinter.CTkButton(master=self, text="Dashboard", text_color="white", image=self._dashboard_image, hover=False)
        self._dashboard_button.grid(row=1, column=0, padx=30, pady=3, sticky="WW")

        self._dashboard_button = customtkinter.CTkButton(master=self, text="New Task", text_color="white", image=self._add_image)
        self._dashboard_button.grid(row=3, column=0, padx=26, pady=3, sticky="WW")

        self._dashboard_button = customtkinter.CTkButton(master=self, text="History", text_color="white", image=self._history_image)
        self._dashboard_button.grid(row=2, column=0, padx=23, pady=3, sticky="WW")

        self._logo = customtkinter.CTkButton(master=self,
                                             text="",
                                             width=50,
                                             height=50,
                                             image=self._logo_image,
                                             hover_color="#282c3c")
        self._logo.grid(row=0, column=0, padx=85, pady=3, sticky="WN")

        self._trading_login_entry = customtkinter.CTkEntry(master=self,
                                                           placeholder_text="Trading account",
                                                           text_font=("Hack NF", -12),
                                                           bg="#202023",
                                                           fg="#4ec9b0",
                                                           corner_radius=10)
        self._trading_login_entry.grid(row=4, column=0, padx=40, pady=3, sticky="W")

        self._dashboard_name = customtkinter.CTkLabel(master=self, text=f"{Username.user}", text_color="white", text_font=("Hack NF", -11))
        self._dashboard_name.grid(row=12, column=0, padx=30, pady=3, sticky="WS")

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
